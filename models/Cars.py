import Battery, Engine, datetime

class Serviceable():
    def needs_service(self) -> bool:
        pass


class Car(Serviceable):
    def __init__(self, engine: Engine.Engine, battery: Battery.Battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
    
class CarFactory():
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        spindler_battery = Battery.SpindlerBattery(last_service_date, current_date)
        capulet_engine = Engine.CapuletEngine(last_service_mileage, current_mileage)

        calliope = Car(capulet_engine, spindler_battery)

        return calliope
    
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        spindler_battery = Battery.SpindlerBattery(last_service_date, current_date)
        willoughby_engine = Engine.WilloughbyEngine(last_service_mileage, current_mileage)

        glissade = Car(willoughby_engine, spindler_battery)
        return glissade
    
    def create_palindrome(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        spindler_battery = Battery.SpindlerBattery(last_service_date, current_date)
        sternman_engine = Engine.SternmanEngine(last_service_mileage, current_mileage)

        palindrome = Car(sternman_engine, spindler_battery)
        return palindrome
    
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        nubbin_battery = Battery.NubbinBattery(last_service_date, current_date)
        willoughby_engine = Engine.WilloughbyEngine(last_service_mileage, current_mileage)
        
        rorschach = Car(willoughby_engine, nubbin_battery)
        return rorschach
    
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        nubbin_battery = Battery.NubbinBattery(last_service_date, current_date)
        capulet_engine = Engine.CapuletEngine(last_service_mileage, current_mileage)

        thovex = Car(capulet_engine, nubbin_battery)
        return thovex
        
