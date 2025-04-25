📦 GPT Calendar Assistant 部署教學（Render 版）

1️⃣ 申請 Google Calendar API 並取得以下資料：
   - CLIENT_ID
   - CLIENT_SECRET
   - REFRESH_TOKEN

2️⃣ 修改 `.render.yaml` 裡的三個變數，把 value 改成你的資料。

3️⃣ 把整個資料夾 push 到 GitHub
   也可上傳 zip 解壓縮後，建立一個 GitHub repo

4️⃣ 前往 https://render.com 新建 Web Service：
   - 點「New +」> Web Service
   - 選擇你剛剛建立的 repo
   - Render 會自動偵測 `.render.yaml` 自動建立並部署

5️⃣ 等候部署完成，會得到一組網址（例如 https://gpt-calendar-assistant.onrender.com）

6️⃣ 測試時會執行 `main.py`，新增一筆測試行程

✅ 完成！你可以修改 main.py 加入更多功能，例如每日提醒、Webhook 推播等。