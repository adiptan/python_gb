class Worker:
    _income = {'wage': 0,
               'bonus:': 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus



class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

    def get_full_name(self):
        return self.name, self.surname


a = Position('Alex', 'Diptan', 'Python-developer', 7000, 2000)
print(f'Coworker name: {a.get_full_name()[0]} {a.get_full_name()[1]}, total income is {a.get_total_income()}$')
