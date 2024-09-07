import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate random experience values (between 1 and 15 years)
experience = np.round(np.random.uniform(1, 15, 40), 1)

# Generate random salaries with some correlation to experience
# Base salary with some random noise
base_salary = 30000 + experience * 5000 + np.random.normal(0, 5000, 40)
salary = np.round(base_salary, 2)

# Create a DataFrame
data = pd.DataFrame({
    'Experience (Years)': experience,
    'Salary': salary
})

print(data)
