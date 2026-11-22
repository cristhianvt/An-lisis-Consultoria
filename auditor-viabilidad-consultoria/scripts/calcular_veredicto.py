#!/usr/bin/env python3
"""Calcula el índice ponderado, el veredicto y las brechas de una auditoría
de viabilidad para consultoría independiente.

Uso:
    python calcular_veredicto.py --d1 7 --d2 5 --d3 6 --d4 8 --d5 4 [--json]

La lógica replica la sección "Índice y veredicto" de references/rubrica.md.
"""

import argparse
import json
import sys

DIMENSIONES = {
    "d1": ("Profundidad técnica y de nicho", 0.25),
    "d2": ("Paquetes de servicio vendibles", 0.20),
    "d3": ("Red de contactos y posicionamiento", 0.20),
    "d4": ("Gestión de proyectos y entregables", 0.15),
    "d5": ("Mentalidad comercial", 0.20),
}

VEREDICTOS = [  # de mejor a peor
    "VIABLE — Lanzar ahora",
    "VIABLE CON CONDICIONES",
    "EN PREPARACIÓN",
    "NO VIABLE AÚN",
]

UMBRAL_LANZAMIENTO = 7


def veredicto_base(indice):
    if indice >= 7.5:
        return 0
    if indice >= 6.0:
        return 1
    if indice >= 4.5:
        return 2
    return 3


def evaluar(p):
    indice = round(sum(p[k] * DIMENSIONES[k][1] for k in DIMENSIONES), 1)
    nivel = veredicto_base(indice)
    reglas = []
    dims_en_tope = set()

    def tope(nivel_max, nombre, motivo, dims):
        # Registra toda regla que aplique, aunque el veredicto ya estuviera por
        # debajo de su tope: el informe debe mostrar todas las alarmas.
        nonlocal nivel
        cambia = nivel < nivel_max
        if cambia:
            nivel = nivel_max
        reglas.append({"regla": nombre, "motivo": motivo,
                       "tope": VEREDICTOS[nivel_max], "cambio_veredicto": cambia})
        dims_en_tope.update(dims)

    if p["d1"] < 6:
        tope(2, "Regla de nicho", "D1 < 6: sin especialidad clara se compite por precio.", ["d1"])
    bajas = [k for k in DIMENSIONES if p[k] <= 3]
    if bajas:
        tope(2, "Regla de piso",
             "Dimensión(es) ≤ 3: " + ", ".join(k.upper() for k in bajas) + ".", bajas)
    if p["d3"] <= 4 and p["d5"] <= 4:
        tope(3, "Regla de demanda",
             "D3 ≤ 4 y D5 ≤ 4: sin red ni capacidad de venta no habrá primeros clientes.",
             ["d3", "d5"])
    bajo_6 = [k for k in DIMENSIONES if p[k] < 6]
    if bajo_6:
        tope(1, "Regla de lanzamiento",
             "Dimensión(es) < 6 impiden lanzar ya: " + ", ".join(k.upper() for k in bajo_6) + ".",
             [])

    brechas = []
    for k, (nombre, _) in DIMENSIONES.items():
        b = UMBRAL_LANZAMIENTO - p[k]
        if b <= 0:
            continue
        if k in dims_en_tope or b >= 3:
            sev = "Crítica"
        elif b == 2:
            sev = "Importante"
        else:
            sev = "Deseable"
        brechas.append({"dimension": k.upper(), "nombre": nombre,
                        "puntaje": p[k], "brecha": b, "severidad": sev})
    orden = {"Crítica": 0, "Importante": 1, "Deseable": 2}
    brechas.sort(key=lambda x: (orden[x["severidad"]], -x["brecha"]))

    return {
        "puntajes": {k.upper(): p[k] for k in DIMENSIONES},
        "indice": indice,
        "veredicto_base": VEREDICTOS[veredicto_base(indice)],
        "veredicto": VEREDICTOS[nivel],
        "reglas_activadas": reglas,
        "brechas": brechas,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    for k, (nombre, _) in DIMENSIONES.items():
        ap.add_argument(f"--{k}", type=int, required=True, help=nombre)
    ap.add_argument("--json", action="store_true", help="Salida en JSON")
    args = ap.parse_args()
    p = {k: getattr(args, k) for k in DIMENSIONES}
    fuera = [k for k, v in p.items() if not 1 <= v <= 10]
    if fuera:
        sys.exit(f"Error: los puntajes deben estar entre 1 y 10 ({', '.join(fuera)}).")

    r = evaluar(p)
    if args.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
        return

    print("Puntajes:")
    for k, (nombre, peso) in DIMENSIONES.items():
        print(f"  {k.upper()} {nombre:<38} {p[k]:>2}/10  (peso {int(peso * 100)} %)")
    print(f"\nÍndice ponderado: {r['indice']}/10")
    print(f"Veredicto base por índice: {r['veredicto_base']}")
    if r["reglas_activadas"]:
        print("Reglas de tope que aplican:")
        for x in r["reglas_activadas"]:
            efecto = "bajó el veredicto" if x["cambio_veredicto"] else "ya cubierta por el índice"
            print(f"  - {x['regla']} (tope: {x['tope']}; {efecto}): {x['motivo']}")
    print(f"VEREDICTO FINAL: {r['veredicto']}")
    if r["brechas"]:
        print("\nBrechas frente al umbral de lanzamiento (7):")
        for b in r["brechas"]:
            print(f"  - [{b['severidad']}] {b['dimension']} {b['nombre']}: "
                  f"{b['puntaje']}/10 (faltan {b['brecha']})")
    else:
        print("\nSin brechas frente al umbral de lanzamiento (7).")


if __name__ == "__main__":
    main()
