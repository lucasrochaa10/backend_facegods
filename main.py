from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from firebase_config import db, collection_name

app = FastAPI()

# ✅ Modelo completo que coincide con el formulario del frontend
class Pedido(BaseModel):
    nombre: str
    direccion: str
    cp: str
    ciudad: str
    provincia: str
    telefono: str
    email: str
    tarjeta: str
    expiracion: str
    cvv: str
    productos: list  # 👈 Array de productos del carrito

# 🌐 Orígenes permitidos
origins = [
    "http://localhost:4200",
    "https://facegods.web.app"
]

# 🛡️ Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📦 Ruta para crear pedido
@app.post("/pedido")
async def crear_pedido(pedido: Pedido):
    try:
        # Convierte el modelo en diccionario
        pedido_dict = pedido.dict()
        print("Pedido recibido:", pedido_dict)

        # Guarda en Firestore
        pedido_ref = db.collection(collection_name).document()
        pedido_ref.set(pedido_dict)

        return {"message": "Pedido guardado correctamente", "id": pedido_ref.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar el pedido: {str(e)}")
