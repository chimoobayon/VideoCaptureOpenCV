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

import cv2, time

video = cv2.VideoCapture(0)

a = 1

while True : 
    a = a + 1
    check, frame = video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Captura',gray)
    key=cv2.waitKey(1)
# wait de 1 signifiva esperar 1 milisegundo, por lo que genera un frame cada milisegundo
    if key == ord('q'):
        break

print ('Se han mostrado ' , a , ' frames.')

# time.sleep(3)


video.release()

cv2.destroyAllWindows()