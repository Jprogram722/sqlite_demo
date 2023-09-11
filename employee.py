# This is just the employee class for the sqlite demo

class Employee:

    """
    This is a class for an Employee object
    """
    
    def __init__(self, fname: str, lname: str, salary: str) -> None:
        self.fname = fname
        self.lname = lname
        self.salary = salary

    @property
    def email(self) -> str:
        return f"{self.fname}.{self.lname}.olgee.com"
    
    @property
    def fullname(self) -> str:
        return f"{self.fname} {self.lname}"
    
    def __repr__(self) -> str:
        return f"Employee({self.fname}, {self.lname}, {self.salary})"
