class Vehicle:
    def __init__(self, gas):
        self.gas = gas


# Ground Vehicle extended from Vehicle 
class GroundVehicle(Vehicle):
    def __init__(self, gas, wheelsize):
        super().__init__(gas)
        self.wheelsize = wheelsize




# Car extended from GroundVehicle
class Car(GroundVehicle):
    def __init__(self, gas, wheelsize, model):
        super().__init__(gas, wheelsize)
        self.model = model



# Motorcyle extended from GroundVehicle
class Motorcylce(GroundVehicle):
    def __init__(self, gas, wheelsize):
           super().__init__(gas, wheelsize)



# Flight Vehicle extended from Vehicle
class FlightVehicle(Vehicle):
    def __init__(self, gas, wingspan):
        super().__init__(gas)
        self.wingspan = wingspan

# Starship extended from FlightVehicle
class Starship(FlightVehicle):
    def __init__(self, gas, wingspan, planet):
        super().__init__(gas, wingspan)
        self.planet = planet 


# Airplane extended from FlightVehicle 
class Airplane(FlightVehicle):
    def __init__(self, gas, wingspan, pilot):
        super().__init__(gas, wingspan)
        self.pilot = pilot