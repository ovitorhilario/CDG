from tkinter import *
import cv2
import numpy as np
import utils

def errorMessage():
    app = Tk()
    app.title('Erro')
    app.geometry('380x100')
    app.resizable(False, False)

    frameError = Frame()
    frameError.pack(pady=10)

    def end():
        frameError.destroy()
        app.destroy()

    Label(frameError, text='Não foi possível estabelecer uma conexão com a camera.').grid(row=0, column=0, pady=5)
    Button(frameError, text='Ok', command=end).grid(row=2, column=0, sticky=E, ipadx=5)

    app.mainloop()

def program(ans, nQ, nApQ, CanValue, resCan):

    cap = cv2.VideoCapture(CanValue)
    cap.set(10, 160)
    widthImg = resCan[0]
    heightImg = resCan[1]

    while True:
        ret, img = cap.read()

        if not ret:
            errorMessage()
            break

        img = cv2.resize(img, (widthImg, heightImg))
        imgFinal = img.copy()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
        imgCanny = cv2.Canny(imgBlur, 10, 70)

        try:
            imgContours = img.copy()
            imgBigContour = img.copy()
            contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10)
            rectCon = utils.rectContour(contours)
            biggestPoints = utils.getCornerPoints(rectCon[0])
            gradePoints = utils.getCornerPoints(rectCon[1])

            if biggestPoints.size != 0 and gradePoints.size != 0:

                # MAIOR RETANGULO

                rWidth = nApQ * 100
                rHeight = nQ * 100

                biggestPoints = utils.reorder(biggestPoints)
                cv2.drawContours(imgBigContour, biggestPoints, -1, (0, 255, 0), 20)
                pts1 = np.float32(biggestPoints)
                pts2 = np.float32([[0, 0], [rWidth, 0], [0, rHeight], [rWidth, rHeight]])
                matrix = cv2.getPerspectiveTransform(pts1, pts2)

                imgWarpColored = cv2.warpPerspective(img, matrix, (rWidth, rHeight))

                # 2 MAIOR RETANGULO
                cv2.drawContours(imgBigContour, gradePoints, -1, (255, 0, 0), 20)
                gradePoints = utils.reorder(gradePoints)
                ptsG1 = np.float32(gradePoints)
                ptsG2 = np.float32([[0, 0], [325, 0], [0, 150], [325, 150]])
                matrixG = cv2.getPerspectiveTransform(ptsG1, ptsG2)
                imgGradeDisplay = cv2.warpPerspective(img, matrixG, (325, 150))

                imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
                imgThresh = cv2.threshold(imgWarpGray, 170, 255, cv2.THRESH_BINARY_INV)[1]

                boxes = utils.splitBoxes(imgThresh, nQ, nApQ)  # AGRUPA EM UMA LISTA TODAS AS ALTERNATIVAS

                countR = 0
                countC = 0

                myPixelVal = np.zeros((nQ, nApQ))  # ARMAZENAR OS VALORES DIFERENTES DE ZERO DE CADA CAIXA

                for image in boxes:
                    totalPixels = cv2.countNonZero(image)
                    myPixelVal[countR][countC] = totalPixels
                    countC += 1
                    if (countC == nApQ): countC = 0; countR += 1

                myIndex = []

                for x in range(0, nQ):
                    arr = myPixelVal[x]
                    myIndexVal = np.where(arr == np.amax(arr))
                    myIndex.append(myIndexVal[0][0])

                grading = []
                for x in range(0, nQ):
                    if ans[x] == myIndex[x]:
                        grading.append(1)
                    else:
                        grading.append(0)

                score = (sum(grading) / nQ) * 100

                # DESENHO DAS RESPOSTAS
                utils.showAnswers(imgWarpColored, myIndex, grading, ans, nQ, nApQ)
                utils.drawGrid(imgWarpColored, nQ, nApQ)
                imgRawDrawings = np.zeros_like(imgWarpColored)
                utils.showAnswers(imgRawDrawings, myIndex, grading, ans, nQ, nApQ)

                invMatrix = cv2.getPerspectiveTransform(pts2, pts1)
                imgInvWarp = cv2.warpPerspective(imgRawDrawings, invMatrix, (widthImg, heightImg))

                # DESENHO DAS NOTAS
                imgRawGrade = np.zeros_like(imgGradeDisplay, np.uint8)
                cv2.putText(imgRawGrade, str(int(score)) + "%", (70, 100), cv2.FONT_HERSHEY_DUPLEX, 3, (0, 255, 255), 3)
                invMatrixG = cv2.getPerspectiveTransform(ptsG2, ptsG1)
                imgInvGradeDisplay = cv2.warpPerspective(imgRawGrade, invMatrixG, (widthImg, heightImg))

                imgFinal = cv2.addWeighted(imgFinal, 1, imgInvWarp, 1, 0)
                imgFinal = cv2.addWeighted(imgFinal, 1, imgInvGradeDisplay, 1, 0)

        except:
            print('Identificando...')

        cv2.imshow('Clique (s) para sair', imgFinal)
        if cv2.waitKey(1) & 0xFF == ord('s') or 0xFF == ord('S'):
            break

    cap.release()
    cv2.destroyAllWindows()