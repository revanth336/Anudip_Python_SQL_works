import pandas as pd
import numpy as np

# Sample Python dictionary data and list labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

# Create a DataFrame from the 'exam_data' dictionary
df = pd.DataFrame(exam_data)

# Select the 'name' and 'score' columns
df_selected = df[['name', 'score']]

print(df_selected)
