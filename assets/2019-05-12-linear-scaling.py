import numpy as np
import matplotlib.pyplot as plt

year, s1, s2, s3, s4, s5 = np.loadtxt("linear-scaling.txt", comments="#", unpack=True)

plt.figure(figsize=(8,4))

plt.ylim(1,1e5)
plt.xlim(1990,2020)

plt.semilogy(year, s1, color = 'green',label='Yang\'s 1991 paper citation')
plt.semilogy(year, s3, color = 'blue',label='Kohn\'s 1996 paper citation')
plt.semilogy(year, s2, color = 'orange',label='Goedecker\'s 1999 paper citation')
plt.semilogy(year, s4, color = 'red',label='electronic structure papers mentioning linear scaling')
plt.semilogy(year, s5, color = 'black',label='electronic structure papers')
plt.title('linear-scaling electronic structure publication data')
plt.xlabel('year')
plt.ylabel('# of publications per year')
plt.legend()

plt.savefig("2019-05-12-linear-scaling.pdf",bbox_inches='tight',pad_inches=0.01)
