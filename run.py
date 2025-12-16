import uvicorn
import webbrowser
import threading

def open_swagger():
    webbrowser.open("http://127.0.0.1:8000/docs#/")

if __name__ == "__main__":

    #Abrir navegador automáticamente
    threading.Timer(1.5, open_swagger).start()

    #Correr FastAPI
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)