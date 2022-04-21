# redegal_prueba_tecnica
- requirements.txt: contiene las dependencias necesarias para la correcta ejecución del script python main.py

- main.py: script python con el código para el procesado de datos

EJECUCIÓN:
1- Ejecutar el comando "pip3 install -r requirements.txt" para instalar las librerías necesarias para la ejecución del script python.
2- Ejecutar el script python con el comando "python3 main.py [ruta_fichero_datos_entrada.csv] [ruta_fichero_zonas_taxi.csv] [ruta_fichero_resultados.csv]"

FUNCIONAMIENTO:
El script que se ha desarrollado lee la información de los 2 ficheros de entrada (fichero con los datos de los viajes y fichero con los ids de las zonas). Posteriormente se procesan los datos deentrada, se imprime el resultado por terminal y adicionalmente se guardan en un fichero csv.

Tal y como se explica en el apartado "EJECUCIÓN", el script tiene unos argumentos necesarios para la obtención de los datos de entrada y guardad el resultado obtenido. 

APROXIMACIÓN AL PROBLEMA:
1- Lectura de datos de entrada (viajes e ID de zonas).
2- Fitrado de datos (nos quedamos con los datos cuya distancia de viaje es mayor al percentil 0.95 y cuyo id de zona está comprendido entre 1 y 263).
3- Procesado de datos filtrados y cruce de IDs para obtener "borough" y "zone", así como sumatorio de viajes a cada una de las zonas identificadas.
4- Mostrar resultado obtenido.
5- Generación de fichero csv con el resultado obtenido.

LIBRERÍAS USADAS:
Fundamentalmente se ha usado la libraría PANDAS para la manipulación y análisis de los datos. En particular se ha usado para la manipulación y filtrado de los datos contenidos en los DataFrames.



