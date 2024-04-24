import datetime

class RoomType:
    def __init__(self, type_id, name, features, price):
        self.type_id = type_id
        self.name = name
        self.features = features
        self.price = price

ROOM_TYPES = [
    RoomType(1, "Single Room", "Private Bathroom", 100),
    RoomType(2, "Double Room", "Queen Bed", 150),
    RoomType(3, "Suite", "Living Room with Jacuzzi", 200),
    RoomType(4, "Penthouse Suite", "Luxury Furnishings with Ocean View", 3000),
    RoomType(5, "Standard Room", "Shared Bathroom", 80),
    RoomType(6, "Deluxe Room", "King Bed", 180),
    RoomType(7, "Family Suite", "Large Living Area", 250),
    RoomType(8, "Executive Suite", "Work Desk and Lounge", 350),
    RoomType(9, "Honeymoon Suite", "Romantic Decor and Champagne", 400),
    RoomType(10, "Presidential Suite", "Private Balcony and Butler Service", 500),
    RoomType(11, "Studio Apartment", "Kitchenette and Dining Area", 150),
    RoomType(12, "Accessible Room", "Wider Doors and Roll-in Shower", 120),
    RoomType(13, "Bungalow", "Private Garden", 220),
    RoomType(14, "Cottage", "Rustic Decor", 200),
    RoomType(15, "Villa", "Private Pool and Oceanfront", 600),
    RoomType(16, "Chalet", "Mountain View", 180),
    RoomType(17, "Loft", "Open Floor Plan", 170),
    RoomType(18, "Condo", "Full Kitchen and Washer/Dryer", 300),
    RoomType(19, "Treehouse", "Canopy Bed", 150),
    RoomType(20, "Beach House", "Direct Beach Access", 400),
    RoomType(21, "Log Cabin", "Fireplace", 200),
    RoomType(22, "Boat House", "Waterfront View", 250),
    RoomType(23, "Tent", "Outdoor Camping Experience", 100),
    RoomType(24, "Yurt", "Traditional Mongolian Design", 120),
    RoomType(25, "Igloo", "Arctic Adventure", 400),
    RoomType(26, "Caravan", "Mobile Accommodation", 180),
    RoomType(27, "Tipi", "Native American Style", 150),
    RoomType(28, "Castle Suite", "Regal Decor", 800),
    RoomType(29, "Underwater Room", "Marine Life Views", 1000),
    RoomType(30, "Space Station", "Panoramic Views", 1500)
]

class RoomDetails:
    def __init__(self, room_id, room_number, type_id, price, available):
        self.room_id = room_id
        self.room_number = room_number
        self.type_id = type_id
        self.price = price
        self.available = available

class Room:
    def __init__(self, room_type):
        self.room_type = room_type
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
        if check_in_date == check_out_date:
            nights = 1
        else:
            nights = (check_out_date - check_in_date).days

        return nights * self.room_type.price

class Reservation:
    def __init__(self, reservation_id, guest_name, check_in_date, check_out_date, room_id):
        self.reservation_id = reservation_id
        self.guest_name = guest_name
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room_id = room_id

class Hotel:
    def __init__(self):
        self.rooms = {room_type.name.lower(): [Room(room_type) for _ in range(10)] for room_type in ROOM_TYPES}
        self.reservations = []
        self.room_details = {}


        # Initialize room_details

        for i in range(1, 31):
            room_type = next((rt for rt in ROOM_TYPES if rt.type_id == i), None)
            if room_type:
                room_number = f"{i:03}"  # Format room number with leading zeros
                available = True if i >= 18 else False
                self.room_details[i] = RoomDetails(i, room_number, room_type.type_id, room_type.price, available)




    def book_room(self, room_type, check_in_date, check_out_date):

        if check_in_date > check_out_date:
            print("Check-in date cannot be greater than check-out date.")
            return

        available_rooms = [room for room in self.rooms[room_type] if room.is_available]
        if available_rooms:
            room = available_rooms[0]
            if room.book(check_in_date, check_out_date):
                reservation_id = len(self.reservations) + 1
                guest_name = input("Enter the guest name: ")
                room_id = room.room_type.type_id
                reservation = Reservation(reservation_id, guest_name, check_in_date, check_out_date, room_id)
                self.reservations.append(reservation)
                print(f"Room {room.room_type.name} booked for {check_in_date} to {check_out_date}.")
                print(f"Total cost for the room you have selected: ${room.calculate_cost(check_in_date, check_out_date)}")
                print("Thanks for making a reservation with KED Hotels !!")
            else:
                print("Room is not available for the specified dates.")
        else:
            print(f"No {room_type} rooms available for the specified dates.")


    def release_room(self, room_type, check_in_date, check_out_date):
        for room in self.rooms[room_type]:
            if room.check_in_date == check_in_date and room.check_out_date == check_out_date:
                room.release()
                print(f"Room {room.room_type.name} released for {check_in_date} to {check_out_date}.")
                return
        print("No room found for the specified dates.")

    def display_room_types(self):
        print("\nAvailable Room Types:")
        for room_type in ROOM_TYPES:
            print(f"{room_type.type_id}. {room_type.name} - {room_type.features}")

    def display_availability(self):
        print("\n--- View Room Availability ---")
        for room_type, rooms in self.rooms.items():
            available_rooms = [room for room in rooms if room.is_available]
            print(f"{room_type.capitalize()} rooms available: {len(available_rooms)}")

    def display_reservations(self):
        print("\n--- Reservation Details ---")
        if not self.reservations:
            print("No reservations found.")
        else:
            for reservation in self.reservations:
                room_type = next((rt for rt in ROOM_TYPES if rt.type_id == reservation.room_id), None)
                if room_type:
                    print(f"Reservation ID: {reservation.reservation_id}")
                    print(f"Guest Name: {reservation.guest_name}")
                    print(f"Check-in Date: {reservation.check_in_date}")
                    print(f"Check-out Date: {reservation.check_out_date}")
                    print(f"Room Type: {room_type.name}")
                    print("---")

    def display_room_details(self):
        print("\n--- Room Details ---")
        print("RoomID\tRoomNumber\tTypeID\tPrice\tAvailable")
        for room_detail in self.room_details.values():
            print(f"{room_detail.room_id}\t{room_detail.room_number}\t\t{room_detail.type_id}\t{room_detail.price}\t{room_detail.available}")
