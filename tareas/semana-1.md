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

## Si te trabas

Veinte minutos por tu cuenta; después, al grupo de WhatsApp.
