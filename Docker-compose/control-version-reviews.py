import fileinput
import subprocess

def actualizar_dockerfile(version_actual, version_deseada):
    valores_version = {
        'v1': {
            'SERVICE_VERSION': '${service_version:-v1}',
            'ENABLE_RATINGS': '${enable_ratings:-false}',
            'STAR_COLOR': '${star_color:-black}'
        },
        'v2': {
            'SERVICE_VERSION': '${service_version:-v2}',
            'ENABLE_RATINGS': '${enable_ratings:-true}',
            'STAR_COLOR': '${star_color:-black}'
        },
        'v3': {
            'SERVICE_VERSION': '${service_version:-v3}',
            'ENABLE_RATINGS': '${enable_ratings:-true}',
            'STAR_COLOR': '${star_color:-red}'
        }
    }

    if version_actual == version_deseada:
        print(f'La versión actual y la versión deseada son las mismas ({version_actual}). No se realiza ningún cambio.')
        return

    with fileinput.FileInput('Dockerfile-reviews', inplace=True) as archivo:
        for linea in archivo:
            for variable, valor in valores_version[version_deseada].items():
                linea = linea.replace(f'ENV {variable} {valores_version[version_actual][variable]}',
                                    f'ENV {variable} {valor}')
            print(linea, end='')

def copiar_archivo_compose(version):
    if version == 'v1':
        with open('docker-compose-v1.yml', 'r') as file:
            contenido = file.read()

        with open('docker-compose.yml', 'w') as file:
            file.write(contenido)
    elif version == 'v2':
        with open('docker-compose-v2.yml', 'r') as file:
            contenido = file.read()

        with open('docker-compose.yml', 'w') as file:
            file.write(contenido)
    elif version == 'v3':
        with open('docker-compose-v3.yml', 'r') as file:
            contenido = file.read()

        with open('docker-compose.yml', 'w') as file:
            file.write(contenido)
    else:
        print("Versión no válida")

version_actual = input("Ingrese la versión actual (v1, v2 o v3): ")
version_deseada = input("Ingrese la versión deseada (v1, v2 o v3): ")

actualizar_dockerfile(version_actual, version_deseada)
copiar_archivo_compose(version_deseada)

