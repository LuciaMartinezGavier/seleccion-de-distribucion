# Seleccion de distribución de probabilidad

## Organización del repositorio
En el directorio `plots` se encuentran los gráficos generados.

En el archivo `scattle_diagram` se encuentra la función que genera el digrama de dispersión de la muesta. (EJERCICIO 1)

El archivo parse_sample contiene una función que toma un archivo con extensión `.dat` de muestras separadas por `\n` y retorna un arreglo con dichos muestras.

En el archivo `histogram.py` se encuentran las funciones que plotean el histograma (con y sin las funciones de densidad de probabilidad de la gamma y la log-normal). (EJERCICIO 2b)

En el archivo `box plot` está el código correspondiente al gráfico del box plot y también se encuentran las funciones de los estimadores y el cálculo de los cuantiles. (EJERCICIO 2a y 2b)

En el archivo `estimations.py` se encuentran las funciones que devuelven los estimadores de máxima verosimilitud de las distribuciones log-normal y gamma. Además se encuentra una función que plotea el histograma junto a las funciones de densidad de la distribucion gamma y log-normal con los parametros obtenidos a partir de los datos. (EJERCICIO 3)
