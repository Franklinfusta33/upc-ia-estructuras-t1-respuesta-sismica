"""T1: instrucciones. No finge haber descargado datos ni entrenado modelos."""

from pathlib import Path

if __name__ == "__main__":
    print("Proyecto UPC T1 | predicción de desplazamiento espectral")
    print("1. Descarga el flatfile NGA-West2 desde https://peer.berkeley.edu/node/74")
    print("2. Verifica columnas y unidades para Sa(0.80 s, 5 %), Mw, distancia y Vs30")
    print("3. Documenta el dataset en data/README.md antes de iniciar T2")
    print("Datos locales disponibles:", [p.name for p in Path("data").glob("*.csv")])
