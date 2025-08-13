# HET 3.0 - SAT Hardness via Ricci Curvature

**A simple, testable hypothesis**:  
The difficulty of SAT instances correlates with the Ricci curvature of their partial solution space.

## 🎯 Quick Test

1. Install: `pip install networkx pysat GraphRicciCurvature`
2. Run: `python HET3.py uf50-01.cnf`
3. Expect: negative values for easy instances, positive for hard ones.

## 📊 Validation Package

- `HET3.py` - Minimal implementation (50 lines)
- `data/instances.txt` - 20 benchmark instances (10 easy, 10 hard)
- `results/` - For your validation outputs

## 🤝 How to Help

Just run `HET3.py` on any SAT instance and share the HET3 value + solving time.  
Results → open a GitHub issue or email me.

## 📬 Contact
berny berny7147@gmail.com

## 📄 License
CC BY-NC 4.0 
