#! python3

import numpy as np

def create_polymer_chains(n_chains, n_monomers, box_size):
    total_atoms = n_chains * n_monomers
    total_bonds = n_chains * (n_monomers - 1)

    with open('init.data', 'w') as f:
        f.write("LAMMPS data file - polymer chains\n\n")
        f.write(f"{total_atoms} atoms\n")
        f.write(f"{total_bonds} bonds\n")
        f.write("0 angles\n0 dihedrals\n0 impropers\n\n")
        f.write("1 atom types\n")
        f.write("1 bond types\n\n")
        f.write(f"{-box_size} {box_size} xlo xhi\n")
        f.write(f"{-box_size} {box_size} ylo yhi\n")
        f.write(f"{-box_size} {box_size} zlo zhi\n\n")
        f.write("Masses\n\n")
        f.write("1 1.0\n\n")

        # Write atoms
        f.write("Atoms # molecular\n\n")
        atom_id = 1
        for chain_id in range(1, n_chains + 1):
            # Random starting position
            cx = np.random.uniform(-box_size+10, box_size-10)
            cy = np.random.uniform(-box_size+10, box_size-10)
            cz = np.random.uniform(-box_size+10, box_size-10)

            for i in range(n_monomers):
                # Start compact along x-axis
                x = cx + i * 0.97
                y = cy + np.random.uniform(-0.1, 0.1)
                z = cz + np.random.uniform(-0.1, 0.1)
                f.write(f"{atom_id} {chain_id} 1 {x:.6f} {y:.6f} {z:.6f}\n")
                atom_id += 1

        # Write bonds
        f.write("\nBonds\n\n")
        bond_id = 1
        atom_id = 1
        for chain_id in range(n_chains):
            for i in range(n_monomers - 1):
                f.write(f"{bond_id} 1 {atom_id} {atom_id+1}\n")
                bond_id += 1
                atom_id += 1
            atom_id += 1  # Skip to next chain

create_polymer_chains(500, 20, 20)
# 500 chains of 20 monomers each in size 40 box
