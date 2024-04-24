import datetime

class Boat:
    def __init__(self, name, rental_price):
        self.name = name
        self.rental_price = rental_price
        self.available_dates = []

    def check_availability(self, start_date, end_date):
        for reservation in self.available_dates:
            if (start_date <= reservation.end_date and end_date >= reservation.start_date) or \
                    (start_date >= reservation.start_date and end_date <= reservation.end_date):
                return False
        return True

    def add_reservation(self, reservation):
        self.available_dates.append(reservation)

    def remove_reservation(self, reservation):
        self.available_dates.remove(reservation)

class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Reservation:
    def __init__(self, customer, boat, start_date, end_date):
        self.customer = customer
        self.boat = boat
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = self.calculate_cost()

    def calculate_cost(self):
        days = (self.end_date - self.start_date).days
        return days * self.boat.rental_price

    def __str__(self):
        return f"Reservation for {self.customer.name} on {self.boat.name} from {self.start_date} to {self.end_date} (Total cost: ${self.total_cost:.2f})"

class BoatRentalSystem:
    def __init__(self):
        self.boats = []
        self.customers = []
        self.reservations = []

    def add_boat(self, boat):
        self.boats.append(boat)

    def add_customer(self, customer):
        self.customers.append(customer)



    def make_reservation(self, customer, boat, start_date, end_date):
        if boat.check_availability(start_date, end_date):
            reservation = Reservation(customer, boat, start_date, end_date)
            self.reservations.append(reservation)
            boat.add_reservation(reservation)
            print(f"Reservation made for {customer.name} on {boat.name} from {start_date} to {end_date}.")
        else:
            print(f"Sorry, {boat.name} is not available from {start_date} to {end_date}.")

    def cancel_reservation(self, reservation):
        self.reservations.remove(reservation)
        reservation.boat.remove_reservation(reservation)
        print(f"Reservation for {reservation.customer.name} on {reservation.boat.name} from {reservation.start_date} to {reservation.end_date} has been cancelled.")

    def display_reservations(self):
        for reservation in self.reservations:
            print(reservation)

    def display_available_boats(self, start_date, end_date):
        available_boats = [boat for boat in self.boats if boat.check_availability(start_date, end_date)]
        if available_boats:
            print("Available boats:")
            for boat in available_boats:
                print(f"{boat.name} - ${boat.rental_price}/day")
        else:
            print("No boats available for the specified dates.")

def main():
    rental_system = BoatRentalSystem()

    # Add some boats
    rental_system.add_boat(Boat("Speedboat", 200))
    rental_system.add_boat(Boat("Pontoon Boat", 150))
    rental_system.add_boat(Boat("Kayak", 50))

    # Add some customers
    rental_system.add_customer(Customer("John Doe", "555-1234", "john@example.com"))
    rental_system.add_customer(Customer("Jane Smith", "555-5678", "jane@example.com"))

    # Make some reservations
    rental_system.make_reservation(rental_system.customers[0], rental_system.boats[0], datetime.date(2023, 6, 1), datetime.date(2023, 6, 5))
    rental_system.make_reservation(rental_system.customers[1], rental_system.boats[1], datetime.date(2023, 6, 10), datetime.date(2023, 6, 12))

    # Display reservations
    rental_system.display_reservations()

    # Display available boats
    rental_system.display_available_boats(datetime.date(2023, 6, 15), datetime.date(2023, 6, 20))

    # Cancel a reservation
    rental_system.cancel_reservation(rental_system.reservations[0])

    # Display reservations again
    rental_system.display_reservations()

if __name__ == "__main__":
    main()