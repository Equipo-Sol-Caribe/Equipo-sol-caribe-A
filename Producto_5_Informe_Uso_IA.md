# Informe del uso de la inteligencia artificial generativa

Cadena Hotelera Sol Caribe, Alternativa A
Fundamentos de Programación, Universidad del Magdalena

Equipo: Miguel Vergara, Jhonatan Gonzales, Estefany Idarraga y Juan Montes.

## 1. Herramienta y evidencias

Usamos Claude, de Anthropic y gemini. Las evidencias están en la carpeta `evidencias_ia/` del repositorio, y cada interacción de este informe dice en qué evidencia está.

| Evidencia | Integrante | Qué contiene | Enlace o archivo |
|---|---|---|---|
| E1 | Jhonatan | La conversación de las interacciones I1 a I8 (del 15 al 21 de noviembre de 2026) | (https://claude.ai/share/9d7cfda3-e86a-41c5-8ec1-fea43a430077o) |
| E2 | | | |
| E3 | | | |
| E4 | | | |

## 2. Cómo usamos la IA

La primera vez le pasamos a la IA los términos de referencia y el documento de la Alternativa A, y le pedimos el proyecto completo. Nos devolvió un programa que funcionaba, pero muy largo y con cosas que no vimos en clase. Desde ahí la mayor parte del trabajo fue revisar lo que proponía, pedirle cambios y comprobar cada versión ejecutando el programa. El código pasó por cuatro versiones: la primera de la IA, una simplificada al nivel del curso, otra ajustada a las reglas de estilo de la clase y la final con las correcciones.

Como la primera respuesta ya traía el programa completo, varias interacciones tocan todos los incrementos a la vez. Por eso en la sección 3 está, para cada incremento, qué hizo la IA en cada actividad y en qué interacción; el detalle de cada interacción está en la sección 4.

## 3. La IA en cada incremento

### Incremento 1: hoteles, registro y simulación (requisitos 1, 2, 3, 10 y 14)

| Actividad | Qué hizo la IA | Interacción |
|---|---|---|
| Análisis | Sacó el orden de las cuatro condiciones del requisito 1 y la diferencia entre el requisito 2 (repetir el dato) y el 3 (volver al menú). Propuso el rango de años 2000 a 2100 y el tope de 365 días por simulación. | I1, I2 |
| Diseño | Propuso las clases `Hotel` y `CadenaHotelera`, el registro como una lista de enteros y que los métodos que validan devuelvan el mensaje de error. Después cambió el diccionario de hoteles por una lista y metió la bandera `seguir` de la opción 3. | I1, I2, I4 |
| Codificación | Escribió `crear_hotel`, `buscar_hotel`, `registrar_dia`, `simular_dias`, el menú, la limpieza de consola y la pausa con Enter. | I1, I2, I4 |
| Verificación | Propuso los casos 1.1 a 2.19. Con una prueba de datos al azar encontró que un hotel creado en el año 9999 tumbaba el programa. | I1, I2, I3, I6 |

### Incremento 2: informe del hotel (requisitos 4 a 9)

| Actividad | Qué hizo la IA | Interacción |
|---|---|---|
| Análisis | Revisó las fórmulas contra los ejemplos del enunciado (Rodadero, Taganga y Minca). | I1 |
| Diseño | Un método por indicador. Acumuladores en vez de `sum`, `None` cuando la lista está vacía y los días sin registrar calculados con `fecha_siguiente`. | I1, I2, I4 |
| Codificación | Escribió los métodos del informe y la opción 4. | I1, I2, I4 |
| Verificación | Propuso los casos 3.1 a 3.18 y 4.6 a 4.8. Comparó los indicadores contra un cálculo aparte con miles de hoteles al azar. | I1, I2, I4, I6 |

### Incremento 3: comparación y carga de archivos (requisitos 11, 12 y 13)

| Actividad | Qué hizo la IA | Interacción |
|---|---|---|
| Análisis | Listó los detalles de la carga: encabezado, líneas vacías, espacios, número de línea y orden de las causas. | I1 |
| Diseño | Encontró el problema de decimales en el empate del 48 % y propuso la división única. Propuso reutilizar `crear_hotel` en la carga. Después movió la búsqueda del hotel en `cargar_ocupacion`. | I1, I5 |
| Codificación | Escribió la comparación, las dos cargas y la opción 6. | I1, I2, I4, I5 |
| Verificación | Propuso los casos 4.1 a 4.5 y 5.1 a 5.10, y los archivos `hoteles_empate.csv` y `hoteles_espacios.csv`. Escribió mal la salida esperada de un caso (ver la sección 5). | I1, I2, I3, I6 |

### Incremento 4: guardado y correcciones (requisito 15 y arreglos)

| Actividad | Qué hizo la IA | Interacción |
|---|---|---|
| Análisis | Propuso guardar al salir como requisito agregado, a partir de lo que le pedimos sobre persistencia. | I1 |
| Diseño | Nombres fijos para los archivos guardados y el mismo formato de la carga. | I2 |
| Codificación | Escribió `guardar` y `opcion_salir`. Hizo las correcciones de los issues #9, #10 y #11. | I1, I2, I4, I5 |
| Verificación | Propuso los casos 5.14 a 5.16 y volvió a correr todos los casos después de cada cambio. | I4, I5, I6 |

## 4. Las interacciones

### I1. Pedir el proyecto completo (Jhonatan, 15 de noviembre)

Lo que se le pidió: Jhonatan le pasó los términos y la Alternativa A, y le pidió el proyecto completo. Tenía que traer las 7 opciones del menú, todas las validaciones, que no se cayera con datos mal escritos, carga y guardado de archivos, y casos de prueba con datos de ejemplo.

Lo que respondió: un programa de unas 990 líneas en `business_logic.py` y `user_interface.py`, la carpeta `datos` con los CSV de prueba y un documento de casos de más de 1.200 líneas. Antes de programar probó la fórmula del porcentaje y encontró que, tal como viene en el enunciado, da decimales distintos para dos hoteles con el mismo 48 %, así que usó una sola división. También agregó el guardado al salir como requisito nuevo.

Qué aceptamos: la estructura en dos clases, el registro como una lista, la forma de validar devolviendo el mensaje, la división única del porcentaje, el guardado al salir y los archivos de datos.

Qué corregimos o rechazamos: todo lo demás lo cambiamos en la interacción siguiente, porque el código era demasiado complejo para el curso.

Evidencia: E1.

### I2. Simplificar el código al nivel del curso (Jhonatan, 17 de noviembre)

Lo que se le pidió: Jhonatan le dijo que el proyecto funcionaba pero estaba demasiado complejo y se notaba hecho por IA. Le pidió una versión más sencilla, al nivel de primer cuatrimestre, y que le explicara todo.

Lo que respondió: una versión de 559 líneas. Quitó los docstrings largos, el `except Exception` que atrapaba cualquier error, el manejo de Ctrl+C, el tope de calendario con `date.max` y el diccionario de hoteles. También explicó cada clase y cada algoritmo con ejemplos, y dejó una lista de preguntas probables del examen oral. Al probar esta versión con datos al azar encontró que un hotel creado en el año 9999 se caía al registrar días, y propuso el rango de años 2000 a 2100. Propuso además el tope de 365 días por simulación.

Qué aceptamos: la versión simplificada, las dos reglas nuevas y la explicación, que usamos para estudiar.

Qué corregimos o rechazamos: al ejecutar los casos de esa versión, uno falló por un error de la IA en la salida esperada (ver la sección 5), y se corrigió el caso. Además, el documento de casos (101 casos) seguía siendo muy largo, y lo cambiamos en I3.

Evidencia: E1.

### I3. Acortar el documento de casos (Jhonatan, 17 de noviembre)

Lo que se le pidió: que el documento de casos estaba lleno de texto y se notaba hecho por IA.

Lo que respondió: lo pasó a tablas cortas por requisito, con 82 casos y menos de la mitad del texto. Cada caso lo comprobó ejecutando el programa.

Qué aceptamos: el formato de tablas.

Qué corregimos o rechazamos: nada.

Evidencia: E1.

### I4. Ajustar el código a las reglas de la clase (Jhonatan, 17 de noviembre)

Lo que se le pidió: reescribir los dos archivos con las reglas del curso. Las reglas eran: sin docstrings, solo comentarios `# Decisión:`, un solo `return` al final de cada función, nada de ternarios, comprensiones, `lambda`, `sum`, `max`, `min` ni `any`, `try / except ValueError` en la interfaz, limpieza de consola, `date.today()` solo en la interfaz y pasado por parámetro, y anotaciones de tipo.

Lo que respondió: los dos archivos reescritos (517 líneas). Revisó las reglas con un programa que recorre el código, y volvió a correr los casos y miles de sesiones con entradas al azar. Agregó una pausa con Enter después de cada opción, porque al limpiar la consola se borraba el resultado antes de leerlo.

Qué aceptamos: todo, incluida la pausa.

Qué corregimos o rechazamos: nada en esta interacción. Los detalles que encontramos después en esta versión están en I5.

Evidencia: E1.

### I5. Tres ajustes al código (Jhonatan, 17 de noviembre)

Lo que se le pidió: revisando el código, Jhonatan encontró tres cosas. En `cargar_ocupacion` se buscaba el hotel con `campos[0]` antes de revisar que la línea tuviera dos campos. La interfaz usaba `hotel.ocupadas[-dias:]`, que toca la lista directo y usa slicing negativo, que no vimos en clase. Y podía haber diccionarios y tuplas que tampoco hubiéramos visto. Le pidió corregirlas.

Lo que respondió: movió la búsqueda del hotel dentro del `else`, después de revisar los dos campos, y explicó que antes no fallaba porque `split` siempre devuelve al menos un elemento. Creó el método `ultimos_dias` en `Hotel`, con un `for` y `range`. Los diccionarios y las tuplas los dejó, y preguntó si los habíamos visto antes de cambiarlos.

Qué aceptamos: los dos primeros cambios.

Qué corregimos o rechazamos: sobre los diccionarios y las tuplas decidimos (completar: si se quedan porque los vimos en clase, o si se cambian).

Evidencia: E1.

### I6. Reescribir el documento de casos como lo escribiríamos nosotros (Jhonatan, 17 de noviembre)

Lo que se le pidió: reescribir los casos en lenguaje de estudiante, por bloques de prueba en la consola, con años de prueba realistas y algunas notas de fallos que encontramos al probar. Como ejemplo de nota le dimos un problema con `.strip()`.

Lo que respondió: el documento en cinco bloques, con 77 casos, todos comprobados contra el programa. No puso el ejemplo del `.strip()` porque ese fallo no pasó. En su lugar puso cuatro fallos reales del proyecto: el año 9999, el `OverflowError`, el empate del 48 % y el caso mal escrito. Avisó que al cambiar el año de prueba a 99999 ningún caso de la tabla pasa ya por el `except OverflowError`, y que eso queda contado solo en una nota.

Qué aceptamos: el documento como quedó, con las notas reales, porque en el oral pueden preguntar por cualquier cosa que esté escrita ahí.

Qué corregimos o rechazamos: nada.

Evidencia: E1.

### I7. Textos para GitHub (Jhonatan, 21 de noviembre)

Lo que se le pidió: los milestones, los issues de cada paso, los issues de dificultades con su discusión, el tablero y el README de las evidencias.

Lo que respondió: escribió todo eso, menos la discusión de los issues de dificultades. Explicó que los términos piden la discusión real del equipo, y propuso que cada integrante comentara después de revisar algo concreto, como correr un caso o probar una cuenta en la consola de Python.

Qué aceptamos: los textos y la forma de hacer la discusión.

Qué corregimos o rechazamos: (completar si cambiaron algo al publicarlos).

Evidencia: E1.

### I8. Borradores de los documentos (Jhonatan, 21 de noviembre)

Lo que se le pidió: el documento de análisis, el informe integral y este informe.

Lo que respondió: los tres documentos, escritos a partir del enunciado, del código final y de la conversación. Dibujó los diagramas del informe integral para comprobar que se ven bien en GitHub, y verificó en el programa los límites que menciona antes de escribirlos.

Qué aceptamos: (completar después de revisarlos contra el código y el enunciado).

Qué corregimos o rechazamos: (completar).

Evidencia: E1.

### Interacciones de los demás integrantes

Si Miguel, Estefany o Juan usaron la IA en su parte, cada interacción va aquí con el mismo formato: qué se le pidió, qué respondió, qué se aceptó, qué se corrigió o rechazó y por qué, y su evidencia (E2, E3, E4).

## 5. Errores de la IA que encontramos

| Error | Cómo lo detectamos | Qué hicimos |
|---|---|---|
| La primera versión era demasiado compleja y usaba cosas que no vimos en clase (manejo de Ctrl+C, `except Exception`, `date.max`, docstrings largos) | Leyendo el código; no lo íbamos a poder explicar en el oral | Pedimos simplificarla (I2) |
| El documento de casos era demasiado largo (más de 1.200 líneas, después 101 casos) | Leyéndolo | Pedimos acortarlo y reescribirlo (I3, I6) |
| En la versión simplificada, un hotel creado en el año 9999 se caía al registrar días | Una prueba con datos al azar | Rango de años 2000 a 2100 (issue #9) |
| La salida esperada del caso de los archivos con espacios (hoy el 5.9) estaba mal: decía que no debía salir ninguna "Línea 4 descartada" | El caso falló al ejecutarlo; el programa estaba bien, porque esa línea del archivo de ocupación sí tiene un campo de más | Se corrigió el caso |
| `cargar_ocupacion` buscaba el hotel antes de revisar que la línea tuviera dos campos | Revisión del código (Jhonatan) | Se cambió el orden (I5, issue #11) |
| La interfaz tocaba `hotel.ocupadas` directo y con slicing negativo | Revisión del código (Jhonatan) | Método `ultimos_dias` (I5, issue #11) |
| Diccionarios y tuplas que tal vez no vimos en clase | Revisión del código (Jhonatan) | (completar la decisión del equipo) |

Además de estos errores, la IA encontró cosas que nos sirvieron antes de que fueran un problema. Una fue el empate del 48 %, que con la fórmula del enunciado tal cual sale mal por los decimales (issue #10). Otra, que `date()` lanza `OverflowError` y no `ValueError` con un año de muchísimos dígitos. También encontró dos límites del programa que dejamos anotados en el informe integral: el punto y coma en el nombre al guardar, y las habitaciones de más de 150 cifras.

## 6. Lo que nos dejó

La IA escribió casi todo el código, pero casi nada quedó como lo entregó la primera vez. Lo que más nos sirvió fue pedirle que explicara cada decisión y comprobar cada versión ejecutando los casos, porque ahí salieron sus errores. Lo que más tuvimos que corregir fue el nivel: tiende a escribir más de lo necesario y con herramientas que no vimos, así que hubo que pedirle varias veces que lo dejara con lo de clase.
