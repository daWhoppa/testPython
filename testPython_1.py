class RentalAgency:
    def __init__(self, name):
        # Initialize properties Rupert
        self.name = name
        self.vehicles = {}  # Dictionary to store vehicles (key: VIN, value: Vehicle object)
        self.rentals = {}   # Dictionary to store rentals (key: rental_id, value: Rental object)
        self.next_rental_id = 1
    
    def add_vehicle(self, vehicle):
        # TODO: Add the vehicle to the vehicles dictionary using its VIN as the key
        # TODO: Return True to indicate successful completion
        self.vehicles[vehicle.vin] = vehicle
        return True

    def rent_vehicle(self, vin, customer_name, days):
        # TODO: Check if the vehicle with the given VIN exists in self.vehicles
        # TODO: If not, return None
        # TODO: Get the vehicle object from self.vehicles
        # TODO: Check if the vehicle is available
        # TODO: If not available, return None
        # TODO: Create a rental_id string in the format "R{self.next_rental_id}"
        # TODO: Increment self.next_rental_id
        # TODO: Create a new Rental object with the rental_id, vehicle, customer_name, and days
        # TODO: Call the vehicle's start_rental method
        # TODO: Add the rental to self.rentals using rental_id as the key
        # TODO: Return the rental_id
        if vin not in self.vehicles:
            return None

        vehicle = self.vehicles[vin]
        if not vehicle.available:
            return None

        rental_id = f"R{self.next_rental_id}"
        self.next_rental_id += 1

        rental = Rental(rental_id, vehicle, customer_name, days)
        vehicle.start_rental()
        self.rentals[rental_id] = rental
        return rental_id

    def return_vehicle(self, rental_id):
        # TODO: Check if the rental with the given rental_id exists in self.rentals
        # TODO: If not, return False
        # TODO: Get the rental object from self.rentals
        # TODO: Check if the rental is active
        # TODO: If not active, return False
        # TODO: Call the rental's end_rental method and return its result
        if rental_id not in self.rentals:
            return False

        rental = self.rentals[rental_id]
        if not rental.active:
            return False

        result = rental.end_rental()
        del self.rentals[rental_id]
        return result

    def available_vehicles(self):
        # TODO: Return a list of all vehicles in self.vehicles.values() where vehicle.available is True
        # TODO: Use a list comprehension for this
        return [vehicle for vehicle in self.vehicles.values() if vehicle.available]