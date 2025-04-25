from calendar_helper import create_event
import datetime
import pytz  # 要加上 pytz

tz = pytz.timezone("Asia/Taipei")
now = datetime.datetime.now(tz)
start = (now + datetime.timedelta(minutes=30)).isoformat()
end = (now + datetime.timedelta(minutes=60)).isoformat()
create_event("🎯 GPT Calendar 測試行程", start, end)
