from calendar_helper import create_event
import datetime

# 範例：建立一筆 30 分鐘後的行程
now = datetime.datetime.now()
start = (now + datetime.timedelta(minutes=30)).isoformat()
end = (now + datetime.timedelta(minutes=60)).isoformat()
create_event("🎯 GPT Calendar 測試行程", start, end)