from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_number, engine_capacity):
        self._vehicle_number = vehicle_number
        self._capacity = engine_capacity

    @property
    def vehicle_number(self):
        return self._vehicle_number

    @property
    def capacity(self):
        return self._capacity

    # polymorphic, cuz any vehicles can have its own intepretaton of the road tax
    @abstractmethod
    def compute_road_tax(self):
        pass

    def __str__(self):
        return f"{self.compute_road_tax()} {self._vehicle_number} {self._capacity}"


class PassengerVehicle(Vehicle):
    def __init__(self, owner, age, vehicle_number, engine_capacity):
        super().__init__(vehicle_number, engine_capacity)
        self._owner = owner
        self._age = age

    def compute_road_tax(self):
        road_tax = 1 * self._capacity
        if self._age >= 55:
            return road_tax * 0.9
        else:
            return road_tax

    def __str__(self):
        return f"{self._owner} {self._age} {super().__str__()}"


class CommercialVehicle(Vehicle):
    def __init__(self, comp_registration_no, max_laden_weight, vehicle_number, engine_capacity):
        super().__init__(vehicle_number, engine_capacity)
        self._comp_registration_no = comp_registration_no
        self._max_laden_weight = max_laden_weight

    def compute_road_tax(self):
        if self._max_laden_weight <= 3:
            return 1 * self._capacity
        else:
            return 1.5 * self._capacity

    def __str__(self):
        return f"{self._comp_registration_no} {self._max_laden_weight} {super().__str__()}"


if __name__ == '__main__':
    pv1 = PassengerVehicle('Jensen', 54, '8888', 1500)
    pv2 = PassengerVehicle('Thomas', 55, '8889', 2000)
    print(pv1, pv2, sep='\n')
    cv1 = CommercialVehicle('ABC123', 3, '8887', 3000)
    cv2 = CommercialVehicle('ABC346', 3.5, '8886', 3500)
    print(cv1, cv2, sep='\n')

    vehicles = [pv1, pv2, cv1, cv2]

    for veh in vehicles:
        print(f"Vehicle: {veh.vehicle_number}, requires to pay road tax: ${veh.compute_road_tax()}")
