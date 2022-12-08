import cv2
import numpy as np

def reorder(myPoints):

    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)] #[0,0]
    myPointsNew[3] = myPoints[np.argmax(add)] #[w,h]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)] #[w,0]
    myPointsNew[2] = myPoints[np.argmax(diff)] #[h,0]

    return myPointsNew

def rectContour(contours):
    rectCon = []
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 50:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if len(approx) == 4:
                rectCon.append(i)
    rectCon = sorted(rectCon, key=cv2.contourArea, reverse=True)
    return rectCon

def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True)
    approx = cv2.approxPolyDP(cont, 0.02 * peri, True)
    return approx

def splitBoxes(img, nQ, nApQ):
    rows = np.vsplit(img, nQ)
    boxes = []
    for r in rows:
        cols = np.hsplit(r, nApQ)
        for box in cols:
            boxes.append(box)
    return boxes

def drawGrid(img, nQ, nApQ):
    secH = int(img.shape[0] / nQ)  # HEIGHT / NUMERO DE QUESTOES
    secW = int(img.shape[1] / nApQ)  # LARGURA / NUMERO DE RESPOSTAS POR QUESTAO

    for i in range(0, nQ):
        pt1 = (0, secH * i)
        pt2 = (img.shape[1], secH * i)
        pt3 = (secW * i, 0)
        pt4 = (secW * i, img.shape[0])
        cv2.line(img, pt1, pt2, (255, 255, 0), 2)
        cv2.line(img, pt3, pt4, (255, 255, 0), 2)


    return img

def showAnswers(img, myIndex, grading, ans, nQ, nApQ):
     secH = int(img.shape[0] / nQ)
     secW = int(img.shape[1] / nApQ)

     for x in range(0, nQ):
         myAns = myIndex[x]
         cX = (myAns * secW) + secW // 2
         cY = (x * secH) + secH // 2

         if grading[x] == 1:
             # REPOSTA CORRETA
             myColor = (0, 255, 0)
             cv2.circle(img, (cX, cY), 35, myColor, -1)
         else:
             myColor = (0, 0, 255)
             cv2.circle(img, (cX, cY), 35, myColor, -1)

             # A RESPOSTA QUE SERIA A CORRETA
             myColor = (128, 0, 128)
             correctAns = ans[x]
             cv2.circle(img, ((correctAns * secW) + secW // 2, (x * secH) + secH // 2), 25, myColor, -4)

