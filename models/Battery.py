import datetime
import math


class Battery():
    def needs_service(self) -> bool:
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).total_seconds() >= 2*365*24*3600
    
class NubbinBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).total_seconds() >= 4*365*24*3600
        