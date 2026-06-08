# Simulador del Árbol Parcial Mínimo de Prim

## ¿Qué es?

El algoritmo de Prim es un procedimiento que permite encontrar un árbol parcial mínimo dentro de un grafo conectado, no dirigido y con pesos.

Un árbol parcial mínimo es una forma de conectar todos los nodos del grafo usando solamente las aristas necesarias, sin formar ciclos y procurando que la suma total de los pesos sea la menor posible.

En términos más sencillos, Prim ayuda a unir varios puntos gastando lo menos posible.

## ¿Para qué sirve?

Sirve para resolver problemas donde se necesita conectar varios elementos con el costo más bajo.

El peso de cada conexión puede representar distancia, dinero, tiempo, cable, energía o cualquier recurso que se quiera reducir.

Por eso, este algoritmo es útil en problemas de optimización donde se busca una red eficiente.

Algunos ejemplos son:

- Diseño de redes de cableado.
- Conexión de equipos de comunicación.
- Instalación de redes eléctricas.
- Planeación de tuberías.
- Distribución de servicios.
- Diseño de rutas internas en una planta.

## ¿Cómo funciona?

El algoritmo comienza desde un nodo inicial. A partir de ahí, revisa las aristas disponibles y selecciona la de menor peso que conecte con un nodo que todavía no ha sido agregado al árbol.

Después, el nuevo nodo se agrega al conjunto de nodos conectados y se revisan sus conexiones.

Este proceso se repite hasta que todos los nodos del grafo quedan conectados.

La regla principal es que en cada paso se elige la conexión más barata posible, siempre evitando formar ciclos.

## ¿Cómo se implementa en el mundo?

En el mundo real, Prim puede utilizarse para diseñar redes donde se busca reducir costos.

Por ejemplo, una empresa que necesita instalar cableado entre varias áreas puede representar cada área como un nodo y cada posible conexión como una arista con cierto costo.

Después, el algoritmo puede ayudar a elegir qué conexiones convienen más para que todas las áreas queden conectadas con el menor costo total.

También se puede aplicar en redes de internet, sistemas eléctricos, telecomunicaciones, distribución de agua o planeación de infraestructura.

## ¿Cómo lo implementaría en mi vida?

Lo implementaría en situaciones donde necesite conectar varios puntos sin gastar de más.

Por ejemplo, si quisiera organizar la conexión de varios dispositivos en una casa, taller o laboratorio, podría representar cada dispositivo como un nodo y medir la distancia entre ellos como el peso de cada conexión.

Con eso podría encontrar una forma de conectar todo usando menos cable y evitando conexiones innecesarias.

También podría aplicarse para organizar lugares o actividades relacionadas, buscando una manera eficiente de unirlas sin repetir caminos.

## ¿Cómo lo implementaría en mi trabajo o trabajo de ensueño?

En un trabajo relacionado con mecatrónica, automatización o ingeniería industrial, lo implementaría para diseñar conexiones dentro de una planta o línea de producción.

Por ejemplo, si se tienen sensores, PLCs, robots, estaciones de ensamble y módulos de control, cada uno podría representarse como un nodo.

Las conexiones podrían tener pesos dependiendo de la distancia, costo de cableado, dificultad de instalación o tiempo de mantenimiento.

Aplicando Prim, se podría obtener una red de conexión más eficiente, con menor costo y menos material desperdiciado.

Esto sería útil para mejorar instalaciones industriales, reducir gastos y mantener un sistema más ordenado.

## Conclusión

El algoritmo de Prim es una herramienta útil para optimizar conexiones dentro de un sistema.

En esta práctica se realizó un simulador en Python que muestra el procedimiento paso a paso en consola. Además, se generó una visualización en HTML donde se puede observar el grafo y el árbol parcial mínimo resaltado de forma interactiva.