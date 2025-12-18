#csv - simple file storage, beginner friendly
import csv

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, etc): ")
    amount = input("Enter amount: ")
    
    #with open() - opens file safely and closes it automatically

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense added successfully!")

def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            total = 0
            print("\nDate | Category | Amount")
            print("-------------------------")
            for row in reader:
                print(row[0], "|", row[1], "|", row[2])
                total += int(row[2])
            print("-------------------------")
            print("Total Expense:", total)
    except FileNotFoundError:
        print("No expenses found.")

#keeps program running until user exits
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")



        
