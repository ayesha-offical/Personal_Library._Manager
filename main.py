import json


class BookColection: # class is blue print to creat object jis kunder data or methods hote hian  "class is basically printer" 
    """A class to manage a collection of books, allowing users to store and organize their reading materials."""  

# __init__ is constructer jo k aik specific function ko ch;ane ka km anjam de rahe hote hian
    def __init__(self): # self keyword is used to access variables that belongs to the class it is used to create new objects (data ko manage krne ka km kr rha hai)
        """Initialize a new book collection with an empty list and set up file storage."""
        self.books_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()
    def read_from_file(self) : # method whihc return nothing
        """Load saved books from a JSON file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:  # with k keyword ka istimal for the resource managemnt
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError): # FileNotFoundError, json.JSONDecodeError they both are builtin class
            self.book_list = []       # variable which hold the empty list 
    def save_to_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4) # dump mere data ko json format mien phenk rha means save kr krha  # identation (ident) is use for space (4 finger space)
    def create_new_book(self):
            """Add a new book to the collection by gathering information from the user."""
            book_title = input("Enter the title of the book: ")
            book_author = input("Enter the author of the book: ")
            publication_year = input("Enter the publication year: ")
            book_genre = input("Enter the genre of the book: ")
            is_book_read =( # boolean one
                    input("Have you read this book? (Yes/no): ").strip().lower() == "yes"  # .stripe method is used to remove spaces .lower() value ko lower case mien convert krha (both are builtin string method )
            )

            new_book ={ # dictionary is use to store data in key value pair
                    "title":book_title,
                    "author": book_author,
                    "publication_year": publication_year,
                    "genre": book_genre,
                    "is_read": is_book_read,
            }

            self.books_list.append(new_book)  
            self.save_to_file()
            print("Book added successfully!\n")
    def delete_book(self):
            """Delete a book from the collection by its title."""
            book_title = input("Enter the title of the book to remove: ")

            for book in self.books_list:
                    if book["title"] == book_title.lower():
                            self.books_list.remove(book)
                            self.save_to_file()
                            print("Book '{book_title}' removed successfully!\n")
                            return    
            print("Book not found!\n")       
    def find_book(self):
                    """Search for books in the collection by title or author name."""
                    search_type = input("Search by:\n1.Title\n2.author\nEnter Your Choice: ")
                    search_text = input("Enter search term: ").lower()
                    found_books = [
                            book
                            for book in self.books_list
                            if search_text in book["title"].lower()
                            or search_text in book["author"].lower()
                    ]

                    if found_books:
                            print("Found Books: ")
                            for index, book in enumerate(found_books, 1):
                                reading_status  = "Read" if book ["read"] else "Unread"
                                print(
                                        f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
                                )    
                    else:
                                print("No matching books found.\n")
    def update_book(self): 
            """Modify the details of an existing book in the collection."""
            book_title = input("Enter the title of the book to update: ")
            for book in self.book_list:
                   if book["title"].lower() == book_title.lower():
                       print("Leave blank to keep existing value.")
                       book["title"] = input(f"New title ({book['title']}): ")  or book['title']
                       book["author"]  =(
                              input(f"New author ({book['author']}): ") or book['author']
                       )   
                       book["year"] = input(f"New Year ({book['year']}): ") or book['year']
                       book["genre"] = input(f"New genre ({book['genre']}): ") or book['genre']
                       book["read"] = (
                              input("Have y ou read this book? (Yes or no): ").strip().lower()
                              == "yes" 
                       )      
                       self.save_to_file()
                       print("Book updated successfully!\n")
                       return
                   print("Book not found!\n")                       
    def show_all_books(self):    
        """Display all books in the collection with their details."""
        if not self.books_list:
            print("Your Collection is empty.\n")
            return
        
        print("Your Book Collection:")
        for index, book in enumerate(self.books_list, 1):
            reading_status = "Read" if book["is_read"] else "Unread"  # Changed from "read" to "is_read"
            print(
                f"{index}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {reading_status}"
            )

        print()                               
    def show_reading_progress(self):
           """Display the percentage of books read in the collection."""
           total_books =len(self.book_list)        
           completed_books = sum(1 for book in self.book_list if book["read"])  
           completion_rate = (
                completed_books / total_books * 100 if total_books > 0 else 0 
           )   
           print(f"Total books in collection: {total_books}")
           print(f"Reading Progress: {completion_rate: .2f}% \n")
    def start_application(self):
           """Start the application by displaying the main menu and handling user input."""        
           while True:
                  print("📚 Welcome to Your Book Collection Manager! 📚")
                  print("1. Add a new book")
                  print("2. Remove a book")
                  print("3. Search for books")
                  print("4. Update book details")
                  print("5. View all books")
                  print("6. View reading progress")
                  print("7. Exit")
                  user_choice = input("Please choose an option (1-7): ")

                  if user_choice == "1":
                         self.create_new_book()
                  elif user_choice == "2":
                         self.delete_book()
                  elif user_choice == "3":
                         self.find_book()
                  elif user_choice == "4":         
                         self.update_book()
                  elif user_choice == "5":
                         self.show_all_books()            
                  elif user_choice == "6":
                         self.show_reading_progress()
                  elif user_choice == "7":
                         self.save_to_file()
                         print("Thank you ✨ for using Book Collection Manager. Goodbye👋!")
                         break
                  else:
                         print("Invalid choice. Please try again.\n")
if __name__ == "__main__":
       book_manager = BookColection()
       book_manager.start_application()


