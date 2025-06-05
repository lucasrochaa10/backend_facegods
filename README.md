# Face Gods - Backend 🔗

Este repositorio contiene el backend de mi proyecto **Face Gods**, una tienda online desarrollada como parte de mi **Trabajo de Fin de Grado** del ciclo de Desarrollo de Aplicaciones Web (DAW).

Este backend ha sido desarrollado en Python utilizando **FastAPI** y se conecta a **Firebase Firestore** como base de datos para almacenar los pedidos enviados desde el frontend.

---

## 🛠️ Tecnologías que he utilizado

- FastAPI (Python)
- Firebase Firestore (base de datos NoSQL)
- Firebase Admin SDK
- CORS para comunicación con frontend
- Pydantic para validación de modelos

---

## 🚀 Funcionalidades implementadas

- Endpoint `/pedido` que recibe los pedidos del cliente
- Validación del pedido con modelo `Pydantic`
- Guardado del pedido completo en Firebase Firestore
- Configuración segura mediante archivo `.env` (no subido al repo)

---

## 📦 Cómo ejecutar este backend en local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/lucasrochaa10/backend_facegods.git
2.Entrar en la carpeta del proyecto:


cd backend_facegods
3.Crear un entorno virtual:


python -m venv env

4.Activar el entorno:

En Windows:

.\env\Scripts\activate
En Mac/Linux:


source env/bin/activate
Instalar dependencias:


pip install -r requirements.txt
Colocar el archivo firebase-key.json (clave privada) en la raíz del proyecto

⚠️ Este archivo no se sube al repositorio por seguridad.

Crear un archivo .env con el siguiente contenido:

FIREBASE_CREDENTIALS=firebase-key.json
FIREBASE_COLLECTION=pedidos
Ejecutar el servidor:


uvicorn main:app --reload
El backend estará disponible en: http://localhost:8000

🔗 Frontend relacionado
Este backend recibe los pedidos desde el frontend Angular que también he desarrollado:
👉 https://github.com/lucasrochaa10/facegods-frontend

👨‍💻 Autor
Lucas Rocha
Alumno del ciclo de Desarrollo de Aplicaciones Web (DAW)
Trabajo de Fin de Grado 2025












