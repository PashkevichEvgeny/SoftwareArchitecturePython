class BusStop:
    _id = 0

    def __init__(self, name: str, latitude: float, longitude: float):
        BusStop._id += 1
        self.id = BusStop._id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, new_id: int):
        self._id = new_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, new_lat: float):
        self._latitude = new_lat

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, new_long: float):
        self._longitude = new_long
