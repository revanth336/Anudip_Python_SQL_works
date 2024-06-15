import pandas as pd

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Create a Pandas Series from the exam scores data
exam_scores_series = pd.Series(exam_scores, index=students)

print(exam_scores_series)
