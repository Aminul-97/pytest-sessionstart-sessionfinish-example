import requests

class Manage_api:
    """
    Class to manage API calls.

    Args:
    link:str

    Returns:
    None
    """
    def __init__(self, link:str):
        self.link = link
    
    def check_connection(self) -> str:
        """
        Function to check api connection.
        """
        try:
            response = requests.get(self.link)
            return response.status_code
        except requests.exceptions.RequestException as e:
            return None
    
    def get_data(self) -> str:
        """
        Function to get api response.
        """
        try:
            response = requests.get(self.link)
            return response.text
        except requests.exceptions.RequestException as e:
            return None

api_mgr = Manage_api("https://digidates.de/api/v1/checkdate?date=2023-01-01")
print(api_mgr.check_connection())
print(api_mgr.get_data())

    
