import csv

def average_grade(grades):
    total = len(grades)
    grade_sum = 0
    for grade in grades:
        grade_sum += int(grade)
    return grade_sum / total

student_grades = {}
# Open the CSV file in read mode ('r')
with open('../files/students.csv', 'r', newline='') as file:
    # Create a csv.reader object
    reader = csv.reader(file)
    # Optionally, skip the header row if present
    header = next(reader)
    print(f"Header: {header}")
    # Iterate over each row in the CSV file
    for row in reader:
        student_grades[row[0]] = average_grade(row[1:])
print(student_grades)

def address_book():
    contacts = {}

    while True:
        print("\n--- Address Book ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()

            if name and phone:
                contacts[name] = phone
                print(f"Contact '{name}' added successfully!")
            else:
                print("Name and phone number cannot be empty.")

        elif choice == "2":
            name = input("Enter name to search: ").strip()
            if name in contacts:
                print(f"{name}: {contacts[name]}")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == "3":
            print("Exiting address book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the address book function
address_book()