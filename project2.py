import matplotlib.pyplot as plt


def get_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def create_bar_chart(user_name, user_data):
    categories = list(user_data.keys())
    expenses = list(user_data.values())

    plt.figure(figsize=(8, 6))
    plt.bar(categories, expenses)
    plt.xlabel('Expense Categories')
    plt.ylabel('Amount')
    plt.title(f'Expense Breakdown for {user_name}')
    plt.show()


def main():
    num_users = int(input("Enter the number of users: "))

    users_data = {}
    for i in range(num_users):
        user_name = input(f"\nEnter name for user {i + 1}: ")

        # Get user input for salary and expenses
        salary = get_user_input(f"Enter salary for user {user_name}: ")
        rent = get_user_input(f"Enter rent expense for user {user_name}: ")
        groceries = get_user_input(f"Enter groceries expense for user {user_name}: ")
        utilities = get_user_input(f"Enter utilities expense for user {user_name}: ")
        other_expenses = get_user_input(f"Enter other expenses for user {user_name}: ")

        # Calculate total expenses
        total_expenses = rent + groceries + utilities + other_expenses

        # Calculate savings
        savings = salary - total_expenses

        # Store user's financial data in the dictionary
        users_data[user_name] = {
            'Salary': salary,
            'Rent': rent,
            'Groceries': groceries,
            'Utilities': utilities,
            'Other\nExpenses': other_expenses,
            'Total Expenses': total_expenses,
            'Savings': savings
        }

    # Display data for all users
    print("\nFinancial data for all users:")
    for user, data in users_data.items():
        print(f"\nUser: {user}")
        for key, value in data.items():
            print(f"{key}: {value}")

    # Create pie charts for each user's expense breakdown
    for user, data in users_data.items():
        create_bar_chart(user, data)

    # Create a bar graph to compare users' total expenses
    users_list = list(users_data.keys())
    expenses_list = [users_data[user]['Total Expenses'] for user in users_list]

    plt.figure(figsize=(10, 6))
    plt.bar(users_list, expenses_list)
    plt.xlabel('Users')
    plt.ylabel('Total Expenses')
    plt.title('Comparison of Users\' Total Expenses')
    plt.show()

    # Display savings for each user
    plt.figure(figsize=(10, 6))
    savings_list = [users_data[user]['Savings'] for user in users_list]
    plt.bar(users_list, savings_list, color='green')
    plt.xlabel('Users')
    plt.ylabel('Savings')
    plt.title('Savings of Users')
    plt.show()


if __name__ == "__main__":
    main()
