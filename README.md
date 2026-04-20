# Proyecto 6: Computer Vision

## Descripción del proyecto

Este proyecto implementa un prototipo de asistente de hogar inteligente que utiliza visión por computadora y reconocimiento facial para validar la identidad del usuario antes de ejecutar ciertas acciones. El sistema emplea `OpenCV` para la captura de video en tiempo real y la detección de rostros, y utiliza `DeepFace` para comparar la imagen capturada contra una base de datos local de usuarios registrados.

El objetivo del proyecto es simular un esquema básico de seguridad biométrica aplicado a tareas de automatización del hogar, por ejemplo:

- abrir o cerrar la válvula de gas
- abrir o cerrar puertas
- abrir o cerrar persianas
- reproducir música
- registrar nuevos usuarios

Una parte importante del flujo es que ciertas acciones requieren confirmación facial previa. Además, para dar de alta un nuevo usuario, primero debe autenticarse una persona ya autorizada.

## Tecnologías utilizadas

- Python
- OpenCV
- DeepFace
- TensorFlow
- tf-keras
- pathlib

## Estructura general del proyecto

- `main.py`
  Archivo principal. Controla el menú general del sistema y el flujo de ejecución.

- `funciones.py`
  Contiene funciones de apoyo para mostrar menús, inicializar la cámara, ejecutar el reconocimiento facial y mostrar el resultado de la coincidencia.

- `photo.py`
  Contiene la clase `Camara`, encargada de:
  - abrir la webcam
  - detectar rostros con Haar Cascades
  - guardar imágenes temporales para comparación
  - registrar nuevos usuarios en la base de datos

- `vision.py`
  Contiene la clase `ReconocimientoFacial`, encargada de buscar coincidencias entre la imagen capturada y las imágenes almacenadas en la carpeta de usuarios registrados.

- `photos_DB/`
  Carpeta que funciona como base de datos de usuarios. Aquí se almacenan las fotos de los usuarios autorizados.

- `photos_captured/`
  Carpeta donde se guarda temporalmente la imagen que se toma al momento de realizar la comparación facial.

## Requisitos previos

Antes de ejecutar el proyecto se recomienda contar con:

- Python 3.10 o superior
- Webcam funcional
- Conexión a internet durante la instalación de dependencias

## Instructivo de uso

### 1. Clonar o descargar el proyecto

Descarga este repositorio y ubícate dentro de la carpeta del proyecto.

### 2. Crear un entorno virtual

En Windows, dentro de la carpeta del proyecto, ejecuta:

```powershell
python -m venv .venv
```

En Ubuntu o Linux en general, dentro de la carpeta del proyecto, ejecuta:

```bash
python3 -m venv .venv
```

### 3. Activar el entorno virtual

En PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

En CMD:

```cmd
.\.venv\Scripts\activate
```

En Ubuntu o Linux:

```bash
source .venv/bin/activate
```

### 4. Instalar dependencias

Con el entorno virtual activado, instala las librerías necesarias:

```powershell
pip install -r requirements.txt
```

En Ubuntu o Linux también puede usarse:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` incluye:

- `deepface`
- `opencv-python`
- `tensorflow`
- `tf-keras`

### 5. Verificar carpetas necesarias

Antes de ejecutar el sistema, asegúrate de que existan estas carpetas en la raíz del proyecto:

- `photos_DB`
- `photos_captured`

Si no existen, créalas manualmente.

### 5.1 Cargar una fotografía del usuario autorizado

Antes de utilizar el reconocimiento facial, es necesario colocar al menos una fotografía reciente del usuario autorizado dentro de la carpeta `photos_DB`.

Recomendaciones para esa fotografía:

- que el rostro se vea claramente
- que la imagen tenga buena iluminación
- que solo aparezca una persona en la foto
- que la fotografía sea reciente para mejorar la coincidencia

Esta imagen será utilizada como referencia para comparar la fotografía capturada por la cámara durante la ejecución del sistema.

### 6. Ejecutar el programa

Desde la carpeta raíz del proyecto, ejecuta:

```powershell
python main.py
```

En Ubuntu o Linux:

```bash
python3 main.py
```

## Funcionamiento general del sistema

Al iniciar el programa aparecerá un menú principal con distintas acciones del hogar inteligente.

Dependiendo de la opción seleccionada, el sistema solicitará confirmación facial antes de continuar.

### Acciones del menú

1. Abrir o cerrar válvula de gas  
2. Abrir o cerrar puertas  
3. Abrir o cerrar persianas  
4. Reproducir música  
5. Ingresar nuevo usuario  

## Flujo de reconocimiento facial

Cuando una opción requiere validación:

1. El sistema inicializa la cámara.
2. Se detecta el rostro del usuario en tiempo real.
3. El usuario debe colocarse frente a la cámara.
4. Cuando el sistema detecta un solo rostro, se presiona la tecla `S`.
5. La imagen capturada se guarda temporalmente en `photos_captured/img.jpg`.
6. Esa imagen se compara contra las fotos almacenadas en `photos_DB`.
7. Si existe coincidencia, el sistema muestra el nombre del usuario reconocido y autoriza la acción.
8. Si no existe coincidencia, se informa que el usuario no está registrado.

## Registro de un nuevo usuario

El alta de nuevos usuarios tiene un control adicional:

1. Primero se autentica una persona autorizada mediante reconocimiento facial.
2. Después de esa validación, el sistema vuelve a abrir la cámara.
3. Para registrar al nuevo usuario, se debe presionar la tecla `N`.
4. El sistema pedirá confirmación para guardar la imagen.
5. Después solicitará el nombre del nuevo usuario.
6. La foto se guarda dentro de `photos_DB` con el nombre del usuario y la fecha actual.

## Teclas utilizadas durante la cámara

- `S`
  Captura una imagen para realizar la comparación facial. Esta opción funciona cuando solo hay un rostro detectado.

- `N`
  Permite registrar un nuevo usuario en la base de datos.

## Consideraciones importantes

- Para la comparación facial, procura que solo haya una persona frente a la cámara.
- Si no se detecta ningún rostro, el sistema pedirá al usuario colocarse correctamente frente a la webcam.
- Si se detectan varios rostros al mismo tiempo, el sistema no realiza la comparación.
- La calidad de iluminación puede influir en la detección y en la coincidencia del reconocimiento.

## Ejemplo de uso

1. Ejecutar `python main.py`
2. Seleccionar una opción del menú, por ejemplo abrir una puerta
3. Esperar a que se inicialice la cámara
4. Colocarse frente a la webcam
5. Presionar `S` para capturar la imagen
6. Esperar el resultado del reconocimiento
7. Si el usuario está autorizado, el sistema indica que la acción puede realizarse

## Observaciones

Este proyecto es un prototipo académico orientado a demostrar la integración de:

- visión por computadora
- reconocimiento facial
- validación de identidad
- simulación de acciones de un hogar inteligente

No está pensado como un sistema de seguridad comercial final, sino como una prueba funcional de conceptos de inteligencia artificial y visión artificial.

## Limitaciones actuales

- El sistema requiere una fotografía inicial de referencia dentro de la carpeta `photos_DB` para poder reconocer al primer usuario autorizado.
- La precisión del reconocimiento depende de la iluminación, la calidad de la cámara y la posición del rostro frente a la webcam.
- El flujo de comparación funciona mejor cuando solo aparece una persona a la vez frente a la cámara.
- El sistema está diseñado como un prototipo académico, por lo que no incluye mecanismos avanzados de seguridad, cifrado o gestión de usuarios.
- Algunas decisiones del flujo se encuentran enfocadas en la demostración funcional del proyecto y no en un entorno de producción.

## Mejoras futuras

- Implementar un mecanismo de superusuario o administrador inicial para registrar al primer usuario sin depender de una carga manual de imagen.
- Agregar una interfaz gráfica para mejorar la experiencia de uso.
- Incorporar una eliminación automática más controlada de imágenes temporales.
- Mejorar el manejo de errores y validaciones de entrada del menú.
- Incorporar métodos de detección y reconocimiento más robustos para escenarios con iluminación variable.

## Conclusión

Este proyecto demuestra la integración de herramientas de visión por computadora y reconocimiento facial en un escenario aplicado a un hogar inteligente. Aunque se trata de una solución académica y prototipo, permite ilustrar de forma clara el uso de autenticación biométrica para autorizar acciones dentro de un sistema automatizado.
