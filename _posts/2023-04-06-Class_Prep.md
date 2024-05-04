---
title: 기초개발 워크숍 필수 준비사항
author: Woen-Sug Choi
date: 2023-04-06
last-modified-at: 2023-04-06
layout: post
exclude: true
---

워크숍 참여를 환영합니다 🥳🎉
본 페이지는 직접 주소를 입력해 접속해야만 보실 수 있습니다!

> **📢 본 내용을 수행해두지 않으면 워크숍 시간 내 챗봇은 완성할 수 없습니다**
> 
> **문의사항은 '워크숍 참여 멤버 오픈톡방'에서 문의해 주시기 바랍니다**
> - 워크숍 참여멤버 오픈톡방 : [접속링크](https://open.kakao.com/o/gqCA5Odf) (비밀번호 : `chatgee`)

<br>

## 목차

- [💬  카카오톡 채널 개설/설정하기](#--카카오톡-채널-개설설정하기)
  - [👤 카카오톡 채널 관리계정 생성](#카카오톡-채널-관리계정-생성)
  - [플러스 채널 생성](#플러스-채널-생성)
    - [카카오톡 비즈니스 계정 생성](#카카오톡-비즈니스-계정-생성)
    - [카카오톡 채널 생성](#카카오톡-채널-생성)
  - [챗봇 계정 생성](#챗봇-계정-생성)
    - [챗봇 관리자센터 오픈베타 참여신청](#챗봇-관리자센터-오픈베타-참여신청)


## 필요 프로그램 설치

### 파이썬 3.10 설치

- 공식 파이썬 3.10.10 다운로드 링크
  - 맥버전 : [다운로드 링크](https://www.python.org/ftp/python/3.10.10/python-3.10.10-macos11.pkg)
  - 윈도우 : [다운로드 링크](https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe)
    - 📢📢 윈도우 주의사항!! 아래 스크린샷과 같이 아래 `Add python.exe to PATH` 클릭 필수!
    - ADD PATH는 파이썬이 어느곳에서든지 실행되도록 설정하는 내용
  
      <img src="https://woensug-choi.github.io/ChatGee_Doc/assets/images/python1.jpg" style="height:270px;">

- 설치확인
  - 맥
    - `Terminal`앱을 실행시키고 `python --version`을 입력하여 파이썬 버전 3.10.10 확인
  - 윈도우
    - 윈도우 시작버튼을 누른 후 `cmd`를 검색해서 검은 창을 실행하고 `python --version`을 입력하여 파이썬 버전 3.10.10 확인


### VSCode 설치

- VS Code는 Microsoft에서 개발한 소스코드 편집기
  - 파이썬, 자바스크립트, HTML, CSS 등 다양한 언어를 지원
  - 다양한 플러그인을 설치하여 개발에 유용하게 사용 가능
  - <a href="https://code.visualstudio.com/download" target="_blank">📢 VS Code 다운로드 링크 : code.visualstudio.com/download</a>
    - 윈도우면 윈도우 아이콘, 맥은 맥 아이콘을 눌러 설치파일 다운로드
  - 다운로드 후 설치 진행



# 💬  카카오톡 채널 개설/설정하기

---

<aside>
💡 [카카오톡 채널 관리자센터](https://center-pf.kakao.com) 계정이 있으시다면 본 단계는 진행할 필요 없습니다

</aside>

<aside>
💡 카카오톡 채널 생성이 처음이라면 먼저 카카오톡 채널 관리계정을 만들어주세요
🔗 [카카오톡 채널 관리계정 생성 바로가기 (클릭!)](https://accounts.kakao.com/weblogin/create_account/?lang=ko&continue=https%3A%2F%2Fbusiness.kakao.com%2Fdashboard%2F#selectVerifyMethod)

</aside>

## 👤 카카오톡 채널 관리계정 생성

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/0c4cab46-0ec6-4da5-9c40-9340ab541ce6/Untitled.png)


## 플러스 채널 생성

### 카카오톡 비즈니스 계정 생성
카카오 비즈니스 홈페이지에 접속하여 오른 쪽 상단 `로그인` 에서 카카오톡 비즈니스 계정을 생성, 로그인합니다.
- 카카오비즈니스 : [https://business.kakao.com/](https://business.kakao.com/)
> 개인도 가능합니다! 오히려 개인으로 등록하고 진행하는 것이 전체적인 절차 처리가 빠릅니다. 회사계정을 등록하려면 공식적 절차상 서류도 많이 필요하고 시간도 오래 걸립니다.

![fig-1](https://woensug-choi.github.io/ChatGee/assets/images/1.jpg)

- 계정 생성 후 다시 비즈니스 채널 페이지로 돌아와서 오른쪽 상단 `내 비즈니스`로 들어갑니다.

![fig-2](https://woensug-choi.github.io/ChatGee/assets/images/2.jpg)

### 카카오톡 채널 생성

- `비즈니스 관리자 센터`로 들어가서 `채널 시작하기`를 클릭합니다.
  - 채널 생성 페이지로 들어가며 `+ 새 채널만들기`를 클립합니다.
  - 프로필 사진, 채널이름, 검색용 아이디, 소개글과, 카테고리를 설정합니다.
  - 프로필 사진은 언제든지 번경 가능하지만, 채널 이름은 변경이 아주 어렵습니다! 신중하게 설정해주세요.

![fig-3](https://woensug-choi.github.io/ChatGee/assets/images/3.jpg)
![fig-4](https://woensug-choi.github.io/ChatGee/assets/images/4.jpg)
![fig-5](https://woensug-choi.github.io/ChatGee/assets/images/5.jpg)

- 생성이 완료되면 `채널 관리자 센터`로 접속되며 여기서 기본적으로 프로필 공개설정을 합니다.
  - 화면 오른쪽 하단의 `채널 공개` 및 `검색 허용`을 `On`으로 설정합니다.

![fig-6](https://woensug-choi.github.io/ChatGee/assets/images/6.jpg)

- 채널의 주소를 확인해보시기 바랍니다.
  - `채널 URL`은 `https://pf.kakao.com/_xaxaxaxax`와 같은 형태입니다.
  - 이 주소는 챗봇 설정에서 필요하므로 따로 복사해 두시기 바랍니다.
  - `채널 URL`은 `채널 관리자 센터`의 왼쪽 탭들 중 `채널 홍보`에서 확인할 수 있습니다.

![fig-8](https://woensug-choi.github.io/ChatGee/assets/images/8.jpg)
- 이제 채널이 생성되었으며, 이 채널을 통해 채널과 챗봇을 연결시키는 작업으로 넘어갑니다.
  - 먼저 `채널 관리자 센터`의 왼쪽 탭 중 `비즈니스 도구 > 챗봇`으로 들어갑니다.
  - 여기서, `챗봇 관리자센터 바로가기`를 클릭합니다.

![fig-7](https://woensug-choi.github.io/ChatGee/assets/images/7.jpg)

## 챗봇 계정 생성

- `챗봇 관리자센터`에 들어가려면 `OBT (오픈베타)` 신청을 해야합니다. 이 신청을 대게 3~5일 정도 소요되므로 미리 신청해 두시는게 좋습니다. 또한, 개인은 쉽게 승인이 되나 회사계정 또는 비즈니스는 까다로운 서류 절차를 진행해야 하므로 먼저 개인으로 전체적인 챗봇 개발과정을 진행해 보시는 것을 추천드립니다.

### 챗봇 관리자센터 오픈베타 참여신청

- `기업`과 `개인` 중 개인을 선택하고 앞서 생성한 카카오톡 채널의 URL을 입력합니다.
  - `채널 URL`은 `https://pf.kakao.com/_xaxaxaxax`와 같은 형태입니다.
  - `채널 URL`은 `채널 관리자 센터`의 왼쪽 탭들 중 `채널 홍보`에서 확인할 수 있습니다.
- 신청사유는 간단이 기입하셔도 문제 없었습니다.

![fig-9](https://woensug-choi.github.io/ChatGee/assets/images/9.jpg)

- 신청이 완료되면, `챗봇 관리자센터`로 들어가지고 다음과 같은 페이지를 보실 수 있습니다. 여기까지 하시면 워크숍 준비는 끝입니다! 곧 뵙겠습니다!

![fig-8](https://woensug-choi.github.io/ChatGee/assets/images/8.jpg)

