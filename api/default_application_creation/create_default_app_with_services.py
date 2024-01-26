#!/usr/bin/python3
import json
import pathlib

import requests

# Folder needs to be created e.g. "/home/alex/oakestra/alex_utils"
DEV_UTILS_PATH = pathlib.Path(<your_custom_path>)

IP = "192.168.178.35"
PORT = 10000
CORE_URL = f"http://{IP}:{PORT}"

login_query = {
    "url": f"{CORE_URL}/api/auth/login",
    "headers": {"accept": "application/json", "Content-Type": "application/json"},
    "data": {
        "username": "Admin",
        "password": "Admin",
    },
}

login_response = requests.post(
    login_query["url"], headers=login_query["headers"], json=login_query["data"]
)
bearer_auth_token = login_response.json()["token"]

default_SLA = ""
with open(DEV_UTILS_PATH / "default_SLA.json", "r") as f:
    default_SLA = json.load(f)

application_creation_query = {
    "url": f"{CORE_URL}/api/application/",
    "headers": {"Authorization": f"Bearer {bearer_auth_token}", "Content-Type": "application/json"},
    "data": default_SLA,
}

application_creation_response = requests.post(
    application_creation_query["url"],
    headers=application_creation_query["headers"],
    json=application_creation_query["data"],
)

if application_creation_response.status_code == 200:
    print("Successfully created new default application with services")
else:
    print("FAILED to created new default application with services !!!")
    print("response:", application_creation_response)
