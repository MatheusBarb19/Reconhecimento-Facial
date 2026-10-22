import cv2 #Bilbioteca para processamento de imagens
import mediapipe as mp #Bibliteoca de reconhecimento de imagens

webcam = cv2.VideoCapture(0) #Inicia a webcam

reconhecer_rosto = mp.solutions.face_detection #Inicia o reconhecimento facial
reconhecedor_rosto = reconhecer_rosto.FaceDetection() #Cria um objeto para o reconhecimento facial
desenho_facial = mp.solutions.drawing_utils #Cria um objeto para desenhar o rosto

while True:
    verificador, frame = webcam.read() #Lê a imagem da webcam
    