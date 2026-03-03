
# library ={
#     "Python": {"author": "John", "status": "available"},
#     "Data Structure": {"author": "Smith", "status": "issued"}
# }

# while True:
#     print("\nLibrary Management System Menu:")
#     print("1. Add a book")
#     print("2. View all books")
#     print("3. Issue a book")
#     print("4. Return a book")
#     # print("3. Update book status")
#     print("5. Delete a book")
#     print("6. Search a book")
#     print("7. Exit")

#     choice = input("Enter your choice (1-7): ")

#     # 1. Add a book
#     if choice == '1':
#         title = input("Enter book title: ")
#         author = input("Enter author name: ")
#         if title in library:
#             print(f"Error: '{title}' already exists in the library.")
#         else:
#             library[title] = {"author": author, "status": "available"}
#             print(f"Book '{title}' added successfully.")

#     # 2. View all books
#     elif choice == '2':
#         if not library: # check kre library empty chhe ke nai
#             print("The library is currently empty.")
#         else:
#             #sarkhu formatting mate table format ma
#             print("Current books in the library:")
#             print("{:<25} {:<20} {:<15}".format("Title", "Author", "Status"))
#             print("-" * 60)
#             for title, details in library.items():
#                 # < = specify left alignment
#                 # : = separates field name
#                 # 25,20,20 = number specify minimum width of table
#                 #   25 character sudhi ni left side space reserved
#                 print("{:<25} {:<20} {:<15}".format(title, details["author"], details["status"]))

#             # else:
#             # simple format ma
#             # print("Current books in the library:")
#             # print("Title", "Author", "Status")
#             # print("-" * 60)
#             # for title, details in library.items():
#             #     print(title, details["author"], details["status"])
        
#     # 3. Update book status
#     # elif choice == '3':
#     #     title = input("Enter the title of the book to update: ")
#     #     if title in library:
#     #         new_status = input("Enter new status (e.g., available, issued): ")
#     #         library[title]["status"] = new_status
#     #         print(f"Status for '{title}' updated to '{new_status}'.")
#     #     else:
#     #         print(f"Error: Book '{title}' not found.")


#      # 3. Issue a book
#     elif choice == '3':
#         title = input("Enter book title to issue: ")
#         if title in library:
#             if library[title]["status"] == "available":
#                 library[title]["status"] = "issued"
#                 print(f"Book '{title}' has been issued.")
#             else:
#                 print(f"Book '{title}' is already issued.")
#         else:
#             print(f"Book '{title}' not found.")

#     # 4. Return a book
#     elif choice == '4':
#         title = input("Enter book title to return: ")
#         if title in library:
#             if library[title]["status"] == "issued":
#                 library[title]["status"] = "available"
#                 print(f"Book '{title}' has been returned.")
#             else:
#                 print(f"Book '{title}' was not issued.")
#         else:
#             print(f"Book '{title}' not found.")


#     # 5. Delete 
#     elif choice == '5':
#         title = input("Enter the title of the book to delete: ")
#         if title in library:
#             del library[title]
#             print(f"Book '{title}' deleted successfully.")
#         else:
#             print(f"Error: Book '{title}' not found.")


#     # 6. Search
#     elif choice == '6':
#         search_term = input("Enter search term (title or author): ").strip()
        
#         search_term_lower = search_term.lower()
#         results = []
        
#         for title, details in library.items():
#             book_title = title.lower()
#             book_author = details["author"].lower()
            
#             title_found = book_title.find(search_term_lower) != -1
#             author_found = book_author.find(search_term_lower) != -1
            
#             if title_found or author_found:
#                 results.append((title, details))
#         # Display
#         if results:
#             print(f"\nFound {len(results)} matching book(s):")
#             for title, details in results:
#                 print(f"{title} - {details['author']} - {details['status']}")
#         else:
#             print(f"No books found matching '{search_term}'")


#     # 7. Exit 
#     elif choice == '7':
#         print("Exiting Library Management System. Goodbye!")
#         break







# Login

    users = {
    "admin1": {"password": "admin123", "role": "admin1"},
    "user1": {"password": "user123", "role": "user1"}
}

library = {
    "Python": {"author": "John", "status": "available"},
    "Data Structure": {"author": "Smith", "status": "issued"}
}

print("===== LOGIN =====")
user_id = input("Enter ID: ").strip().lower()
password = input("Enter Password: ").strip()

if user_id in users and users[user_id]["password"] == password:
    role = users[user_id]["role"]
    print("Login Successful!")
    print("Your Role:", role)
else:
    print("Invalid ID or Password!")
    exit()

while True:

    print("\n===== MENU =====")

    if role == "admin":

        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Delete Book")
        print("6. Search Book")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library[title] = {"author": author, "status": "available"}
            print("Book Added Successfully!")

        elif choice == '2':
            for t, d in library.items():
                print(f"{t} - {d['author']} - {d['status']}")

        elif choice == '3':
            title = input("Enter book to issue: ")
            if title in library and library[title]["status"] == "available":
                library[title]["status"] = "issued"
                print("Book Issued!")
            else:
                print("Book Not Available!")

        elif choice == '4':
            title = input("Enter book to return: ")
            if title in library and library[title]["status"] == "issued":
                library[title]["status"] = "available"
                print("Book Returned!")
            else:
                print("Invalid Book!")

        elif choice == '5':
            title = input("Enter book to delete: ")
            if title in library:
                del library[title]
                print("Book Deleted!")

        elif choice == '6':
            search = input("Search title/author: ").lower()
            for t, d in library.items():
                if search in t.lower() or search in d["author"].lower():
                    print(f"{t} - {d['author']} - {d['status']}")

        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid Choice!")

    # ---------------- USER MENU ----------------
    else:

        print("1. View Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            for t, d in library.items():
                print(f"{t} - {d['author']} - {d['status']}")

        elif choice == '2':
            title = input("Enter book to issue: ")
            if title in library and library[title]["status"] == "available":
                library[title]["status"] = "issued"
                print("Book Issued!")
            else:
                print("Not Available!")

        elif choice == '3':
            title = input("Enter book to return: ")
            if title in library and library[title]["status"] == "issued":
                library[title]["status"] = "available"
                print("Book Returned!")
            else:
                print("Invalid Book!")

        elif choice == '4':
            search = input("Search title/author: ").lower()
            for t, d in library.items():
                if search in t.lower() or search in d["author"].lower():
                    print(f"{t} - {d['author']} - {d['status']}")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid Choice!")
    # -------- USERS DATABASE --------
users = {}

# -------- REGISTER --------
print("===== REGISTER =====")
new_id = input("Create ID: ").strip().lower()

if new_id in users:
    print("User already exists!")
else:
    new_pass = input("Create Password: ").strip()
    role = input("Enter Role (admin/user): ").strip().lower()

    if role not in ["admin", "user"]:
        print("Invalid role! Default set to user.")
        role = "user"

    users[new_id] = {"password": new_pass, "role": role}
    print("Registration Successful!")

# -------- LOGIN --------
print("\n===== LOGIN =====")
user_id = input("Enter ID: ").strip().lower()
password = input("Enter Password: ").strip()

if user_id in users and users[user_id]["password"] == password:
    role = users[user_id]["role"]
    print("Login Successful!")
    print("Your Role:", role)
else:
    print("Invalid ID or Password!")
    exit()

# -------- SAMPLE LIBRARY --------
library = {
    "Python": {"author": "John", "status": "available"},
    "Data Structure": {"author": "Smith", "status": "issued"}
}

# -------- MENU --------
while True:

    print("\n===== MENU =====")

    if role == "admin":

        print("1. Add Book")
        print("2. View Books")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library[title] = {"author": author, "status": "available"}
            print("Book Added Successfully!")

        elif choice == '2':
            for t, d in library.items():
                print(f"{t} - {d['author']} - {d['status']}")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid Choice!")

    else:

        print("1. View Books")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            for t, d in library.items():
                print(f"{t} - {d['author']} - {d['status']}")

        elif choice == '2':
            print("Goodbye!")
            break

        else:
            print("Invalid Choice!")


    
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
