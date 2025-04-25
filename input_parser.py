from datetime import datetime, timedelta
import pytz


def get_user_input():
    return input("請輸入活動指令：")


def parse_event_data(text):
    if "明天下午兩點" in text:
        tz = pytz.timezone("Asia/Taipei")
        now = datetime.now(tz)
        tomorrow = now + timedelta(days=1)
        start = tz.localize(datetime(tomorrow.year, tomorrow.month, tomorrow.day, 14, 0))
        end = start + timedelta(hours=1)

        return {
            "summary": "測試活動",
            "start": {"dateTime": start.isoformat(), "timeZone": "Asia/Taipei"},
            "end": {"dateTime": end.isoformat(), "timeZone": "Asia/Taipei"},
        }
    return None