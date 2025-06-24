#importamos las funciones desde flask
from flask import Flask, render_template, request, redirect
#Persistencia de datos. importamos json y modulo os
import json
import os

#Creamos la aplicacion flask

app = Flask(__name__)

#Lista donde se van a guardar los mensajes enviados

mensajes = []

#Ruta principal de la app, acepta tanto GET(para ver la pagina)
#como POST (cuando se envia el formulario)

@app.route("/", methods=["GET", "POST"])
def index():
    #Si el usuario envio el formulario (metodo POST)
    if request.method == "POST":
        #obtenemos los datos del formulario
        nombre = request.form["nombre"]
        mensaje = request.form["mensaje"]
        
        #agregamos el mensaje como una tupla (nombre, mensaje) a la lista mensajes = []
        mensajes.append({"nombre": nombre, "mensaje": mensaje})
        
        guardar_mensajes(mensajes)
        
        #redirigimos al inicio para que al actualizar no se vuelva a enviar el mismo mensaje
        return redirect("/")
    
    #si el metodo GET (o despues del redirect), mostramos la página con los mensajes ya guardados
    return render_template("index.html", mensajes=mensajes)

ARCHIVOS_MENSAJES = "mensajes.json"
def cargar_mensajes():
    if not os.path.exists(ARCHIVOS_MENSAJES):
        return [] #si no existe devuelve una lista vacia
    try:
        with open(ARCHIVOS_MENSAJES, 'r', encoding="UTF-8") as f:
            mensajes = json.load(f)
            return mensajes[-50:] #devolvemos solo los ultimos 20 mensajes
    except (json.JSONDecodeError, ValueError):
        #si el JSON esta corrupto o vacio, retornamos lista vacia
        return []

mensajes = cargar_mensajes()

def guardar_mensajes(mensajes):
    with open(ARCHIVOS_MENSAJES, "w", encoding="UTF-8") as f:
        json.dump(mensajes, f, indent=4, ensure_ascii=False)


#Este bloque hace que flask arranque la app si ejecutamos directamente el script

if __name__ == "__main__":
    app.run(debug=True)