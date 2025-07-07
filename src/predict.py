import pandas as pd

# Load data
df = pd.read_csv('data/students.csv')

# Simple rule-based predictor (demo)
def predict_performance(row):
    avg = (row['Test1'] + row['Test2'] + row['Assignment']) / 3
    if avg >= 85:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

# Apply prediction
df['Predicted_Grade'] = df.apply(predict_performance, axis=1)

# Output result
print(df[['Student_ID', 'Final_Grade', 'Predicted_Grade']])

# Save to file
df.to_csv('output/predicted_grades.csv', index=False)
