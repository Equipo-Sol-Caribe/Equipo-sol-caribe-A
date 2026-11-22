# Documento de análisis

Cadena Hotelera Sol Caribe, Alternativa A
Fundamentos de Programación, Universidad del Magdalena

Equipo: Miguel Vergara, Jhonatan Gonzales, Estefany Idarraga y Juan Montes.

Este documento es la especificación final del programa. Partimos del enunciado de la Alternativa A y revisamos cada requisito hasta dejar claro qué datos entran, qué muestra el programa y qué reglas se cumplen. Donde el enunciado dejaba algo abierto lo precisamos, y en ese requisito decimos por qué. Al final está el requisito que agregamos nosotros, guardar los datos al salir, y una tabla con todo lo que precisamos. Cómo llegamos a esta versión, incremento por incremento, está en el informe integral.

## Los datos del programa

Un hotel tiene un nombre, un número de habitaciones habilitadas, una fecha de inicio y su registro de ocupación.

El nombre es un texto sin espacios al principio ni al final, no puede quedar vacío y no puede haber dos hoteles con el mismo nombre. Las habitaciones habilitadas son un número entero de al menos 1. La fecha de inicio es una fecha del calendario con el año entre 2000 y 2100.

El registro es una lista con las habitaciones ocupadas de cada día, en orden y sin saltarse días. La posición 0 de la lista es el día de la fecha de inicio, la posición 1 es el día siguiente, y así. Por eso no guardamos la fecha de cada día: se calcula como la fecha de inicio más la posición del día en la lista.

La cadena guarda todos los hoteles en una lista, en el orden en que se crearon o se cargaron. Ese orden es el que decide los empates del requisito 11.

## Reglas que valen para todo el programa

Los requisitos 2, 3 y 4 empiezan leyendo el nombre de un hotel. Si no hay un hotel con ese nombre, el programa muestra "No hay un hotel con ese nombre." y vuelve al menú.

El nombre se compara tal como está escrito, con mayúsculas y tildes, pero sin los espacios del principio y del final. "  Sol Caribe Rodadero  " encuentra a Sol Caribe Rodadero, y "sol caribe rodadero" no lo encuentra.

Un número tecleado o leído de un archivo puede tener espacios alrededor (" 20 " vale como 20). Un texto con letras o con decimales, como "veinte" o "20.5", no es un número entero.

Las fechas se muestran con el formato AAAA-MM-DD, por ejemplo 2026-11-05. El promedio, los porcentajes y la desviación estándar se muestran redondeados a dos decimales con `round`, que no completa con ceros: 64 se muestra como 64.0 y no como 64.00.

Después de cada opción del menú, menos la de salir, el programa espera a que se oprima Enter, limpia la consola y vuelve a mostrar el menú.

## Requisito 1. Crear un hotel

Entradas: el nombre, las habitaciones habilitadas y el año, el mes y el día de la fecha de inicio, en ese orden. El programa lee los cinco datos y después los revisa.

Salidas: si todo está bien, "Se creó el hotel Sol Caribe Minca, sin días registrados." (con el nombre que corresponda). Si algo falla, solo el mensaje de la primera condición que no se cumple, y no crea el hotel.

Reglas: las condiciones se revisan en este orden, y apenas una falla el programa no sigue revisando las demás.

| Orden | Condición que falla | Mensaje |
|---|---|---|
| 1 | El nombre está vacío (o solo tiene espacios) | El nombre no puede estar vacío. |
| 1 | Ya hay un hotel con ese nombre | Ya existe un hotel llamado Sol Caribe Taganga. |
| 2 | Las habitaciones no son un número entero | Las habitaciones habilitadas deben ser un número entero. |
| 3 | Las habitaciones son menos de 1 | El hotel debe tener al menos una habitación habilitada. |
| 4 | El año, el mes y el día no forman una fecha del calendario | La fecha no es válida. |
| 4 | El año está antes de 2000 o después de 2100 | El año de inicio debe estar entre 2000 y 2100. |

Un número negativo como -5 sí es un entero, así que falla en la condición 3 y no en la 2. Una fecha no es válida si alguno de los tres datos no es entero ("noviembre"), si el día no existe en ese mes (31 de noviembre) o si es 29 de febrero en un año que no es bisiesto.

El rango de años lo precisamos nosotros. Con un año como 9999, al registrar días el programa se pasaba del 31 de diciembre de 9999, que es la última fecha que maneja Python, y se cerraba. El nombre queda guardado sin los espacios de los lados, y el hotel nuevo no tiene días registrados.

Ejemplos: con Sol Caribe Minca, 20 y 2026/11/1 se crea el hotel. Con 0 habitaciones y la fecha 2026/11/31 solo avisa que el hotel debe tener al menos una habitación habilitada.

## Requisito 2. Registrar las habitaciones ocupadas del día siguiente

Entradas: el nombre del hotel y las habitaciones ocupadas del día siguiente. Este último dato se vuelve a pedir hasta que sea válido.

Salidas: primero "Día siguiente del registro: 2026-11-01". Si el dato está mal, uno de estos mensajes, y se vuelve a pedir el mismo día:

- "Las habitaciones ocupadas deben ser un número entero." si no es un entero.
- "Las habitaciones ocupadas de Sol Caribe Minca van de 0 a 20." si está fuera del rango.

Cuando el dato está bien: "Se registró el día 2026-11-01."

Reglas: el día siguiente es la fecha de inicio más los días ya registrados. En un hotel que empieza el 30 de diciembre de 2026 y tiene tres días, el siguiente es el 2027-01-02. Las habitaciones ocupadas son un entero desde 0 hasta las habitaciones habilitadas, con los dos extremos incluidos. El día válido se agrega al final del registro.

## Requisito 3. Simular días

Entradas: el nombre del hotel y después, uno por uno, el número de días, las habitaciones ocupadas mínimas y las máximas.

Salidas: si todo está bien, "Se simularon 3 día(s)." y la lista de las habitaciones ocupadas que se agregaron, por ejemplo "Habitaciones ocupadas simuladas: [14, 10, 19]". Si un dato está mal, uno de estos mensajes, y vuelve al menú:

| Dato | Problema | Mensaje |
|---|---|---|
| Días | No es un entero | El número de días debe ser un número entero. |
| Días | Es menor que 1 | Se debe simular al menos un día. |
| Días | Es mayor que 365 | Se pueden simular máximo 365 días cada vez. |
| Mínimo o máximo | No es un entero | Las habitaciones ocupadas deben ser un número entero. |
| Mínimo o máximo | Está fuera de 0 a las habilitadas | Las habitaciones ocupadas de Sol Caribe Minca van de 0 a 20. |
| Mínimo y máximo | El mínimo es mayor que el máximo | El mínimo no puede ser mayor que el máximo. |

Reglas: cada dato se revisa apenas se lee. Si está mal, el programa no lee los que faltan y no agrega ningún día. La revisión de que el mínimo no sea mayor que el máximo se hace después de leer el máximo. Cada día simulado se agrega como el día siguiente del registro, con un número al azar entre el mínimo y el máximo, los dos incluidos.

El máximo de 365 días por simulación lo precisamos nosotros. Si alguien mete millones de días por error, el programa tarda muchísimo y el registro termina pasándose del año 9999.

## Requisito 4. El informe de un hotel

Entradas: el nombre del hotel.

Salidas, en este orden:

```text
Hotel: Sol Caribe Rodadero
Habitaciones habilitadas: 80
Días registrados: 5
Noches vendidas: 256
Promedio de habitaciones ocupadas por día: 51.2
Porcentaje de ocupación: 64.0 %
```

Después siguen las líneas de los requisitos 5 a 9. Si el hotel no tiene días, después de las habitaciones habilitadas solo muestra "El hotel no tiene días registrados." y nada más.

Reglas: las noches vendidas son la suma de las habitaciones ocupadas de todos los días, y el promedio son las noches vendidas divididas entre los días registrados. El porcentaje de ocupación es el promedio dividido entre las habitaciones habilitadas, por 100. Lo calculamos como noches × 100 / (días × habitaciones), que es la misma cuenta. El porqué está en el informe integral.

Ejemplos: Rodadero (80 habitaciones; 70, 28, 30, 52 y 76) da 5 días, 256 noches, 51.2 y 64.0 %. Taganga (40 habitaciones; 14, 22, 30 y 36) da 4 días, 102 noches, 25.5 y 63.75 %.

## Requisito 5. La desviación estándar

Entradas: las del requisito 4.

Salidas: "Desviación estándar: 19.78".

Reglas: a las habitaciones ocupadas de cada día se les resta el promedio y la diferencia se eleva al cuadrado. Los cuadrados se suman, la suma se divide entre los días registrados y la desviación es la raíz cuadrada de ese resultado. Con un solo día da 0.0.

Ejemplo: en Taganga los cuadrados son 132.25, 12.25, 20.25 y 110.25. Suman 275, que entre 4 da 68.75, y la raíz es 8.29.

## Requisito 6. El día de más y el de menos habitaciones ocupadas

Entradas: las del requisito 4.

Salidas: "Día con más habitaciones ocupadas: 2026-11-05" y "Día con menos habitaciones ocupadas: 2026-11-02".

Reglas: si varios días empatan en el máximo o en el mínimo, se muestra el primero de ellos.

Ejemplo: en un hotel de 80 habitaciones con 40, 80, 80, 16 y 16 desde el 2026-11-01, el de más es el 2026-11-02 y el de menos, el 2026-11-04.

## Requisito 7. Los días en cada nivel de ocupación

Entradas: las del requisito 4.

Salidas:

```text
Días en cada nivel de ocupación:
  Crítica: 2
  Baja: 0
  Media: 1
  Alta: 2
```

Reglas: el porcentaje de un día son sus habitaciones ocupadas divididas entre las habilitadas, por 100. Con menos de 40 % el día está en ocupación crítica, desde 40 % hasta menos de 60 % en baja, desde 60 % hasta menos de 80 % en media, y con 80 % o más en alta. Siempre se muestran los cuatro niveles en ese orden, también los que tienen 0 días.

Ejemplo: en un hotel de 80 habitaciones, 31 es crítica, 32 y 47 son baja, 48 y 63 son media, y 64 es alta.

## Requisito 8. La racha más larga en ocupación crítica

Entradas: las del requisito 4.

Salidas: "Racha más larga en ocupación crítica: 3 día(s), desde el 2026-11-04", o "El hotel no tuvo ningún día en ocupación crítica." si no hubo ninguno.

Reglas: una racha es una serie de días seguidos del registro, todos en ocupación crítica. Se muestra cuántos días tiene la más larga y la fecha del día en que empezó. Si dos rachas empatan, se muestra la que empezó primero.

Ejemplo: con 20, 24, 60, 28, 16, 30 y 70 en un hotel de 80 habitaciones hay una racha de 2 días desde el 2026-11-01 y otra de 3 días desde el 2026-11-04. Se muestra la de 3.

## Requisito 9. Los días sin registrar

Entradas: las del requisito 4, más la fecha actual del computador. La interfaz la toma con `date.today()` y se la pasa a la lógica.

Salidas: "Último día registrado: 2026-11-05", y después una de estas dos:

- "El registro está al día."
- "Días que faltan por registrar: 14, del 2026-11-06 al 2026-11-19"

Reglas: cada día se registra cuando ya terminó, así que con el registro completo el último día registrado es ayer. Los días que faltan son la fecha de hoy menos el día siguiente al último registrado. Si eso da 0 o menos, el registro está al día; da menos de 0 cuando se simularon días hasta después de hoy. El periodo que se muestra va del día siguiente al último registrado hasta ayer.

Ejemplos: ejecutado el 2026-11-20, Rodadero (último día 2026-11-05) tiene 14 días sin registrar. Ejecutado el 2026-11-02, Minca (único día 2026-11-01) está al día.

## Requisito 10. Varios hoteles en el mismo programa

Entradas: el nombre del hotel en los requisitos 2, 3 y 4, y el nombre de los hoteles que se crean o se cargan.

Salidas: "No hay un hotel con ese nombre." cuando no existe, y "Ya existe un hotel llamado ..." cuando se intenta crear uno repetido.

Reglas: el programa guarda todos los hoteles creados desde el teclado o cargados desde archivos, y cada uno tiene sus propios datos. La búsqueda sigue la regla de comparación de nombres de arriba. Si se intenta crear un hotel con un nombre que ya existe, no se crea y el que existía sigue igual.

## Requisito 11. El porcentaje de ocupación más alto y el más bajo

Entradas: ninguna; es la opción 5 del menú.

Salidas: "Porcentaje de ocupación más alto: Sol Caribe Rodadero, con 64.0 %" y "Porcentaje de ocupación más bajo: Sol Caribe Minca, con 55.0 %". Si ningún hotel tiene días, "Ningún hotel tiene días registrados."

Reglas: solo cuentan los hoteles con al menos un día registrado. Los porcentajes se comparan sin redondear, y se muestran redondeados. Si dos hoteles empatan, cuenta el que se creó o se cargó primero. Si un solo hotel tiene días, es a la vez el más alto y el más bajo.

## Requisito 12. Cargar los hoteles desde un archivo

Entradas: la ruta del archivo de hoteles y, si se pudo leer, la del archivo de ocupación (requisito 13).

Salidas:

- Un mensaje "Línea 4 descartada: El hotel debe tener al menos una habitación habilitada." por cada línea descartada, con su número y su causa.
- Al final, "Hoteles cargados: 2".
- Si el programa ya tiene hoteles: "La carga solo se hace con el programa sin hoteles.", sin pedir ninguna ruta.
- Si el archivo no existe: "El archivo no existe."
- Si la ruta es una carpeta o el archivo no está en UTF-8: "No se pudo leer el archivo."

Reglas: la carga solo se hace con el programa sin hoteles, para que los días de los archivos no se mezclen con los que ya hay. El archivo está en UTF-8 y su primera línea es el encabezado, que no se carga. Cada línea siguiente tiene cinco campos separados por punto y coma: nombre, habitaciones, año, mes y día. Los espacios alrededor de un campo no cuentan, y una línea vacía se salta sin aviso. El número de línea que se muestra es el de la línea en el archivo, contando el encabezado como la línea 1.

Las causas para descartar una línea se revisan en el mismo orden que al crear un hotel desde el teclado: primero que tenga cinco campos ("No tiene cinco campos.") y después las condiciones del requisito 1, con sus mismos mensajes. Una línea descartada no detiene la carga. Si el archivo de hoteles no se puede leer, no se carga ningún hotel y no se pide la ruta del archivo de ocupación.

La parte de "No se pudo leer el archivo." la precisamos nosotros, porque el enunciado solo habla del archivo que no existe.

Ejemplo: con `datos/hoteles_enunciado.csv` se cargan Sol Caribe Rodadero y Sol Caribe Taganga. Se descartan la línea 4 (0 habitaciones), la 5 (cuatro campos), la 6 ("cuarenta"), la 7 (Taganga repetido) y la 8 (30 de febrero).

## Requisito 13. Cargar la ocupación desde un archivo

Entradas: la ruta del archivo de ocupación.

Salidas: un mensaje "Línea N descartada: causa" por cada línea descartada y, al final, "Días cargados: 9". Si el archivo no existe: "El archivo no existe. Los hoteles quedan cargados, sin días registrados." Si no se puede leer: "No se pudo leer el archivo. Los hoteles quedan cargados, sin días registrados."

Reglas: la primera línea es el encabezado. Cada línea siguiente tiene dos campos, el nombre del hotel y las habitaciones ocupadas, y agrega a ese hotel el día que sigue en su registro. Las líneas de varios hoteles pueden venir intercaladas, siempre que las de cada hotel estén en el orden de sus días. Los espacios y las líneas vacías se tratan igual que en el archivo de hoteles.

Las causas para descartar una línea se revisan en este orden:

1. No tiene dos campos: "No tiene dos campos."
2. No hay un hotel con ese nombre: "No hay un hotel llamado Sol Caribe Riohacha."
3. Las habitaciones ocupadas no son un entero: "Las habitaciones ocupadas deben ser un número entero."
4. Están fuera de 0 a las habilitadas: "Las habitaciones ocupadas de Sol Caribe Taganga van de 0 a 40."

Si el archivo de ocupación no existe, los hoteles quedan cargados sin días. Para cargar después la ocupación hay que ejecutar el programa otra vez, porque la carga solo se hace con el programa vacío.

Ejemplo: con los archivos del enunciado, Rodadero queda con 70, 28, 30, 52 y 76, Taganga con 14, 22, 30 y 36, y se cargan 9 días. Se descartan las líneas 10, 12, 13, 14 y 15.

## Requisito 14. El menú

Entradas: el número de la opción, tecleado como texto; los espacios a los lados no cuentan.

Salidas: el menú con sus siete opciones en este orden:

```text
1. Crear un hotel
2. Registrar las habitaciones ocupadas del día siguiente
3. Simular días
4. Ver el informe de un hotel
5. Ver el hotel con el porcentaje de ocupación más alto y el más bajo
6. Cargar los hoteles y la ocupación desde archivos
7. Salir
```

Con una opción que no existe, como 8 o "dos", muestra "La opción no es válida."

Reglas: después de cualquier opción que no sea la 7, el programa pide Enter ("Presione Enter para continuar..."), limpia la consola y vuelve a mostrar el menú. La pausa la agregamos para que el resultado de cada opción no se borre antes de leerlo. Con la 7 se hace lo del requisito 15 y el programa termina.

## Requisito 15 (agregado por el equipo). Guardar los datos al salir

Este requisito no está en el enunciado. Lo agregamos para que los datos no se pierdan al cerrar el programa.

Entradas: la respuesta a "¿Desea guardar los datos antes de salir? (s/n): ".

Salidas: si se guarda, "Datos guardados en hoteles_guardados.csv y ocupacion_guardada.csv." y "La próxima vez se pueden cargar con la opción 6." Si no se puede escribir, "No se pudieron guardar los datos." En todos los casos termina con "Fin del programa."

Reglas: la pregunta solo se hace si el programa tiene hoteles. Se guarda solo si la respuesta es s (mayúscula o minúscula); cualquier otra respuesta no guarda. Los dos archivos quedan en la carpeta desde donde se ejecuta el programa, con el mismo formato que leen los requisitos 12 y 13. Así, al cargarlos en otra ejecución, se recuperan los mismos hoteles con los mismos días.

## Lo que precisamos o agregamos

| Regla | Requisito | Por qué |
|---|---|---|
| El año de inicio va entre 2000 y 2100 | 1 y 12 | Con un año como 9999 el programa se cerraba al registrar días |
| Máximo 365 días por simulación | 3 | Para que el programa no se quede pegado con millones de días |
| "No se pudo leer el archivo." si la ruta es una carpeta o el archivo no está en UTF-8 | 12 y 13 | Para que el programa no se cierre con esas rutas |
| Pausa con Enter después de cada opción y consola limpia antes del menú | 14 | Para que se alcance a leer el resultado |
| Guardar los datos al salir | 15 | Para no perder los datos al cerrar el programa |
