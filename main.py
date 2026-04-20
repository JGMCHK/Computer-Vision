from datetime   import date
import funciones
import time

hoy         = date.today()



while True:
    temporal    = funciones.Borrar()
    print(f'''Bienvenido a tu asistente de Hogar Inteligente
    porfavor dime como te puedo ayudar el dia de hoy {hoy}
    ''')
    submenu,menu    = funciones.SubMenu()
    if (menu >= 1 and menu <=3 ) and (submenu >= 1 and submenu <=2 ):
        print(f'''          Se necesita Confirmacion para continuar
                Espere a que la camara inicie
                Coloquese de frente para el reconocimiento Facial
                Presione "S" para Capturar Imagen
                ''')
        camara      = funciones.LiveCam()
        desicion    = funciones.Desicion(camara)
    elif menu ==4  and submenu == 1 :
        camara  = funciones.LiveCam()
        desicion    = funciones.Desicion(camara)
    elif menu ==5  and submenu == 1 :
        print("Espera a que alguien autorizado de los permisos necesarios")
        camara  = funciones.LiveCam()
        desicion    = funciones.Desicion(camara)
        print(f'''
            Para dar de alta un nuevo usuario espoere a que la camara se inicialice otra vez
            Precione la tecla "N"
            ''')
        camara  = funciones.LiveCam()
        resultado       = funciones.Reconocer()
        regresar    = input('Pulse culquier tecla para Continuar ')
    elif menu == 6:
        break
        