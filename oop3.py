class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)
    def check_budget(self, budget):
        #check if the budget is valid
        if not isinstance(budget, (int, float)):
            print('enter float or int')
            exit()
        if budget < 0:
            print('sorry you don\'t have money')
            exit()
    def get_change(self, budget):
        return budget - self.price
    
    def sell(self, budget):
        self.check_budget(budget)
        if budget >= self.price:
            print('its complete')
        else:
            print(f'here is your change {self.get_change(budget)}')
        exit('thanks for your transmission')

small = Coffee('Small', 2)
regular = Coffee('Regular', 5)
big = Coffee('Big', 6)
 
try:
   user_budget = float(input('What is your budget? '))
except ValueError:
   exit('Please enter a number')
  
for coffee in [big, regular, small]:
   coffee.sell(user_budget)