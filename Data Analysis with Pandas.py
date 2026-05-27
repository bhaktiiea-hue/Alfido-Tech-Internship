# Import pandas
import pandas as pd

# Load CSV dataset
try:
    df = pd.read_csv("employees.csv")

    print("Original Dataset:\n")
    print(df)

    # Check missing values
    print("\nMissing Values:\n")
    print(df.isnull().sum())


    # Fill missing salary with average salary
    average_salary = df['Salary'].mean()
    df['Salary'].fillna(average_salary, inplace=True)


    print("\nUpdated Dataset:\n")
    print(df)


    # Filter employees from IT department
    print("\nEmployees from IT Department:\n")
    it_employees = df[df['Department'] == 'IT']
    print(it_employees)


    # Group by department and calculate average salary
    print("\nAverage Salary by Department:\n")
    avg_salary = df.groupby('Department')['Salary'].mean()
    print(avg_salary)


except FileNotFoundError:
    print("CSV file not found.")

except Exception as e:
    print("Error:", e)
