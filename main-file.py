budget = { 'food': 0.0,
          'drinks': 0.0
}

def print_all():
    print(f"Total Budget: {budget}")
    print("Expenses:")
    for key, value in budget.items():
        print(f"{key}=={value}")

def add_expense():
    e1 = input("Enter the expense details (food, drinks etc.): ")
    a1 = float(input("Enter the amount: "))
    for e1 in budget.keys():
        print("Updating budget")
        a1 += budget[e1]
        budget.update({e1:a1})
        print_all()
    else:
        budget.update({e1:a1})
        print_all()

def remove_expense():
    r_1 = input("Enter the expense that need to be removed: ")
    if r_1 in budget.keys():
        budget.pop(r_1)
        print_all()
    else:
        print("The expense is not in the list")


def main():
    print("Let's start the party tonight")
    initial_budget = float(input("What is your budget: "))
    # filepath = 'budget_data.json'  # Define the path to your JSON file
    # initial_budget, expenses = load_budget_data(filepath)
    budget = initial_budget
    expenses = []

    while True:
        print("\n Let's the expense begin")
        print("1. Add an expense")
        print("2. Delete an expense")
        print("3. Budget review")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            remove_expense()
        elif choice == "3":
           print_all()
        elif choice == "4":
            print("Enjoy the party!")
            break
        else:
            print("Choose a valid option.")

if __name__ == "__main__":
    main()