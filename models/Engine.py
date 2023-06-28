class Engine():
    def needs_service(self) -> bool:
        pass

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return (self.last_service_mileage - self.current_mileage) >= 30000
    
class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return (self.last_service_mileage - self.current_mileage) >= 60000
    
class SternmanEngine(Engine):
    def __init__(self, warning_light_on) -> None:
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on
    