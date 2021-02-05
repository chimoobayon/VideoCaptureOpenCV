# Despues de abrir el folder con el archivo .py, 
# Se seleciona el interprete Python
# Se abre un Termina de VSCode (Ctrl + Shift + ñ)
# cd C:\Users\chimo\Desktop\Python\VideoCaptureOpenCV
# Se crea entorno virtual
# python -m venv .videocv2env
# Se activa el entorno virtual
# C:\Users\chimo\Desktop\Python\VideoCaptureOpenCV\.videocv2env\Scripts\Activate.ps1
# pip3 install opencv-python
# Me dio el error "ConnectionRefusedError: [WinError 10061] " y lo solucione quitando la deteccion de proxy automatica de la conexion de internet.

# ESTE EJEMPLO ES PARA HACER CAPTURA DE MOVIMIENTO CON WEBCAM

import cv2, time

video = cv2.VideoCapture(0)

a = 1

first_frame = None

while True : 
    a = a + 1
    check, frame = video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_delta = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)
 #   (_,cnts,_) = cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    (cnts,_) = cv2.findContours(thresh_delta.copy(),cv2.RETR_TREE    ,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0),3)

    cv2.imshow('frame',frame)
    cv2.imshow('Captura',gray)
    cv2.imshow('Delta',delta_frame)
    cv2.imshow('Thresh',thresh_delta)

    key=cv2.waitKey(1)
# wait de 1 signifiva esperar 1 milisegundo, por lo que genera un frame cada milisegundo
    if key == ord('q'):
        break

print ('Se han mostrado ' , a , ' frames.')

# time.sleep(3)


video.release()

cv2.destroyAllWindows()