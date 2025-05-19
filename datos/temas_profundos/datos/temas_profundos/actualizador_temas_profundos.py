import os
import subprocess
import shutil

def actualizar_temas_profundos():
    token = "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"

    # Repositorio de temas profundos (ajusta si cambia el nombre del repo)
    repo_url = f"https://{token}@github.com/sanchezbond007/predicacion_temas.git"

    # Ruta del proyecto
    ruta_base = "/home/anasirabond007/Documents/asistente_predicacion_codigo_fuente"

    # Ruta temporal para clonar
    ruta_temp = os.path.join(ruta_base, "temas_temp")

    # Ruta de destino final
    ruta_destino = os.path.join(ruta_base, "datos", "temas_profundos")

    # Elimina carpeta temporal si existe
    if os.path.exists(ruta_temp):
        shutil.rmtree(ruta_temp)

    print("Clonando el repositorio de temas profundos...")
    subprocess.run(["git", "clone", repo_url, ruta_temp])

    # Mueve archivos .json a temas_profundos
    if os.path.exists(ruta_temp):
        archivos_json = [f for f in os.listdir(ruta_temp) if f.endswith(".json")]
        os.makedirs(ruta_destino, exist_ok=True)

        for archivo in archivos_json:
            origen = os.path.join(ruta_temp, archivo)
            destino = os.path.join(ruta_destino, archivo)
            shutil.move(origen, destino)
            print(f"Archivo actualizado: {archivo}")

        shutil.rmtree(ruta_temp)
        print("Actualización completada y carpeta temporal eliminada.")
    else:
        print("No se pudo clonar el repositorio.")

if __name__ == "__main__":
    actualizar_temas_profundos()
