from nothing import Nothing

class Inhabitant(object):
    """description of class"""

    amount_members = 0
    def __init__(self, name = Nothing(), surname = Nothing(), gender = Nothing(), age = Nothing(), status = Nothing()):
        Inhabitant.amount_members += 1

        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.status = status
        
        if(status == 'S'):
            self.duty_degree = 2
        else:
            self.duty_degree = 0

    def __str__(self):
        return f"name - {self.name} surname - {self.surname} hender - {self.gender} age - {self.age}; status - {self.status}"

    def __del__(self):  # Деструктор класса
        Inhabitant.amount_members -= 1


