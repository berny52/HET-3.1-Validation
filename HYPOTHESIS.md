# HET 3.0 - Hipótesis de validación

## Idea central
La curvatura de Ricci del grafo de soluciones parciales (90% de cláusulas satisfechas) correlaciona (en promedio) de forma inversa con el tiempo de resolución de SAT.

## Predicción mínima reproducible
- **Instancias más fáciles**: HET3 promedio < 0  
- **Instancias más difíciles**: HET3 promedio > 0

## Protocolo sugerido
1. Seleccionar 10 instancias 'uf50' (SATLIB) y 10 instancias difíciles (SAT-Comp).
2. Generar muestras de asignaciones aleatorias, filtrar 0.9 de cláusulas satisfechas.
3. Construir el grafo (nodos=asignaciones; aristas si distancia de Hamming = 1).
4. Calcular curvatura de Ricci (Ollivier, alpha=0.5) y promediar por instancia y por set.
5. Comparar el promedio HET3 con los tiempos reales (p.ej. CaDiCaL).

## Notas
- Resultados preliminares, semilla fija para reproducibilidad.
- Ajustar threshold/samples si el grafo queda muy disperso (NaN).
- No constituye afirmación teórica final.
