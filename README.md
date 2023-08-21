# Chaos in Topological Dynamical Systems

A dissertation submitted for the degree of BSc (Hons) Mathematics for Fraser Robert Love from the School of Mathematics and Statistics, University of St Andrews.

![alt text](https://fraser.love/content/images/2023/08/bifurcation.png)

## Abstract
A topological dynamical system is comprised of a continuous mapping acting on a compact metric space. This project studies the complex, chaotic behaviour that can arise in these systems. Using the extra condition of compactness present in these systems, proves beneficial
in analysis of chaos and the behaviour of these systems as the underlying mapping is iterated ad infinitum. Various definitions of chaos will be examined, namely, Devaney chaos, Li-Yorke chaos and topological chaos. These definitions encompass aspects of indecomposability, repetitiveness and unpredictability; which when combined give a natural interpretation of chaos. This project shall study how these definitions specifically apply to topological dynamical systems on the interval, the unit circle, in sequence space and on compact countable sets. Numerous important topological properties of chaos will be introduced; such as topological transitivity, sensitive dependence, dense periodic points, scrambled sets, Li-Yorke pairs and positive topological entropy. Foundational tools from symbolic dynamics will be combined with topological conjugacy, to transfer these topological properties between systems. Finally, this text shall conclude by characterising various chaotic systems and comparing the definitions of chaos.

## Contents
- An Introduction to Topological Dynamics
    - Topology, Discrete Dynamics and Topological Dynamical Systems
    - Examples of Topological Dynamical Systems
- Topological and Symbolic Relationships
    - Topological Conjugacy
    - Symbolic Dynamics and the Shift Map
    - Sharkovsky's Forcing and Realisation Theorems
- Topological Characteristics and Definitions of Chaos
    - Topological Transitivity and the Existence of a Dense Orbit
    - Sensitive Dependence on Initial Conditions
    - Devaney Chaos
    - Scrambled Sets and Li-Yorke Chaos
    - Topological Entropy and Topological Chaos
    - Compairing Definitions of Chaos
- Conclusion
- Bibliography

## Installation and Usage of Python Scripts
1. **Create a Python Virtual Environment:**
```bash
python -m venv .venv
source .venv/bin/activate
```

2. **Install Dependencies via PIP:**

```bash
pip install -r requirements.txt
```

3. **Run Any Script:**
```bash
cd code
python diagram.py
```
Images of diagrams are saved as a `.pdf` under the `images` directory.
