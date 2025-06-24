# 🖊️ HolaMundoBoard

Un sencillo proyecto web con Flask para dejar mensajes en un muro digital.

---

## Descripción

HolaMundoBoard es una aplicación web minimalista donde los usuarios pueden dejar mensajes públicos y ver los mensajes anteriores. Está construido con Flask y utiliza un archivo JSON para almacenar los mensajes. 


---

## Características

- Envío de mensajes con nombre y texto.
- Visualización de los últimos 20 mensajes.
- Diseño simple y limpio con Bootstrap.
- Sin necesidad de registro o autenticación.
- Código fácil de entender y modificar.



## 🛠️ Tecnologías usadas

- Python 3
- Flask
- HTML + Jinja2
- Bootstrap (CDN)
- JSON para almacenamiento


## Instalación

**1️⃣. Clona este repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/HolaMundoBoard.git
   cd HolaMundoBoard
```

**2️⃣ Crea y activa un entorno virtual (opcional pero recomendado):**

```bash
python -m venv .venv
source .venv/bin/activate     # En Linux / macOS
.venv\Scripts\activate        # En Windows PowerShell
```

**3️⃣Instala las dependencias**

```bash
pip install -r requirements.txt
```

**4️⃣Ejecutar:**

```bash
flask --app app.py run   
```

**5️⃣Luego de ejecutar el servidor abrir en el navegador**


```bash
http://127.0.0.1:5000/
```


## 🌎Contribuciones

Este proyecto es para aprendizaje y portafolio. Si quieres sugerir mejoras o reportar algún problema, por favor abre un issue o pull request!.
