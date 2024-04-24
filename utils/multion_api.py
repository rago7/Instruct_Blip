# utils/multion_api.py
import requests

def execute_command(command):
    # Example POST request to the MultiOn API
    response = requests.post("https://api.multion.example/execute", json={"command": command})
    return response.json()
