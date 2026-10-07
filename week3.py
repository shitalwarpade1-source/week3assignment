# Taking input from the user and casting it into a Float data type
student_GPA = float(input("Enter your GPA: ")) 

# Using If-Elif-Else control flow to determine the letter grade
if student_GPA <= 2.0:
    letter_grade = "D"
elif student_GPA <= 3.0:
    letter_grade = "C"
elif student_GPA <= 3.8:
    letter_grade = "B"
else:
    letter_grade = "A"

# Using an F-String to display the dynamically constructed output
print(f"The student's final letter grade is: {letter_grade}")


import pandas as pd

# 1. Reading the CSV dataset into a DataFrame
df = pd.read_csv("student_data.csv")
print("Original Dataset Preview:")
print(df.head())

# 2. Handling Missing Values (Data Cleaning)
# Finding the average GPA score and using it to fill missing (NaN) values
avg_gpa = df['GPA'].mean()
df['GPA'] = df['GPA'].fillna(avg_gpa)

# 3. Creating a Calculated Column
# Multiplying the age column by 12 to generate a new column for age in months
df['Age_in_Months'] = df['Age'] * 12

# 4. Filtering Rows based on structural criteria
# Filtering the dataset to keep rows where the student's age is greater than 18
filtered_df = df[df['Age'] > 18]

print("\nCleaned and Filtered Dataset Preview:")
print(filtered_df.head())





import matplotlib.pyplot as plt

# Defining structural lists for the plotting parameters
students = ['Alice', 'Bob', 'Charlie', 'David']
gpa_scores = [3.85, 2.90, 3.50, 1.80]

# 1. Generating a standard vertical Bar Chart
plt.bar(students, gpa_scores, color='skyblue')

# 2. Adding informative Visual Metadata (Labels and Title)
plt.xlabel("Student Names")
plt.ylabel("GPA Scores")
plt.title("Student Performance Map (GPA)")

# 3. Executing the layout display rendering interface
plt.show()







