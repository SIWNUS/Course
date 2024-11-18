class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin, destination, out_time, reach_time, stops):
        self.dict = {
            "origin": origin,
            "departure": out_time,
            "destination": destination,
            "arrival": reach_time,
            "price": price,
            "stops": stops - 1,
        }
            
