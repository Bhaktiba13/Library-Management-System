
library ={
    "Python Basics": {"author": "John Doe", "status": "available"},
    "Data Science": {"author": "Jane Smith", "status": "issued"}
}

while True:
    print("\nLibrary Management System Menu:")
    print("1. Add a book")
    print("2. View all books")
    print("3. Update book status")
    print("4. Delete a book")
    print("5. Search a book")
    print("6. Exit")

    choice = input("Enter your choice (1-5): ")

    # 1. Add a book
    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        if title in library:
            print(f"Error: '{title}' already exists in the library.")
        else:
            library[title] = {"author": author, "status": "available"}
            print(f"Book '{title}' added successfully.")

    # 2. View all books
    elif choice == '2':
        if not library: # check kre library empty chhe ke nai
            print("The library is currently empty.")
        else:
            #sarkhu formatting mate table format ma
            print("Current books in the library:")
            print("{:<25} {:<20} {:<15}".format("Title", "Author", "Status"))
            print("-" * 60)
            for title, details in library.items():
                # < = specify left alignment
                # : = separates field name
                # 25,20,20 = number specify minimum width of table
                #   25 character sudhi ni left side space reserved
                print("{:<25} {:<20} {:<15}".format(title, details["author"], details["status"]))

            # else:
            # simple format ma
            # print("Current books in the library:")
            # print("Title", "Author", "Status")
            # print("-" * 60)
            # for title, details in library.items():
            #     print(title, details["author"], details["status"])
        
    # 3. Update book status
    elif choice == '3':
        title = input("Enter the title of the book to update: ")
        if title in library:
            new_status = input("Enter new status (e.g., available, issued): ")
            library[title]["status"] = new_status
            print(f"Status for '{title}' updated to '{new_status}'.")
        else:
            print(f"Error: Book '{title}' not found.")

    # 4. Delete 
    elif choice == '4':
        title = input("Enter the title of the book to delete: ")
        if title in library:
            del library[title]
            print(f"Book '{title}' deleted successfully.")
        else:
            print(f"Error: Book '{title}' not found.")


    # 5. Search
    elif choice == '5':
        search_term = input("Enter search term (title or author): ").strip()
        
        search_term_lower = search_term.lower()
        results = []
        
        for title, details in library.items():
            book_title = title.lower()
            book_author = details["author"].lower()
            
            title_found = book_title.find(search_term_lower) != -1
            author_found = book_author.find(search_term_lower) != -1
            
            if title_found or author_found:
                results.append((title, details))
        # Display
        if results:
            print(f"\nFound {len(results)} matching book(s):")
            for title, details in results:
                print(f"{title} - {details['author']} - {details['status']}")
        else:
            print(f"No books found matching '{search_term}'")


    # 6. Exit 
    elif choice == '6':
        print("Exiting Library Management System. Goodbye!")
        break
    
    
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
