# video guia - https://www.youtube.com/watch?v=xa804S90WWw
import glob, os, msvcrt, shutil, cv2, imutils
from . import Entrenamiento as enternar

def capturas(usu_new):

    # Cargamos funciones del reconocimiento
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    faceClasific = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    contadorImg = 0

    while True:
        ret, frame = cap.read()
        if ret == False:
            break

        frame = imutils.resize(frame, width=400)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()

        faces = faceClasific.detectMultiScale(gray, 1.3, 5)

        # Remarcamos el area del rostro
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            rostro = auxFrame[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (720, 720), interpolation=cv2.INTER_CUBIC)

            # Tomamos la captura y guardamos en la carpeta creada
            f = cv2.waitKey(1)
            if f == 107: # la key es la k de foto
                cv2.imwrite(usu_new + '\\rostro_{}.jpg'.format(contadorImg), rostro)
                contadorImg = contadorImg + 1
                print("\t Captura " + str(contadorImg))
 
        cv2.imshow('CapturasFotos presione la K', frame)
        

        k = cv2.waitKey(1)
        # Finalizamos si se cumple alguna cde las condiciones
        # Damos escape o Capturamos 9 fotos
        if k == 27:
            shutil.rmtree(usu_new)
            print("CARPETA ELIMINADA......")
            break
            # print (f)
        elif contadorImg >= 10:
            enternar.main()
            break        

def main():
    os.system("cls")
    # Agregamos infomacion para nueva carpeta
    rutaData = os.getcwd() + '\ImgUsu'
    ntUsu = input("\n\n Ingrese usuario NT : " )
    docUsu = input("\n Ingrese N_Doc usuario : " )
    personName = ntUsu + '_' + docUsu
    usu_new = rutaData + '\\' + personName

    # Validamos que no exista carpeta con numDocUsu
    dirExist = glob.glob(rutaData+"\\"+f"*_{str(docUsu)}")
    #print(dirExist)
    if len(dirExist) > 0: 
        dirExist = dirExist[0].split("\\")
        i = len(dirExist)-1
        print("\n\t Ya existe numero de documento -> " + dirExist[i])

    else:
        print("\n\t Carpeta Creada: " + personName)
        os.makedirs(usu_new)
        

    # Pasamos a segunda funcion
    print("\n\n Presione cualquier tecla para continuar....") 
    msvcrt.getch()
    capturas(usu_new)

if __name__ == "__main__":
    main()
    