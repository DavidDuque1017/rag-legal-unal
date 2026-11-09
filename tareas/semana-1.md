# Semana 1: normas y conjunto de prueba

**Entrega:** parte 1, miércoles 11 de noviembre; parte 2, viernes 13 de noviembre antes de la reunión (8 p. m.).

**Para qué:** antes de escribir el RAG necesitamos dos cosas: los textos de las normas y una forma de saber si el sistema acierta. Es como armar el examen con su solucionario antes de que el estudiante lo presente. El viernes 13 cerramos la parte de datos y empezamos con el resto del RAG.

Esta guía dice qué hay que lograr y en qué formato se entrega. El cómo lo decide cada uno: buscar, equivocarse y encontrar el camino es parte del trabajo. Nadie tiene que esperar a otro para empezar.

## Alcance de la primera versión

- **Qué entra:** las normas de pregrado publicadas en el [Régimen Legal](https://legal.unal.edu.co/rlunal/home/) (acuerdos, resoluciones y las circulares que una norma cite) y el calendario académico de la sede Medellín, porque varios plazos dependen de él.
- **Qué no entra como fuente:** guías de facultad, cartillas y copias en otros sitios. Sirven de pista para encontrar la norma, pero la respuesta y el texto salen de las fuentes de arriba.
- **Cuando la respuesta depende de la sede o la facultad:** se responde para la sede Medellín y se anota que depende.

## Parte 1 (todos, hasta el miércoles 11)

### 1. Trae 5 preguntas nuevas

Pregúntales a compañeros de verdad qué dudas tienen sobre la normativa y crea cada una como [pregunta del proyecto](https://github.com/Mr-Percival/rag-legal-unal/issues/new?template=pregunta.yml). Mientras más se parezcan a como habla un estudiante, mejor. Con 25 preguntas nuevas pasamos de 8 a más de 30.

### 2. Responde 3 preguntas que no hayas escrito tú

Escógelas en la [lista de preguntas](https://github.com/Mr-Percival/rag-legal-unal/issues?q=is%3Aissue+label%3Apregunta) y comenta `Yo la tomo` para que nadie repita. Luego responde en el mismo issue con este formato:

```text
Respuesta: lo que diría una persona que conoce la norma, en 1 a 3 frases.
Norma: tipo, número, año y órgano. Ejemplo: Acuerdo 000 de 0000 del CSU.
Artículo: el artículo y el parágrafo exactos.
Texto: copia aquí el fragmento literal que lo sustenta.
Enlace: la dirección de la norma en el Régimen Legal.
Vigencia: ¿alguna norma posterior la modificó? Di cuál o escribe "no encontré".
```

Si la norma no resuelve la pregunta, no fija lo que se pregunta o dos normas se contradicen, eso es lo que se escribe. «La norma no lo fija; lo que dice es esto» es una respuesta válida, y esos casos son valiosos: el sistema debe aprender a decir «no encontré sustento».

No copies la respuesta de un chatbot. Esta es la referencia con la que vamos a calificar al RAG, así que tiene que salir de la norma.

### 3. Guarda el texto completo de cada norma que citaste

Un archivo por norma en `datos/normas/`, con el nombre en minúsculas y con guiones: `acuerdo-000-0000-csu.md`. Si el archivo ya existe, otra persona ya la guardó. El archivo empieza con esta ficha y sigue con el texto de la norma, copiado tal cual, con sus notas:

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

El Régimen Legal no tiene una casilla de «vigente»: las notas van dentro del texto de la norma, y no todas significan lo mismo.

| Nota | Qué significa | Dónde va en la ficha |
|---|---|---|
| Deroga | Le quita validez a la norma o al artículo | `modificada_por`; `vigente: no` o `parcial` |
| Modifica | Le cambia el texto | `modificada_por` |
| Reglamenta | Detalla cómo se aplica, sin cambiarla | `relacionadas` |
| Delega | Le pasa a otro órgano la decisión | `relacionadas` |
| Exceptúa | Suspende un artículo para un caso o un periodo | `relacionadas` |

**El sitio tiene verificación anti-robots: no la saltes.** Las normas se abren y se guardan a mano.

## Parte 2 (tu frente, hasta el viernes 13)

Cada frente es una pregunta que su responsable le contesta al grupo el viernes, en 5 minutos: qué encontró, cómo lo sabe y qué no funcionó.

| Frente | Responsable | La pregunta que defiende |
|---|---|---|
| Mapa y vigencia | Kelineth | ¿Qué normas necesita la primera versión y cuáles siguen vigentes? |
| Estatuto Estudiantil | David | ¿Qué dice hoy el Estatuto y en qué se diferencia de lo que se aprobó en 2008? |
| Normas faltantes | Gustavo | ¿Qué nos falta para responder las preguntas, y hay una fuente mejor que el Régimen Legal? |
| Cómo vamos a calificar | Juan Diego | ¿Cómo sabemos que el sistema acertó? |
| Formatos y extracción | Nicolás | ¿Se pueden separar los artículos de forma automática sin dañar el texto? |

**Mapa y vigencia (Kelineth).** Entregable: `datos/normas.csv` con nombre, enlace, tema, vigente, modificada por, relacionadas y si ya está guardada. Tiene que quedar claro con qué criterio una norma entra o se queda por fuera.

**Estatuto Estudiantil (David).** Entregable: el Acuerdo 008 de 2008 del CSU completo en `datos/normas/`, a más tardar el martes 10 en la noche, porque muchas preguntas pasan por él. Y la lista de los artículos que han cambiado desde 2008, con la norma que los cambió.

**Normas faltantes (Gustavo).** Entregable: guardadas las normas que respondan preguntas que nadie tomó, las que el mapa marque como faltantes y el calendario académico vigente de la sede Medellín. Y una nota corta con las fuentes oficiales que revisaste y qué tan confiables son.

**Cómo vamos a calificar (Juan Diego).** Entregable: un issue de menos de una página con la propuesta para medir tres cosas (si encontró el artículo correcto, si la respuesta es fiel a ese artículo y qué hace cuando la norma no responde) y un ejemplo calificado a mano con una de tus preguntas.

**Formatos y extracción (Nicolás).** Entregable: una prueba con 3 normas de formatos distintos en `exploracion/` y una nota con lo que funcionó y lo que no. Nicolás también mantiene el repositorio.

## Parte 3 (todos): un recurso para el grupo

Cada uno agrega a [`recursos.md`](../recursos.md) un recurso que haya encontrado sobre su frente (un artículo, un video, un repositorio, un proyecto parecido), con tres líneas: qué es, por qué sirve y para qué parte del proyecto. El viernes lo cuenta en un minuto. La idea es que el material del proyecto lo armemos entre todos.

## Si te trabas

Dale primero 20 minutos por tu cuenta. Si sigues trabado, pregunta por el grupo de WhatsApp: es mejor preguntar el martes que llegar sin nada el viernes.
