# VDLS - 12/26/18 - Excercises Chapter 8 Python Crash Course.
# 8.1 Message
def display_message():
    print("I'm learning functions in this chapter!")

display_message()

# 8.2 Favorite book.
def favorite_book(title):
    print("One of my favorite books is " + title + "!" )

title = input("Please enter the name of your favorite book:\t")
favorite_book(title)