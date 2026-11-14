"""Carga de chunks y preguntas. Todas las piezas leen los datos por aquí."""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CHUNKS = RAIZ / "datos" / "chunks.jsonl"
CHUNKS_EJEMPLO = RAIZ / "datos" / "ejemplo" / "chunks.jsonl"
PREGUNTAS = RAIZ / "datos" / "preguntas.jsonl"


def _leer_jsonl(ruta: Path) -> list[dict]:
    with open(ruta, encoding="utf-8") as f:
        return [json.loads(linea) for linea in f if linea.strip()]


def cargar_chunks() -> list[dict]:
    """Usa datos/chunks.jsonl si existe; si no, el archivo de ejemplo."""
    return _leer_jsonl(CHUNKS if CHUNKS.exists() else CHUNKS_EJEMPLO)


def cargar_preguntas() -> list[dict]:
    return _leer_jsonl(PREGUNTAS)
