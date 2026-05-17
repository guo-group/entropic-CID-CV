# entropic-CID-CV

This repository contains **simulation data only** from "[An Information-theoretic Collective Variable for Configurational Entropy](https://arxiv.org/abs/2602.22440)" by A.Z. Guo, K. Chang, and N.J. Corrente (2026).

The CID calculation code is developed and maintained separately as [kappa-py](https://github.com/guo-group/kappa-py), where two specific simulations, reproduced from the data shared here, serve as examples to illustrate usage. 

## Repository Structure

```
.
├── 0_single-LJ/                # Single-component Lennard-Jones melting
│   ├── NVT-0.85/               # Density of 0.85, melting from FCC to liquid
│   └── NVT-low_density_void/   # Lower density, melting with void formation
├── 1_binary-LJ/                # Binary LJ phase separation
│   ├── bicontinuous/           # Bicontinuous morphology runs
│   └── slab/                   # Slab morphology runs
├── 2_homopolymer/              # Coarse-grained homopolymer condensation/dispersion
└── 3_carbons/                  # Amorphous carbon networks
```

## Systems

Each system directory contains LAMMPS input scripts, saved snapshots, and all computed order parameters (CID, Q<sub>6</sub>, pair correlation entropies, Shannon entropy estimates) for one specific system. Full simulation details are described in the paper. 

### 0. Single-Component Lennard-Jones

4000 LJ atoms in FCC crystal (ρ* = 0.85) heated linearly from T* = 0.01 to T* = 1.5. A lower density example, which forms a void during melting, is also shared. 

### 1. Binary Lennard-Jones Phase Separation

13,500 atoms (equimolar A/B) with asymmetric interactions at ρ* = 0.8. Equilibrated at T* = 5.0, then quenched to T* = 1.0. Independent runs produce both slab and bicontinuous morphologies, which are shared in separate folders. 

### 2. Coarse-Grained Homopolymer

500 chains × 20 bead homopolymer system undergoing thermal cycling from T* = 5.0 to T* = 0.1, then to T* = 5.0, followed by stepwise cooling back to T* = 0.1.

### 3. Amorphous Carbons

Approximately 4000 carbon atoms at densities 0.5–2.0 g/cm<sup>3</sup>, generated via annealed molecular dynamics with the EDIP/c potential, each annealed at 4000 K for 3 ns.

## Citation

If you use this data, please cite the accompanying paper:

```
@misc{guo2026configentropycv,
      title={An Information-theoretic Collective Variable for Configurational Entropy}, 
      author={Ashley Z. Guo and Kaelyn Chang and Nicholas J. Corrente},
      year={2026},
      eprint={2602.22440},
      archivePrefix={arXiv},
      primaryClass={cond-mat.stat-mech},
      url={https://arxiv.org/abs/2602.22440}, 
}
```



