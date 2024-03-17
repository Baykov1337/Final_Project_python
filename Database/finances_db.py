from users import Users

class Income():
    def __init__(self, user_id, income, description, source, date):
        self.user_id = user_id
        self.income = income
        self.description = description
        self.source = source
        self.date = date

class Expenses():
    def __init__(self, user_id, expenses, description,source, date):
        self.user_id = user_id
        self.expenses = expenses
        self.description = description
        self.source = source
        self.date = date


class User_Income(Users):
    def __init__(self, FirstName, LastName, user_id, income, description, source, date):
        super().__init__(FirstName, LastName, user_id, income, description, source, date)
        self.user_id = user_id
        self.income = income
        self.description = description
        self.date = date


class User_Expenses(Users):
    def __init__(self, FirstName, LastName, user_id, expenses, description, source, date):
        super().__init__(FirstName, LastName, user_id, expenses, description, source, date)
        self.user_id = user_id
        self.expenses = expenses
        self.description = description
        self.date = date