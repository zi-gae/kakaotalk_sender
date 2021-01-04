# 카카오톡 자동메세지 전송 프로그램

KakaoAutoMSGSender 입니다.

# 사용법

img 디렉터리 안에는 캡쳐 프로그램으로 기존 아이콘들을 대체하여야 합니다.

코드 설명과 사용법은 [영상](https://www.youtube.com/watch?v=oNjRH1Cz9k4)을 참고해주세요.

# 다운로드
```
git clone https://gitlab.com/Whackur/kakaoautomsgsender
```

# 모듈 설치 스크립트
opencv 모듈을 설치하지 않으면 confidence 관련 오류가 납니다.
```
pip install opencv-python
pip install pyperclip
pip install pyautogui
```

# 실행 스크립트
```
python main.py
```

# 기능추가
* 로그아웃을 구현하였습니다.
* 전송할 메세지를 파일 (send_for_text.txt) 로부터 읽어옵니다.