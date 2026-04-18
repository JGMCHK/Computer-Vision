from deepface   import DeepFace
from pathlib    import Path
class   ReconocimientoFacial():
    def __init__(self,imgCapt,imgDB):
        self.imgCapt    = imgCapt
        self.imgDB      = imgDB
    def _buscar(self):
        resultado   = DeepFace.find(self.imgCapt,self.imgDB)
        return resultado
    def _comparacion(self):
        frame   = self._buscar()
        if frame[0].empty:
            datos   = {"user":None,"distancia":None,"umbral":None,"porcentaje":None}
            return datos
        else:
            datos   = {"user":Path(frame[0]['identity'][0]).stem,"distancia":frame[0]['distance'][0],"umbral":frame[0]['threshold'][0],"porcentaje":frame[0]['confidence'][0]}
            return datos
    def _decidir(self):
        cotejar = self._comparacion()
        if cotejar["user"] is None:
            resultante  =   {'usuarioReconocido':False,'usuario':None,'coincidencia':None}
            return resultante
        else:
            if cotejar['distancia']<=cotejar['umbral']:
                resultante  =   {'usuarioReconocido':True,'usuario':cotejar['user'],'coincidencia':cotejar['porcentaje']}
                return resultante
            else:
                resultante  =   {'usuarioReconocido':False,'usuario':cotejar['user'],'coincidencia':cotejar['porcentaje']}
                return resultante
    def coincidencia(self):
        conformidad = self._decidir()
        return conformidad