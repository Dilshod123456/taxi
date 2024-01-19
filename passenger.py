from place import Place

class Passenger():
    def __init__(self) -> None:
        pass

    def getPlace(self, adres, tuman, mahalla):
        place = Place(adres, tuman, mahalla)
        return place