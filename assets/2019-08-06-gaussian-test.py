import psi4
import numpy as np

atom = psi4.geometry("""
  0 1
  He 0.0 0.0 0.0
  He 0.0 0.0 1.0
""")

def basisspec_psi4_yo__anonymous775(mol, role):
    basstrings = {}
    mol.set_basis_by_symbol("He", "heonlys", role=role)
    basstrings['heonlys'] = """
cartesian
****
He  0
S    1  1.0
0.78125 1.0
****
"""
    return basstrings

psi4.qcdb.libmintsbasisset.basishorde['USERDEFINED'] = basisspec_psi4_yo__anonymous775
psi4.set_options({'basis': 'userdefined',
                  'scf_type': 'pk',
                  'e_convergence': 11,
                  'd_convergence': 11})

eb, wfn = psi4.energy('scf', return_wfn=True)
mints = psi4.core.MintsHelper(wfn.basisset())
S = np.asarray(mints.ao_overlap())
T = np.asarray(mints.ao_kinetic())
V = np.asarray(mints.ao_potential())
H = T + V
print(S)
print(H)
print(T)
print(V)

print(2*(H@np.linalg.inv(S)).trace())
print(2*(T@np.linalg.inv(S)).trace())
print(2*(V@np.linalg.inv(S)).trace())
