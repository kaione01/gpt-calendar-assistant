📦 GPT Calendar Assistant Render 部署教學（乾淨版）

✅ 功能：
- 提供 POST API (/add-event) 來新增 Google Calendar 行程
- 你可以從 GPT 或 curl 呼叫這個 API，自動寫入日曆
- Render 啟動時不會自動新增任何行程

1️⃣ 建立 Google Calendar API，取得 CLIENT_ID、CLIENT_SECRET、REFRESH_TOKEN
2️⃣ 修改 .render.yaml 中的三個變數，填入你的金鑰資料
3️⃣ 上傳整包專案到 GitHub
4️⃣ Render 建立 Web Service，自動偵測 .render.yaml 進行部署
5️⃣ 完成後你會有一個網址，例如：
   https://gpt-calendar-assistant.onrender.com

📨 呼叫新增行程範例（curl）：
curl -X POST https://你的網址/add-event \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Tesla 試駕",
    "start": "2025-04-26T14:30:00+08:00",
    "end": "2025-04-26T15:30:00+08:00"
  }'

✅ 完成！
