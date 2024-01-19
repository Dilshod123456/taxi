class InvalidTaxiName(Exception):
    def __init__(self, id):
        self.id = id
        self.message = f"{id} -- InvalidTaxiName!!.."
        super().__init__(self.message)