import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Department": ["CSE", "CSE", "ECE", "EEE", "CSE"],
    "Company": ["TCS", "Infosys", "None", "Wipro", "Accenture"],
    "Package_LPA": [4.5, 5.0, 0, 3.8, 6.2],
    "Status": ["Placed", "Placed", "Not Placed", "Placed", "Placed"]
}

df = pd.DataFrame(data)

df.to_csv("placements.csv", index=False)

print("CSV created successfully")