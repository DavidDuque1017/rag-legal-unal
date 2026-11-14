# Sprint 1 (13 al 20 de noviembre)

- **Meta:** una pregunta entra, sale una respuesta con el artículo citado, y medimos cuántas acierta.
- **Corpus:** solo el Estatuto Estudiantil, en `datos/normas/acuerdo-008-2008-csu.md`.
- **Examen:** `datos/preguntas.jsonl`.
- **Entrega:** viernes 20, 8 p. m. Código en `main` por *pull request* y demostración de 5 minutos con tu número.

## Tu tarea

| Quién | Qué construyes | Archivo | Hecho cuando | Lectura (Huyen) |
|---|---|---|---|---|
| David | Partidor: un chunk por artículo o parágrafo, con la norma que lo modificó o derogó | `rag/partir.py` → `datos/chunks.jsonl` | Una prueba reconstruye la norma desde los chunks sin perder ni duplicar texto | Cap. 6, pp. 267-273 |
| Kelineth | Búsqueda por palabras (BM25) | `rag/buscar_bm25.py` | Supera en `recall@5` a `rag.buscar_simple` y compara al menos dos formas de preparar el texto | Cap. 6, pp. 257-267 |
| Juan Diego | Búsqueda por significado (embeddings) | `rag/buscar_denso.py` | Supera en `recall@5` a `rag.buscar_simple` y compara al menos dos modelos de embeddings | Cap. 6, pp. 257-267; cap. 3, pp. 134-136 |
| Gustavo | Respuesta con cita literal y abstención | `rag/responder.py`, `rag/verificar_cita.py` | Reporta el porcentaje de citas que pasan la comprobación por código y el de abstenciones correctas | Cap. 5, pp. 220-235; cap. 2, pp. 99-105 |
| Nicolás | Medición de las respuestas y ensamble | `evaluar.py`, `rag/pipeline.py` | Un comando imprime los números de todos | Cap. 4, pp. 200-208 |

Todos: cap. 6, pp. 253-257 (qué es un RAG y cómo se arma).

## Para empezar hoy

- **Chunks:** mientras no exista `datos/chunks.jsonl`, `rag.datos.cargar_chunks()` entrega `datos/ejemplo/chunks.jsonl`, con los 62 artículos partidos de forma simple.
- **Medición:** `python evaluar.py rag.buscar_simple` imprime `recall@5` y MRR; con `--fallos` lista las preguntas que no acertó. Cambia el nombre del módulo por el tuyo.
- **Piso:** `rag/buscar_simple.py` cuenta palabras en común. Es el número que hay que superar.
- **Gustavo:** `responder` recibe el buscador como parámetro y usa `rag.buscar_simple` por defecto, así no depende de las búsquedas de los demás.
- **El recorrido completo:** `python -m rag.pipeline "¿Puedo aplazar el semestre?"` corre búsqueda y respuesta con piezas de referencia. Ahí se ve dónde encaja la tuya.

## Por dónde empezar

Es un punto de partida, no una obligación: si encuentras algo mejor, úsalo y defiéndelo.

| Quién | Herramienta | Video |
|---|---|---|
| Todos | Leer `rag/buscar_simple.py`: 20 líneas que ya cumplen el contrato | [Sparse, Dense & Hybrid](https://www.youtube.com/watch?v=r0Dciuq0knU) (8 min) |
| David | Expresiones regulares (`re`) sobre el texto de la norma | [RAG From Scratch, parte 2](https://www.youtube.com/watch?v=bjb_EMsTDKI) (5 min) |
| Kelineth | La librería `bm25s` | [BM25 and Hybrid Search](https://www.youtube.com/watch?v=lD3_VF5bmWg) (10 min) |
| Juan Diego | La librería `sentence-transformers` con un modelo multilingüe | [¿Qué son las bases de datos vectoriales?](https://www.youtube.com/watch?v=MCqViT-yHpY) (14 min, en español) |
| Gustavo | La API gratuita de Gemini o de Groq, con salida en JSON | [RAG From Scratch, parte 2](https://www.youtube.com/watch?v=bjb_EMsTDKI) (5 min) |

## Glosario

| Término | En una línea |
|---|---|
| Chunk | Un pedazo de la norma que se busca y se cita por separado; aquí, un artículo o un parágrafo |
| BM25 | Búsqueda que puntúa cada chunk según las palabras que comparte con la pregunta y qué tan raras son |
| Embedding | Un vector de números que representa el significado de un texto; textos parecidos quedan cerca |
| `recall@5` | De cada 100 preguntas, en cuántas aparece el artículo correcto entre los 5 primeros resultados |
| MRR | Qué tan arriba queda el artículo correcto: 1 si sale de primero, 0,5 si sale de segundo |
| Cita literal | Un fragmento copiado tal cual del chunk; se comprueba por código que existe |
| Abstención | Responder «no encontré sustento» en vez de inventar |
| Contrato | El formato fijo de entrada y salida de cada pieza; por dentro, cada uno hace lo que quiera |

## Contratos

`datos/chunks.jsonl`, una línea por chunk:

```json
{"id": "acuerdo-008-2008-csu#art-12", "norma": "Acuerdo 008 de 2008 del CSU", "articulo": "Artículo 12", "jerarquia": "Capítulo II > Artículo 12", "texto": "...", "enlace": "...", "vigente": "sí", "modificado_por": []}
```

El `id` de un parágrafo empieza por el de su artículo: `acuerdo-008-2008-csu#art-12-par-1`.

`datos/preguntas.jsonl`, una línea por pregunta:

```json
{"id": "s001", "pregunta": "...", "ids_correctos": ["acuerdo-008-2008-csu#art-12"], "respuesta_referencia": "...", "tiene_sustento": true}
```

Funciones:

```python
def buscar(pregunta: str, k: int = 5) -> list[dict]:
    # [{"id": ..., "puntaje": ..., "texto": ...}], del más al menos relevante

def responder(pregunta: str, buscar=buscar_simple) -> dict:
    # {"respuesta": str, "ids_citados": [str], "cita_literal": str, "sin_sustento": bool}
```

Una búsqueda acierta si alguno de los `k` resultados es un artículo correcto o uno de sus parágrafos.

## Reglas

- La herramienta y el método los escoges y los defiendes tú.
- Todo *pull request* lleva al menos una prueba.
- Las llaves de los modelos no se suben.
- Si una pregunta hace fallar tu pieza, agrégala al examen.
- Puedes programar con asistentes de IA. El viernes explicas cualquier línea de tu código si te la preguntan.

## Si te trabas

Veinte minutos por tu cuenta; después, al grupo de WhatsApp.
