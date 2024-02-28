from managers import sheetymanager, flightdatamanager

sheetyManager = sheetymanager.SheetyManager()
flightManager = flightdatamanager.FlightDataManager()

storedFlightData = sheetyManager.getSheetyData()

for data in storedFlightData:
    if data.get("iataCode") == "":
        iataCode = flightManager.getCityIataCode(data.get("city"))
        data["iataCode"] = iataCode
        sheetyManager.updateSheetyData(data)

