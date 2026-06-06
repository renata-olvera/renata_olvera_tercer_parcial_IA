"""
Dijkstra encuentra el camino de menor costo desde un nodo inicial hacia
los demás nodos de un grafo con pesos no negativos.

Grafo usado:
A -> B(2), C(4)
B -> C(1), D(7)
C -> E(3)
E -> D(2), F(5)
D -> F(1)
F -> sin salidas

El programa muestra el proceso en consola y genera Ruta_Grafica.html
para visualizar el resultado con Live Server.
"""

import heapq
import os


# Grafo dirigido: cada nodo tiene sus salidas con su respectivo peso.
GRAFO = {
    "A": [("B", 2), ("C", 4)],
    "B": [("C", 1), ("D", 7)],
    "C": [("E", 3)],
    "D": [("F", 1)],
    "E": [("D", 2), ("F", 5)],
    "F": []
}


# Posiciones de los nodos para dibujarlos en el archivo HTML.
POSICIONES = {
    "A": (120, 90),
    "B": (300, 90),
    "C": (120, 260),
    "D": (480, 260),
    "E": (300, 420),
    "F": (600, 420)
}


def mostrar_grafo():
    """Muestra los nodos y conexiones disponibles."""

    print("\nNODOS Y CONEXIONES")
    print("-" * 45)

    for nodo, conexiones in GRAFO.items():
        if not conexiones:
            print(f"{nodo} -> sin salidas")
        else:
            texto = [f"{destino}({peso})" for destino, peso in conexiones]
            print(f"{nodo} -> {', '.join(texto)}")


def pedir_nodo(mensaje):
    """Pide un nodo válido al usuario."""

    while True:
        nodo = input(mensaje).strip().upper()

        if nodo in GRAFO:
            return nodo

        print(f"Nodo inválido. Usa: {', '.join(sorted(GRAFO.keys()))}")


def imprimir_tabla(distancias, anteriores, visitados):
    """Imprime el estado actual del algoritmo."""

    print("\nTABLA ACTUAL")
    print(f"{'Nodo':<8}{'Costo':<12}{'Anterior':<12}{'Visitado'}")
    print("-" * 45)

    for nodo in sorted(GRAFO.keys()):
        costo = "∞" if distancias[nodo] == float("inf") else distancias[nodo]
        anterior = "-" if anteriores[nodo] is None else anteriores[nodo]
        visitado = "Sí" if nodo in visitados else "No"

        print(f"{nodo:<8}{str(costo):<12}{anterior:<12}{visitado}")


def dijkstra(inicio):
    """Ejecuta Dijkstra desde el nodo inicial."""

    distancias = {nodo: float("inf") for nodo in GRAFO}
    anteriores = {nodo: None for nodo in GRAFO}
    visitados = set()

    distancias[inicio] = 0
    cola = [(0, inicio)]

    print("\nPROCESO DEL ALGORITMO")
    print("-" * 45)
    print(f"Nodo inicial: {inicio}")
    print("El nodo inicial vale 0 y los demás inician en infinito.")

    paso = 1

    while cola:
        costo_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual in visitados:
            continue

        print("\n" + "=" * 45)
        print(f"PASO {paso}")
        print("=" * 45)
        print(f"Nodo seleccionado: {nodo_actual}")
        print(f"Costo acumulado: {costo_actual}")

        visitados.add(nodo_actual)

        if not GRAFO[nodo_actual]:
            print(f"{nodo_actual} no tiene conexiones de salida.")

        for vecino, peso in GRAFO[nodo_actual]:
            nuevo_costo = costo_actual + peso

            print(f"\nRevisando {nodo_actual} -> {vecino}")
            print(f"Cálculo: {costo_actual} + {peso} = {nuevo_costo}")

            if nuevo_costo < distancias[vecino]:
                print(f"Se actualiza {vecino}: {distancias[vecino]} -> {nuevo_costo}")

                distancias[vecino] = nuevo_costo
                anteriores[vecino] = nodo_actual
                heapq.heappush(cola, (nuevo_costo, vecino))
            else:
                print(f"No se actualiza {vecino}")

        imprimir_tabla(distancias, anteriores, visitados)
        paso += 1

    return distancias, anteriores


def reconstruir_ruta(anteriores, inicio, destino):
    """Reconstruye la ruta desde el destino hacia el inicio."""

    ruta = []
    actual = destino

    while actual is not None:
        ruta.insert(0, actual)

        if actual == inicio:
            break

        actual = anteriores[actual]

    if ruta and ruta[0] == inicio:
        return ruta

    return []


def obtener_aristas():
    """Convierte el grafo en una lista de conexiones para dibujar."""

    aristas = []

    for origen, conexiones in GRAFO.items():
        for destino, peso in conexiones:
            aristas.append((origen, destino, peso))

    return aristas


def generar_html(ruta, inicio, destino, distancia):
    """Genera la gráfica en HTML para abrirla con Live Server."""

    archivo = "Ruta_Grafica.html"
    aristas_ruta = [(ruta[i], ruta[i + 1]) for i in range(len(ruta) - 1)]

    lineas_svg = ""
    nodos_svg = ""

    # Dibuja conexiones.
    for origen, destino_arista, peso in obtener_aristas():
        x1, y1 = POSICIONES[origen]
        x2, y2 = POSICIONES[destino_arista]

        en_ruta = (origen, destino_arista) in aristas_ruta
        color = "#f97316" if en_ruta else "#475569"
        grosor = 5 if en_ruta else 2

        medio_x = (x1 + x2) / 2
        medio_y = (y1 + y2) / 2

        lineas_svg += f"""
        <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"
              stroke="{color}" stroke-width="{grosor}" marker-end="url(#flecha)" />

        <text x="{medio_x}" y="{medio_y - 10}" text-anchor="middle"
              font-size="14" font-weight="bold">{peso}</text>
        """

    # Dibuja nodos.
    for nodo, (x, y) in POSICIONES.items():
        if nodo == inicio:
            color = "#fde68a"
        elif nodo == destino:
            color = "#a5f3fc"
        elif nodo in ruta:
            color = "#fed7aa"
        else:
            color = "#ffffff"

        nodos_svg += f"""
        <circle cx="{x}" cy="{y}" r="26" fill="{color}"
                stroke="#0f172a" stroke-width="2" />

        <text x="{x}" y="{y + 6}" text-anchor="middle"
              font-size="16" font-weight="bold">{nodo}</text>
        """

    ruta_texto = " → ".join(ruta) if ruta else "No existe ruta"
    distancia_texto = "∞" if distancia == float("inf") else distancia

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Ruta gráfica con Dijkstra</title>

  <style>
    body {{
      font-family: Arial, sans-serif;
      background: #f4f7fb;
      color: #1f2937;
      padding: 18px;
    }}

    h1 {{
      color: #1e3a8a;
      text-align: center;
    }}

    .layout {{
      display: grid;
      grid-template-columns: 300px 1fr;
      gap: 18px;
    }}

    .panel {{
      background: white;
      padding: 16px;
      border-radius: 10px;
      box-shadow: 0 8px 20px rgba(15, 23, 42, 0.08);
    }}

    svg {{
      width: 100%;
      height: 520px;
      background: #eef2ff;
      border-radius: 12px;
      border: 1px solid #c7d2fe;
    }}

    .ruta {{
      color: #f97316;
      font-weight: bold;
      font-size: 18px;
    }}
  </style>
</head>

<body>
  <h1>Ruta Gráfica de Dijkstra</h1>

  <div class="layout">
    <section class="panel">
      <h2>Resultado</h2>
      <p><strong>Inicio:</strong> {inicio}</p>
      <p><strong>Destino:</strong> {destino}</p>
      <p><strong>Distancia mínima:</strong> {distancia_texto}</p>
      <p><strong>Camino:</strong></p>
      <p class="ruta">{ruta_texto}</p>

      <p>
        La ruta más corta aparece en color naranja.
        El nodo inicial aparece en amarillo y el destino en azul.
      </p>
    </section>

    <section class="panel">
      <svg viewBox="0 0 750 520">
        <defs>
          <marker id="flecha" markerWidth="10" markerHeight="10"
                  refX="8" refY="3" orient="auto">
            <path d="M0,0 L0,6 L8,3 z" fill="#475569" />
          </marker>
        </defs>

        {lineas_svg}
        {nodos_svg}
      </svg>
    </section>
  </div>
</body>
</html>
"""

    salida = os.path.join(os.path.dirname(__file__), archivo)

    with open(salida, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\nArchivo generado: {archivo}")
    print("Ábrelo con Live Server para ver la gráfica.")


def main():
    """Control principal del programa."""

    print("Simulador del algoritmo de Dijkstra")
    print("-" * 45)

    mostrar_grafo()

    print("\nNodos disponibles:")
    print(", ".join(sorted(GRAFO.keys())))

    inicio = pedir_nodo("\nNodo inicial: ")
    destino = pedir_nodo("Nodo destino: ")

    distancias, anteriores = dijkstra(inicio)
    ruta = reconstruir_ruta(anteriores, inicio, destino)

    if ruta:
        distancia = distancias[destino]
    else:
        distancia = float("inf")

    print("\nRESULTADO FINAL")
    print("-" * 45)

    if ruta:
        print(f"Ruta encontrada: {' → '.join(ruta)}")
        print(f"Distancia total: {distancia}")
    else:
        print(f"No existe ruta desde {inicio} hasta {destino}.")

    generar_html(ruta, inicio, destino, distancia)


if __name__ == "__main__":
    main()