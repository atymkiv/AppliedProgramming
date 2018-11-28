# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Task 1
# Importing the dataset
dataset = pd.read_csv('NYC_Jobs.csv')

# Task 2
# Вивести 10 значень датасету 
ten = dataset.iloc[:10, :]

# Вивести значення стовпця "Agency" для перших десяти
Agency_ten = dataset.iloc[:10,1]

# Вивести значення стовпців “Agency”, “Business Title” та “Work Location 1” для всіх записів датасету. 
ABW_all = dataset.iloc[:,[1,4,13]]
dataset[['Agency', 'Business Title', 'Work Location']]

# Task 3 
# Вивести назви агентств та кількість вакансій, які вони подали. 
AgVac = dataset.iloc[:,[1,3]].values

# Використовуючи бібліотеку Matplotlib відобразити отримані дані у вигляді стовпцеві діаграми. 
index = np.arange(len(AgVac[:,0]))
plt.bar(index,AgVac[:,1])
plt.xlabel('Name of Agency', fontsize=5)
plt.ylabel('No of vacations', fontsize=5)
plt.xticks(index, AgVac[:,0], fontsize=5, rotation=30)
plt.show()