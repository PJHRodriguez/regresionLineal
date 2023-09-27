
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Salary_dataset.csv')

expe = df['YearsExperience'].values
sala = df['Salary'].values
proy = []

n = expe.size
sum1 = 0
sum2 = 0
sum3 = 0
px = 0
py = 0


for i in range(n):
    px += expe[i] 
    py += sala[i] 


px /=n
py /=n


for i in range(n):
    xi = expe[i]
    yi = sala[i]
    sum1 = sum1 + (xi-px) * (yi-py)
    sum2 = sum2 + (xi-px)**2


m = sum1/sum2
b = py - (m * px)

for i in range(n):
    proy.append(b + m * expe[i]) 

 
plt.xlabel('Años de Experiencia')
plt.ylabel('Salario')
plt.title('Regresion lineal simple Pablo Jesus Hernandez Rodriguez')
plt.plot(expe,proy, linestyle='-', color='red', )
plt.scatter(expe,sala,color="blue",marker='o')
plt.show()
