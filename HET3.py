#!/usr/bin/env python3
"""
HET 3.0 - Discrete Ricci curvature predictor for SAT hardness
Usage: python HET3.py <instance.cnf>
"""

import sys, numpy as np, networkx as nx
from pysat.formula import CNF
from GraphRicciCurvature.OllivierRicci import OllivierRicci

def compute_het3(cnf_path, threshold=0.9, samples=500):
    cnf = CNF(from_file=cnf_path)
    n = cnf.nv
    clauses = cnf.clauses
    total = len(clauses)
    
    # Generar asignaciones aleatorias
    valid = []
    for _ in range(samples):
        a = np.random.randint(0, 2, n)
        sat = sum(any((lit>0)==a[abs(lit)-1] for lit in cl) for cl in clauses)
        if sat/total >= threshold:
            valid.append(tuple(a))
    
    if len(valid) < 2:
        return None
    
    # Construir grafo
    G = nx.Graph()
    for a in valid:
        G.add_node(a)
    for i, u in enumerate(valid):
        for v in valid[i+1:]:
            if sum(a!=b for a,b in zip(u,v)) == 1:
                G.add_edge(u, v)
    
    if G.number_of_edges() == 0:
        return None
    
    # Calcular curvatura
    orc = OllivierRicci(G, alpha=0.5)
    orc.compute_ricci_curvature()
    return np.mean([d['ricciCurvature'] for _,_,d in orc.G.edges(data=True)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python HET3.py <instance.cnf>")
        sys.exit(1)
    result = compute_het3(sys.argv[1])
    print("HET3:", result if result is not None else "NaN")
