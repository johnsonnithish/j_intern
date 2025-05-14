import pandas as pd

emp = pd.read_csv("Employee 1000x.csv")

class Employees():
    def __init__(self, emp=emp):
        self.emp = emp

    def emp_info(self):
        return self.emp.head(5).to_dict(orient="records")

    def gender_div(self):
        return self.emp["Sex"].value_counts().to_dict()
