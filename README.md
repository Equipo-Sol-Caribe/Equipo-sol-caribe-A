Cadena Hotelera Sol Caribe (Alternativa A)

Trabajo final de programación hecho en Python para llevar el control de la ocupación diaria de los hoteles de la cadena Sol Caribe. Funciona completamente por consola y usa solo librerías estándar de Python.

Integrantes

- Miguel Vergara (leMichael158)
- Jhonatan Gonzales (JhonatanGonzalez-Ruiz)
- Estefany Idarraga (estefanyidarraga22)
- Juan Montes (juanescalderon35-max)

Video explicativo

Enlace del video: https://youtu.be/ooW1YHiyC70

Archivos del proyecto

- `business_logic.py`: tiene las clases `Hotel` y `CadenaHotelera` con la lógica, validaciones, cálculos y lectura/escritura de los archivos CSV.
- `user_interface.py`: contiene el menú por consola y todo lo que interactúa con el usuario.
- `datos/`: carpeta con los archivos `.csv` de prueba (hoteles y ocupación).
- `casos_de_verificacion.md`: casos probados para revisar errores y verificar el cumplimiento del enunciado.
- `Producto_1_Documento_de_Analisis.md`: documento de análisis.
- `Producto_2_Informe_Integral.md`: informe integral del desarrollo, decisiones y verificación.
- `Producto_5_Informe_Uso_IA.md`: informe formal y verificable del uso de IA generativa.
- `evidencias_ia/`: índice de enlaces y evidencias asociadas al informe de IA.
- `datos/`: archivos CSV usados para comprobar la carga y persistencia.

 Qué permite hacer el programa

1. Crear hoteles validando nombre, habitaciones habilitadas y fecha de inicio.
2. Registrar las habitaciones ocupadas del día siguiente uno por uno.
3. Simular varios días de ocupación eligiendo un mínimo y un máximo.
4. Consultar el informe completo de un hotel (noches vendidas, promedio, porcentaje de ocupación, desviación estándar, día más y menos ocupado, días por nivel, racha crítica más larga y días faltantes por registrar).
5. Ver qué hotel tiene el porcentaje de ocupación más alto y cuál el más bajo.
6. Cargar hoteles y registros de ocupación desde archivos `.csv` separados por punto y coma (`;`).
7. Guardar los datos

