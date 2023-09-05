from ArchAux import CreaBD as crear
from ArchAux import ReconoFace as registro
import os, getpass

def app():
    os.system("cls")
    opc = input("""
    SELECCIONE UNA OPCION
        
        1. Crear nuevo Perfil
        2. Registrar Entrad/Salida
        3. Traer Archivo Registro
        4. Salir
        **
            Opcion: """)

    if opc != '1' and opc!='2' and opc!='3':
        print('Opcion no Valida')
        app()
    elif opc == '1':
        p = getpass.getpass(prompt='\t\tIngese clave: ')
        if p == '1073672345':
            crear.main()
        else:
            print("Calve NO es correcta")
            app()
    elif opc == '2':
        registro.main()
    elif opc == '3':
        os.system("cls")
        print("Copiando Archivo de Registros")
        #rutaData = os.getcwd()
        archivo = 'Registro.csv'        
        print(os.path.exists(archivo))
        
        #shutil.copy(archivo,"Downloads\\"+archivo)


    else:
        exit()

if __name__ == "__main__":
    app()
