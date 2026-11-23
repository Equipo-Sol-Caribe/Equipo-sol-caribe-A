# Informe del uso de inteligencia artificial generativa

**Proyecto:** Cadena Hotelera Sol Caribe (Alternativa A)
**Fecha de corte:** 22 de noviembre de 2026
**Repositorio:** [Equipo-Sol-Caribe/Equipo-sol-caribe-A](https://github.com/Equipo-Sol-Caribe/Equipo-sol-caribe-A)

## 1. Objeto y alcance

Este informe reconstruye el uso de IA generativa durante el desarrollo del sistema de gestión de ocupación hotelera. Se identifican solicitudes, respuestas, decisiones aceptadas, corregidas o rechazadas, errores encontrados y formas de verificación.

No se atribuye una conversación a una persona concreta si el enlace no lo demuestra. Las cuentas de GitHub permiten verificar participación en el repositorio, pero no prueban quién escribió cada mensaje en Claude.

## 2. Fuentes verificables

| Fuente | Evidencia |
|---|---|
| [Conversación 1 de Claude](https://claude.ai/share/9d7cfda3-e86a-41c5-8ec1-fea43a430077) | Solicitud de desarrollo, generación del código, simplificación y reducción de casos de verificación. |
| [Conversación 2 de Claude](https://claude.ai/share/79bed8c4-9898-4374-915b-af5859360b7c) | Revisión del proyecto, detección de errores, correcciones y comparación con los requisitos. |
| [Repositorio](https://github.com/Equipo-Sol-Caribe/Equipo-sol-caribe-A) | Código, datos, documentos, historial y organización del trabajo. |
| [Historial de commits](https://github.com/Equipo-Sol-Caribe/Equipo-sol-caribe-A/commits/main) | Evolución verificable del código y de la documentación. |

Los enlaces 1-2 y 3-4 entregados originalmente eran repetidos; por eso se revisaron dos conversaciones únicas.

## 3. Participantes verificables

El README y GitHub identifican estas cuentas: Miguel Vergara (`leMichael158`), Jhonatan Gonzales (`JhonatanGonzalez-Ruiz`), Estefany Idarraga (`estefanyidarraga22`) y Juan Montes (`juanescalderon35-max`). El historial muestra participación de cuentas del proyecto. Esto no permite asignar cada interacción de Claude a un integrante específico.

## 4. Reconstrucción de las interacciones

### 4.1 Desarrollo inicial

En la [Conversación 1](https://claude.ai/share/9d7cfda3-e86a-41c5-8ec1-fea43a430077) se solicitó desarrollar la Alternativa A completa: menú, validaciones, estadísticas, persistencia CSV y casos de verificación. Claude produjo la base de `business_logic.py`, `user_interface.py` y el documento de casos.

**Decisión:** aceptada como base del proyecto.
**Evidencia:** archivos actuales del repositorio e historial de commits.

### 4.2 Simplificación del código

Se indicó que la primera propuesta era demasiado compleja para un curso inicial y que parecía evidenciar el uso de IA. Claude simplificó estructuras, anotaciones y explicaciones, conservando las validaciones y funcionalidades principales.

**Decisión:** aceptada.
**Verificación reportada en el chat:** reducción de líneas y ejecución de casos. Estas cifras se conservan como resultados declarados por Claude, no como una prueba independiente de este informe.

### 4.3 Simplificación de casos

Se pidió reducir el texto de `casos_de_verificacion.md`. Claude lo reorganizó en tablas y casos breves. Durante la revisión se corrigió una expectativa de prueba relacionada con la carga simultánea de hoteles y ocupación.

**Decisión:** aceptada con corrección de la expectativa.
**Evidencia:** [casos de verificación](https://github.com/Equipo-Sol-Caribe/Equipo-sol-caribe-A/blob/main/casos_de_verificacion.md).

### 4.4 Revisión y corrección

En la [Conversación 2](https://claude.ai/share/79bed8c4-9898-4374-915b-af5859360b7c) se revisaron código, CSV y requisitos. Se detectaron problemas con nombres que contenían punto y coma, respuestas de guardado, validación interna, límites y cobertura de pruebas.

Las correcciones quedaron relacionadas con estos commits:

- [`a4df79f`](https://github.com/Equipo-Sol-Caribe/Equipo-sol-caribe-A/commit/a4df79f): validaciones, carga y casos límite.
- [`fdca395`](https://github.com/Equipo-Sol-Caribe/Equipo-sol-caribe-A/commit/fdca395): persistencia en CSV.
- [`c4877fd`](https://github.com/Equipo-Sol-Caribe/Equipo-sol-caribe-A/commit/c4877fd): rechazo del punto y coma en nombres.
- [`14ba168`](https://github.com/Equipo-Sol-Caribe/Equipo-sol-caribe-A/commit/14ba168): cálculo del nivel diario.

## 5. Decisiones aceptadas, corregidas o rechazadas

| Propuesta | Resultado | Motivo o evidencia |
|---|---|---|
| Generar el sistema completo con siete opciones | Aceptada | Código y menú actuales. |
| Simplificarlo al nivel del curso | Aceptada | Código y documentos actuales. |
| Reducir y humanizar los casos | Aceptada | Archivo de casos actual. |
| Rechazar nombres con `;` | Aceptada | Requisito de CSV y commit `c4877fd`. |
| Validar también desde la lógica interna | Aceptada | `business_logic.py`. |
| Cancelar la opción 2 con Enter | Rechazada | Contradice la repetición obligatoria del requisito. |
| Ignorar mayúsculas en nombres | Rechazada | No coincide con la comparación exigida. |
| Reintentar automáticamente rutas de archivos | Rechazada | No coincide con el flujo solicitado. |

## 6. Errores y verificación

Se revisaron límites de habitaciones, fechas, ocupación, simulación, empates, estadísticas, CSV, hoteles inexistentes y persistencia. La verificación se apoyó en casos documentados, revisión de código, ejecución independiente de la lógica R1-R13 y R15, compilación de los módulos y una prueba básica del menú.

La revisión independiente confirmó:

- lógica de los requisitos R1-R13 y R15: correcta;
- compilación de `business_logic.py` y `user_interface.py`: correcta;
- arranque del menú por consola: correcto;
- R14: revisado en código y flujo del menú.

No se afirma que todos los casos históricos de Claude hayan sido ejecutados nuevamente por un tercero. Las marcas `OK` del documento de casos son evidencia documental del equipo.

## 7. Conclusión

La IA generativa se utilizó como apoyo activo para analizar requisitos, producir código, redactar casos, revisar errores y explicar decisiones. El resultado muestra iteraciones: el equipo pidió simplificación, corrigió expectativas, rechazó propuestas incompatibles y verificó el código mediante casos, revisión y ejecución.

No es verificable con los enlaces quién escribió cada mensaje de Claude. Sí es verificable la evolución técnica mediante los archivos, commits y documentos publicados en el repositorio.

## 8. Evidencias

- [Código principal](https://github.com/Equipo-Sol-Caribe/Equipo-sol-caribe-A/blob/main/business_logic.py)
- [Interfaz](https://github.com/Equipo-Sol-Caribe/Equipo-sol-caribe-A/blob/main/user_interface.py)
- [Casos de verificación](https://github.com/Equipo-Sol-Caribe/Equipo-sol-caribe-A/blob/main/casos_de_verificacion.md)
- [Informe integral](https://github.com/Equipo-Sol-Caribe/Equipo-sol-caribe-A/blob/main/Producto_2_Informe_Integral.md)
- [Tablero GitHub](https://github.com/users/leMichael158/projects/1)
- [Organización y equipo](https://github.com/orgs/Equipo-Sol-Caribe/teams/equipo-sol-caribe/members)
