from ArchAux import CreaBD as crear
from ArchAux import ReconoFace as registro
import os, getpass, shutil

def app():
    os.system("cls")
    opc = input("""
    SELECCIONE UNA OPCION
        
        1. Crear nuevo Perfil
        2. Registrar Entrad/Salida
        3. Exportar Archivo Registro
        4. Salir
        **
            Opcion: """
    )

    match opc:
        case '1':
            p = getpass.getpass(prompt='\t\tIngese clave: ')
            if p == '12345':
                crear.main()
            else:
                print("Calve NO es correcta")
                app()
        case '2':
           registro.main()
        case '3':
            os.system("cls")
            print("\n")
            print("Copiando Archivo de Registros\n\n")
            #rutaData = os.getcwd()
            archivo = 'Registro.csv'
            if (os.path.exists(archivo)):
                rutaDestino = input("Ingrese ruta de descarga:")
                shutil.copy(archivo,rutaDestino)

        case '4':
            exit

        case _:
            print('Opcion no Valida')
            app()

if __name__ == "__main__":
    app()
