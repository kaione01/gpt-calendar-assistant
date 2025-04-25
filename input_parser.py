# input_parser.py
from datetime import datetime, timedelta
import pytz
import re


def get_user_input():
    return input("請輸入活動指令：")


def parse_event_data(text):
    tz = pytz.timezone("Asia/Taipei")
    now = datetime.now(tz)

    if "明天" in text:
        tomorrow = now + timedelta(days=1)

        # 預設時間範圍
        hour = 9  # 早上 9 點

        if "下午" in text:
            hour = 14
        elif "晚上" in text:
            hour = 19
        elif "早上" in text:
            hour = 9
        elif "中午" in text:
            hour = 12

        start = tz.localize(datetime(tomorrow.year, tomorrow.month, tomorrow.day, hour, 0))
        end = start + timedelta(hours=1)

        return {
            "summary": "測試活動",
            "start": {"dateTime": start.isoformat(), "timeZone": "Asia/Taipei"},
            "end": {"dateTime": end.isoformat(), "timeZone": "Asia/Taipei"},
        }

    return None
