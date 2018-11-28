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
AgVac = dataset[['Agency', '# Of Positions']]
AgVac = AgVac.groupby('Agency', sort = False).sum()


# Використовуючи бібліотеку Matplotlib відобразити отримані дані у вигляді стовпцеві діаграми. 
AgVac[:20].plot(kind = 'bar')

# Task 4
# Відобразити графіки залежності середнього значення 
# зарплати від локації та категорії роботи. 

#Залежність середнього значення зарплати від локації
Location_Salary =  dataset[['Work Location', 'Salary Range To']]
Location_Salary.columns = ['Work Location', 'Mean Salary']
Salary = (dataset['Salary Range To']+dataset['Salary Range From'])/2
Location_Salary.loc[:]['Mean Salary'] = Salary[:]

# Групуєм однакові локації
Location_Salary = Location_Salary.groupby('Work Location', sort = False).sum()

# Середня зарплата кожної локаці
Location_Salary.loc[:]['Mean Salary'] = Location_Salary['Mean Salary']/dataset['Work Location'].value_counts(sort=False)

# Виводимо графік
Location_Salary[:20].plot(kind='bar')

# Залежність середнього значення зарплати від категорії роботи
Category_Salary = dataset[['Job Category', 'Salary Range To']]
Category_Salary.columns = ['Job Category', 'Mean Salary']
Category_Salary.loc[:]['Mean Salary']= Salary[:]

# Групуєм однакові категорії
Category_Salary = Category_Salary.groupby('Job Category', sort = False).sum()

# Середня зарплата кожної категорії
Category_Salary.loc[:]['Mean Salary'] = Category_Salary['Mean Salary']/dataset['Job Category'].value_counts(sort=False)

# Виводимо графік
Category_Salary[:20].plot(kind='bar')