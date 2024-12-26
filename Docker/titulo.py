import sys

def modificar_codigo(numero_grupo):
    
    archivo_path = '/practica_creativa2/bookinfo/src/productpage/templates/productpage.html'
        
    with open(archivo_path, 'r') as archivo:
        contenido = archivo.read()

    # Reemplazar titulo"
    nuevo_contenido = contenido.replace("BookInfo Sample", f"Grupo {numero_grupo} - Página de Producto")

    # Reemplazar titulo pestaña"
    nuevo_contenido = nuevo_contenido.replace("Simple Bookstore App", f"Grupo {numero_grupo} - Página de Producto")

    with open(archivo_path, 'w') as archivo:
        archivo.write(nuevo_contenido)
        

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Uso: python3 modificar_codigo.py <numero_grupo>")
        sys.exit(1)

   
    numero_grupo = sys.argv[1]

    modificar_codigo(numero_grupo)


