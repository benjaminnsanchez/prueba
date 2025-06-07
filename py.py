from fastapi import FastAPI
import sqlite3

from fastapi.middleware.cors import CORSMiddleware
origins = ["https://prueba-4-6cgf.onrender.com","http://127.0.0.1:8000"]

conexion = sqlite3.connect("producto.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS productos(id_producto INTEGER PRIMARY KEY AUTOINCREMENT, precio INTEGER,stock INTEGER,nombre TEXT)")
cursor.execute("INSERT INTO productos (precio, stock,nombre) VALUES(?,?,?)", (33,33,"hsk"))
conexion.commit()
productos = cursor.execute("SELECT * FROM productos ")
resultado =productos.fetchall()
dicProductos = []
for i in resultado:
    dicProductos.append({"nombre": i[1], "precio": i[2],  "stock": i[3]})
print(dicProductos)
app = FastAPI()  
@app.get("/")
def main():
    return dicProductos