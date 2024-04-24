import datetime
def main_menu():
    print("\n--- Welcome to the KED Hotel Reservation System ---")
    print("1. Book a Room")
    print("2. Release a Room")
    print("3. View Room Availability")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    return choice

def book_room_menu(hotel):
    print("\n--- Book a Room ---")
    room_type = input("Choose the room type: \n standard \n deluxe \n penthouse \n family_suite \n honeymoon_suite \n double \n single \n penthouse_suite \n presidential_suite \n studio_apartment \n accessible \n bungalow \n cottage \n villa \n chalet \n loft \n condo \n treehouse \n beach_house \n log_cabin \n boat_house \n tent \n yurt \n igloo \n caravan \n tipi \n castle_suite \n underwater_room \n space_station \n Enter the room type: ").lower()

    valid_room_types = ['standard', 'deluxe', 'penthouse', 'family_suite', 'honeymoon_suite', 'double', 'single', 'penthouse_suite', 'presidential_suite', 'studio_apartment', 'accessible', 'bungalow', 'cottage', 'villa', 'chalet', 'loft', 'condo', 'treehouse', 'beach_house', 'log_cabin', 'boat_house', 'tent', 'yurt', 'igloo', 'caravan', 'tipi', 'castle_suite', 'underwater_room', 'space_station']

    if room_type not in valid_room_types:
        print("Invalid room type. Please choose from the available room types.")
        return

    check_in_date_str = input("Enter the check-in date (YYYY-MM-DD): ")
    check_out_date_str = input("Enter the check-out date (YYYY-MM-DD): ")

    try:
        check_in_date = datetime.datetime.strptime(check_in_date_str, "%Y-%m-%d").date()
        check_out_date = datetime.datetime.strptime(check_out_date_str, "%Y-%m-%d").date()
        hotel.book_room(room_type, check_in_date, check_out_date)
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")
    # hotel.book_room(room_type, check_in_date, check_out_date)

def release_room_menu(hotel):
    print("\n--- Release a Room ---")
    room_type = input("Choose the room type: \n standard \n deluxe \n penthouse \n family_suite \n honeymoon_suite \n double \n single \n penthouse_suite \n presidential_suite \n studio_apartment \n accessible \n bungalow \n cottage \n villa \n chalet \n loft \n condo \n treehouse \n beach_house \n log_cabin \n boat_house \n tent \n yurt \n igloo \n caravan \n tipi \n castle_suite \n underwater_room \n space_station: \n Enter the room type: ").lower()

    valid_room_types = ['standard', 'deluxe', 'penthouse', 'family_suite', 'honeymoon_suite', 'double', 'single', 'penthouse_suite', 'presidential_suite', 'studio_apartment', 'accessible', 'bungalow', 'cottage', 'villa', 'chalet', 'loft', 'condo', 'treehouse', 'beach_house', 'log_cabin', 'boat_house', 'tent', 'yurt', 'igloo', 'caravan', 'tipi', 'castle_suite', 'underwater_room', 'space_station']

    if room_type not in valid_room_types:
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



def view_availability_menu(hotel):
    print("\n--- View Room Availability ---")
    for room_type, rooms in hotel.rooms.items():
        available_rooms = [room for room in rooms if room.is_available]
        print(f"{room_type.capitalize()} rooms available: {len(available_rooms)}")


