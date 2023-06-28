class Tire():
    def __init__(self, tire_wear: list) -> None:
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        pass

class CarriganTire(Tire):
    def needs_service(self) -> bool:
        for i in self.tire_wear:
            if i >= 0.9:
                return True
        
        return False
    
class OctoprimeTire(Tire):
    def needs_service(self) -> bool:
        return sum(self.tire_wear) >= 3