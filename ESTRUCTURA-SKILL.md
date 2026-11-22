# Estructura de la skill `auditor-viabilidad-consultoria`

## 1. Árbol de archivos

```
auditor-viabilidad-consultoria/
├── SKILL.md                               ← Instrucciones principales (flujo + formato del informe)
├── references/
│   ├── rubrica.md                         ← Criterios de puntuación 1–10, pesos y reglas del veredicto
│   └── preguntas-complementarias.md       ← Banco de preguntas para lo que el CV no muestra
├── scripts/
│   └── calcular_veredicto.py              ← Cálculo automático del índice, veredicto y brechas
└── evals/                                 ← Casos de prueba (no se incluyen en el paquete .skill)
    ├── ciso-banca-sin-experiencia-comercial/
    │   ├── prompt.md
    │   ├── case.yaml
    │   ├── place-files.sh
    │   ├── files/cv_ciso.md
    │   └── graders/01-expected-output.md
    ├── analista-junior-generalista/
    │   ├── prompt.md
    │   ├── case.yaml
    │   └── graders/01-expected-output.md
    └── ingeniero-logistica-info-minima/
        ├── prompt.md
        ├── case.yaml
        └── graders/01-expected-output.md
```

Paquete instalable: `auditor-viabilidad-consultoria.skill` (contiene `SKILL.md`, `references/` y `scripts/`).

---

## 2. Qué hace cada archivo

| Archivo | Función |
|---|---|
| `SKILL.md` | Define cuándo se activa la skill, los 6 pasos de trabajo y la plantilla exacta del informe final. |
| `references/rubrica.md` | Describe 5 niveles (1–2, 3–4, 5–6, 7–8, 9–10) por cada dimensión, con señales positivas y de alerta. Contiene los pesos y las reglas que pueden bajar el veredicto. |
| `references/preguntas-complementarias.md` | Preguntas agrupadas por dimensión. Se usan como máximo 6, en una sola ronda, solo si falta información. |
| `scripts/calcular_veredicto.py` | Recibe los 5 puntajes y devuelve el índice ponderado, el veredicto, las reglas aplicadas y las brechas con su severidad. Garantiza que el mismo perfil reciba siempre el mismo veredicto. |
| `evals/` | Tres perfiles ficticios para probar la skill: un CISO senior que nunca ha vendido, una analista junior generalista y un ingeniero con información mínima. |

---

## 3. Flujo de trabajo de la skill

1. **Reunir el material:** lee el CV, las certificaciones y el perfil. Si faltan datos sobre red de contactos, experiencia comercial o finanzas, hace hasta 6 preguntas en una sola ronda.
2. **Inventario de evidencia:** extrae roles, logros cuantificados, certificaciones (de nicho o genéricas), exposición a clientes, entregables, visibilidad pública y experiencia comercial.
3. **Puntuar las 5 dimensiones (1–10):** cada puntaje lleva la evidencia que lo justifica, lo que falta para subir y el nivel de confianza (alta, media o baja).
4. **Calcular el índice y el veredicto** con el script.
5. **Diagnóstico de brechas:** clasifica cada brecha como crítica, importante o deseable, y señala las fortalezas que se pueden aprovechar.
6. **Plan de 30 días:** 4 semanas, cada una con objetivo, acciones concretas, entregable y métrica, y un punto de decisión al día 30.

---

## 4. Las 5 dimensiones y sus pesos

| # | Dimensión | Peso | Pregunta clave |
|---|---|---|---|
| D1 | Profundidad técnica y de nicho | 25 % | ¿Hay un problema específico que resuelves mejor que la media y por el que se paga a externos? |
| D2 | Paquetes de servicio vendibles | 20 % | ¿Puedes convertir lo que sabes en ofertas con alcance, entregables y precio? |
| D3 | Red de contactos y posicionamiento | 20 % | ¿Cuántos decisores te conocen y te contratarían o recomendarían en 90 días? |
| D4 | Gestión de proyectos y entregables | 15 % | ¿Puedes prometer un resultado con alcance, plazo y presupuesto, y cumplirlo? |
| D5 | Mentalidad comercial | 20 % | ¿Puedes generar demanda, hablar de dinero y vivir con ingresos variables? |

**Umbral de lanzamiento:** 7 = suficiente para operar como consultor independiente en esa dimensión.

---

## 5. Veredicto

**Índice ponderado** = suma de (puntaje × peso).

| Índice | Veredicto | Significado |
|---|---|---|
| 7,5 o más | **VIABLE — Lanzar ahora** | Puede formalizar la firma en el corto plazo. |
| 6,0 – 7,4 | **VIABLE CON CONDICIONES** | Lanzar cerrando 1–2 brechas en paralelo y con colchón financiero. |
| 4,5 – 5,9 | **EN PREPARACIÓN** | Práctica paralela al empleo durante 3–6 meses. |
| Menos de 4,5 | **NO VIABLE AÚN** | Construir base primero (6–12 meses). |

**Reglas de tope** (solo bajan el veredicto, nunca lo suben):

1. **Nicho:** D1 < 6 → como máximo EN PREPARACIÓN.
2. **Piso:** cualquier dimensión ≤ 3 → como máximo EN PREPARACIÓN.
3. **Demanda:** D3 ≤ 4 y D5 ≤ 4 → NO VIABLE AÚN.
4. **Lanzamiento:** cualquier dimensión < 6 → como máximo VIABLE CON CONDICIONES.

**Severidad de brechas** (brecha = 7 − puntaje):
- **Crítica:** activó una regla de tope, o la brecha es de 3 o más.
- **Importante:** brecha de 2.
- **Deseable:** brecha de 1.

---

## 6. Estructura del informe que entrega

1. Resumen ejecutivo
2. Perfil analizado (nicho identificado, supuestos y lo que no se pudo verificar)
3. Tabla de puntuación por dimensión + índice ponderado
4. Detalle por dimensión (evidencia y lo que falta para subir)
5. Diagnóstico de brechas + fortalezas aprovechables
6. Veredicto razonado
7. Plan de 30 días (semanas 1–4) + punto de decisión al día 30

---

## 7. Uso del script

```bash
python scripts/calcular_veredicto.py --d1 8 --d2 6 --d3 7 --d4 8 --d5 4
python scripts/calcular_veredicto.py --d1 8 --d2 6 --d3 7 --d4 8 --d5 4 --json
```
