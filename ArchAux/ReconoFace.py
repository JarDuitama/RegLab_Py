# video guia - https://www.youtube.com/watch?v=xa804S90WWw
import cv2, glob, os, csv
import datetime as dt

def capturasLive(usuList,indice):

    # Ceamos una matriz de reconocimiento 
    # faceLearn = cv2.face.EigenFaceRecognizer_create() # Genero Error
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    # faceLearn = cv2.face.FisherFaceRecognizer_create() # No se a probado

    # Tomamos la matriz ya creada con los diferentes usuarios
    face_recognizer.read('ModeloBdFaces.xml')

    # Cargamos funciones del reconocimiento
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    faceClasific = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    matriz = [] 
    #while True or len(matriz) < 3:
    while len(matriz) < 3:
        ret, frame = cap.read()
        if ret == False:
            break
        
        # capturamos laimagen u la pasamos a grises y validacion de xmls
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClasific.detectMultiScale(gray, 1.3, 5)

        # Remarcamos el area del rostro
        for (x, y, w, h) in faces:
            rostro = auxFrame[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)
            
            if result[1] > 75 and result[1] < 90 and int(result[0]) == (indice) :# and f == 114: # tecla r de registro
                cv2.putText(frame,'{}'.format(usuList[indice]), (x, y-25), 2, 1.1,(0, 255, 0), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                #rutaData = os.getcwd()
                fchHra = dt.datetime.now()
                lista = [usuList[indice],int(result[1]),str(fchHra)]
                matriz.append(lista)

            else:
                cv2.putText(frame, 'DESCONOCIDO', (x, y-20), 2, 0.8, (0, 0, 233), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        cv2.imshow('ValidacionFace', frame)

        # Damos escape y cierra camara
        k = cv2.waitKey(1)
        if k == 27:
            matriz = []
            break

    cap.release()
    cv2.destroyAllWindows()
    
    # Guardamos el Registro
    if len(matriz) == 3:
        with open('Registro.csv', 'a', newline='') as reg:
            writer = csv.writer(reg, delimiter=',')
            writer.writerows(matriz)
    

def main():
    os.system("cls")
    rutaData = os.getcwd() + '\ImgUsu'
    usuList = os.listdir(rutaData)
    docUsu = input("\n Ingrese N_Doc : " )
    #print(" Lista carpetas -> ", usuList)

    # Validamos que exista carpeta con numDocUsu y tomamos el index
    dirExist = glob.glob(rutaData+"\\"+f"*_{str(docUsu)}")
    indice = 0
    if len(dirExist) > 0: 
        dirExist = dirExist[0].split("\\")
        i = len(dirExist)-1
        #print("\n\t Existe Carpeta -> " + dirExist[i])
        indice = usuList.index(dirExist[i])
        #print("\n\t El indice es -> " + str(indice))
        # Pasamos a segunda funcion
        capturasLive(usuList,indice)

    else:
        print("\n\t Usuario no registrado")
        

if __name__ == "__main__":
    main()
    