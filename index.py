from fastapi import FastAPI

from routes.productosRouter import productoRouter
from routes.usuarioRouter import usuarioRouter
from routes.carritoRouter import carritoRouter
from routes.tiposRouter import tiposRouter

from config.metadata import Metadata

from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(
    openapi_tags=Metadata.tags,
    title= "FastAPI para TiendaMagia",
    description="CRUD usuarios y productos"
    )


origins= ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(productoRouter, prefix="/productos", tags=["productos"])
app.include_router(carritoRouter, prefix="/carrito", tags=["carrito"])
app.include_router(usuarioRouter, prefix="/usuario", tags=["usuarios"])
app.include_router(tiposRouter, prefix="/tipo", tags=["tipo"])
