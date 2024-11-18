class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin, destination, out_time, reach_time):
        self.price = price
        self.origin_airport = origin
        self.destination_airport = destination
        self.dep = out_time
        self.arr = reach_time
        self.dict = {
            "origin": self.origin_airport,
            "departure": self.dep,
            "destination": self.destination_airport,
            "arrival": self.arr,
            "price": self.price,
        }
            
