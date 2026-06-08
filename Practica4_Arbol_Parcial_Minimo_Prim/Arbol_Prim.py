"""
Este archivo trabaja con un grafo de ejemplo formado por seis puntos:
A, B, C, D, E y F. Cada unión tiene un número asociado que representa
el costo de conexión entre dos puntos.

La práctica consiste en construir una red que conecte todos los puntos
sin repetir caminos innecesarios y procurando que la suma de costos sea
la más baja posible. Para lograrlo se aplica el algoritmo de Prim.

Conexiones utilizadas:
- A se une con B con costo 6, con C con costo 3 y con D con costo 5.
- B se une con A con costo 6, con C con costo 2 y con E con costo 4.
- C se une con A con costo 3, con B con costo 2, con D con costo 4 y con E con costo 7.
- D se une con A con costo 5, con C con costo 4 y con F con costo 8.
- E se une con B con costo 4, con C con costo 7 y con F con costo 1.
- F se une con D con costo 8 y con E con costo 1.

Al ejecutar el programa se muestra en consola cómo se van seleccionando
las conexiones. Al final se crea el archivo Prim.html, que se
abre con Live Server para ver la red y el árbol resultante de forma gráfica.
"""

import heapq
import json
import os


# Grafo no dirigido. Cada conexión aparece en ambos sentidos.
mapa = {
    "A": [("B", 6), ("C", 3), ("D", 5)],
    "B": [("A", 6), ("C", 2), ("E", 4)],
    "C": [("A", 3), ("B", 2), ("D", 4), ("E", 7)],
    "D": [("A", 5), ("C", 4), ("F", 8)],
    "E": [("B", 4), ("C", 7), ("F", 1)],
    "F": [("D", 8), ("E", 1)]
}


# Coordenadas para dibujar los nodos en el HTML.
nodos_html = [
    {"id": "A", "x": 120, "y": 120},
    {"id": "B", "x": 360, "y": 90},
    {"id": "C", "x": 240, "y": 260},
    {"id": "D", "x": 500, "y": 250},
    {"id": "E", "x": 380, "y": 420},
    {"id": "F", "x": 650, "y": 380}
]


def listar_conexiones():
    """Muestra el grafo completo en consola."""

    print("\nGRAFO DE TRABAJO")
    print("-" * 50)

    for nodo, conexiones in mapa.items():
        texto = [f"{vecino}({peso})" for vecino, peso in conexiones]
        print(f"{nodo} -> {', '.join(texto)}")


def pedir_inicio():
    """Pide un nodo inicial válido para comenzar el algoritmo."""

    opciones = ", ".join(sorted(mapa.keys()))

    while True:
        nodo = input("\nSelecciona el nodo inicial: ").strip().upper()

        if nodo in mapa:
            return nodo

        print(f"Nodo no válido. Opciones disponibles: {opciones}")


def aristas_sin_repetir():
    """Obtiene las aristas del grafo sin duplicarlas."""

    aristas = []
    usadas = set()

    for origen, conexiones in mapa.items():
        for destino, peso in conexiones:
            clave = tuple(sorted((origen, destino)))

            if clave not in usadas:
                aristas.append({
                    "from": origen,
                    "to": destino,
                    "weight": peso
                })
                usadas.add(clave)

    return aristas


def mostrar_resumen(parcial, total, visitados):
    """Imprime el avance actual del árbol parcial mínimo."""

    print("\nAvance del árbol:")
    print(f"Nodos conectados: {', '.join(sorted(visitados))}")
    print(f"{'Origen':<10}{'Destino':<10}{'Peso'}")
    print("-" * 28)

    if not parcial:
        print("Aún no se ha elegido ninguna arista.")
    else:
        for origen, destino, peso in parcial:
            print(f"{origen:<10}{destino:<10}{peso}")

    print(f"Costo acumulado: {total}")


def algoritmo_prim(inicio):
    """
    Ejecuta Prim desde el nodo inicial.

    Se usa una cola de prioridad para elegir siempre la arista disponible
    con menor peso.
    """

    visitados = {inicio}
    candidatas = []
    resultado = []
    costo = 0
    paso = 1

    # Se cargan las primeras aristas candidatas.
    for vecino, peso in mapa[inicio]:
        heapq.heappush(candidatas, (peso, inicio, vecino))

    print("\nPROCEDIMIENTO DEL ALGORITMO DE PRIM")
    print("-" * 50)
    print(f"Nodo inicial: {inicio}")

    while candidatas and len(visitados) < len(mapa):
        peso, origen, destino = heapq.heappop(candidatas)

        print("\n" + "=" * 50)
        print(f"PASO {paso}")
        print("=" * 50)
        print(f"Arista revisada: {origen} - {destino} con peso {peso}")

        if destino in visitados:
            print(f"No se agrega porque {destino} ya pertenece al árbol.")
            paso += 1
            continue

        print("Se agrega porque conecta un nodo nuevo con el árbol.")

        visitados.add(destino)
        resultado.append((origen, destino, peso))
        costo += peso

        # Se agregan nuevas candidatas desde el nodo recién conectado.
        for vecino, peso_vecino in mapa[destino]:
            if vecino not in visitados:
                heapq.heappush(candidatas, (peso_vecino, destino, vecino))
                print(f"Nueva candidata: {destino} - {vecino} peso {peso_vecino}")

        mostrar_resumen(resultado, costo, visitados)
        paso += 1

    return resultado, costo


def preparar_tramos(arbol):
    """Convierte las aristas seleccionadas en formato fácil para JavaScript."""

    return [
        {"from": origen, "to": destino, "weight": peso}
        for origen, destino, peso in arbol
    ]


def crear_html(inicio, arbol, costo_total):
    """Genera el archivo HTML interactivo para abrirlo con Live Server."""

    archivo = "Prim.html"

    datos = {
        "nodes": nodos_html,
        "edges": aristas_sin_repetir(),
        "start": inicio,
        "tree": preparar_tramos(arbol),
        "total": costo_total
    }

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Prim - Árbol Parcial Mínimo</title>

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
    }}

    .zona {{
      display: grid;
      grid-template-columns: 330px 1fr;
      gap: 18px;
    }}

    .tarjeta {{
      background: white;
      padding: 16px;
      border-radius: 14px;
      box-shadow: 0 8px 18px rgba(157, 23, 77, 0.15);
    }}

    label {{
      font-weight: bold;
      display: block;
      margin-top: 10px;
    }}

    select, button {{
      width: 100%;
      margin-top: 6px;
      padding: 10px;
      border-radius: 10px;
      border: 1px solid #f9a8d4;
    }}

    button {{
      background: #db2777;
      color: white;
      font-weight: bold;
      cursor: pointer;
    }}

    button:hover {{
      background: #be185d;
    }}

    svg {{
      width: 100%;
      height: 540px;
      background: #fff1f2;
      border: 1px solid #fbcfe8;
      border-radius: 14px;
    }}

    table {{
      width: 100%;
      margin-top: 12px;
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

    .total {{
      color: #be185d;
      font-size: 22px;
      font-weight: bold;
    }}

    .nota {{
      color: #6b445f;
      line-height: 1.5;
    }}
  </style>
</head>

<body>
  <h1>Árbol Parcial Mínimo con Prim</h1>

  <div class="zona">
    <section class="tarjeta">
      <p class="nota">
        La visualización muestra el grafo completo y resalta las aristas
        que forman el árbol parcial mínimo.
      </p>

      <label for="inicio">Nodo inicial</label>
      <select id="inicio"></select>

      <button onclick="calcularDesdePagina()">Recalcular en la página</button>

      <h2>Resultado</h2>
      <p><strong>Inicio:</strong> <span id="nodoInicio"></span></p>
      <p><strong>Costo total:</strong></p>
      <p class="total" id="costoTotal"></p>

      <h2>Aristas seleccionadas</h2>
      <table>
        <thead>
          <tr>
            <th>Origen</th>
            <th>Destino</th>
            <th>Peso</th>
          </tr>
        </thead>
        <tbody id="tabla"></tbody>
      </table>
    </section>

    <section class="tarjeta">
      <svg id="lienzo" viewBox="0 0 780 540"></svg>
    </section>
  </div>

  <script>
    const datosIniciales = {json.dumps(datos, ensure_ascii=False)};
    const nodos = datosIniciales.nodes;
    const aristas = datosIniciales.edges;

    const selector = document.getElementById("inicio");
    const lienzo = document.getElementById("lienzo");
    const tabla = document.getElementById("tabla");

    function llenarSelector() {{
      nodos.forEach(nodo => {{
        const opcion = document.createElement("option");
        opcion.value = nodo.id;
        opcion.textContent = nodo.id;
        selector.appendChild(opcion);
      }});

      selector.value = datosIniciales.start;
    }}

    function buscarNodo(id) {{
      return nodos.find(nodo => nodo.id === id);
    }}

    function crearListaAdyacencia() {{
      const lista = {{}};

      nodos.forEach(nodo => {{
        lista[nodo.id] = [];
      }});

      aristas.forEach(arista => {{
        lista[arista.from].push({{ to: arista.to, weight: arista.weight }});
        lista[arista.to].push({{ to: arista.from, weight: arista.weight }});
      }});

      return lista;
    }}

    function primWeb(inicio) {{
      const lista = crearListaAdyacencia();
      const visitados = new Set([inicio]);
      const candidatas = [];
      const arbol = [];
      let total = 0;

      lista[inicio].forEach(arista => {{
        candidatas.push({{ from: inicio, to: arista.to, weight: arista.weight }});
      }});

      while (candidatas.length > 0 && visitados.size < nodos.length) {{
        candidatas.sort((a, b) => a.weight - b.weight);
        const mejor = candidatas.shift();

        if (visitados.has(mejor.to)) {{
          continue;
        }}

        visitados.add(mejor.to);
        arbol.push(mejor);
        total += mejor.weight;

        lista[mejor.to].forEach(arista => {{
          if (!visitados.has(arista.to)) {{
            candidatas.push({{ from: mejor.to, to: arista.to, weight: arista.weight }});
          }}
        }});
      }}

      return {{ arbol, total }};
    }}

    function esDelArbol(arista, arbol) {{
      return arbol.some(rama => {{
        const igualNormal = rama.from === arista.from && rama.to === arista.to;
        const igualInvertido = rama.from === arista.to && rama.to === arista.from;
        return igualNormal || igualInvertido;
      }});
    }}

    function dibujar(arbol) {{
      lienzo.innerHTML = "";

      aristas.forEach(arista => {{
        const a = buscarNodo(arista.from);
        const b = buscarNodo(arista.to);
        const marcada = esDelArbol(arista, arbol);

        const linea = document.createElementNS("http://www.w3.org/2000/svg", "line");
        linea.setAttribute("x1", a.x);
        linea.setAttribute("y1", a.y);
        linea.setAttribute("x2", b.x);
        linea.setAttribute("y2", b.y);
        linea.setAttribute("stroke", marcada ? "#db2777" : "#9ca3af");
        linea.setAttribute("stroke-width", marcada ? "5" : "2");
        lienzo.appendChild(linea);

        const mx = (a.x + b.x) / 2;
        const my = (a.y + b.y) / 2;

        const peso = document.createElementNS("http://www.w3.org/2000/svg", "text");
        peso.setAttribute("x", mx);
        peso.setAttribute("y", my - 8);
        peso.setAttribute("text-anchor", "middle");
        peso.setAttribute("font-weight", "bold");
        peso.textContent = arista.weight;
        lienzo.appendChild(peso);
      }});

      nodos.forEach(nodo => {{
        const circulo = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        circulo.setAttribute("cx", nodo.x);
        circulo.setAttribute("cy", nodo.y);
        circulo.setAttribute("r", "27");
        circulo.setAttribute("fill", nodo.id === selector.value ? "#f9a8d4" : "#ffffff");
        circulo.setAttribute("stroke", "#9d174d");
        circulo.setAttribute("stroke-width", "2");
        lienzo.appendChild(circulo);

        const texto = document.createElementNS("http://www.w3.org/2000/svg", "text");
        texto.setAttribute("x", nodo.x);
        texto.setAttribute("y", nodo.y + 6);
        texto.setAttribute("text-anchor", "middle");
        texto.setAttribute("font-size", "16");
        texto.setAttribute("font-weight", "bold");
        texto.textContent = nodo.id;
        lienzo.appendChild(texto);
      }});
    }}

    function llenarTabla(arbol) {{
      tabla.innerHTML = "";

      arbol.forEach(arista => {{
        const fila = document.createElement("tr");
        fila.innerHTML = `
          <td>${{arista.from}}</td>
          <td>${{arista.to}}</td>
          <td>${{arista.weight}}</td>
        `;
        tabla.appendChild(fila);
      }});
    }}

    function calcularDesdePagina() {{
      const inicio = selector.value;
      const resultado = primWeb(inicio);

      document.getElementById("nodoInicio").textContent = inicio;
      document.getElementById("costoTotal").textContent = resultado.total;

      llenarTabla(resultado.arbol);
      dibujar(resultado.arbol);
    }}

    llenarSelector();
    calcularDesdePagina();
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
    """Control principal del programa."""

    print("Simulador del algoritmo de Prim")
    print("-" * 50)

    listar_conexiones()

    print("\nNodos disponibles:")
    print(", ".join(sorted(mapa.keys())))

    inicio = pedir_inicio()
    arbol, costo = algoritmo_prim(inicio)

    print("\nRESULTADO FINAL")
    print("-" * 50)

    for origen, destino, peso in arbol:
        print(f"{origen} - {destino}: {peso}")

    print(f"\nCosto total del árbol parcial mínimo: {costo}")

    crear_html(inicio, arbol, costo)


if __name__ == "__main__":
    main()