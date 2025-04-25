from calendar_helper import create_event, get_calendar_service
from input_parser import parse_event_data, get_user_input


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


if __name__ == '__main__':
    main()
