from vision     import ReconocimientoFacial
from photo      import Camara
from pathlib    import Path
import time
base    = Path("photos_DB")
comp    = Path("photos_captured")
img     = comp / "img.jpg"

def LiveCam():
    webcam                 = Camara(base,comp).Stream()
    return webcam

def Reconocer():
    reconocimientoUsuario   = ReconocimientoFacial(img,base).coincidencia()
    return reconocimientoUsuario

def Coincidencia(resultado):
    if resultado["usuarioReconocido"]:
        return (f'''Usuario Reconocido : {resultado["usuario"]} con un {resultado["coincidencia"]}% de Coincidencia
        Realizando Accion Solicitada
                ''')
    else:
        return (f"Usuario no registrado Intente de Nuevo Porfavor")

def Menu():
    try:
        seleccion   = int(input(f'''-------------------------Menu-------------------------
        1.- Abrir/Cerrar Valvula de Gas
        2.- Abrir/Cerrar Puertas
        3.- Abrir Cerrar Percianas
        4.- Reproducir Musica
        5.- Ingresar Nuevo Usuario
        6.- Salir de la Aplicacion
        Opcion Seleccionada:  
        '''))
        return seleccion
    except ValueError:
        print("Opcion Invalida intente de nuevo porfavor")
        seleccion   = None
        return seleccion
    
def SubMenu():
    opciones    = [0,"Valvula de Gas","Puertas","Percianas","Reprodur Musica","Dar de alta nuevo Usuario"]
    listaOpciones   = Menu()
    if listaOpciones is not None:
        if listaOpciones >= 1 and listaOpciones <= 3:
            try:
                opcion  = int(input(f'''
                1.- Abrir {opciones[listaOpciones]} 
                2.- Cerrar {opciones[listaOpciones]}
                '''))
                return opcion,listaOpciones
            except ValueError:
                print("Opcion Invalida intente de nuevo porfavor")
                opcion  = None
                return opcion,listaOpciones

        elif listaOpciones in range(4,6):
                print(f'''          Se necesita Confirmacion para continuar con {opciones[listaOpciones]}
                Espere a que la camara inicie
                Coloquese de frente para el reconocimiento Facial
                Presione "S" para Capturar Imagen
                ''')
                try:
                    opcion  = int(input("Presione 1 para contuar : "))
                    return opcion,listaOpciones
                except ValueError:
                    print("Opcion Invalida Intente d eNuevo")
                    opcion  = None
                    return opcion,listaOpciones
        elif listaOpciones == 6:
                print("Saliendo de la Aplicación")
                opcion  = None
                return opcion,listaOpciones
def Desicion(camara):
    if camara:
        resultado       = Reconocer()
        coincidencia    = Coincidencia(resultado)
        print(f'''{coincidencia}
                     ''')
        time.sleep(0.5)
        regresar    = input('Pulse culquier tecla para Continuar ')
        return regresar
    else:
        pass
def Borrar():
    if img.exists():
        img.unlink()
                         