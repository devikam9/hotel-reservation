import datetime

class Room:
    def __init__(self, room_type, rate):
        self.room_type = room_type
        self.rate = rate
        self.is_available = True
        self.check_in_date = None
        self.check_out_date = None

    def book(self, check_in_date, check_out_date):
        if self.is_available:
            self.check_in_date = check_in_date
            self.check_out_date = check_out_date
            self.is_available = False
            return True
        else:
            return False

    def release(self):
        self.check_in_date = None
        self.check_out_date = None
        self.is_available = True

    def calculate_cost(self, check_in_date, check_out_date):
        nights = (check_out_date - check_in_date).days
        return nights * self.rate

class Hotel:
    def __init__(self):
        self.rooms = {
            'single': [Room('Single', 80) for _ in range(5)],
            'double': [Room('Double', 120) for _ in range(10)],
            'suite': [Room('Suite', 200) for _ in range(3)],
            'penthouse_suite': [Room('Penthouse Suite', 400) for _ in range(1)],
            'standard': [Room('Standard', 100) for _ in range(10)],
            'deluxe': [Room('Deluxe', 150) for _ in range(5)],
            'family_suite': [Room('Family Suite', 250) for _ in range(2)],
            'executive_suite': [Room('Executive Suite', 300) for _ in range(2)],
            'honeymoon_suite': [Room('Honeymoon Suite', 350) for _ in range(1)],
            'presidential_suite': [Room('Presidential Suite', 500) for _ in range(1)],
            'studio_apartment': [Room('Studio Apartment', 120) for _ in range(5)],
            'accessible': [Room('Accessible', 120) for _ in range(3)],
            'bungalow': [Room('Bungalow', 180) for _ in range(2)],
            'cottage': [Room('Cottage', 150) for _ in range(3)],
            'villa': [Room('Villa', 300) for _ in range(2)],
            'chalet': [Room('Chalet', 220) for _ in range(2)],
            'loft': [Room('Loft', 180) for _ in range(3)],
            'condo': [Room('Condo', 200) for _ in range(3)],
            'treehouse': [Room('Treehouse', 250) for _ in range(1)],
            'beach_house': [Room('Beach House', 300) for _ in range(1)],
            'log_cabin': [Room('Log Cabin', 180) for _ in range(2)],
            'boat_house': [Room('Boat House', 250) for _ in range(1)],
            'tent': [Room('Tent', 50) for _ in range(5)],
            'yurt': [Room('Yurt', 120) for _ in range(2)],
            'igloo': [Room('Igloo', 80) for _ in range(1)],
            'caravan': [Room('Caravan', 100) for _ in range(2)],
            'tipi': [Room('Tipi', 90) for _ in range(2)],
            'castle_suite': [Room('Castle Suite', 400) for _ in range(1)],
            'underwater_room': [Room('Underwater Room', 350) for _ in range(1)],
            'space_station': [Room('Space Station', 500) for _ in range(1)]
        }

    def book_room(self, room_type, check_in_date, check_out_date):
        available_rooms = [room for room in self.rooms[room_type] if room.is_available]
        if available_rooms:
            room = available_rooms[0]
            if room.book(check_in_date, check_out_date):
                print(f"Room {room.room_type} booked for {check_in_date} to {check_out_date}.")
                print(f"Total cost: ${room.calculate_cost(check_in_date, check_out_date)}")
            else:
                print("Room is not available for the specified dates.")
        else:
            print(f"No {room_type} rooms available for the specified dates.")

    def release_room(self, room_type, check_in_date, check_out_date):
        for room in self.rooms[room_type]:
            if room.check_in_date == check_in_date and room.check_out_date == check_out_date:
                room.release()
                print(f"Room {room.room_type} released for {check_in_date} to {check_out_date}.")
                return
        print("No room found for the specified dates.")
# Book a standard room
# check_in_date = datetime.date(2023, 5, 1)
# check_out_date = datetime.date(2023, 5, 5)
# hotel.book_room('standard', check_in_date, check_out_date)
#
# # Book a deluxe room
# check_in_date = datetime.date(2023, 6, 1)
# check_out_date = datetime.date(2023, 6, 3)
# hotel.book_room('deluxe', check_in_date, check_out_date)
#
# # Book a penthouse suite
# check_in_date = datetime.date(2023, 7, 1)
# check_out_date = datetime.date(2023, 7, 5)
# hotel.book_room('penthouse', check_in_date, check_out_date)
#
# # Release a room
# check_in_date = datetime.date(2023, 5, 1)
# check_out_date = datetime.date(2023, 5, 5)
# hotel.release_room('standard', check_in_date, check_out_date)