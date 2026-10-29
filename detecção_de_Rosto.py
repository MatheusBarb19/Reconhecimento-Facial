#OBJETIVO: Reconhecimento facial em tempo real utilizando a biblioteca mediapipe e OpenCV.
import cv2 #Bilbioteca para processamento de imagens
import mediapipe as mp #Bibliteoca de reconhecimento de imagens

#=========================================
#Inicilização da WebCam
#=========================================

webcam = cv2.VideoCapture(0) #Inicia a webcam

#Verifica se a webcam foi iniciada corretamente
if not webcam.isOpened():
    print("Erro ao abrir a webcam")
    exit() #Encerra o programa caso a webcam não tenha sido iniciada corretamente

#=========================================
#Configuração do Reconhecimento Facial
#=========================================

reconhecer_rosto = mp.solutions.face_detection #Inicia o reconhecimento facial
reconhecedor_rosto = reconhecer_rosto.FaceDetection(model_selection=0, min_detection_confidence=0.6) #Cria um objeto para o reconhecimento facial
desenho_facial = mp.solutions.drawing_utils #Cria um objeto para desenhar o rosto


#=========================================
#Captura e Processamento de Quadros
#=========================================

try:
    while True:
        verificador, frame = webcam.read() #Lê a imagem da webcam

        if not verificador: #Verifica se a imagem foi lida corretamente
            print("Erro ao capturar o quadro da webcam")
            break

        #Reconhcer rosto dentro da lista
        lista_facial = reconhecedor_rosto.process(frame) #Processa a imagem para reconhecer o rosto

        if lista_facial.detections: #Verifica se o rosto foi reconhecido
            for rosto in lista_facial.detections: #Percorre a lista de rostos reconhecidos
                desenho_facial.draw_detection(frame, rosto) #Desenha o rosto na imagem

        cv2.imshow("Reconhecimento Facial", frame) #Mostra a imagem na tela
        if cv2.waitKey(5) == 27: #Verifica se a tecla ESC foi pressionada
            break
while True:
    verificador, frame = webcam.read() #Lê a imagem da webcam

    if not verificador: #Verifica se a imagem foi lida corretamente
        break

    #Reconhcer rosto dentro da lista
    lista_facial = reconhecedor_rosto.process(frame) #Processa a imagem para reconhecer o rosto

    if lista_facial.detections: #Verifica se o rosto foi reconhecido
        for rosto in lista_facial.detections: #Percorre a lista de rostos reconhecidos
            desenho_facial.draw_detection(frame, rosto) #Desenha o rosto na imagem

    cv2.imshow("Reconhecimento Facial", frame) #Mostra a imagem na tela
    if cv2.waitKey(5) == 27: #Verifica se a tecla ESC foi pressionada
        break   

webcam.release() #Libera a webcam
cv2.destroyAllWindows() #Fecha todas as janelas abertas