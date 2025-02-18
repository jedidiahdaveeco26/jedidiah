class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        """Displays the book details."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print()

# Creating three book objects
book1 = Book("Noli mi tangre", "Jose P. Rizal", 1887)
book2 = Book("The Reign of Greed", "Jose P. Rizal", 1891)
book3 = Book("The Poems of Jose Rizal", "Jose P. Rizal", 1961)

# Displaying book details
book1.describe()
book2.describe()
book3.describe()