import cv2
from deepface import DeepFace

imagem = cv2.imread("teste.jpg") #Carrega a imagem para reconhecimento facial
resultado = DeepFace.analyze(imagem, actions=('age', 'emotion'))