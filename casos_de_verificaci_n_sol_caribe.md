# Casos de verificacion - Sol Caribe (Alternativa A)

En este archivo dejamos anotadas las pruebas que fuimos haciendo desde la consola corriendo `python user_interface.py` en la carpeta raiz del proyecto. Despues de ejecutar cada opcion el programa siempre pide presionar Enter para regresar al menu.

Todos los archivos CSV que usamos para probar estan guardados en la carpeta `datos/`:

- `hoteles_enunciado.csv` y `ocupacion_enunciado.csv`: son los datos base del enunciado, incluyendo las lineas con errores.
- `hoteles_ejemplos.csv` y `ocupacion_ejemplos.csv`: hoteles que creamos aparte para revisar empates, limites de niveles, rachas y cambio de año.
- `hoteles.csv` y `ocupacion.csv`: datos de dos semanas de noviembre de 2026 para Rodadero, Taganga, Minca, Cienaga y Palomino.
- `hoteles_empate.csv` y `ocupacion_empate.csv`: archivo especifico para probar empates entre hoteles (Buritaca y Don Diego, ambos con 48 %).
- `hoteles_espacios.csv` y `ocupacion_espacios.csv`: archivos con lineas vacias y espacios extra al inicio o al final.

## 1. Creacion de hoteles y validacion de habitaciones y fechas

Estas pruebas las hicimos con el programa recien abierto usando la opcion 1. Los datos se metieron en el orden que pide el programa: nombre, habitaciones y fecha (año/mes/dia).

| Caso | Que probamos | Datos ingresados | Resultado en pantalla | Estado |
|---|---|---|---|---|
| 1.1 | Crear un hotel normal | Sol Caribe Minca, 20, 2026/11/1 | Crea el hotel y avisa que queda sin dias registrados | OK |
| 1.2 | Habitaciones en cero | Sol Caribe Minca, 0, 2026/11/1 | No deja crearlo y pide al menos una habitacion habilitada | OK |
| 1.3 | Habitaciones negativas | Sol Caribe Minca, -5, 2026/11/1 | Mismo mensaje que con el 0 | OK |
| 1.4 | Habitaciones en letras | Sol Caribe Minca, veinte, 2026/11/1 | Avisa que tiene que ser un numero entero | OK |
| 1.5 | Habitaciones con decimales | Sol Caribe Minca, 20.5, 2026/11/1 | Tambien exige un numero entero | OK |
| 1.6 | Dejar el nombre vacio | (Enter), 20, 2026/11/1 | Indica que el nombre no puede quedar vacio | OK |
| 1.7 | Nombre con espacios a los lados | "  Sol Caribe Minca  ", 20, 2026/11/1 | Quita los espacios y lo guarda como "Sol Caribe Minca" | OK |
| 1.8 | Fecha que no existe | Sol Caribe Minca, 20, 2026/11/31 | Muestra que la fecha no es valida | OK |
| 1.9 | Mes escrito en texto | Sol Caribe Minca, 20, 2026/noviembre/1 | Muestra que la fecha no es valida | OK |
| 1.10 | Fecha en año bisiesto | Sol Caribe Minca, 20, 2028/2/29 | Lo crea sin problema | OK |
| 1.11 | 29 de febrero en año no bisiesto | Sol Caribe Minca, 20, 2026/2/29 | Rechaza la fecha porque febrero de 2026 solo tiene 28 dias | OK |
| 1.12 | Año exageradamente grande | Sol Caribe Minca, 20, 99999/1/1 | Avisa que la fecha no es valida | OK |
| 1.13 | Dos errores en el mismo registro | Sol Caribe Minca, 0, 2026/11/31 | Se frena en el error de las habitaciones y ya no evalua la fecha | OK |
| 1.14 | Año anterior al 2000 | Sol Caribe Minca, 20, 1999/12/31 | Pide que el año este entre 2000 y 2100 | OK |
| 1.15 | Año 9999 | Sol Caribe Minca, 20, 9999/12/31 | Igual, pide un año entre 2000 y 2100 | OK |
| 1.16 | Ver informe apenas se crea | Crear Minca y entrar a opcion 4 con Minca | Muestra que el hotel no tiene dias registrados | OK |

Sobre el rango de años entre 2000 y 2100, eso no estaba en el enunciado pero nos toco ponerlo despues de encontrar un fallo: probando datos extremos creamos un hotel en el año 9999 y al intentar registrarle dias el programa se cerro con `OverflowError`, ya que Python no soporta fechas despues del 31-12-9999. Ademas, al meter un año con demasiados digitos vimos que `date()` tambien lanza `OverflowError` en lugar de `ValueError`, asi que dejamos `crear_fecha` capturando las dos excepciones para que no se caiga.

## 2. Registro de dias y simulacion de ocupacion

Para esta parte creamos primero a Sol Caribe Minca con 20 habitaciones y fecha de inicio 2026/11/1.

Primero probamos la opcion 2 (registrar el dia siguiente):

| Caso | Que probamos | Datos ingresados | Resultado en pantalla | Estado |
|---|---|---|---|---|
| 2.1 | Registrar el primer dia | Minca, 11 | Muestra la fecha 2026-11-01 y guarda el registro | OK |
| 2.2 | Meter letras en vez de numero | Minca, x y luego 11 | Dice que debe ser un numero entero y vuelve a pedir el mismo dia | OK |
| 2.3 | Pasarse de la capacidad del hotel | Minca, 21 y luego 11 | Avisa que en Minca el rango es de 0 a 20 y pide el dato otra vez | OK |
| 2.4 | Numero negativo | Minca, -1 y luego 11 | Hace lo mismo que en el caso 2.3 | OK |
| 2.5 | Probar los bordes 0 y 20 | Minca, 0; de nuevo opcion 2, Minca, 20 | Guarda los dos sin problema y el segundo queda en el 2026-11-02 | OK |
| 2.6 | Hotel que no existe | Sol Caribe Cartagena | Avisa que no hay ningun hotel con ese nombre y vuelve al menu | OK |
| 2.7 | Salto de año | Con `hoteles_ejemplos.csv` y `ocupacion_ejemplos.csv` cargados: Ejemplo Fin de Año, 5 | Pide el 2027-01-02 porque ese hotel arranca el 30 de diciembre y ya tenia 3 dias | OK |

Luego probamos la opcion 3 (simular dias), metiendo los datos en el orden dias, minimo y maximo:

| Caso | Que probamos | Datos ingresados | Resultado en pantalla | Estado |
|---|---|---|---|---|
| 2.8 | Simular 3 dias entre 10 y 20 | Minca, 3, 10, 20 | Agrega 3 valores al azar; cambian en cada corrida pero siempre quedan entre 10 y 20 | OK |
| 2.9 | Dias escritos en letras | Minca, tres | Pide un numero entero y corta ahi sin preguntar el minimo | OK |
| 2.10 | Simular 0 dias | Minca, 0 | Avisa que minimo se debe simular un dia | OK |
| 2.11 | Simular mas de un año seguido | Minca, 366 | Avisa que el limite por simulacion es de 365 dias | OK |
| 2.12 | Minimo en letras | Minca, 3, x | Pide un numero entero y no llega a pedir el maximo | OK |
| 2.13 | Minimo negativo | Minca, 3, -1 | Avisa que las ocupadas van de 0 a 20 y frena ahi | OK |
| 2.14 | Maximo mayor a las habitaciones | Minca, 3, 10, 21 | Avisa que las ocupadas van de 0 a 20 | OK |
| 2.15 | Minimo mayor que el maximo | Minca, 3, 15, 10 | Indica que el minimo no puede superar al maximo | OK |
| 2.16 | Confirmar que no guarde nada tras error | Hacer el caso 2.15 y revisar opcion 4 con Minca | El hotel sigue sin dias registrados | OK |
| 2.17 | Minimo igual al maximo | Minca, 2, 7, 7 | Imprime `[7, 7]` | OK |
| 2.18 | Mezclar registro manual y simulacion | Registrar 11, simular 2 dias con 5 y 5, y registrar otro dia | El nuevo dia que pide es el 2026-11-04 | OK |
| 2.19 | Simular en un hotel inexistente | Sol Caribe Cartagena | Dice que no existe y no pide los dias | OK |

El limite de 365 dias por simulacion lo decidimos en el equipo porque si alguien escribe un numero gigante por descuido, el bucle se queda pegado demasiado tiempo y ademas las fechas podrian pasarse del limite de Python.

## 3. Informes, niveles y rachas criticas

Para arrancar esta tanda cargamos con la opcion 6 los archivos `hoteles_enunciado.csv` y `ocupacion_enunciado.csv`. Aparte creamos a mano a Sol Caribe Minca (20 habitaciones, 2026/11/1) con un solo dia de 11 ocupadas, y a Sol Caribe Palomino (30 habitaciones, 2026/11/1) sin dias. Todo se reviso desde la opcion 4.

| Caso | Que probamos | Datos ingresados | Resultado en pantalla | Estado |
|---|---|---|---|---|
| 3.1 | Numeros generales de Rodadero (70, 28, 30, 52, 76) | Sol Caribe Rodadero | 5 dias, 256 noches vendidas, promedio 51.2, ocupacion 64.0 % y desviacion 19.78 | OK |
| 3.2 | Dia de mayor y menor ocupacion en Rodadero | Sol Caribe Rodadero | Mayor ocupacion el 2026-11-05 y menor el 2026-11-02 | OK |
| 3.3 | Niveles y racha en Rodadero | Sol Caribe Rodadero | Critica 2, baja 0, media 1, alta 2; racha critica de 2 dias desde el 2026-11-02 | OK |
| 3.4 | Numeros generales de Taganga (14, 22, 30, 36) | Sol Caribe Taganga | 4 dias, 102 noches vendidas, promedio 25.5, ocupacion 63.75 % y desviacion 8.29 | OK |
| 3.5 | Extremos y niveles de Taganga | Sol Caribe Taganga | Mas ocupado el 2026-11-04, menos ocupado el 2026-11-01 y 1 dia en cada nivel | OK |
| 3.6 | Minca con un solo dia registrado | Sol Caribe Minca | 1 dia, 11 noches, promedio 11.0, 55.0 % y desviacion 0.0; sin dias criticos (baja en 1 y el resto en 0) | OK |
| 3.7 | Palomino sin dias | Sol Caribe Palomino | Solo muestra nombre, las 30 habitaciones y avisa que no tiene dias registrados | OK |
| 3.8 | Empate en dia mas y menos ocupado | Con los ejemplos cargados: Ejemplo Empates (40, 80, 80, 16, 16) | Mas ocupado 2026-11-02 y menos ocupado 2026-11-04 (se queda con el primero en ambos empates) | OK |
| 3.9 | Valores exactos en el borde de cada nivel | Ejemplo Niveles (31, 32, 47, 48, 63, 64 sobre 80 hab.) | Critica 1, baja 2, media 2, alta 1 (32 entra en baja, 48 en media y 64 en alta) | OK |
| 3.10 | Dos rachas criticas distintas | Ejemplo Rachas (20, 24, 60, 28, 16, 30, 70) | Toma la racha de 3 dias desde el 2026-11-04 y no la de 2 dias | OK |
| 3.11 | Buscar con el nombre en minusculas | sol caribe rodadero | No lo encuentra porque distingue mayusculas y minusculas | OK |
| 3.12 | Buscar con espacios extra | "  Sol Caribe Rodadero  " | Si lo encuentra y muestra el informe | OK |
| 3.13 | Pedir informe de hotel que no existe | Sol Caribe Cartagena | Avisa que no hay ningun hotel con ese nombre | OK |
| 3.14 | Intentar duplicar un hotel ya creado | Opcion 1: Sol Caribe Taganga, 50, 2026/11/1, y luego ver su informe | Avisa que ya existe y Taganga conserva sus 40 habitaciones originales | OK |

Para estar seguros con el calculo de la desviacion estandar poblacional, verificamos la de Taganga a mano: $(14 - 25.5)^2 + (22 - 25.5)^2 + (30 - 25.5)^2 + (36 - 25.5)^2 = 132.25 + 12.25 + 20.25 + 110.25 = 275$. Al dividir $275 / 4$ da $68.75$, y su raiz cuadrada es $\sqrt{68.75} \approx 8.29$, que coincide exacto con lo que imprime el programa.

Despues hicimos otra pasada usando `hoteles.csv` y `ocupacion.csv` (las dos semanas completas de noviembre):

| Caso | Que probamos | Datos ingresados | Resultado en pantalla | Estado |
|---|---|---|---|---|
| 3.15 | Rodadero | Sol Caribe Rodadero | 82.14 % y cero dias criticos; el dia mas ocupado sale el 2026-11-07 (el 14 tambien tuvo 80, pero muestra el primero) | OK |
| 3.16 | Taganga | Sol Caribe Taganga | Tiene dos rachas de 2 dias y muestra la primera, que empieza el 2026-11-03 | OK |
| 3.17 | Minca | Sol Caribe Minca | 45.71 % y una racha critica de 4 dias desde el 2026-11-09 | OK |
| 3.18 | Cienaga con 25 ocupadas todos los dias | Sol Caribe Cienaga | Desviacion estandar en 0.0 | OK |

## 4. Comparacion entre hoteles y dias pendientes por registrar

Primero revisamos la opcion 5 del menu:

| Caso | Que probamos | Datos ingresados | Resultado en pantalla | Estado |
|---|---|---|---|---|
| 4.1 | Comparar sin tener hoteles | Programa recien abierto | Avisa que ningun hotel tiene dias registrados | OK |
| 4.2 | Un solo hotel sin dias | Crear Palomino y entrar a opcion 5 | Sale el mismo aviso | OK |
| 4.3 | Datos del enunciado junto con Minca y Palomino | Mismos datos cargados en la seccion 3 | Mas alto Rodadero (64.0 %) y mas bajo Minca (55.0 %); a Palomino lo ignora porque no tiene dias | OK |
| 4.4 | Empate exacto entre dos hoteles | `hoteles_empate.csv` y `ocupacion_empate.csv` | Sol Caribe Buritaca sale como el mas alto y el mas bajo (48.0 %) por haberse cargado antes que Don Diego | OK |
| 4.5 | Los cinco hoteles de noviembre | `hoteles.csv` y `ocupacion.csv` | Mas alto Rodadero (82.14 %) y mas bajo Minca (45.71 %) | OK |

El caso 4.4 lo agregamos por un error raro de decimales que detectamos probando: si haciamos `promedio / habitaciones * 100` tal cual, Python daba `48.0` para Buritaca pero `48.00000000000001` para Don Diego, haciendo que Don Diego ganara el empate cuando los dos tenian exactamente 48 %. Lo resolvimos haciendo una sola division: `noches * 100 / (dias * habitaciones)`.

Luego probamos el conteo de dias sin registrar en la opcion 4. Este dato depende de la fecha del computador (se resta la fecha de hoy menos el dia siguiente al ultimo registrado; si da 0 o negativo, aparece al dia):

| Caso | Que probamos | Datos ingresados | Resultado en pantalla | Estado |
|---|---|---|---|---|
| 4.6 | Rodadero con la fecha del PC en 20 de noviembre de 2026 | Datos de la seccion 3, Sol Caribe Rodadero | Ultimo dia 2026-11-05 y faltan 14 dias, del 2026-11-06 al 2026-11-19 | OK |
| 4.7 | Minca con el PC en 2 de noviembre de 2026 | Datos de la seccion 3, Sol Caribe Minca | Avisa que el registro esta al dia | OK |
| 4.8 | Hotel con fecha futura (año 2030) | Crear Hotel Futuro (10, 2030/1/1), registrar 5 y abrir informe | Aparece al dia porque su ultimo dia registrado es posterior a hoy | OK |

## 5. Carga desde CSV, menu y guardado al salir

Para la opcion 6 siempre arrancamos con el programa recien abierto:

| Caso | Que probamos | Datos ingresados | Resultado en pantalla | Estado |
|---|---|---|---|---|
| 5.1 | Cargar hoteles del enunciado | `hoteles_enunciado.csv` | Carga 2 hoteles y reporta 5 lineas descartadas: linea 4 (0 hab.), 5 (falta un campo), 6 ("cuarenta"), 7 (Taganga repetido) y 8 (30 de febrero) | OK |
| 5.2 | Cargar ocupacion del enunciado | `ocupacion_enunciado.csv` | Carga 9 dias y descarta 5 lineas: linea 10 (-1 en Taganga), 12 (Riohacha no existe), 13 (81 en Rodadero), 14 ("setenta") y 15 (falta el numero) | OK |
| 5.3 | Verificar orden de fechas tras cargar | Despues del 5.2, opcion 4 con Rodadero | Tiene 5 dias y el ultimo corresponde al 2026-11-05 | OK |
| 5.4 | Ruta de archivo que no existe | `datos/no_existe.csv` | Avisa que el archivo no existe y no pide el de ocupacion | OK |
| 5.5 | Poner una carpeta en vez de archivo | `datos` | Avisa que no se pudo leer el archivo | OK |
| 5.6 | Hoteles bien pero ocupacion inexistente | `hoteles_enunciado.csv` y `datos/no_existe.csv`, luego informe de Rodadero | Los hoteles quedan cargados en memoria pero sin dias registrados | OK |
| 5.7 | Intentar cargar ya teniendo hoteles | Crear Minca y entrar a opcion 6 | Bloquea la carga avisando que solo se permite sin hoteles y no pide rutas | OK |
| 5.8 | Cargar archivos dos veces seguidas | Cargar los del enunciado y volver a opcion 6 | Muestra el mismo aviso y no deja volver a cargar | OK |
| 5.9 | Archivos con espacios y lineas en blanco | `hoteles_espacios.csv` y `ocupacion_espacios.csv` | Carga 1 hotel y descarta solo la linea 5 (nombre vacio). En ocupacion carga 2 dias y descarta linea 4 (un campo de mas) y linea 5 (nombre en minuscula) | OK |
| 5.10 | Carga completa de los 5 hoteles de noviembre | `hoteles.csv` y `ocupacion.csv` | Carga 5 hoteles y 52 dias sin descartar ninguna linea | OK |

Con el caso 5.9 nos paso algo curioso al principio: habiamos anotado que no debia descartar la linea 4 y la prueba nos fallo. Revisando el archivo de ocupacion nos dimos cuenta de que el codigo estaba bien y la linea 4 de verdad traia un campo de mas, asi que ajustamos el caso de prueba.

Por ultimo, probamos validaciones del menu principal y la opcion 7 (salir):

| Caso | Que probamos | Datos ingresados | Resultado en pantalla | Estado |
|---|---|---|---|---|
| 5.11 | Numero de opcion que no existe | 8 | Dice que la opcion no es valida y regresa al menu | OK |
| 5.12 | Opcion escrita con letras | dos | Mismo comportamiento | OK |
| 5.13 | Salir sin hoteles creados | 7 | Cierra directo sin preguntar si desea guardar | OK |
| 5.14 | Salir eligiendo no guardar | Crear Minca, opcion 7, responder `n` | Cierra el programa sin generar archivos | OK |
| 5.15 | Guardar al salir | Crear Minca, simular 4 dias con 5 y 5, crear Palomino (30, 2026/11/10), opcion 7, responder `s` | Genera `hoteles_guardados.csv` y `ocupacion_guardada.csv` | OK |
| 5.16 | Volver a cargar lo guardado | Abrir el programa de nuevo, opcion 6 con `hoteles_guardados.csv` y `ocupacion_guardada.csv`, y ver informe de Minca | Carga los 2 hoteles y 4 dias; Minca aparece con 20 noches vendidas | OK |

La opcion de guardar al salir fue el requisito adicional que decidimos incluir como equipo para poder conservar los datos entre una ejecucion y otra sin tener que digitar todo de nuevo.