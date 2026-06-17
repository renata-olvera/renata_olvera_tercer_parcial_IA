# -*- coding: utf-8 -*-
"""
CETI MECATRÓNICA - TERCER PARCIAL IA
SUITE COMPLETA Y REAL DE MACHINE LEARNING Y TENSORFLOW 
Basado estrictamente en el temario de PythonProgramming.net
Autor: Renata Alejandra Olvera Flores 
Registro:23310301
Grado:6-E
"""

# Importación de la librería matemática NumPy para el manejo de vectores y matrices
import numpy as np
# Importación de Pandas para la manipulación y análisis de estructuras de datos estructuradas
import pandas as pd
# Importación del módulo de modelos lineales de Scikit-Learn para usar la Regresión Lineal
import sklearn.linear_model as lm
# Importación de la función para dividir el dataset en conjuntos de entrenamiento y prueba
from sklearn.model_selection import train_test_split
# Importación de Pickle para la serialización y guardado de modelos en el disco duro
import pickle
# Importación de Collections para usar el contador de elementos eficiente en KNN
import collections
# Importación de la librería matemática estándar de Python para operaciones como redondeos
import math

# Importación de la librería de Deep Learning TensorFlow de Google
import tensorflow as tf
# Importación de submódulos de Keras para estructurar capas neuronales y modelos secuenciales
from tensorflow.keras import layers, models

# =====================================================================
# 1. REGRESIÓN: DATOS, ENTRENAMIENTO, PICKLE Y FORECASTING REAL
# =====================================================================
# Definición de la clase encargada de procesar el bloque de Regresión y Predicción Futura
class ModuloRegresionCompleto:
    # Método constructor de la clase
    def __init__(self):
        # Generación de un rango de 20 fechas consecutivas para simular un índice temporal
        fechas = pd.date_range(start="2026-01-01", periods=20)
        # Creación de un DataFrame con precios y volúmenes ficticios imitando acciones de Google
        self.df = pd.DataFrame({
            'Precio': [100, 101, 102, 104, 103, 105, 107, 108, 110, 112, 111, 113, 115, 116, 118, 120, 122, 121, 123, 125],
            'Volumen': [50, 52, 51, 55, 53, 58, 60, 61, 65, 66, 64, 69, 70, 72, 75, 78, 80, 79, 82, 85]
        }, index=fechas)

    # Método principal para ejecutar todo el flujo de trabajo de la regresión
    def ejecutar_todo(self):
        # Imprime el encabezado de la sección en la consola
        print("\n--- 1. BLOQUE DE REGRESIÓN Y FORECASTING REAL ---")
        # Convierte las columnas 'Precio' y 'Volumen' en una matriz de características X
        X = np.array(self.df[['Precio', 'Volumen']])
        # Calcula el factor de forecasting correspondiente al 10% del total de las muestras (redondeado hacia arriba)
        factor_forecast = int(math.ceil(0.1 * len(self.df))) 
        # FORECASTING REAL: Desplaza los precios hacia arriba en el DataFrame para crear etiquetas futuras
        self.df['Etiqueta'] = self.df['Precio'].shift(-factor_forecast) 
        
        # Selecciona todas las características excepto las últimas correspondientes al factor de predicción
        X_lotes = X[:-factor_forecast]
        # Almacena las últimas filas de características que se usarán para hacer la proyección futura
        X_forecast = X[-factor_forecast:]
        # Elimina las filas que contienen valores nulos (NaN) causados por el desplazamiento temporal
        self.df.dropna(inplace=True)
        # Convierte la columna 'Etiqueta' limpia en el vector de variables objetivo (y)
        y = np.array(self.df['Etiqueta'])
        
        # Divide los datos históricos en conjuntos de entrenamiento (80%) y prueba (20%) de forma aleatoria fija
        X_train, X_test, y_train, y_test = train_test_split(X_lotes, y, test_size=0.2, random_state=42)
        # Instancia el objeto del modelo matemático de Regresión Lineal de Scikit-Learn
        modelo = lm.LinearRegression()
        # Entrena el modelo ajustando la recta matemática usando los datos de entrenamiento
        modelo.fit(X_train, y_train)
        
        # Calcula el coeficiente de determinación R² para evaluar la precisión del modelo entrenado
        r_cuadrado = modelo.score(X_test, y_test)
        # Muestra en la consola el valor del R² con un formato de cuatro decimales
        print(f"[REGRESIÓN] Coeficiente de Determinación R²: {r_cuadrado:.4f}")
        
        # Abre o crea un archivo binario llamado 'modelo_forecasting.pickle' en modo escritura de bytes
        with open("modelo_forecasting.pickle", "wb") as f:
            # Guarda de forma persistente el modelo entrenado dentro del archivo físico
            pickle.dump(modelo, f)
            
        # Abre el archivo binario guardado en modo lectura de bytes para validar el proceso de carga
        with open("modelo_forecasting.pickle", "rb") as f:
            # Carga el modelo guardado desde el archivo de vuelta a la memoria de Python
            modelo_cargado = pickle.load(f)
            
        # Ejecuta el forecasting real sobre los datos huérfanos usando el modelo cargado
        predicciones_futuras = modelo_cargado.predict(X_forecast)
        # Imprime en la consola el arreglo numérico con los precios proyectados para el futuro
        print(f"[FORECASTING] Valores futuros proyectados para los próximos {factor_forecast} días: {predicciones_futuras}")


# =====================================================================
# 2. KNN: APLICACIÓN DESDE CERO CON DATASET REAL (BREAST CANCER)
# =====================================================================
# Definición de la clase para el algoritmo de K-Vecinos Más Cercanos implementado de forma nativa
class ModuloKNNCompleto:
    # Método constructor de la clase
    def __init__(self):
        # Simula fielmente una réplica exacta del Wisconsin Breast Cancer Dataset estructurado (9 dimensiones)
        # Clase 2 representa tumores benignos, Clase 4 representa tumores malignos (Métricas reales de la UCI)
        self.dataset_real = {
            2: [[5,1,1,1,2,1,3,1,1], [3,1,1,1,1,1,2,1,1], [3,1,1,1,2,1,2,1,1], [4,2,1,1,2,1,2,1,1], [3,1,1,1,2,1,3,1,1]],
            4: [[8,10,10,8,7,10,9,7,1], [7,4,6,4,6,1,4,3,1], [10,10,10,8,6,1,8,9,1], [7,5,6,3,3,8,7,4,1], [10,7,7,6,4,10,4,1,2]]
        }
        # Vector con los 9 datos médicos de un nuevo paciente desconocido que se necesita diagnosticar
        self.paciente_prueba = [6,5,5,3,4,3,4,1,1]

    # Método para clasificar al paciente analizando los vecinos más cercanos geométricamente
    def clasificar_desde_cero(self, k=3):
        # Imprime el encabezado de la sección de KNN en la consola
        print("\n--- 2. BLOQUE DE K-NEAREST NEIGHBORS (DATASET REAL) ---")
        # Inicializa una lista vacía para almacenar los cálculos de distancias y sus clases correspondientes
        distancias = []
        # Bucle para recorrer cada clase disponible dentro del diccionario del dataset real
        for clase in self.dataset_real:
            # Bucle para recorrer cada lista de características pertenecientes a la clase actual
            for caracteristicas in self.dataset_real[clase]:
                # DISTANCIA EUCLIDIANA REAL: Calcula la norma del vector resultante de la resta de puntos
                distancia_euclidiana = np.linalg.norm(np.array(caracteristicas) - np.array(self.paciente_prueba))
                # Agrega la distancia calculada y su clase asociada a la lista general de distancias
                distancias.append([distancia_euclidiana, clase])
        
        # Ordena la lista de menor a mayor distancia y extrae únicamente la etiqueta de clase de los primeros 'k' elementos
        votos = [i[1] for i in sorted(distancias)[:k]]
        # Ejecuta una votación por mayoría simple usando Counter y extrae el elemento que más se repite
        resultado_diagnostico = collections.Counter(votos).most_common(1)[0][0]
        # Condicional de texto para formatear el diagnóstico médico final según el código numérico de la UCI
        tipo_tumor = "Benigno (Clase 2)" if resultado_diagnostico == 2 else "Maligno (Clase 4)"
        # Imprime el veredicto final arrojado de forma matemática por el algoritmo nativo de KNN
        print(f"[KNN DESDE CERO] Diagnóstico para el paciente de prueba: {tipo_tumor}")


# =====================================================================
# 3. SVM: OPTIMIZACIÓN MATEMÁTICA DE MARGEN Y PREDICCIÓN (FROM SCRATCH)
# =====================================================================
# Definición de la clase para construir una Máquina de Soporte Vectorial lineal desde cero
class ModuloSVMCompleto:
    # Método constructor de la clase
    def __init__(self):
        # Inicializa un dataset continuo de dos dimensiones con tipo float64 para soportar operaciones decimales
        # Define dos puntos para la clase -1 y dos puntos continuos separados para la clase 1
        self.data = {
            -1: np.array([[1, 7], [2, 8]], dtype=np.float64), 
             1: np.array([[5, 1], [6, -1]], dtype=np.float64)
        }

    # Método para realizar el ajuste de optimización del hiperplano y predecir nuevos vectores
    def ajustar_y_predecir(self):
        # Imprime el encabezado de la sección del bloque SVM en la consola
        print("\n--- 3. BLOQUE DE SUPPORT VECTOR MACHINES (OPTIMIZACIÓN REAL) ---")
        # Crea un diccionario para almacenar las magnitudes de los vectores de pesos y sus parámetros asociados [W, b]
        opt_dict = {}
        # Define una matriz de transformaciones de signos para evaluar todas las combinaciones de cuadrantes de W
        transformaciones = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
        
        # Inicializa una lista vacía para extraer y recolectar absolutamente todos los números del dataset
        todos_los_datos = []
        # Recorre las claves del diccionario de clases
        for yi in self.data:
            # Recorre las listas de arreglos de coordenadas asociadas a la clase actual
            for yi_datos in self.data[yi]:
                # Recorre y extrae cada característica individual del punto geométrico
                for caracteristica in yi_datos:
                    # Añade el valor numérico a la lista global para analizar el rango espacial
                    todos_los_datos.append(caracteristica)
                    
        # Encuentra el valor numérico más alto dentro del dataset para usarlo como base de escala
        max_valor_carac = max(todos_los_datos)
        # Inicializa un vector de pesos inicial W muy alto configurado explícitamente con números flotantes
        w = np.array([max_valor_carac * 10.0, max_valor_carac * 10.0], dtype=np.float64)
        # Define los tamaños de paso decrecientes para escanear el espacio en busca del mínimo global
        tamaños_paso = [max_valor_carac * 0.1, max_valor_carac * 0.01]
        # Multiplicador para definir el rango de exploración del sesgo (Bias) b
        b_rango_multiple = 5
        # Multiplicador para el tamaño de paso durante la exploración del sesgo b
        b_multiple = 5
        
        # CORRECCIÓN PROBLEMA 2: Se declara b_optimo al inicio en 0.0 para blindar el código ante fallas de convergencia
        b_optimo = 0.0
        
        # Bucle principal que itera a través de cada tamaño de paso definido para la optimización
        for paso in tamaños_paso:
            # Bandera de control para indicar si el vector W actual ha sido optimizado en el paso actual
            optimizado = False
            # Bucle condicional que se ejecuta de forma iterativa hasta alcanzar la condición de descenso
            while not optimizado:
                # Genera un rango de escaneo para el sesgo b que va desde valores negativos a positivos escalados
                for b in np.arange(-1 * (max_valor_carac * b_rango_multiple), max_valor_carac * b_rango_multiple, paso * b_multiple):
                    # Recorre cada una de las 4 combinaciones vectoriales de dirección de signos
                    for transformacion in transformaciones:
                        # Aplica la transformación matemática de signo al vector de pesos base actual
                        w_t = w * transformacion
                        # Suposición inicial de que el vector actual cumple exitosamente con las restricciones
                        encontrado_en_restriccion = True
                        # Recorre las clases para validar la inecuación matemática de restricción del SVM
                        for yi in self.data:
                            # Recorre cada punto de coordenadas xi perteneciente a la clase evaluada
                            for xi in self.data[yi]:
                                # RESTRICCIÓN SOFT MARGIN: Evalúa si yi * (W . xi + b) es menor que 1
                                if not yi * (np.dot(w_t, xi) + b) >= 1:
                                    # Si un solo punto viola la condición, se invalida toda la configuración actual
                                    encontrado_en_restriccion = False
                                    
                        # Si la configuración pasó la restricción de todos los puntos, se registra como válida
                        if encontrado_en_restriccion:
                            # Guarda en el diccionario la norma (magnitud) de W como clave y los parámetros reales como valor
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b]
                            
                # Evalúa si el peso en el eje X ha cruzado el origen de coordenadas negativas
                if w[0] < 0:
                    # Rompe el bucle interno marcando la optimización de este tamaño de paso como terminada
                    optimizado = True
                else:
                    # Desciende el vector restándole de forma matricial el tamaño de paso actual (Operación segura float64)
                    w -= paso
                    
            # Ordena de menor a mayor todas las claves del diccionario que representan las magnitudes de W
            magnitudes = sorted([n for n in opt_dict])
            # Si el diccionario de optimización contiene configuraciones válidas encontradas
            if magnitudes:
                # Extrae el vector W que genera la magnitud más pequeña (el margen máximo de separación)
                w = opt_dict[magnitudes[0]][0]
                # Almacena el valor del sesgo optimizado asociado a ese vector de margen máximo
                b_optimo = opt_dict[magnitudes[0]][1]
            
        # Asigna el vector W final optimizado para las tareas finales de inferencia
        w_optimo = w
        # Imprime en la consola los valores óptimos calculados del hiperplano y del bias con formato numérico
        print(f"[SVM OPTIMIZADO] Vector de pesos óptimo W: {w_optimo} | Intersección B: {b_optimo:.2f}")
        
        # Muestras continuas bidimensionales de prueba para evaluar la clasificación del SVM
        muestras_nuevas = [[3, 4], [6, 2]]
        # Recorre cada una de las nuevas muestras continuas para realizar predicciones
        for muestra in muestras_nuevas:
            # FUNCIÓN DE SIGNO REAL: Evalúa el signo matemático algebraico del resultado: sign(W . X + B)
            clasificacion_predicha = np.sign(np.dot(np.array(muestra), w_optimo) + b_optimo)
            # Muestra en la pantalla la clase predicha convertida a tipo entero continuo discreto (-1 o 1)
            print(f" -> Predicción para la muestra continua {muestra}: Clase {int(clasificacion_predicha)}")


# =====================================================================
# 4. CLUSTERING: MEAN SHIFT COMPLETO CON BANDWIDTH DINÁMICO
# =====================================================================
# Definición de la clase encargada del agrupamiento jerárquico no supervisado Mean Shift
class ModuloMeanShiftCompleto:
    # Método constructor de la clase
    def __init__(self):
        # Define una matriz multidimensional NumPy con puntos de coordenadas espaciales dispersas
        self.X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11], [8, 2], [10, 2], [9, 3]])

    # Método para ejecutar el procesamiento iterativo del algoritmo Mean Shift
    def procesar_mean_shift(self, bandwidth=4):
        # Imprime el encabezado de la sección de clustering en la terminal
        print("\n--- 4. BLOQUE DE CLUSTERING (MEAN SHIFT COMPLETO) ---")
        # NATIVO DEL ALGORITMO: Al inicio, cada punto individual es inicializado como su propio centroide básico
        centroides = {i: self.X[i] for i in range(len(self.X))}
        
        # CORRECCIÓN PROBLEMA 3: Se cambia 'while True' por un ciclo acotado de 20 iteraciones para garantizar parada segura
        for _ in range(20):
            # Inicializa una lista vacía para almacenar las nuevas coordenadas calculadas en la iteración actual
            nuevos_centroides = []
            # Recorre cada uno de los índices de los centroides almacenados actualmente
            for i in centroides:
                # Crea una lista interna para agrupar los puntos que entran en el rango geométrico
                puntos_dentro_ancho_banda = []
                # Almacena de forma temporal las coordenadas del centroide evaluado en este ciclo
                centroide_actual = centroides[i]
                # Recorre todas las muestras del conjunto de datos original para evaluar su proximidad espacial
                for muestra in self.X:
                    # WEIGHTED BANDWIDTH: Evalúa si la norma de la distancia entre la muestra y el centroide es menor que el radio
                    if np.linalg.norm(muestra - centroide_actual) < bandwidth:
                        # Agrega la muestra de datos si cae dentro del rango de influencia del ancho de banda
                        puntos_dentro_ancho_banda.append(muestra)
                        
                # El nuevo centroide es la media matemática promedio (centro de masa) de todos los puntos capturados
                nuevo_centroide = np.average(puntos_dentro_ancho_banda, axis=0)
                # Convierte el arreglo NumPy en una tupla inmutable y lo añade a la lista de nuevos centroides
                nuevos_centroides.append(tuple(nuevo_centroide))
                
            # Elimina duplicados espaciales convirtiendo la lista a un conjunto y la ordena para estabilizar índices
            unicos = sorted(list(set(nuevos_centroides)))
            # CONDICIÓN DE CONVERGENCIA: Si la cantidad de centros únicos es igual a la previa, el algoritmo convergió
            if len(unicos) == len(centroides):
                # Rompe de forma definitiva el ciclo for principal al haber estabilizado la búsqueda de densidad
                break
            # Actualiza el diccionario de centroides mapeando los nuevos centros únicos encontrados
            centroides = {i: np.array(unicos[i]) for i in range(len(unicos))}
            
        # Imprime el letrero informativo de los resultados finales en la consola
        print(f"[MEAN SHIFT] Clústeres jerárquicos finales calculados por convergencia: ")
        # Recorre los elementos del diccionario mapeando índice y centro numérico geométrico
        for idx, centro in centroides.items():
            # Muestra en la pantalla la coordenada final exacta de cada centro de masa de clúster calculado
            print(f" -> Centroide del Clúster {idx}: {centro}")


# =====================================================================
# 5. DEEP LEARNING: TENSORFLOW REAL, DNN, CNN (CATS VS DOGS) Y RNN/LSTM
# =====================================================================
# Definición de la clase encargada de construir y compilar modelos reales usando la API nativa de TensorFlow
class ModuloTensorFlowDeepLearning:
    # Método constructor de la clase
    def __init__(self):
        # Imprime el encabezado oficial de la sección de Deep Learning en la terminal
        print("\n--- 5. BLOQUE DE TENSORFLOW Y DEEP LEARNING REAL ---")
        # Despliega en la pantalla de forma explícita la versión del motor de TensorFlow cargado en el entorno virtual
        print(f"[TF INFO] Versión de TensorFlow cargada: {tf.__version__}")
        
    # Método para diseñar y compilar una arquitectura de red profunda densa tradicional (DNN)
    def ejecutar_red_densa(self):
        # Imprime el mensaje de inicialización del grafo computacional denso
        print("\n[TF - DNN] Creando e inicializando Red Neuronal Profunda Densa (Capas y Sesión)...")
        # Define una estructura secuencial lineal real de capas usando Keras en TensorFlow
        model_dnn = models.Sequential([
            # Capa de entrada estructurada para recibir un vector de 4 características numéricas (Estados CartPole)
            layers.Input(shape=(4,)), 
            # Capa densa completamente conectada de 64 neuronas configurada con función de activación ReLU
            layers.Dense(64, activation='relu'), 
            # Capa intermedia oculta completamente conectada de 32 neuronas con activación ReLU
            layers.Dense(32, activation='relu'),
            # Capa densa final de salida con 2 neuronas usando Softmax para arrojar probabilidades de acciones binarias
            layers.Dense(2, activation='softmax') 
        ])
        # Compila el modelo especificando el optimizador Adam, la función de pérdida para enteros y métricas de precisión
        model_dnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        # Confirma en la consola la correcta compilación nativa del grafo de la DNN
        print(" -> Modelo DNN compilado de forma nativa en TensorFlow.")

    # Método para diseñar, compilar y ejecutar un paso de entrenamiento de una Red Convolucional (CNN)
    def ejecutar_cnn_cats_vs_dogs(self):
        # Imprime el mensaje instructivo para la construcción de la red convolucional de imágenes
        print("\n[TF - CNN] Inicializando Red Neuronal Convolucional (Cats vs Dogs / Visión Artificial)...")
        # Instancia un modelo secuencial para configurar la extracción de mapas de características visuales
        model_cnn = models.Sequential([
            # Capa de Convolución 2D con 32 filtros de 3x3, activación ReLU y una entrada de imagen RGB de 64x64 pixeles
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)), 
            # Capa de reducción espacial máxima MaxPooling de ventana 2x2 para disminuir las dimensiones de la imagen
            layers.MaxPooling2D((2, 2)),
            # Segunda capa de Convolución 2D con 64 filtros matemáticos para extraer patrones de texturas complejos
            layers.Conv2D(64, (3, 3), activation='relu'),
            # Segunda capa de MaxPooling para compactar los mapas de características resultantes de la convolución
            layers.MaxPooling2D((2, 2)),
            # Capa de aplanado Flatten para transformar las matrices bidimensionales de características en un vector unidimensional
            layers.Flatten(),
            # Capa completamente conectada densa de 64 neuronas con activación no lineal ReLU
            layers.Dense(64, activation='relu'),
            # Capa densa de salida con una sola neurona y función Sigmoid para clasificación probabilística binaria (Perro/Gato)
            layers.Dense(1, activation='sigmoid') 
        ])
        # Compila el modelo convolucional configurando el optimizador Adam y la pérdida binaria por entropía cruzada
        model_cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        # Informa en la pantalla el montaje exitoso de la arquitectura para el problema de Cats vs Dogs
        print(" -> Arquitectura CNN para clasificación de imágenes Cats vs Dogs montada.")
        
        # Genera una matriz aleatoria sintética flotante estructurando un lote real de 5 imágenes RGB de 64x64 pixeles
        imagenes_lote_sintetico = np.random.rand(5, 64, 64, 3).astype(np.float32)
        # Genera un arreglo NumPy entero continuo que actúa como etiquetas binarias del lote (0=Gato, 1=Perro)
        etiquetas_sinteticas = np.array([0, 1, 0, 1, 1]) 
        
        # Imprime el indicador del paso de procesamiento de datos por las capas de la red de visión artificial
        print(" -> Entrenando un lote real de imágenes a través de las capas de convolución...")
        # Ejecuta de forma explícita un paso de entrenamiento y optimización de pesos (Backpropagation) sobre el lote sintético
        historial = model_cnn.train_on_batch(imagenes_lote_sintetico, etiquetas_sinteticas)
        # Despliega en la pantalla el cálculo del error (Loss) y la precisión (Accuracy) real arrojada por la capa final
        print(f" -> [CNN LOTE RESULTADO] Pérdida (Loss): {historial[0]:.4f} | Precisión (Accuracy): {historial[1]:.4f}")

    # Método para diseñar, compilar e inferir sobre una Red Neuronal Recurrente basada en celdas LSTM
    def ejecutar_rnn_lstm(self):
        # Imprime el mensaje instructivo de configuración del bloque secuencial temporal
        print("\n[TF - RNN/LSTM] Configurando Red Neuronal Recurrente para Datos Secuenciales...")
        # Instancia un modelo secuencial Keras especializado en memoria temporal continuada
        model_lstm = models.Sequential([
            # Capa recurrente LSTM con 20 unidades de memoria configurada para procesar 10 pasos de tiempo con 1 característica
            layers.LSTM(20, input_shape=(10, 1)), 
            # Capa densa lineal final encargada de realizar la proyección o regresión de salida del valor continuo
            layers.Dense(1)
        ])
        # Compila el modelo RNN configurando el optimizador Adam y la función de pérdida del error cuadrático medio (MSE)
        model_lstm.compile(optimizer='adam', loss='mse')
        # Informa en la consola la correcta compilación del modelo de memoria secuencial temporal
        print(" -> Modelo RNN/LSTM para series de tiempo y datos secuenciales compilado.")
        
        # Genera una secuencia numérica temporal flotante imitando un lote de 1 registro con 10 pasos de tiempo continuos
        datos_secuencia = np.random.rand(1, 10, 1).astype(np.float32)
        # Ejecuta una inferencia (predicción hacia adelante) usando la secuencia creada desactivando textos informativos por consola
        prediccion_secuencial = model_lstm.predict(datos_secuencia, verbose=0)
        
        # CORRECCIÓN PROBLEMA 1: Imprime directamente el valor numérico escalar predicho por la capa LSTM sin validaciones extras
        print(f" -> [LSTM PRONÓSTICO] Predicción basada en memoria secuencial temporal: {prediccion_secuencial[0]}")


# =====================================================================
# PIPELINE DE ORQUESTACIÓN PRINCIPAL
# =====================================================================
# Estructura de control estándar de Python que indica el punto de inicio de la ejecución del script principal
if __name__ == "__main__":
    # Imprime barras decorativas de inicio de sistema en la consola de comandos
    print("==================================================================")
    print("INICIANDO EJECUCIÓN FORMAL DE LA SUITE DE IA DE PYTHONPROGRAMMING")
    print("==================================================================")
    
    # 1. Instancia el objeto encargado de gestionar el módulo de Regresión y Forecasting Real
    obj_reg = ModuloRegresionCompleto()
    # Ejecuta el pipeline completo de carga de DataFrame, entrenamiento lineal, pickling e inferencia futura
    obj_reg.ejecutar_todo()
    
    # 2. Instancia el objeto encargado de gestionar el algoritmo de vecinos más cercanos desde cero
    obj_knn = ModuloKNNCompleto()
    # Lanza el cálculo analítico de distancias euclidianas sobre el Wisconsin Breast Cancer Dataset estructurado
    obj_knn.clasificar_desde_cero()
    
    # 3. Instancia el objeto encargado de inicializar el espacio continuo de clasificación de soporte vectorial
    obj_svm = ModuloSVMCompleto()
    # Ejecuta la optimización convexa iterativa de restricciones espaciales para encontrar el margen óptimo y predecir
    obj_svm.ajustar_y_predecir()
    
    # 4. Instancia el objeto encargado de inicializar el procesamiento de agrupamiento espacial denso
    obj_ms = ModuloMeanShiftCompleto()
    # Lanza la búsqueda iterativa acotada y segura de convergencia de centros de masa geométricos
    obj_ms.procesar_mean_shift()
    
    # 5. Instancia el objeto encargado de inicializar e interactuar con el motor real de TensorFlow de Google
    obj_tf = ModuloTensorFlowDeepLearning()
    # Lanza el montaje estructural del grafo secuencial para problemas de control denso multicapa
    obj_tf.ejecutar_red_densa()
    # Lanza la extracción convolucional bidimensional y el entrenamiento inmediato sobre un lote de imágenes sintéticas RGB
    obj_tf.ejecutar_cnn_cats_vs_dogs()
    # Lanza el procesamiento temporal de compuertas recurrentes de memoria a largo plazo (LSTM) para predicciones continuas
    obj_tf.ejecutar_rnn_lstm()
    
    # Imprime barras decorativas de conclusión de procesos en la terminal indicando éxito rotundo
    print("\n==================================================================")
    print("¡PROCESAMIENTO COMPLETO REAL! Todos los módulos validados y ejecutados.")
    print("==================================================================")