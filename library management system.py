import datetime

# Dictionary to store books
library = {
    "Python Basics": {"available": True},
    "Data Structures": {"available": True},
    "Algorithms": {"available": True}
}

# Dictionary to store issued books
issued_books = {}


# 📖 Display all books
def display_books():
    print("\n📚 Available Books:")
    for book, info in library.items():
        status = "Available" if info["available"] else "Issued"
        print(f"- {book} [{status}]")


# 📥 Issue Book
def issue_book():
    book_name = input("\nEnter book name to issue: ")

    if book_name in library and library[book_name]["available"]:
        student = input("Enter student name: ")
        days = int(input("Enter number of days to issue: "))

        issue_date = datetime.date.today()

        issued_books[book_name] = {
            "student": student,
            "issue_date": issue_date,
            "days": days
        }

        library[book_name]["available"] = False

        print(f"\n✅ Book issued successfully to {student}")
        print(f"Issue Date: {issue_date}")
        print(f"Return within {days} days")

        print("\n⚠️ Fine Policy:")
        print("1st week: ₹10/day")
        print("2nd week: ₹20/day")
        print("3rd week: ₹60/day (increasing pattern)")

    else:
        print("❌ Book not available!")


# 💰 Fine Calculation
def calculate_fine(days_late):
    fine = 0
    rate = 10

    for week in range(1, (days_late // 7) + 2):
        fine += rate * week * min(7, days_late)
        days_late -= 7
        if days_late <= 0:
            break

    return fine


# 📤 Return Book
def return_book():
    book_name = input("\nEnter book name to return: ")

    if book_name in issued_books:
        return_date = datetime.date.today()
        record = issued_books[book_name]

        allowed_days = record["days"]
        issue_date = record["issue_date"]

        days_used = (return_date - issue_date).days

        print(f"\n📅 Days used: {days_used}")

        if days_used > allowed_days:
            late_days = days_used - allowed_days
            fine = calculate_fine(late_days)

            print(f"⚠️ Late by {late_days} days")
            print(f"💰 Fine to pay: ₹{fine}")
        else:
            print("✅ Returned on time. No fine!")

        # Update records
        library[book_name]["available"] = True
        del issued_books[book_name]

    else:
        print("❌ This book was not issued!")


# 📜 Menu
def menu():
    while True:
        print("\n====== 📚 LIBRARY MENU ======")
        print("1. View Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_books()
        elif choice == '2':
            issue_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            print("👋 Thank you for using the library system!")
            break
        else:
            print("❌ Invalid choice. Try again.")


# Run program
if __name__ == "__main__":
    menu()