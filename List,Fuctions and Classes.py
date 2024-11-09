# Superclass Vehicle
class Vehicle: 
    def __init__(self, vehicle_type): 
        self.vehicle_type = vehicle_type 

# Subclass Automobile inheriting from Vehicle 
class Automobile(Vehicle): 
    def __init__(self, vehicle_type, year, make, model, doors, roof): 
        super().__init__(vehicle_type)
        self.year = year 
        self.make = make 
        self.model = model 
        self.doors = doors 
        self.roof = roof 

    def display_info(self): 
        print("Vehicle Information:") 
        print(f"  Vehicle type: {self.vehicle_type}") 
        print(f"  Year: {self.year}") 
        print(f"  Make: {self.make}")
        print(f"  Model: {self.model}") 
        print(f"  Number of doors: {self.doors}")
        print(f"  Type of roof: {self.roof}") 

# Main function to gather input an display the vehicle information 
def main(): 
    print("Enter details of the car:") 
    vehicle_type = "car" 
    year = input("Year: ") 
    make = input("Make: ") 
    model = input("Model: ") 
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sun roof): ") 

# Create an instance of Automobile with user inputs 
    car = Automobile(vehicle_type, year, make, model, doors, roof) 
    car.display_info() 

# Run the main function 
if __name__ == "__main__": 
    main()