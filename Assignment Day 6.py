#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

# 1. Create DataFrame
data = {'Name': ['John', 'Alice', 'Bob', 'Diana'],
        'Age': [28, 34, 23, 29],
        'Department': ['HR', 'IT', 'Marketing', 'Finance'],
        'Salary': [45000, 60000, 35000, 50000]}
df = pd.DataFrame(data)

# 2. Display first 2 rows
print("First 2 rows:")
print(df.head(2))

# 3. Add 'Bonus' column
df['Bonus'] = df['Salary'] * 0.10

# 4. Calculate average salary
avg_salary = df['Salary'].mean()
print(f"\nAverage Salary: {avg_salary}")

# 5. Filter employees older than 25
older_than_25 = df[df['Age'] > 25]
print("\nEmployees older than 25:")
print(older_than_25)


# In[ ]:




