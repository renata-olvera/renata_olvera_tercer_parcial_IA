"""
Este programa trabaja con un grafo no dirigido formado por seis nodos:
A, B, C, D, E y F. Cada conexión tiene un peso que representa un costo.

La práctica consiste en obtener dos árboles usando Kruskal:
uno de mínimo coste y otro de máximo coste. En ambos casos se conectan
todos los nodos sin formar ciclos.

Conexiones usadas:
A-B(6), A-C(3), A-D(5)
B-C(2), B-E(4)
C-D(4), C-E(7)
D-F(8)
E-F(1)

Al ejecutar el archivo se muestra el procedimiento paso a paso en consola.
También se genera Grafica_Min_Max_Kruskal.html para ver el resultado con
Live Server.
"""

import os


CONEXIONES = [
    ("A", "B", 6),
    ("A", "C", 3),
    ("A", "D", 5),
    ("B", "C", 2),
    ("B", "E", 4),
    ("C", "D", 4),
    ("C", "E", 7),
    ("D", "F", 8),
    ("E", "F", 1)
]


UBICACION_NODOS = {
    "A": (120, 120),
    "B": (350, 90),
    "C": (230, 270),
    "D": (500, 250),
    "E": (390, 430),
    "F": (660, 360)
}


def nodos_del_grafo():
    """Obtiene los nodos que aparecen en la lista de conexiones."""

    nodos = set()

    for origen, destino, peso in CONEXIONES:
        nodos.add(origen)
        nodos.add(destino)

    return sorted(nodos)


def ver_conexiones():
    """Muestra el grafo original en consola."""

    print("\nCONEXIONES DEL GRAFO")
    print("-" * 42)
    print(f"{'Nodo 1':<10}{'Nodo 2':<10}{'Costo'}")
    print("-" * 42)

    for origen, destino, peso in CONEXIONES:
        print(f"{origen:<10}{destino:<10}{peso}")


def preparar_grupos(nodos):
    """Crea un grupo individual para cada nodo."""

    grupos = {}

    for nodo in nodos:
        grupos[nodo] = nodo

    return grupos


def buscar_raiz(grupos, nodo):
    """Busca el representante principal del grupo de un nodo."""

    while grupos[nodo] != nodo:
        nodo = grupos[nodo]

    return nodo


def unir_grupos(grupos, nodo_1, nodo_2):
    """
    Une dos grupos si son diferentes.

    Si los dos nodos ya están en el mismo grupo, unirlos formaría un ciclo.
    """

    raiz_1 = buscar_raiz(grupos, nodo_1)
    raiz_2 = buscar_raiz(grupos, nodo_2)

    if raiz_1 == raiz_2:
        return False

    grupos[raiz_2] = raiz_1
    return True


def mostrar_avance(nombre, seleccionadas, total):
    """Imprime las conexiones que ya fueron aceptadas."""

    print(f"\n{nombre}")
    print(f"{'Origen':<10}{'Destino':<10}{'Peso'}")
    print("-" * 30)

    if not seleccionadas:
        print("Aún no hay conexiones seleccionadas.")
    else:
        for origen, destino, peso in seleccionadas:
            print(f"{origen:<10}{destino:<10}{peso}")

    print(f"Costo acumulado: {total}")


def kruskal(modo):
    """
    Ejecuta Kruskal para mínimo o máximo coste.

    modo = "min" ordena las conexiones de menor a mayor.
    modo = "max" ordena las conexiones de mayor a menor.
    """

    nodos = nodos_del_grafo()
    grupos = preparar_grupos(nodos)
    seleccionadas = []
    total = 0

    if modo == "min":
        ordenadas = sorted(CONEXIONES, key=lambda dato: dato[2])
        nombre = "ÁRBOL DE MÍNIMO COSTE"
    else:
        ordenadas = sorted(CONEXIONES, key=lambda dato: dato[2], reverse=True)
        nombre = "ÁRBOL DE MÁXIMO COSTE"

    print("\n" + "=" * 52)
    print(f"PROCEDIMIENTO: {nombre}")
    print("=" * 52)

    print("\nOrden en que se revisarán las conexiones:")
    for origen, destino, peso in ordenadas:
        print(f"{origen}-{destino}({peso})")

    paso = 1

    for origen, destino, peso in ordenadas:
        print("\n" + "-" * 52)
        print(f"PASO {paso}")
        print("-" * 52)
        print(f"Conexión revisada: {origen} - {destino} con peso {peso}")

        raiz_origen = buscar_raiz(grupos, origen)
        raiz_destino = buscar_raiz(grupos, destino)

        print(f"Grupo de {origen}: {raiz_origen}")
        print(f"Grupo de {destino}: {raiz_destino}")

        if unir_grupos(grupos, origen, destino):
            print("Se acepta porque conecta grupos diferentes.")

            seleccionadas.append((origen, destino, peso))
            total += peso
        else:
            print("Se rechaza porque formaría un ciclo.")

        mostrar_avance(nombre, seleccionadas, total)

        if len(seleccionadas) == len(nodos) - 1:
            print("\nYa se tienen las conexiones necesarias para unir todos los nodos.")
            break

        paso += 1

    return seleccionadas, total


def claves_arbol(arbol):
    """Convierte las conexiones seleccionadas en claves comparables."""

    return {
        tuple(sorted((origen, destino)))
        for origen, destino, peso in arbol
    }


def filas_tabla(arbol):
    """Genera las filas HTML para una tabla."""

    filas = ""

    for origen, destino, peso in arbol:
        filas += f"""
        <tr>
          <td>{origen}</td>
          <td>{destino}</td>
          <td>{peso}</td>
        </tr>
        """

    return filas


def crear_elementos_svg(arbol_min, arbol_max):
    """Crea el dibujo SVG del grafo."""

    min_claves = claves_arbol(arbol_min)
    max_claves = claves_arbol(arbol_max)

    lineas = ""
    nodos = ""

    for origen, destino, peso in CONEXIONES:
        x1, y1 = UBICACION_NODOS[origen]
        x2, y2 = UBICACION_NODOS[destino]
        clave = tuple(sorted((origen, destino)))

        es_min = clave in min_claves
        es_max = clave in max_claves

        if es_min and es_max:
            color = "#9333ea"
            grosor = 6
            clase = "ambos"
        elif es_min:
            color = "#db2777"
            grosor = 5
            clase = "minimo"
        elif es_max:
            color = "#0ea5e9"
            grosor = 5
            clase = "maximo"
        else:
            color = "#9ca3af"
            grosor = 2
            clase = "normal"

        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2

        lineas += f"""
        <g class="arista {clase}">
          <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"
                stroke="{color}" stroke-width="{grosor}" />
          <circle cx="{mx}" cy="{my}" r="14" fill="#fff7fb" />
          <text x="{mx}" y="{my + 5}" text-anchor="middle"
                font-size="13" font-weight="bold">{peso}</text>
        </g>
        """

    for nodo, (x, y) in UBICACION_NODOS.items():
        nodos += f"""
        <g>
          <circle cx="{x}" cy="{y}" r="27"
                  fill="#ffffff" stroke="#9d174d" stroke-width="2" />
          <text x="{x}" y="{y + 6}" text-anchor="middle"
                font-size="16" font-weight="bold">{nodo}</text>
        </g>
        """

    return lineas + nodos


def crear_html(arbol_min, costo_min, arbol_max, costo_max):
    """Genera el archivo HTML interactivo para Live Server."""

    archivo = "Grafica_Min_Max_Kruskal.html"

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Kruskal - Mínimo y Máximo Coste</title>

  <style>
    body {{
      margin: 0;
      padding: 20px;
      font-family: Arial, sans-serif;
      background: #fff7fb;
      color: #312033;
    }}

    h1 {{
      text-align: center;
      color: #9d174d;
      margin-top: 0;
    }}

    .contenedor {{
      display: grid;
      grid-template-columns: 350px 1fr;
      gap: 18px;
    }}

    .tarjeta {{
      background: white;
      padding: 16px;
      border-radius: 14px;
      box-shadow: 0 8px 18px rgba(157, 23, 77, 0.15);
    }}

    .botones {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 14px;
    }}

    button {{
      border: none;
      padding: 10px;
      border-radius: 10px;
      color: white;
      font-weight: bold;
      cursor: pointer;
    }}

    .btn-min {{ background: #db2777; }}
    .btn-max {{ background: #0ea5e9; }}
    .btn-all {{ background: #9333ea; grid-column: span 2; }}

    svg {{
      width: 100%;
      height: 540px;
      background: #fff1f2;
      border: 1px solid #fbcfe8;
      border-radius: 14px;
    }}

    table {{
      width: 100%;
      margin-top: 10px;
      border-collapse: collapse;
    }}

    th, td {{
      padding: 8px;
      border-bottom: 1px solid #fce7f3;
      text-align: left;
    }}

    th {{
      background: #fdf2f8;
    }}

    .costo-min {{
      color: #db2777;
      font-size: 20px;
      font-weight: bold;
    }}

    .costo-max {{
      color: #0ea5e9;
      font-size: 20px;
      font-weight: bold;
    }}

    .nota {{
      color: #6b445f;
      line-height: 1.5;
    }}

    .oculto {{
      opacity: 0.15;
    }}
  </style>
</head>

<body>
  <h1>Árbol de Mínimo y Máximo Coste - Kruskal</h1>

  <div class="contenedor">
    <section class="tarjeta">
      <p class="nota">
        La gráfica muestra el grafo completo. Puedes cambiar la vista para
        resaltar el árbol de mínimo coste, el de máximo coste o ambos.
      </p>

      <div class="botones">
        <button class="btn-min" onclick="filtrar('minimo')">Ver mínimo</button>
        <button class="btn-max" onclick="filtrar('maximo')">Ver máximo</button>
        <button class="btn-all" onclick="filtrar('todo')">Ver ambos</button>
      </div>

      <h2>Árbol de mínimo coste</h2>
      <p>Costo total:</p>
      <p class="costo-min">{costo_min}</p>

      <table>
        <thead>
          <tr>
            <th>Origen</th>
            <th>Destino</th>
            <th>Peso</th>
          </tr>
        </thead>
        <tbody>
          {filas_tabla(arbol_min)}
        </tbody>
      </table>

      <h2>Árbol de máximo coste</h2>
      <p>Costo total:</p>
      <p class="costo-max">{costo_max}</p>

      <table>
        <thead>
          <tr>
            <th>Origen</th>
            <th>Destino</th>
            <th>Peso</th>
          </tr>
        </thead>
        <tbody>
          {filas_tabla(arbol_max)}
        </tbody>
      </table>
    </section>

    <section class="tarjeta">
      <svg viewBox="0 0 760 540">
        {crear_elementos_svg(arbol_min, arbol_max)}
      </svg>
    </section>
  </div>

  <script>
    function filtrar(tipo) {{
      const aristas = document.querySelectorAll(".arista");

      aristas.forEach(arista => {{
        arista.classList.remove("oculto");

        if (tipo === "minimo") {{
          if (!arista.classList.contains("minimo") &&
              !arista.classList.contains("ambos")) {{
            arista.classList.add("oculto");
          }}
        }}

        if (tipo === "maximo") {{
          if (!arista.classList.contains("maximo") &&
              !arista.classList.contains("ambos")) {{
            arista.classList.add("oculto");
          }}
        }}
      }});
    }}
  </script>
</body>
</html>
"""

    salida = os.path.join(os.path.dirname(__file__), archivo)

    with open(salida, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\nArchivo generado: {archivo}")
    print("Ábrelo con Live Server para ver la gráfica interactiva.")


def main():
    """Controla la ejecución completa de la práctica."""

    print("Simulador de Kruskal: mínimo y máximo coste")
    print("-" * 52)

    ver_conexiones()

    minimo, costo_minimo = kruskal("min")
    maximo, costo_maximo = kruskal("max")

    print("\nRESULTADOS FINALES")
    print("-" * 52)

    mostrar_avance("ÁRBOL DE MÍNIMO COSTE", minimo, costo_minimo)
    mostrar_avance("ÁRBOL DE MÁXIMO COSTE", maximo, costo_maximo)

    crear_html(minimo, costo_minimo, maximo, costo_maximo)


if __name__ == "__main__":
    main()