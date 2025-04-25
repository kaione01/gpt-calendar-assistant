from calendar_helper import create_event, get_calendar_service
from input_parser import parse_event_data, get_user_input
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/add-event", methods=["POST"])
def add_event():
    data = request.json
    user_input = data.get("text", "")
    if "新增活動" in user_input or "建立事件" in user_input:
        event_data = parse_event_data(user_input)
        if not event_data:
            return jsonify({"error": "無法解析活動內容"}), 400

        service = get_calendar_service()
        event = create_event(service, event_data)
        if event:
            return jsonify({"message": "活動建立成功", "summary": event.get("summary")})
        else:
            return jsonify({"message": "事件已存在，未重複建立"}), 200
    else:
        return jsonify({"message": "未偵測到新增活動的需求"}), 200


def main():
    service = get_calendar_service()
    user_input = get_user_input()  # 從使用者取得指令

    if "新增活動" in user_input or "建立事件" in user_input:
        event_data = parse_event_data(user_input)
        if event_data:
            event = create_event(service, event_data)
            if event:
                print("已建立活動：", event.get("summary"))
        else:
            print("無法解析活動內容，請重新輸入。")
    else:
        print("未偵測到新增活動的需求。")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        main()
    else:
        app.run(host="0.0.0.0", port=10000)
