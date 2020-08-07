# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
# class Vehicle:
#     def __init__(self, gas):
#         self.gas = gas

class Vehicle():
    def __init__(self):
        pass
             

# Ground Vehicle extended from Vehicle 
class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

# Car extended from GroundVehicle
class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass
        

# Motorcyle extended from GroundVehicle
class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass



# Flight Vehicle extended from Vehicle
class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass
    

# Starship extended from FlightVehicle
class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass
    


# Airplane extended from FlightVehicle 
class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass
        
