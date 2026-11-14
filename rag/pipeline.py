"""Recorrido completo con piezas de referencia: pregunta -> buscar -> responder.

Uso:
    python -m rag.pipeline "¿Puedo aplazar el semestre?"

Sirve para ver dónde encaja cada pieza. `responder_simple` no usa un modelo de
lenguaje: solo cita el inicio del chunk mejor puntuado. La pieza real va en
rag/responder.py y debe devolver el mismo formato.
"""
import json
import sys

from rag.buscar_simple import buscar as buscar_simple


def responder_simple(pregunta: str, buscar=buscar_simple) -> dict:
    resultados = buscar(pregunta, 5)
    if not resultados or resultados[0]["puntaje"] <= 0:
        return {"respuesta": "No encontré sustento.", "ids_citados": [], "cita_literal": "", "sin_sustento": True}
    mejor = resultados[0]
    return {
        "respuesta": f"Lo más cercano está en {mejor['id']}.",
        "ids_citados": [mejor["id"]],
        "cita_literal": mejor["texto"][:300],
        "sin_sustento": False,
    }


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    pregunta = " ".join(sys.argv[1:]) or "¿Puedo aplazar el semestre?"
    print("Pregunta:", pregunta)
    print("Encontrados:", [r["id"] for r in buscar_simple(pregunta, 5)])
    print(json.dumps(responder_simple(pregunta), ensure_ascii=False, indent=2))
