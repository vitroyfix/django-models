from .models import Author, Book, Library, Librarian

# ------------------ Sample Queries ------------------

def get_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []


def get_books_in_library(library_name):
    """List all books in a library."""
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []


def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # OneToOne relationship
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# ------------------ Demo Run ------------------
if __name__ == "__main__":
    # Example usage (works when running inside Django shell with proper setup):
    print("Books by Author John Doe:", get_books_by_author("John Doe"))
    print("Books in Central Library:", get_books_in_library("Central Library"))
    print("Librarian for Central Library:", get_librarian_for_library("Central Library"))
