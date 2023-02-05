'''  Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.

Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a child class

Write a program to determine which class a given Bus object belongs to. '''

class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def __init__(self, seating_capacity=50):
        super().__init__(seating_capacity)

    def fare(self):
        base_fare = super().fare()
        return base_fare + base_fare * 0.1


# Create a Vehicle object with a seating capacity of 30
vehicle = Vehicle(30)

# Call the fare method of the Vehicle class
vehicle_fare = vehicle.fare()
print("Fare of the vehicle:", vehicle_fare)

# Create a Bus object
bus = Bus()

# Call the fare method of the Bus class
bus_fare = bus.fare()
print("Fare of the bus:", bus_fare)