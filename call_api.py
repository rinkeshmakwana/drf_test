import datetime

import requests

URL = 'http://127.0.0.1:8000/sync/'

data = {
    "in_session_id": "12345",
    "user_id": 2,
    "project_id": 1,
    "activity_name": "activity name 15",
    "dt_utc_start_time": "2021-09-29 18:01Z",
    "dt_utc_end_time": "2021-09-29 18:30Z",
    "in_mouse_count": 4,
    "in_keyboard_count": 2,
    "in_screenshot_count": 20,
    "in_webcam_count": 15,
    "in_tracker_stop": 0
}

res = requests.post(URL, json=data)


print(res.status_code)
print(res.content)
