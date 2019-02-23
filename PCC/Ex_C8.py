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

# 8.3 T-Shirt / 8.4 Large Shirts
size = input('Enter the size of your shirt:\t'); text = input('Which will be the message on your shirt?\t')
def make_shirt(size='large',text='I love Python'):
    print("A " + size + " shirt, with the message " + text + " will be made.")
# Default Output
make_shirt()
# User Input, Positional Call
make_shirt(size,text)
# Keyword Call
make_shirt(text='Test Shirt',size='medium',)

# 8.5 Cities
def describe_cities(city='Oaxaca',country='Mexico'):
    print(city.title() + " is in " + country.title()) # 8.6 City Names print(city.title()+", "+country.title())
for i in list(range(3)): city=input('Enter city:\t'); country=input('Enter a country:\t'); describe_cities(city,country)

# 8.7 Album / 8.8 User Albums
def make_album(artist_name='Artist',album_title='Title',track_number=''):
    artist_name = input("Enter an Artist Name:\t")
    album_title = input("Enter an Album Name:\t")
    track_number = input("Enter the track number:\t")
    album = {'ar_name': artist_name, 'al_name': album_title}
    if track_number:
        album['t_number'] = track_number
    return album
while True:
    print(make_album())
    another_album = input("Do you want to enter another album? (y/n)\t").strip().lower()
    if another_album == 'n':
        break