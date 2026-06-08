# Simulador de Kruskal para Árbol de Mínimo y Máximo Coste

## ¿Qué es?

El algoritmo de Kruskal es un método utilizado para construir un árbol de expansión dentro de un grafo conectado, no dirigido y con pesos.

Un árbol de expansión es una selección de conexiones que permite unir todos los nodos del grafo sin formar ciclos.

En esta práctica se trabaja con dos variantes:

El árbol de mínimo coste, que busca conectar todos los nodos usando la menor suma posible de pesos.

El árbol de máximo coste, que busca conectar todos los nodos usando la mayor suma posible de pesos, sin perder la condición de no formar ciclos.

## ¿Para qué sirve?

Sirve para analizar y construir redes de conexión de manera ordenada.

Cuando se usa para mínimo coste, ayuda a reducir recursos como cable, distancia, tiempo o dinero.

Cuando se usa para máximo coste, puede ayudar a elegir conexiones de mayor valor, mayor capacidad, mayor prioridad o mayor beneficio.

En ambos casos, el algoritmo evita conexiones repetidas o innecesarias porque no permite formar ciclos.

## ¿Cómo funciona?

Kruskal trabaja revisando las conexiones del grafo en un orden específico.

Para el árbol de mínimo coste, primero se ordenan las conexiones de menor a mayor peso.

Para el árbol de máximo coste, se ordenan de mayor a menor peso.

Después se revisa cada conexión. Si une dos grupos diferentes de nodos, se acepta. Si al agregarla se formaría un ciclo, se rechaza.

El proceso termina cuando todos los nodos están conectados. Para un grafo con n nodos, el árbol final debe tener n - 1 conexiones.

## ¿Cómo se implementa en el mundo?

En el mundo real puede implementarse en problemas donde se necesita conectar varios puntos de manera eficiente.

Por ejemplo, en redes eléctricas, telecomunicaciones, fibra óptica, tuberías, carreteras o conexiones entre equipos.

Si una empresa quiere reducir costos de instalación, puede usar el árbol de mínimo coste para elegir las conexiones más económicas.

Si se quiere priorizar conexiones con mayor capacidad o importancia, se puede analizar un árbol de máximo coste.

## ¿Cómo lo implementaría en mi vida?

Lo implementaría en situaciones donde necesite conectar varios puntos y comparar opciones.

Por ejemplo, si quisiera conectar dispositivos en una casa, taller o laboratorio, podría representar cada dispositivo como un nodo y cada cable como una conexión con cierto costo.

Con el árbol de mínimo coste podría encontrar una forma de conectar todo usando menos material.

También podría usar la idea del máximo coste para priorizar las conexiones más importantes o más fuertes, dependiendo del caso.

## ¿Cómo lo implementaría en mi trabajo o trabajo de ensueño?

En un trabajo relacionado con automatización, mecatrónica o ingeniería industrial, lo implementaría para analizar conexiones entre equipos dentro de una planta.

Los nodos podrían representar PLCs, sensores, robots, estaciones de trabajo, tableros eléctricos o módulos de control.

Las conexiones podrían tener pesos según la distancia, costo de instalación, dificultad de cableado, capacidad de comunicación o prioridad del equipo.

El árbol de mínimo coste ayudaría a reducir material y tiempo de instalación. El árbol de máximo coste podría utilizarse para priorizar conexiones críticas o de mayor capacidad.

## Conclusión

El algoritmo de Kruskal es útil porque permite construir redes conectadas sin ciclos y con un criterio claro de selección.

En esta práctica se realizó un simulador en Python que muestra paso a paso cómo se aceptan o rechazan conexiones. Además, se genera una visualización en HTML donde se pueden observar el árbol de mínimo coste y el árbol de máximo coste.