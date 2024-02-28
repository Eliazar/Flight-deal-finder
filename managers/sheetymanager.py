import requests
import os
from dotenv import load_dotenv

class SheetyManager:
    
    load_dotenv()
    
    API_BASE_URL = "https://api.sheety.co/6d9221e4940f52af56542568ef0fe5cd/flightDeals/prices"
    SHEETY_AUTH = os.getenv("SHEETY_API_KEY")

    sheety_auth_headers = {
        "Authorization": SHEETY_AUTH
    }

    def getSheetyData(self):
        response = requests.get(url=self.API_BASE_URL, headers=self.sheety_auth_headers)
        sheetydata = response.json()
        return sheetydata.get("prices")
    
    def updateSheetyData(self, objToUpdate):
        updateUrl = self.API_BASE_URL + f"/{objToUpdate.get('id')}"

        body = {
            "price": {
                "iataCode": objToUpdate.get("iataCode")
            }
        }
        
        response = requests.put(url=updateUrl, headers=self.sheety_auth_headers, json=body)
        
        if response.status_code == 200:
            print("Row updated successfully")
        else:
            print(f"Failed to update row: {response.text}")
        
        response.raise_for_status()