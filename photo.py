import cv2
from pathlib    import Path
from datetime   import date




class Camara():
    def __init__(self,newReg,tempReg):
        self.newReg     = newReg
        self.tempReg    = tempReg
    def _Deteccion(self):
        faceModel           = Path(cv2.data.haarcascades)/"haarcascade_frontalface_default.xml"
        deteccionRostro     = cv2.CascadeClassifier(faceModel)
        return deteccionRostro
    def _Conexion(self):
        conexion_camara     = cv2.VideoCapture(0)
        return conexion_camara
    def Stream(self):
        iniciarComp     = False
        conexionCamara  = self._Conexion()
        rostroDetectado = self._Deteccion()
        while True:
            exito,imagen    = conexionCamara.read()
            if exito:
                escalaGris          = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
                rostros             = rostroDetectado.detectMultiScale(escalaGris)
                for (x,y,w,h) in rostros:
                    cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.imshow("Camara",imagen)
                tecla   = cv2.waitKey(1)
                if tecla == 110:
                    desicion    = input('Desea Guardar esta foto y/n: ').lower()
                    if desicion == "y":
                        now         = date.today()
                        userName    = input("Ingrese nombre de Usuario :")
                        userNameJPG = userName+'_'+str(now) +'.jpg'
                        cv2.imwrite(self.newReg/userNameJPG,imagen)
                        conexionCamara.release()
                        cv2.destroyAllWindows()
                        break
                    else:
                        pass
                elif tecla  == 115 and len(rostros) == 1:
                    print("Comenzando Comparacion")
                    cv2.imwrite(self.tempReg/"img.jpg",imagen)
                    conexionCamara.release()
                    cv2.destroyAllWindows()
                    iniciarComp  = True
                    break
                elif tecla == 115 and len(rostros) == 0:
                    print("Asegurese de que su rostro esta siendo detectado")
                elif tecla == 115 and len(rostros) > 1:
                    print("Asegurese de que solo haya un rostro a la vez")
                elif tecla == -1:     
                    pass
                else:
                    print("Opcion Invalida, Intente de Nuevo")
                    pass
            else:
                print("Captura Fallida, Reintentando")
                pass
        return iniciarComp