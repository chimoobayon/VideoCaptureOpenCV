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

check, frame = video.read()

# print(check)    <-- Para verificar que puede acceder correctamente a la webcam
# print(frame)

time.sleep(3)

cv2.imshow('Captura',frame)

cv2.waitKey(0)

video.release()

cv2.destroyAllWindows()