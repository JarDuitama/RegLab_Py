# video guia - https://www.youtube.com/watch?v=xa804S90WWw
# tener en cuenta la istalacion de "pip install opencv-contrib-python"
import os, msvcrt
import cv2
import numpy as np

def main():
    os.system("cls")
    # Listamos Carpetas con Capturas o fotos
    rutaData = os.getcwd() + '\ImgUsu'
    usuList = os.listdir(rutaData)
    print("\n\n Lista Carpetas : " , usuList , "\n\n")

    labels = []
    facesData = []
    label = 0

    # Recorremos carpeta por carpeta para detectar las capturas
    for nameDir in usuList:
        dirUsu = rutaData + '/' + nameDir
        print("\t\t Leyendo Carpeta : " + dirUsu)

        for capturaX in os.listdir(dirUsu):
            labels.append(label)

            facesData.append(cv2.imread(dirUsu + '/' + capturaX, 0))
            img = cv2.imread(dirUsu + '/' + capturaX, 0)

            # 2 lineas de prueba
            # cv2.imshow('CapturaX', img)
            # cv2.waitKey(500)

        label = label + 1

    # cv2.destroyAllWindows()

    # Opciones de entrenamiento
    # faceLearn = cv2.face.EigenFaceRecognizer_create() # Genero Error
    faceLearn = cv2.face.LBPHFaceRecognizer_create()
    # faceLearn = cv2.face.FisherFaceRecognizer_create() # No se a probado

    print("\n Entrnando Reconocimiento")
    faceLearn.train(facesData, np.array(labels))

    print("\n Archivo XML de Entrenamiento creado")
    faceLearn.write('ModeloBdFaces.xml')

    # Pasamos a segunda funcion
    print("\n\n Presione cualquier tecla para trminar....") 
    msvcrt.getch()

if __name__ == "__main__":
    main()
    