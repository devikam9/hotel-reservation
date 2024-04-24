import datetime
from Hotel import Hotel, RoomType, Room, ROOM_TYPES

def book_room_menu(hotel):
    print("\n--- Book a Room ---")
    print("Select from the available Room Types:")
    for room_type in ROOM_TYPES:
        print(f"{room_type.name} - {room_type.features}")

    room_type_input = input("Enter the room type: ").lower()

    valid_room_types = [rt.name.lower() for rt in ROOM_TYPES]

    if room_type_input in valid_room_types:
        room_type = [rt.name.lower() for rt in ROOM_TYPES if rt.name.lower() == room_type_input][0]
    else:
        print("Invalid room type selection.")
        return

    check_in_date_str = input("Enter the check-in date (YYYY-MM-DD): ")
    check_out_date_str = input("Enter the check-out date (YYYY-MM-DD): ")

    try:
        check_in_date = datetime.datetime.strptime(check_in_date_str, "%Y-%m-%d").date()
        check_out_date = datetime.datetime.strptime(check_out_date_str, "%Y-%m-%d").date()
        hotel.book_room(room_type, check_in_date, check_out_date)
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")


def release_room_menu(hotel):
    print("\n--- Release a Room ---")
    room_type = input("Enter the room type: ").lower()

    if room_type not in [rt.name.lower() for rt in ROOM_TYPES]:
        print("Invalid room type. Please enter a valid room type.")
        return

    check_in_date_str = input("Enter the check-in date (YYYY-MM-DD): ")
    check_out_date_str = input("Enter the check-out date (YYYY-MM-DD): ")

    try:
        check_in_date = datetime.datetime.strptime(check_in_date_str, "%Y-%m-%d").date()
        check_out_date = datetime.datetime.strptime(check_out_date_str, "%Y-%m-%d").date()
        hotel.release_room(room_type, check_in_date, check_out_date)
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")

def main_menu(hotel):
    while True:
        print("\n--- ***---- @@ Welcome to the KED Hotel Reservation System @@----*** ---")
        print("1. Display Room Types")
        print("2. Display Room Details")
        print("3. Book a Room")
        print("4. Release a Room")
        print("5. View Room Availability")
        print("6. View Reservations")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            hotel.display_room_types()
        elif choice == '2':
            hotel.display_room_details()
        elif choice == '3':
            book_room_menu(hotel)
        elif choice == '4':
            release_room_menu(hotel)
        elif choice == '5':
            hotel.display_availability()
        elif choice == '6':
            hotel.display_reservations()
        elif choice == '7':
            print("Thanks for choosing the KED Hotel. \nExiting the KED Hotel Reservation System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    hotel = Hotel()
    main_menu(hotel)

if __name__ == "__main__":
    main()