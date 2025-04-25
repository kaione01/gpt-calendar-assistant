from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


def get_calendar_service():
    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])
    service = build('calendar', 'v3', credentials=creds)
    return service


def event_exists(service, calendar_id, summary, start_time):
    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=start_time,
        maxResults=10,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    for event in events:
        if event['summary'] == summary:
            return True
    return False


def create_event(service, event_data):
    if event_exists(service, 'primary', event_data['summary'], event_data['start']['dateTime']):
        print("相同的事件已存在，略過建立。")
        return None

    event = service.events().insert(calendarId='primary', body=event_data).execute()
    return event
