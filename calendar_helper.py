import requests
import os

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
refresh_token = os.getenv("REFRESH_TOKEN")

def get_access_token():
    response = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
        },
    )
    return response.json().get("access_token")

def create_event(summary, start_time, end_time):
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    event = {
        "summary": summary,
        "start": {"dateTime": start_time, "timeZone": "Asia/Taipei"},
        "end": {"dateTime": end_time, "timeZone": "Asia/Taipei"},
    }

    response = requests.post(
        "https://www.googleapis.com/calendar/v3/calendars/primary/events",
        headers=headers,
        json=event,
    )

    if response.status_code in [200, 201]:
        return response.json()
    else:
        return {"error": response.text}
