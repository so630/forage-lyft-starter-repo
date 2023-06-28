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
        return math.floor((datetime.timedelta(self.last_service_date - self.current_date).days)/365) >= 2
    
class NubbinBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return math.floor((datetime.timedelta(self.last_service_date - self.current_date).days)/365) >= 4
        