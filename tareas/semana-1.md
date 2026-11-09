# Semana 1: normas y conjunto de prueba

**Entrega:** parte 1, miércoles 11 de noviembre; parte 2, viernes 13 de noviembre antes de la reunión (8 p. m.).

**Para qué:** antes de escribir el RAG necesitamos dos cosas: los textos de las normas y una forma de saber si el sistema acierta. Es como armar el examen con su solucionario antes de que el estudiante lo presente. El viernes 13 cerramos la parte de datos y empezamos con el resto del RAG.

Todos hacen la parte 1. En la parte 2 cada uno tiene un frente asignado. Nadie tiene que esperar a otro para empezar.

## Alcance de la primera versión

- **Qué entra:** las normas de pregrado publicadas en el Régimen Legal (acuerdos, resoluciones y las circulares que una norma cite) y el calendario académico de la sede Medellín, porque varios plazos dependen de él.
- **Qué no entra como fuente:** guías de facultad, cartillas y copias en otros sitios. Sirven de pista para encontrar la norma, pero la respuesta y el texto salen de las fuentes de arriba.
- **Cuando la respuesta depende de la sede o la facultad:** se responde para la sede Medellín y se anota que depende.

Hay una tabla de [pistas por pregunta](semana-1-pistas.md) con las normas que probablemente responden cada una. Son pistas sin verificar: sirven para saber dónde empezar a buscar.

## Parte 1 (todos, hasta el miércoles 11): de la pregunta al texto de la norma

Cada uno recorre el camino completo con 2 preguntas: pregunta, norma y texto guardado.

1. Entra a las [preguntas del proyecto](https://github.com/Mr-Percival/rag-legal-unal/issues?q=is%3Aissue+label%3Apregunta) y escoge 2. Comenta `Yo la tomo` para que nadie repita. Si ya no quedan libres, crea una nueva y respóndela.
2. Busca la respuesta en el [Régimen Legal](https://legal.unal.edu.co/rlunal/home/). El sitio pide una verificación antes de abrir cada norma.
3. Comenta en el issue con este formato:

```text
Respuesta: lo que diría una persona que conoce la norma, en 1 a 3 frases.
Norma: tipo, número, año y órgano. Ejemplo: Acuerdo 000 de 0000 del CSU.
Artículo: el artículo y el parágrafo exactos.
Texto: copia aquí el fragmento literal que lo sustenta.
Enlace: la dirección de la norma en el Régimen Legal.
Vigencia: ¿alguna norma posterior la modificó? Di cuál o escribe "no encontré".
```

4. Guarda el texto completo de cada norma que citaste, en un archivo propio dentro de `datos/normas/`. El nombre va en minúsculas y con guiones: `acuerdo-000-0000-csu.md`. Si el archivo ya existe, otra persona ya la guardó y no hay que repetirla. El archivo empieza con esta ficha y sigue con el texto de la norma, copiado tal cual:

```text
---
norma: Acuerdo 000 de 0000
organo: Consejo Superior Universitario
tema: de qué trata, en una línea
enlace: la dirección en el Régimen Legal
vigente: sí, parcial, no o no sé
modificada_por: las normas que le cambian o le quitan texto, o "no encontré"
relacionadas: las normas que la reglamentan, delegan o le hacen excepciones
formato_origen: HTML, PDF con texto o PDF escaneado
guardada_por: tu usuario de GitHub
---
```

Sin Git también se puede: en GitHub, entra a `datos/normas/`, botón **Add file → Create new file**, pega el contenido y confirma.

Para guardar una norma larga sin copiarla a pedazos: ábrela en el navegador, pasa la verificación, y usa Ctrl+P → «Guardar como PDF». De ese PDF se copia el texto completo con sus notas.

Escribe siempre número, año y órgano. Hay normas con el mismo número: el Acuerdo 033 de 2007 del CSU y el Acuerdo 033 de 2008 del CSU son distintos, y el Acuerdo 026 de 2012 es del Consejo Académico, no del CSU.

**Cómo leer la vigencia.** El Régimen Legal no tiene una casilla de «vigente»: las notas van dentro del texto de la norma. Estas palabras no significan lo mismo:

| Nota | Qué significa | Dónde va en la ficha |
|---|---|---|
| Deroga | Le quita validez a la norma o al artículo | `modificada_por`; `vigente: no` o `parcial` |
| Modifica | Le cambia el texto | `modificada_por` |
| Reglamenta | Detalla cómo se aplica, sin cambiarla | `relacionadas` |
| Delega | Le pasa a otro órgano la decisión | `relacionadas` |
| Exceptúa | Suspende un artículo para un caso o un periodo | `relacionadas` |

Si la norma no resuelve la pregunta, o si dos normas se contradicen, escríbelo. Esos casos también sirven: el sistema debe aprender a decir «no encontré sustento». Va a pasar: varias preguntas usan palabras que la norma no usa, o preguntan por un número que la norma no fija. «La norma no lo fija; lo que dice es esto» es una respuesta válida.

No copies la respuesta de un chatbot. Esta es la referencia con la que vamos a calificar al RAG, así que tiene que salir de la norma.

**El sitio tiene verificación anti-robots: no la saltes.** Las normas se abren y se copian a mano.

## Parte 2 (tu frente, hasta el viernes 13)

| Frente | Responsable |
|---|---|
| A. Mapa y vigencia | Kelineth |
| B1. Formatos y extracción de artículos | Nicolás |
| B2. Estatuto Estudiantil y normas faltantes | David y Gustavo |
| C. Cómo vamos a calificar | Juan Diego |

Los frentes rotan cada semana: al terminar el proyecto, todos habrán pasado por datos, búsqueda, modelo y evaluación. Además, cada semana hay una parte corta que hacemos todos, para que nadie se quede sin tocar el tema de la semana.

### Frente A: mapa y vigencia

No hace falta programar.

1. Lee todas las preguntas (no esperes las respuestas) y haz la lista de las normas que necesita la primera versión, incluidas las que nadie ha guardado todavía. Empieza por estas dos páginas de la Dirección Nacional de Programas de Pregrado, que dicen qué norma y qué artículo rige cada trámite: [marco normativo](https://pregrado.unal.edu.co/marconormativo) y [procesos administrativos](https://pregrado.unal.edu.co/procesosadministrativo). Son índice, no fuente: cada norma se confirma en el Régimen Legal.
2. Por cada norma, revisa si está vigente y qué normas la modifican o la reemplazan.
3. Desde el miércoles, compara tu lista con las fichas de `datos/normas/` y corrige lo que no coincida.

**Entregable:** `datos/normas.csv` (nombre, enlace, tema, vigente, modificada por, relacionadas, si ya está guardada).

### Frente B1: formatos y extracción de artículos

Nicolás también mantiene el repositorio y responde las dudas de la semana.

1. Averigua en qué formato sirve el sitio las normas: HTML, PDF con texto o PDF escaneado.
2. Con 3 normas de formatos distintos, prueba si se pueden separar los artículos y parágrafos sin dañar el texto. Puedes empezar hoy con cualquier norma del sitio.

**Entregable:** el código de la prueba en `exploracion/` y una nota corta con lo que funcionó y lo que no.

### Frente B2: el Estatuto Estudiantil y las normas faltantes

1. David: entre hoy y mañana, guarda completo el Acuerdo 008 de 2008 del CSU (Estatuto Estudiantil) en `datos/normas/`. Casi todas las preguntas pasan por él, así que los demás lo van a necesitar.
2. Gustavo: guarda, con la misma ficha, las normas de las preguntas que nadie tomó y el calendario académico vigente de la sede Medellín. Luego, entre los dos, las que el mapa marque como faltantes.
3. Entre los dos: revisen si alguna dependencia publica las normas con sus notas de vigencia en un formato más cómodo que el Régimen Legal. Lo que encontramos hasta ahora son copias sin notas o con enlaces caídos.

**Entregable:** las normas guardadas y una nota corta con lo que encontraste en el punto 3.

### Frente C: cómo vamos a calificar

Para quien quiere ir a lo de IA.

Propón cómo medir si el sistema acierta, y explícalo en un issue, en menos de una página:

- ¿Cómo sabemos que encontró el artículo correcto?
- ¿Cómo sabemos que la respuesta es fiel a ese artículo?
- ¿Qué hace el sistema cuando la norma no responde la pregunta?

**Entregable:** el issue, con un ejemplo calificado a mano. Usa una de tus propias preguntas de la parte 1 para no depender de nadie.

## Si te trabas

Pregunta por el grupo de WhatsApp. Es mejor preguntar el martes que llegar sin nada el viernes.
