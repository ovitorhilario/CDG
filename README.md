# CDG
## Corretor de Gabaritos - OpenCV

O  CDG, Corretor de Gabaritos, utiliza a linguagem Python e algumas bibliotecas do mesmo, sendo uma adaptação do projeto já existente [Optical Mark Recognition OPENCV](https://github.com/murtazahassan/Optical-Mark-Recognition-OPENCV), trazendo novas implementações como:

- Interface gráfica simples e acessível.
- Flexibilidade na adaptação do número de questões e na quantidade de alternativas por questão.

## Características
A aplicação tem como finalidade corrigir gabaritos através de uma câmera, apresentando as respostas de forma imediata na tela do dispositivo por meio de informações previamente fornecidas ao programa, como o número de questões, a quantidade alternativas por questão e as respectivas respostas corretas de cada questão.

## Começando

[Instalação](https://github.com/vitor-hilario/CDG/releases/tag/v1.0) ⬇️

Para executar o projeto, pode-se instalar o arquivo .exe, não sendo necessário a utilização de outro programa, porém, em caso de teste dos arquivos do código-fonte, será necessário ter um ambiente de desenvolvimento, mostrado no próximo tópico de Desenvolvimento.

Não somente isso, é preciso ter uma saída de vídeo, ou seja, uma câmera, webcam, ou até mesmo a câmera do celular com o uso do DroidCam, assim como é demonstrado nesse [Vídeo](https://youtu.be/fv_OTMaxAiU) de exemplo. 


## Desenvolvimento

Para executar o projeto, é essencial que se tenha o [Python](https://www.python.org/downloads/) instalado, além de uma IDE - Ambiente de desenvolvimento integrado, sendo aconselhado o uso do [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows).

Possuindo as ferramentas fundamentais, crie uma pasta com todos os arquivos presentes neste repositório:
```sh
> CDG
-- main.py
-- omr.py
-- utils.py
```


Instale as bibliotecas através do Terminal na IDE no mesmo diretório do projeto:

```sh
pip install opencv-python
pip install numpy
pip install tk
```

Feito isso, agora inicie o programa a partir do arquivo main.py.

