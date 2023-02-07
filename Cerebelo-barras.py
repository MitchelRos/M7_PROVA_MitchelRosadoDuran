import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from numpy import random


def rng():
    TeenTitans = []
    TeenNotans = []
    for x in range(10):
        num = int(random.uniform(1, 48))
        efe = afa(num)
        ere = ampa(num)
        TeenTitans.append(efe)
        TeenNotans.append(ere)

    return TeenTitans, TeenNotans


def afa(num):
    lt = pd.read_csv("Mitchel Waldi Rosado Duran - Llistat.csv", usecols=['ID', 'NAME']).dropna()
    result = lt[(lt['ID'] == num)]
    result = result['NAME']
    return ''.join(result)


def ampa(num):
    lt = pd.read_csv("Mitchel Waldi Rosado Duran - Llistat.csv", usecols=['ID', 'NOTES']).dropna()
    result = lt[(lt['ID'] == num)]
    result = result['NOTES'].sum()
    return ''.join(result)


fig, ax = plt.subplots()

fruits = rng()[0]
counts = rng()[1]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:red', 'tab:blue', 'tab:red', 'tab:orange','tab:red', 'tab:blue']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('Notas')
ax.set_title('Media de la nota? creo')
ax.legend(title='Mitchel')

plt.show()
