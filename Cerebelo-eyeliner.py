import pandas as pd
import matplotlib.pyplot as plt
from numpy import random


def rng():
    TeenTitans = []
    for x in range(10):
        num = int(random.uniform(1, 48))
        efe = afa(num)
        TeenTitans.append(efe)

    return TeenTitans

def afa(num):
    lt = pd.read_csv("Mitchel Waldi Rosado Duran - Llistat.csv", usecols=['ID', 'NAME']).dropna()
    result = lt[(lt['ID'] == num)]
    result = result['NAME']
    return ''.join(result)


plt.plot([10,30,20], 'go-', label='line 1', linewidth=2)
plt.axis([0, 10, 0, 30])
plt.legend()
plt.show()
