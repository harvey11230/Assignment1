class Book:
    def __init__(self, author="", title=""):
        self.author = author
        self.title = title

def display(bookname):
    print(bookname.title + " written by " + bookname.author)

if __name__ == '__main__':
    a = Book("John Steinbeck", "Of Mice and Men")
    b = Book("Harper Lee", "Kill a Mockingbird")

display(a)
display(b)