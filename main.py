from vision import ReconocimientoFacial
from pathlib    import Path


base    = Path("photos_DB")
comp    = Path("photos_captured")
img    = comp / "yoActual.jpg"

reconocimientoUsuario = ReconocimientoFacial(img,base).coincidencia()
print(reconocimientoUsuario)