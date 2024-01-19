from taxi import Taxi
from invalid import InvalidTaxiName

class TaxiCompany:
    def __init__(self) -> None:
        self.taxi_list: list[Taxi] = []

    def addTaxi(self, newtaxi_id):
        for taxi in self.taxi_list:
            if taxi.id == newtaxi_id:
                raise InvalidTaxiName(id)
        else:
             self.taxi_list.append(taxi.id)
                

    def getAvaliable(self):
        boshtaksi = []
        for taxi in self.taxi_list:
            if taxi.available == False:
                boshtaksi.append(taxi.id)