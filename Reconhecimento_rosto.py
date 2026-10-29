import cv2
from deepface import DeepFace

imagem = cv2.imread("teste.jpg") #Carrega a imagem para reconhecimento facial
resultado = DeepFace.analyze(imagem, actions=['age', 'emotion'], enforce_detection=False) #Analisa a imagem para reconhecer a idade e emoção da pessoa

print("Idade:", resultado[0]["age"]) #Exibe a idade da pessoa na imagem
print("Emoção:", resultado[0]["dominant_emotion"]) #Exibe a emoção dominante da pessoa na imagem