import requests
import os
from dotenv import load_dotenv

class FlightDataManager:
    load_dotenv()
    
    API_BASE_URL = "https://api.tequila.kiwi.com"
    API_KEY = os.getenv("TEQUILA_API_KEY")
    
    AUTH_HEADERS = {
        "apikey": API_KEY
    }

    PARAMS = {
        "term": ""
    }

    def getCityIataCode(self, cityName: str):
        self.PARAMS["term"] = cityName
        checkIataCodeUri = f"{self.API_BASE_URL}/locations/query"
        respose = requests.get(url=checkIataCodeUri, headers=self.AUTH_HEADERS, params=self.PARAMS)
        respose.raise_for_status()

        responseList = respose.json().get("locations")[0]

        return responseList.get("code")