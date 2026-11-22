---
name: auditor-viabilidad-consultoria
description: Audita una hoja de vida (CV), certificaciones y experiencia laboral para decidir si la persona está lista para lanzar una firma o práctica de consultoría independiente. Puntúa de 1 a 10 cinco dimensiones (profundidad técnica y de nicho, capacidad de empaquetar servicios vendibles, red de contactos y posicionamiento, gestión de proyectos y entregables, mentalidad comercial) y entrega un diagnóstico de brechas, un veredicto de viabilidad y un plan de 30 días. Úsala siempre que alguien comparta su CV, perfil de LinkedIn o trayectoria y pregunte si puede o debe independizarse como consultor, montar su propia consultora, trabajar como freelance experto, "dar el salto" desde un empleo corporativo, o quiera saber qué le falta para vender consultoría, aunque no use la palabra "viabilidad" ni "auditoría".
---

# Auditor de viabilidad para consultoría independiente

Esta skill convierte una trayectoria profesional en una decisión: ¿puede esta persona sostener una práctica de consultoría hoy, y si no, qué le falta y qué hace en los próximos 30 días?

El valor está en la franqueza. Quien pregunta esto suele estar a punto de arriesgar ingresos estables; un diagnóstico complaciente le hace más daño que uno duro. Puntúa con base en evidencia, no en adjetivos del CV, y di claramente lo que no está demostrado.

## Flujo de trabajo

### 1. Reunir el material

Trabaja con lo que la persona entregue: CV (PDF, Word, texto pegado), lista de certificaciones, perfil de LinkedIn copiado, descripción libre de su experiencia. Si hay archivos, léelos completos (usa la skill de PDF o DOCX si están disponibles).

Un CV casi nunca muestra tres cosas que pesan mucho en la decisión: la red de contactos real, la experiencia vendiendo y la situación financiera. Si no aparecen, haz **una sola ronda** de máximo 6 preguntas cortas antes de puntuar. Usa `references/preguntas-complementarias.md` para elegir las que falten. Si la persona prefiere no responder o pide el resultado directo, continúa y marca esas dimensiones con confianza baja; no bloquees el informe.

No pidas datos que ya están en el material.

### 2. Construir el inventario de evidencia

Antes de puntuar, extrae los hechos (internamente o en una tabla breve si ayuda a la persona):

- Roles, empresas, sectores, años en cada uno, y la progresión.
- Logros cuantificados (ahorros, ingresos, reducción de riesgos, plazos).
- Certificaciones: cuáles son de nicho y exigentes vs. genéricas o de asistencia; vigencia; relevancia para lo que vendería.
- Exposición a clientes: ¿trabajó del lado del proveedor, en consultoría, en preventa, o siempre como empleado interno?
- Entregables tangibles que ha producido (metodologías, informes, implementaciones, capacitaciones).
- Visibilidad pública: publicaciones, conferencias, docencia, comunidad, contenido.
- Experiencia comercial directa: propuestas, cierres, cuotas, gestión de cuentas, fijación de precios.

Distingue **años** de **profundidad**: diez años repitiendo la misma función operativa no equivalen a diez años resolviendo problemas cada vez más difíciles en un dominio.

### 3. Puntuar las cinco dimensiones

Lee `references/rubrica.md` y asigna a cada dimensión un entero de 1 a 10 usando sus anclas. Para cada una registra:

- **Puntaje** (1–10)
- **Evidencia** que lo justifica (cita hechos concretos del material)
- **Lo que falta** para subir un escalón
- **Confianza** (alta / media / baja) según cuánta evidencia directa hay

Las cinco dimensiones:

1. **Profundidad técnica y de nicho** — ¿Hay un dominio específico donde la persona resuelve problemas que otros no pueden, y por los que alguien pagaría a un externo?
2. **Capacidad de traducir experiencia en paquetes de servicio vendibles** — ¿Puede convertir lo que sabe en ofertas con alcance, entregables, duración y precio definidos?
3. **Red de contactos y posicionamiento** — ¿Quién la conoce, la recomendaría o le compraría, y cómo es percibida en su mercado?
4. **Gestión de proyectos y entregables** — ¿Ha llevado proyectos de inicio a fin, con alcance, plazos, presupuesto y stakeholders, entregando a satisfacción?
5. **Mentalidad comercial** — ¿Ha vendido, negociado, prospectado o asumido riesgo de ingresos? ¿Tiene tolerancia a la incertidumbre de no tener sueldo fijo?

Reglas de calibración (importan porque sin ellas los puntajes se inflan):

- Afirmaciones sin evidencia ("experto en", "líder estratégico") no suben el puntaje. Lo que no se puede verificar en el material cuenta como no demostrado.
- Un 7 significa "suficiente para lanzar en esa dimensión". Reserva 9–10 para casos excepcionales y demostrables.
- Si la confianza es baja, elige el puntaje conservador del rango plausible y dilo.
- No promedies mentalmente las dimensiones entre sí: un nicho brillante no compensa en la puntuación una red inexistente; eso se refleja en el veredicto.

### 4. Calcular el índice y el veredicto

Ejecuta el script (está en la carpeta `scripts/` de esta skill) para que el veredicto sea consistente entre auditorías:

```bash
python <ruta-de-la-skill>/scripts/calcular_veredicto.py --d1 <n> --d2 <n> --d3 <n> --d4 <n> --d5 <n>
```

Devuelve el índice ponderado, el veredicto, las reglas de tope que aplican (y si cambiaron el veredicto) y las brechas contra el umbral de lanzamiento (7) con su severidad. Si no puedes ejecutar Python, aplica a mano la misma lógica descrita en `references/rubrica.md` (sección "Índice y veredicto").

Los cuatro veredictos posibles:

| Veredicto | Significado práctico |
|---|---|
| **VIABLE — Lanzar ahora** | Puede renunciar o formalizar la firma en el corto plazo. |
| **VIABLE CON CONDICIONES** | Puede lanzar, pero cerrando 1–2 brechas en paralelo y con colchón financiero. |
| **EN PREPARACIÓN** | Conviene una práctica paralela (sin dejar el empleo) durante 3–6 meses para validar. |
| **NO VIABLE AÚN** | Primero hay que construir base: nicho, red o experiencia comercial, en 6–12 meses. |

Puedes matizar el veredicto con lo que sepas del contexto (p. ej., ahorros para 12 meses, un primer cliente ya comprometido), pero si te apartas del resultado del script, explica por qué en una frase.

### 5. Diagnóstico de brechas

Para cada dimensión por debajo de 7, describe la brecha en términos concretos y clasifícala:

- **Crítica**: bloquea el lanzamiento o activó una regla de tope.
- **Importante**: frena el crecimiento en los primeros 6 meses.
- **Deseable**: mejora la posición, pero no impide empezar.

Ordena por impacto. Señala también las **fortalezas apalancables**: lo que la persona ya tiene y debe usar como palanca en el plan (por ejemplo, un ex-empleador que podría ser su primer cliente).

### 6. Plan de 30 días

Diseña el plan alrededor de las brechas críticas e importantes, no de una plantilla genérica. Cuatro semanas, y en cada una:

- **Objetivo** de la semana (una frase)
- **Acciones** concretas (3–5), con verbos y cantidades ("contactar a 15 ex-colegas", no "hacer networking")
- **Entregable** verificable al cierre de la semana
- **Métrica** de éxito

Ajusta la ambición al veredicto:

- *Viable / Con condiciones*: el plan apunta a cerrar el primer contrato o piloto pagado en el día 30.
- *En preparación*: el plan apunta a validar la oferta con conversaciones reales y conseguir un primer proyecto pequeño en paralelo al empleo.
- *No viable aún*: el plan apunta a construir la base que falta (nicho, visibilidad, una experiencia comercial) y a reevaluar al día 30.

Todo plan incluye, sin importar el veredicto, conversaciones con compradores potenciales reales desde la semana 2. La razón: la única validación que importa en consultoría es que alguien quiera pagar, y posponer ese contacto es el error más común de quien se independiza.

Cierra el plan con un **punto de decisión al día 30**: qué resultados indicarían avanzar, ajustar o esperar.

## Formato del informe

Responde en español (o en el idioma de la persona si escribe en otro). Usa esta estructura:

```markdown
# Auditoría de viabilidad para consultoría independiente

## Resumen ejecutivo
[3–4 frases: perfil en una línea, veredicto, índice, la brecha principal y la palanca principal.]

## Perfil analizado
[Nicho/oferta potencial identificada y supuestos usados. Lista de lo que no se pudo verificar.]

## Puntuación por dimensión

| # | Dimensión | Puntaje | Confianza |
|---|---|---|---|
| 1 | Profundidad técnica y de nicho | x/10 | alta/media/baja |
| 2 | Paquetes de servicio vendibles | x/10 | ... |
| 3 | Red de contactos y posicionamiento | x/10 | ... |
| 4 | Gestión de proyectos y entregables | x/10 | ... |
| 5 | Mentalidad comercial | x/10 | ... |
| | **Índice de viabilidad ponderado** | **x.x/10** | |

### 1. Profundidad técnica y de nicho — x/10
**Evidencia:** ...
**Lo que falta para subir:** ...
[Repetir para las 5 dimensiones]

## Diagnóstico de brechas
| Brecha | Dimensión | Severidad | Por qué importa |
|---|---|---|---|

**Fortalezas apalancables:** ...

## Veredicto: [VEREDICTO]
[Párrafo con la razón del veredicto, reglas de tope activadas si las hay, y qué cambiaría el veredicto.]

## Plan de 30 días
### Semana 1 (días 1–7): [objetivo]
- Acciones...
- **Entregable:** ...
- **Métrica:** ...
[Semanas 2, 3 y 4]

### Punto de decisión — día 30
[Criterios para avanzar / ajustar / esperar.]
```

Si la persona pide el informe como documento (Word, PDF, doc compartible), genera el archivo con la herramienta o skill correspondiente usando esta misma estructura.

## Recursos

- `references/rubrica.md` — anclas de puntaje por dimensión, señales positivas y de alerta, ponderaciones y reglas del veredicto. Léela siempre antes de puntuar.
- `references/preguntas-complementarias.md` — banco de preguntas para cubrir lo que el CV no muestra.
- `scripts/calcular_veredicto.py` — cálculo determinista del índice, veredicto y brechas.
