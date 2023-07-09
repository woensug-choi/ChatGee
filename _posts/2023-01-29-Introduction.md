---
title: 챗봇빌더 사용설명서
author: Woen-Sug Choi
date: 2023-03-28
last-modified-at: 2023-04-23
layout: post
---

# 오픈소스 AI 카톡 챗봇 빌더 

오픈소스 카카오톡 AI 챗봇 챗지 빌더 🥳🎉

- **챗지 챗봇의 성격, 역할, 내용을 프롬프트로 직접 디자인 가능🎉🎉**
- **내용 기입, 실행파일 실행, 챗봇 설정만으로 코딩 몰라도 가능🎉🎉**
- 기본 포함기능
  - 사용설명서 카드페이지 표시 `📓 사용설명서`
  - 대화내용 삭제 기능 `💫 새로운 시작`
- 카카오톡 채널이 요구하는 5초내 응답조건 대응
  - 5초 내 응답하지 못하면 '생각중'이라는 답을 우선 송신
  - 사용자가 다시 요청 시, DB에 저장된 답변을 송신
- ChatGPTers의 AI 챗봇 개발실과 함께합니다
  - [AI 챗봇 개발실 (ChatGPTers)](https://open.kakao.com/o/gECQhjbf)

> 카카오톡 챗봇 등록에 시간이 최대 6일 소요됩니다. [채널 신설과 챗봇 등록](https://woensug-choi.github.io/ChatGee/KakaoTalk_Channel.html)을 우선 수행해 두시기 바랍니다!

> 5초 후 응답하려면 '광고'의 성격을 가지므로 15원이 소모

# 개발 예제

| [벤치마크](http://pf.kakao.com/_RxoCkxj/chat) | [성경공부](http://pf.kakao.com/_FmUkxj/chat) | [상품소개](http://pf.kakao.com/_BCjxmxj/chat) | 
| :---: | :---: | :---: |
| <img src="https://woensug-choi.github.io/ChatGee/assets/images/ChatGee_Main.png" alt="ChatGee_Main" width="100"> | <img src="https://woensug-choi.github.io/ChatGee/assets/images/ChatGee_Bible.png" alt="ChatGee_Bible" width="100"> | <img src="https://woensug-choi.github.io/ChatGee/assets/images/ChatGee_Travel.png" alt="ChatGee_Travel" width="100"> |
| [카톡링크](http://pf.kakao.com/_RxoCkxj/chat) | [카톡링크](http://pf.kakao.com/_FmUkxj/chat) | [카톡링크](http://pf.kakao.com/_BCjxmxj/chat) | 

# 설치방법

- [초급자용](#초급자용-설치방법)
  - 윈도우 Batch 실행 파일 `ChatGee_Win` 
  - MacOS Shell 실행 파일 `ChatGee_Mac`
- [개발자용](#채발자용-사용방법) : Flask 앱 `chatgee/run_server.py` 
  - `settings.yaml`에서 챗지 성격, 역할, 내용 디자인
  - Flask 내 Threading/Queue 그대로 `uwsgi` 사용가능

## 초급자용 설치방법

- 설치순서
  - [1. 소스코드 다운로드](#1-소스코드-다운로드)
  - [2. 파이썬 설치](#2-파이썬-설치)
  - [3. Settings.yaml 설정](#3-settingsyaml-설정)
  - [4. ChatGee 실행](#4-chatgee-실행)
  - [5. 응답내용 테스트](#5-local_test-에서-챗봇-응답내용-테스트)
  - [6. 카카오톡 채널/챗봇 등록](#6-카카오톡-채널-신설-및-챗봇-등록)
  - [7. 콜백응답 기능 설정](#7-콜백응답-기능-설정)

#### 1. 소스코드 다운로드
- ChatGee(챗지) Github 레포지토리에서 최신 릴리즈 다운로드
  - [최신 릴리즈 다운로드 링크](https://github.com/woensug-choi/ChatGee/releases/latest)
  - 파일 두개 중, 위의 것 (`Source Code.zip`)을 다운로드
  - 다운로드 하면 `ChatGee-XX.zip`(XX는 버전)이 다운로드 되며, 원하는 곳에 압축을 풀고 다음 단계를 진행

#### 2. 파이썬 설치
  - 윈도우 사용자 (맥 사용자는 아래 참조)
    - 압축을 푼 `ChatGee-XX.zip`(XX는 버전) 폴더에 파이썬 설치파일이 동봉되어 있음
    - 동봉된 `python-3.10.10.exe` 또는 직접 파이썬 홈페이지에서 3.10.10 설치파일을 받아 설치
    - (주의사항!!) 아래 스크린샷과 같이 아래 `Add python.exe to PATH` 클릭 필수!
      - ADD PATH는 파이썬이 어느곳에서든지 실행되도록 설정하는 내용
      <img src="https://woensug-choi.github.io/ChatGee/assets/images/python1.jpg" alt="파이썬 설치화면" width="350">

    - 혹시 이미 파이썬이 설치되어 있어서 업그레이드 하거나 위 창을 만나지 못하는 경우, 파이썬이 잘 설치되어 있는지 확인하기 위해 윈도우 시작버튼을 누른 후 `cmd`를 검색해서 검은 창을 실행하고 `python --version`을 입력하여 파이썬 버전이 3.10.10이 나오는지 확인
      - 만약 오류가 있다면, Python 설치파일을 실행하여 삭제 후 다시 설치 진행

  - Mac 사용자
    - 다음 링크를 참고하여 파이썬 설치
      - [맥용 파이썬 3.10.10 설치파일](https://www.python.org/ftp/python/3.10.10/python-3.10.10-macos11.pkg)
      - 설치 후,  `Terminal` 앱에서 `python --version`을 입력하여 파이썬 버전이 3.10.10이 나오는지 확인


#### 3. `Settings.yaml` 설정
- `ChatGee-XX.zip`(XX는 버전) 폴더에 `Settings` 파일이 있음
- `Settings` 파일을 열고, 아래 항목을 설정
  - `메모장` (윈도우) 또는 `TextEdit` (맥) 원하는 편집 프로그램으로 열어서 아래 항목을 설정
  - `연결 프로그램`에서 `메모장` (윈도우) 또는 `TextEdit` (맥) 을 선택하면 메모장으로 열림
- 필수 설정 항목
  - Ngrok Key
    - Ngrok를 이용하면 고정아이피가 없는 상태에서도 외부에서 접속 가능
    - [Ngrok 홈페이지](https://ngrok.com/)에서 회원가입 후 로그인
    - `get-started > your-authtoken` 에서 `authtoken`을 복사하여 `Settings.yaml > NGROK > YOUR_NGROK_TOKEN`에 붙여넣기
  - OpenAI API Key
    - ChatGPT를 이용하기 위해서는 OpenAI의 API Key가 필요. API Key는 무료계정도 받을 수 있으며 최초 2만원 상당의 사용 쿠폰을 제공함
      - [OpenAI API Key 발급](https://platform.openai.com/account/api-keys)에서 OpenAI계정을 생성하고 로그인 하면 API Key를 발급받을 수 있음
      - API Keys 화면에서 `+ Create new secret key`를 눌러서 API Key를 발급받음
      - 발급되면 자동으로 클립보드에 복사되므로 다시 `Settings`에 붙여넣기
      - 만약 복붙에 실패하셨다면, 기존 API Key 를 삭제 후 재발급
    - `Settings.yaml > OPEN_AI > YOUR_OPEN_AI_API_KEY` 에 본인의 API Key를 입력
    - OpenAI 가입 후 API Key를 발급받아 입력하며 됩니다. `sk-복잡한영문키`의 형태
  - 챗지 챗봇의 성격, 역학 내용을 정하는 시스템 프롬프트
    - `settings.yaml > SETTINGS > SYSTEM_PROMPT`에 챗지 챗봇을 정의하는 설명 기입
      - 한글로도 기입가능하지만 영문일 때 컨트롤이 더 잘됨
      - 어떤 역할들이 가능한지는 [Awsome Prompts](https://github.com/f/awesome-chatgpt-prompts#prompts)를 참고
      - 역할을 부여할 때, `ChatGee는 무엇무엇을 한다`로 정의
      - 동본된 `SYSTEM_PROMPT`는 챗지가 영문번역기가 되도록 정의되어 있음

        ```yaml
        - ChatGee act as an English translator, spelling corrector and improver.
        - ChatGee translate User's prompt into English.
        - ChatGee replace simplified A0-level words and sentences with more beautiful and elegant, upper level English words and sentences.
        - ChatGee keep the meaning same, but make them more literary.
        - ChatGee only reply the correction, the improvements and nothing else, do not write explanations.
        - ChatGee doens't answer to User's prompt, but just translate the last User's prompt.
        - If User prompt in English, ChatGee now act as an Korean translator.
        - ChatGee doesnt write explanations, but reply only tranlsated texts.
        ```

  - 첫 사용자에게 보여지는 인사말
    - `settings.yaml > CONTENTS > GREETINGS`에 기입
  - 후원금 링크
    - `settings.yaml > CONTENTS > SUPPORT_LINK`에 기입
    - 빈칸으로 두면 후원금 링크는 보여지지 않음
  - 사용설명서 두번째 페이지
    - `settings.yaml > CONTENTS > EXPLAIN`에 기입
    - 챗지 사용설명서 두번째 페이지에 기입될 내용
    - 기본적인 챗지 사용설명서는 함께 동봉됨
  - 광고 또는 주기적 알림 내용
    - `settings.yaml > CONTENTS > ADVERTISEMENT`에 기입
    - `settings.yaml > CONTENTS > ADVERTISEMENT_FREQUENCY`에서 정의된 주기로 등장
  - 채널 친구가 아닌 상태에서 사용가능 횟수
    - `settings.yaml > SETTINGS > NO_FRIEND_USE_LIMIT`에서 정의

#### 4. `ChatGee` 실행
- 윈도우 사용자 (맥버전은 아래 참조)
  - ChatGee의 소스코드에서 `ChatGee_Win` 실팽파일을 더블클릭으로 실행
    - `Windows의 PC 보호`와 함께 파란색 창이 뜨면, 표시 내용 중 밑줄이 쳐진 `추가정보`를 클릭 후 `실행`을 클릭
    - 총 4 단계로 챗지서버를 구동, 중간 단계에서 `Windows Defender 방화벽`이 서버로 사용되는것을 확인하는 창이 나타나며 이때 `액세스 허용`을 클릭
    - 실행이 완료되면, Ngrok가 발급한 주소가 나타남
      - 주소가 나타나지 않고 `(4/4) Run ngrok`에서 멈춰있다면, 검은 `cmd`창을 종료하고 다시 `ChatGee_Win`을 실행합니다.
    - 뭔가 이상하거나 문제가 생기면 이 창을 종료하고 다시 실행

- MacOS 사용자
  - 챗지 아이콘으로 되어있는 `ChatGee_Mac` 파일을 우클릭 후 `Terminal`로 열기로 실행
    - 실행이 완료되면, Ngrok가 발급한 주소가 나타남
    - 한번 실행 후에는 `ChatGee_Mac` 파일을 더블클릭으로 실행 가능
  - 실행파일이 작동안할 경우,
    - `Terminal`을 실행 후 ChatGee 소스파일 경로로 이동
      - 폴더로 이동하려면 `cd 폴더명`을 사용, 상위 폴더로 이동하려면 `cd ..`을 사용, 현재 폴더의 내용물을 확인하려면 `ls`를 사용
    - ChatGee 소스파일 위치에서 다음 명령어를 실행
      ```bash
      ./ChatGee_Mac.sh
      ```

- 챗지 서버 접속
  - 실행이 완료되면, `ngrok`가 발급한 주소로 접속
  - `https://복잡한-숫자-주소.ngrok-free.app` 
    - 동봉된 `Settings`의 설정값에서는 챗지가 영문번역기가 되도록 정의되어 있으므로 한글을 입력하면 영문을 답하고, 영문이나 그 외 언어를 입력하면 한글을 대답
    - 접속 주소 설명,
      - 챗지 챗봇의 기본 서버 주소: `https://복잡한-숫자-주소.ngrok-free.app`
      - 카카오톡 서버와 주고받을 주소: `https://복잡한-숫자-주소.ngrok-free.app/prompt`


> 마지막에 주소가 나오지 않는다면, ngrok 서버의 문제일 수 있음
  - 브라우저에서 `localhost:6959/local_test`에 접속해서 테스트 (6059는 settings.yaml에서 바꾸지 않았다면 기본포트)

#### 5. `/local_test` 에서 챗봇 응답내용 테스트
- `ChatGee` 실행에서 얻은 `https://복잡한-숫자-주소.ngrok-free.app/local_test`로 `local_test`로 끝나는 주소로 접속
- 사용자가 입력할 내용을 빈칸에 입력 후 `Submit`을 클릭 또는 엔터를 입력하면, 응답소요시간, 응답내용을 확인 가능

#### 6. 카카오톡 채널 신설 및 챗봇 등록
> 카카오톡 챗봇 등록에 시간이 최대 6일 소요됩니다. 카카오톡 채널 신설 및 챗봇 등록을 우선 수행해 두시기 바랍니다!

- [카카오톡 채널 신설 및 챗봇 등록 매뉴얼](https://woensug-choi.github.io/ChatGee/KakaoTalk_Channel.html)

#### 7. 콜백응답 기능 설정

- 카카오톡 서버의 5초 내 응답 제한
  - 카카오톡 서버는 5초안에 챗지서버가 응답을 하지 않으면 연결을 끊어버립니다.
  - 기본적인 챗지서버의 설정은 응답이 지연되면 `생각 다했니?`를 응답해 사용자가 백그라운드에서 저장된 응답을 받을 수 있도록 구성되어 있습니다.
- 카카오톡 콜백응답 기능
  - 5초 이후에 응답을 보내는 기능이 `콜백응답`기능입니다. 해당 기능은 카카오톡측에 직접 메일을 보내 승인을 받아야 합니다.
  - 콜백기능을 활성화 하시려면 [콜백응답 설정](ttps://woensug-choi.github.io/ChatGee/KakaoTalk_Channel.html#콜백응답-설정)을 먼저 수행하시기 바랍니다.
- 콜백기능을 활성화 하셨다면,
  - `settings.yaml > SETTINGS > CALLBACK` 를 `True`로 변경합니다.


## 개발자용 사용방법

저도 이번에 처음 Flask, Queue/Threading을 사용한 병렬처리 방법 등 공부하면서 만든 코드여서 기존의 개발자들이 보시면 많이 어렵지 않을 거라고 생각됩니다!

PR은 언제나 환영입니다! 네이버 라인, GPT 4, 다른 AI 모델들을 접목하는 기능이 쉽게 추가될 수 있도록 고려해 작성해 두었습니다!

현재 운영되고 있는 챗지 카카오톡 채널은 본 코드를 베이스로 `검색기능`, `질문 추천기능` `대화모드 설정기능`, `OCR`, `기타기능`이 추가된 벤치마크 챗봇입니다. 해당 챗봇은 벤치마크 모델로서 지속가능한 형태로의 최소한의 수익만을 목표로 하며, 기타 다른 광고, 세미나 등으로 본 오픈소스를 키워가면 좋겠다고 생각합니다. 함께 채널을 운영하고 코드를 키워나가실 분은 언제나 환영입니다!

# 라이센스 정보
- `BSD 4-Clause "Original" or "Old" License` 라이센스
  - 상업적 사용 가능
  - 수정, 배포 가능
  - 다만!, 본 ChatGee 라이브러리가 사용되었음을 모든 광고물 및 수정, 배포, 상업판에 표기 필수
  - [라이센스 정보 확인](https://github.com/woensug-choi/ChatGee/blob/main/LICENSE)