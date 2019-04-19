import numpy as np
import matplotlib.pyplot as plt

year, dft, sqm, dft_gaussian, sqm_gaussian, dft_vasp, sqm_mopac = np.loadtxt("DFT-vs-SQM.txt", comments="#", unpack=True)

plt.figure(figsize=(8,4))

plt.ylim(1,1e5)
plt.xlim(1965,2020)

plt.semilogy(year, dft, color = 'black',label='DFT')
plt.semilogy(year, sqm, color = 'red',label='SQM')
plt.semilogy(year, dft_gaussian, color = 'black', ls='--',label='DFT (Gaussian)')
plt.semilogy(year, sqm_gaussian, color = 'red', ls='--',label='SQM (Gaussian)')
plt.semilogy(year, dft_vasp, color = 'black', ls=':',label='DFT (VASP)')
plt.semilogy(year, sqm_mopac, color = 'red', ls=':',label='SQM (MOPAC)')
plt.title('scientific publications: DFT vs. semiempirical quantum mechanics (SQM)')
plt.xlabel('year')
plt.ylabel('# of publications')
plt.legend()

plt.savefig("DFT-vs-SQM.pdf",bbox_inches='tight',pad_inches=0.01)
