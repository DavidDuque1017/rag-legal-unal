"""Mide un buscador contra el examen.

Uso:
    python evaluar.py rag.buscar_simple
    python evaluar.py rag.buscar_bm25 --k 5 --fallos

El módulo debe tener una función buscar(pregunta, k) que cumpla el contrato.
"""
import argparse
import importlib

from rag.datos import cargar_preguntas


def acierta(id_recuperado: str, ids_correctos: list[str]) -> bool:
    """Acierta si es el artículo correcto o uno de sus parágrafos (art-12 o art-12-par-1)."""
    return any(id_recuperado == c or id_recuperado.startswith(c + "-") for c in ids_correctos)


def evaluar(buscar, k: int = 5) -> dict:
    preguntas = [p for p in cargar_preguntas() if p["tiene_sustento"]]
    aciertos, suma_rr, fallos = 0, 0.0, []
    for p in preguntas:
        ids = [r["id"] for r in buscar(p["pregunta"], k)]
        posiciones = [i for i, id_ in enumerate(ids, start=1) if acierta(id_, p["ids_correctos"])]
        if posiciones:
            aciertos += 1
            suma_rr += 1 / posiciones[0]
        else:
            fallos.append(p)
    n = len(preguntas)
    return {"preguntas": n, "recall": aciertos / n, "mrr": suma_rr / n, "fallos": fallos}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("modulo", help="por ejemplo rag.buscar_bm25")
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--fallos", action="store_true", help="lista las preguntas que no acertó")
    args = ap.parse_args()

    r = evaluar(importlib.import_module(args.modulo).buscar, args.k)
    print(f"{args.modulo}: recall@{args.k} = {r['recall']:.1%} | MRR = {r['mrr']:.3f} | {r['preguntas']} preguntas")
    if args.fallos:
        for p in r["fallos"]:
            print(f"  {p['id']} {p['ids_correctos']}: {p['pregunta']}")
