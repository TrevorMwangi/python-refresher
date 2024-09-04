import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 92, 78]
})

# Apply a lambda function to create a new column
df['Grade'] = df['Score'].apply(lambda x: 'Pass' if x >= 80 else 'Fail')
print(df)

