from Classes import Hotel,Room
from Menu import main_menu, book_room_menu, release_room_menu, view_availability_menu

def main():
    hotel = Hotel()

    while True:
        choice = main_menu()
        if choice == '1':
            book_room_menu(hotel)
        elif choice == '2':
            release_room_menu(hotel)
        elif choice == '3':
            view_availability_menu(hotel)
        elif choice == '4':
            print("Exiting the Hotel Reservation System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()