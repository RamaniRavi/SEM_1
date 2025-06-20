import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data from Excel
dataframe = pd.read_excel('D:\\Koblenz\Sem1\WIR\Exercise\Assignment 01\code\\titanic_data.xlsx') 

#----------------------------------------
# plot dataframe bar 

gender_counts = dataframe['gender'].value_counts()
gender_counts.plot(kind='bar', color=['steelblue', 'hotpink'])

plt.title('Titanic Passengers by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Passengers')
plt.xticks(rotation=0)

#labels
for index, value in enumerate(gender_counts):
    plt.text(index, value + 5, str(value), ha='center', fontsize=12)

plt.tight_layout()
plt.show()

#----------------------------------------
# SQL like queries (2 Points)
# Write the (SQL like) query for dataframe to retrieval records of males ('M') survived
# Note: the dataframe's name is "dataframe".
male_survivors = dataframe[(dataframe['gender']=='M') & (dataframe['survived'] == 'yes')]

print(male_survivors.head())