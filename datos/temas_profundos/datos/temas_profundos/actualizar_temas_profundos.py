import os
import json

RUTA_TEMAS_PROFUNDOS = "datos/temas_profundos"

def cargar_temas_profundos():
    if not os.path.exists(RUTA_TEMAS_PROFUNDOS):
        print(f"No se encontró la carpeta: {RUTA_TEMAS_PROFUNDOS}")
        return

    archivos = [f for f in os.listdir(RUTA_TEMAS_PROFUNDOS) if f.endswith(".json")]
    if not archivos:
        print("No se encontraron archivos JSON en la carpeta temas_profundos.")
        return

    total_temas = 0
    print(f"\nLeyendo archivos en: {RUTA_TEMAS_PROFUNDOS}\n")
    for archivo in sorted(archivos):
        ruta_completa = os.path.join(RUTA_TEMAS_PROFUNDOS, archivo)
        try:
            with open(ruta_completa, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                temas = datos.get("temas", [])
                cantidad = len(temas)
                total_temas += cantidad
                print(f" - {archivo}: {cantidad} temas")
        except Exception as e:
            print(f" ! Error al leer {archivo}: {e}")

    print(f"\nTOTAL DE TEMAS PROFUNDOS CARGADOS: {total_temas}\n")

if __name__ == "__main__":
    cargar_temas_profundos()
