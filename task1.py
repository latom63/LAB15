students_data = {
    "Name": ["Anna", "Bohdan", "Maria", "Oleksandr", "Iryna", "Dmytro"],
    "Group": ["IT-21", "IT-21", "IT-22", "IT-22", "IT-21", "IT-22"],
    "Subject": ["Math", "Math", "Physics", "Physics", "Math", "Physics"],
    "Score": [89, 76, 91, 85, 78, 95]
}
import pandas as pd

# Перетворення словника у DataFrame
df = pd.DataFrame(students_data)

# Групування за групами та обчислення середнього балу
grouped = df.groupby("Group").agg({"Score": "mean"}).rename(columns={"Score": "Average Score"})

print("Original DataFrame:")
print(df)

print("\nGrouped DataFrame with Average Score:")
print(grouped)
