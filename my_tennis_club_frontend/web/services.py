import requests

API_URL = "http://127.0.0.1:8000/api"

def get_members():
    response = requests.get(f"{API_URL}/members/")
    return response.json() if response.status_code == 200 else []

def get_plans():
    response = requests.get(f"{API_URL}/plans/")
    return response.json() if response.status_code == 200 else []

def get_member_by_id(member_id):
    response = requests.get(f"{API_URL}/member/{member_id}/")
    return response.json() if response.status_code == 200 else None

def create_member(data, files=None):
    response = requests.post(f"{API_URL}/members", data=data, files=files)
    return response.status_code == 201

def update_member(member_id, data, files=None):
    response = requests.put(f"{API_URL}/members/{member_id}/", data=data, files=files)
    return response.status_code == 200

def delete_member(member_id):
    response = requests.put(f"{API_URL}/members/{member_id}/")
    return response.status_code == 204