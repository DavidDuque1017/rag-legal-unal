"""Buscador de referencia: cuenta palabras en común. Es el piso que hay que superar."""
import re

from rag.datos import cargar_chunks

_CHUNKS = cargar_chunks()


def _palabras(texto: str) -> set[str]:
    return set(re.findall(r"\w+", texto.lower()))


_INDICE = [(_palabras(c["texto"]), c) for c in _CHUNKS]


def buscar(pregunta: str, k: int = 5) -> list[dict]:
    consulta = _palabras(pregunta)
    puntuados = sorted(
        ((len(consulta & palabras), c) for palabras, c in _INDICE),
        key=lambda par: par[0],
        reverse=True,
    )
    return [{"id": c["id"], "puntaje": p, "texto": c["texto"]} for p, c in puntuados[:k]]
