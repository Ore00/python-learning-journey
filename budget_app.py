class Category:

    def __init__(self, category):
        self.ledger = []
        self.category = category

    def __str__(self):
        #Create a title for ledger printing sent length to 30 character
        title_max_length = 30
        title_placeholder = "*"
        title = self.category.center(title_max_length).replace(
            ' ', title_placeholder)

        #Format the entries in ledger for printing
        balance = 0
        entries = ''
        description_max_length = 23
        amount_max_length = 7
        for entry in self.ledger:
            balance += entry['amount']
            desc = entry['description'][:description_max_length]
            amt = f"{entry['amount']:.2f}"
            entry_str = desc.ljust(description_max_length) + amt.rjust(
                amount_max_length) + '\n'
            entries += ''.join(entry_str)
        balance = f"Total: {balance:.2f}"
        entries += ''.join(balance)

        return title + "\n" + entries

    #Determine if a budget category has sufficient funds: False if not
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    #Deposit funds within a budget category
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    #Determine the balance of a budget category from it's beginning
    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry['amount']
        return balance

    #Determine how much has been spent within a budget's category
    def get_total_debits(self):
        debits = 0
        for entry in self.ledger:
            if entry['amount'] < 0:
                debits += entry['amount']

        return debits

    #Remove funds from a budget category
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -1 * amount,
                'description': description
            })
            return True
        return False

    #Move funds from one category to another
    def transfer(self, amount, to_category):
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to ' + to_category.category)
            to_category.deposit(amount, 'Transfer from ' + self.category)

            return True
        return False


def create_spend_chart(categories):
    title = "Percentage spent by category"
    chart = ""
    total_spent = 0
    y_axis = range(100, -1, -10)
    x_axis = []
    x_len = len(categories) * 3 + 1
    x_divide = "".rjust(4) + "".rjust(x_len, "-") + "\n"
    x_tab = "".rjust(4)
    x_title_len = 0

    #Determine the total spent in each category
    for ledger in categories:
        x_axis.append(ledger.get_total_debits())

        if len(ledger.category) > x_title_len:
            x_title_len = len(ledger.category)

    total_spent = round(abs(sum(x_axis)), 2)
    total_percent = lambda a: round((abs(a) / total_spent), 2) * 100

    #Determine y axis, along with percentage sent for each category
    for y in y_axis:
        chart += str(y).rjust(3) + "| "

        for x in x_axis:
            if total_percent(x) >= y:
                chart += 'o  '
            else:
                chart += ' '.rjust(3)

        chart += "\n"
    chart += x_divide
    chart += x_tab
    count = 0

    #Determine x axis - category label placement on
    while count < x_title_len:
        for items in categories:
            if items.category[count:count + 1]:
                chart += items.category[count:count + 1].center(3)
            else:
                chart += " ".center(3)

        if count != x_title_len - 1:
            chart += " \n"
            chart += x_tab
        else:
            chart += " "
        count += 1

    return title + "\n" + chart


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(15, 'sweater')

print(food, "\n")
list = [food, clothing]
create_spend_chart(list)
