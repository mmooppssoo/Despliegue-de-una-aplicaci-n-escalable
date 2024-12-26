import os
import subprocess
import json

def instalar_herramientas():
    subprocess.run(["sudo", "apt", "update"], check=True)
    subprocess.run(["sudo", "apt", "install", "--only-upgrade", "python3"], check=True)
    subprocess.run(["sudo", "apt", "install", "git"], check=True)
    subprocess.run(["sudo", "apt", "install", "python3-pip"], check=True)
    
def clonar_repositorio():
    subprocess.run(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"], check=True)

def modificar_requirements():
    with open("practica_creativa2/bookinfo/src/productpage/requirements.txt", "r") as file:
        lines = file.readlines()        
    with open("practica_creativa2/bookinfo/src/productpage/requirements.txt", "w") as file:
        for line in lines:
            if line.strip().startswith("requests=="):
                file.write("requests\n")  # Eliminar la versión específica de requests
            else:
                file.write(line)

def instalar_dependencias():
    os.chdir('practica_creativa2/bookinfo/src/productpage/')
    subprocess.run(["pip3", "install", "-r", "requirements.txt"], check=True)

def modificar_codigo(numero_grupo):
    with open('templates/productpage.html', 'r') as archivo:
        contenido = archivo.read()

    # Reemplazar titulo"
    nuevo_contenido = contenido.replace("BookInfo Sample", f"Grupo {numero_grupo} - Página de Producto")

    # Reemplazar titulo pestaña"
    nuevo_contenido = nuevo_contenido.replace("Simple Bookstore App", f"Grupo {numero_grupo} - Página de Producto")

    with open('templates/productpage.html', 'w') as archivo:
        archivo.write(nuevo_contenido)

def direccion_app(puerto):
    # Obtener la IP pública usando httpbin.org
    ip_publica = subprocess.check_output(["curl", "-s", "http://httpbin.org/ip"]).decode("utf-8")
    ip_json = json.loads(ip_publica)
    ip_direccion = ip_json["origin"]
    print(f"La aplicacion va a estar accesible desde http://{ip_direccion}:{puerto}/productpage")
    
def ejecutar_aplicacion(puerto):
    direccion_app(puerto)
    subprocess.run(["python3", "productpage_monolith.py", f"{puerto}"], check=True)

def main():

    # Establecer variable de entorno
    os.environ['GRUPO_NUMERO'] = '24'
    
    # Obtener el número de grupo desde la variable de entorno
    numero_grupo = os.getenv('GRUPO_NUMERO')
    
    puerto = 9080  # Puerto deseado para recibir peticiones
    
    instalar_herramientas()
    clonar_repositorio()
    modificar_requirements()
    instalar_dependencias()
    modificar_codigo(numero_grupo)
    ejecutar_aplicacion(puerto)

if __name__ == "__main__":
    main()
