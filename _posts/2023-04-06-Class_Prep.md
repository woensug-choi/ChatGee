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

- [목차](#목차)
- [필요 프로그램 설치](#필요-프로그램-설치)
  - [파이썬 3.10 설치](#파이썬-310-설치)
  - [VSCode 설치](#vscode-설치)
- [💬  카카오톡 채널 개설하기](#--카카오톡-채널-개설하기)
  - [👤 카카오톡 채널 관리계정 생성](#카카오톡-채널-관리계정-생성)
  - [🗝️ 카카오톡 관리자센터 로그인](#️카카오톡-관리자센터-로그인)
  - [🚀 카카오톡 채널 설정하기](#카카오톡-채널-설정하기)
    - [1. **채널 만들기**](#1-채널-만들기)
    - [2. **채널 정보 입력하기**](#2-채널-정보-입력하기)
    - [3. **채널 개설 완료**](#3-채널-개설-완료)
    - [4. **채널 공개 설정하기**](#4-채널-공개-설정하기)
    - [5. **채널 URL 확인하기**](#5-채널-url-확인하기)
- [🤖  카카오톡 챗봇 생성하기](#-카카오톡-챗봇-생성하기)
  - [**1. 새로운 봇 생성하기**](#1-새로운-봇-생성하기)
  - [**2. 카카오톡 채널 연동하기**](#2-카카오톡-채널-연동하기)
  - [**3. 콜백 신청하기 (필수)**](#3-콜백-신청하기-필수)
- [네이버 OpenAPI 설정](#네이버-openapi-설정)
  - [네이버 개발자 센터 가입 및 로그인](#네이버-개발자-센터-가입-및-로그인)
    - [네이버 개발자 센터 가입](#네이버-개발자-센터-가입)
  - [어플리케이션 등록](#어플리케이션-등록)
    - [어플리케이션 정보 확인](#어플리케이션-정보-확인)
    - [사용량 확인](#사용량-확인)


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


## 💬  카카오톡 채널 개설하기

---

<aside>
💡 [카카오톡 채널 관리자센터](https://center-pf.kakao.com) 계정이 있으시다면 본 단계는 진행할 필요 없습니다

</aside>

<aside>
💡 카카오톡 채널 생성이 처음이라면 먼저 카카오톡 채널 관리계정을 만들어주세요
🔗 [카카오톡 채널 관리계정 생성 바로가기 (클릭!)](https://accounts.kakao.com/weblogin/create_account/?lang=ko&continue=https%3A%2F%2Fbusiness.kakao.com%2Fdashboard%2F#selectVerifyMethod)

</aside>

### 👤 카카오톡 채널 관리계정 생성

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/0c4cab46-0ec6-4da5-9c40-9340ab541ce6/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/56ce5d4d-6c9e-4645-8739-81c3cf1db2f3/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/3c9c9b68-1352-4878-803e-f8c56bce79ea/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/4873a114-6c1a-4bda-8569-066d4833b065/Untitled.png)

### 🗝️ 카카오톡 관리자센터 로그인

<aside>
💡 **카카오톡 채널을 개설하기 위해서는 카카오톡 채널 관리계정 가입**이 필요합니다.
관리자센터에 가입된 관리계정이 없다면 위 단계에서 관리계정 가입부터 진행해주셔야합니다.

</aside>

1) https://business.kakao.com/info/kakaotalkchannel/ 방문

**2) [로그인]** or **[카카오톡 채널 챗봇 시작하기]** 클릭

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/1d437873-e969-4f4b-a486-4729dfe880a2/Untitled.png)

### 🚀 카카오톡 채널 설정하기

<aside>
💡 내 챗봇과 연결할 카카오톡 채널을 생성합니다.

</aside>

#### 1. **채널 만들기**

- **[+ 새 채널 만들기]**를 클릭해주세요.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/f5f2d214-c12a-4029-ad73-ef5b9e643e0a/Untitled.png)

#### 2. **채널 정보 입력하기**

- 프로필 사진, 채널 이름, 검색용 아이디, 소개글 등을 입력합니다.
- 채널 개설 후 **채널 이름 변경에 제한**이 있기 때문에, 처음 개설 시 신중하게 결정하시는 것이 좋습니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/5b8e41e6-9848-4a8d-b754-5bddcb080666/Untitled.png)

#### 3. **채널 개설 완료**

- 입력한 정보를 확인한 후 버튼을 클릭하면 채널 개설이 완료됩니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/b94f167e-5b53-421d-9b75-e0e646b6c67c/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/f278e744-8038-4ed5-abd3-90e051a0aa97/Untitled.png)

#### 4. **채널 공개 설정하기**

- 대시보드로 이동 후 **채널 공개** 설정을 ON으로 변경합니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/ab4bde28-0864-4c48-9a38-25dcd98db485/Untitled.png)

#### 5. **채널 URL 확인하기**

- 카카오 챗봇을 신청하기 위해서는 채널 URL이 필요합니다.
- **[채널 관리자센터] - [프로필] - [프로필 설정]**에서 확인하실 수 있습니다.

## 🤖  카카오톡 챗봇 생성하기

---

### **1. 새로운 봇 생성하기**

<aside>
💡 로그인 후 [채널] - [챗봇] - [내 챗봇]에서 [+ 봇 만들기] - [카카오톡 챗봇]을 선택하여 카카오톡 챗봇을 생성합니다.

</aside>

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/e58e6701-35fc-4e8e-91f0-fbef68cd0b71/Untitled.png)

### **2. 카카오톡 채널 연동하기**

<aside>
💡 카카오톡 채널 연결은 봇 설정에서 간단하게 할 수 있습니다.

- **[챗봇 관리자센터] - [설정] - [카카오톡 채널 연결] - [운영 채널 연결]**에서 원하는 채널을 선택한 후 **저장(오른쪽 상단 파란버튼)**합니다.
- **[채널 관리자센터] - [1:1채팅] - [채팅설정] 에서 1:1 채팅 사용을 ON**으로 설정하면, 메신저 하단에 상담사 연결  버튼을 표시할 수 있습니다.
</aside>

<aside>
💡 **[참고] 채널 연결이 불가능한 경우**
채널 연결이 불가능하다면, 아래 내용을 확인해주세요.

- **봇은 채널과 1:1 구조**로, 다른 봇에 채널이 연결되어 있을 경우 추가로 연결할 수 없습니다.
- **[채널 관리자센터] - [비즈니스 도구] - [채팅방 메뉴]**에서 채팅방 메뉴 사용이 ON으로 설정되어 있는지 확인해주세요. 
채팅방 메뉴와 챗봇은 동시 사용이 불가능하므로, 채팅방 메뉴 사용을 OFF로 설정해주시면 채널이 챗봇과 연결 가능한 상태로 변경됩니다.
- 챗봇에서는 마스터 권한, 채널에서는 매니저 이상의 권한일 경우에만 연결이 가능합니다.
</aside>

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/e3149efd-786b-410a-a148-be989490ee54/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/d684684a-1148-4b65-a3ff-f5ceb33a1186/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/6c4f6f34-21dd-4474-a785-ac5734a447e3/Untitled.png)

### **3. 콜백 신청하기 (필수)**

<aside>
💡 일반적인 챗봇과 달리 ChatGPT와 같은 언어모델은 응답을 생성하는데 시간이 걸립니다. 따라서 카카오톡 챗봇이 응답이 완료할 때 까지 기다려주도록 별도의 ‘**콜백**’ 기능을 신청해 승인받아야 합니다. AI 챗봇 전환시 콜백기능이 자동 활성화 됩니다.

</aside>

<aside>
💡 챗봇 관리자 센터에서 [설정] - [AI 챗봇 관리] - [AI 챗봇 전환]을 선택하여 신청 목적과 사유를 작성하여 신청합니다.

</aside>

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/9922cf3e-6679-491c-b1f4-ab6601de61f5/Untitled.png)

- 신청 후엔 상태 내용에 심사 중으로 표기됩니다. (1~2일 소요)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/501105f5-bc28-42d5-9bba-dee12725e440/Untitled.png)

- 심사 승인이 완료되면 상태 내용에 ON으로 표기됩니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/af77a7d6-fde2-4058-a60a-0b337d8e5458/a6555e68-dadc-43aa-b736-ee42ed18e7b0/Untitled.png)


## 네이버 OpenAPI 설정

### 네이버 개발자 센터 가입 및 로그인

#### 네이버 개발자 센터 가입
  - <a href="https://developers.naver.com/main/" target="_blank">https://developers.naver.com/main/</a>접속 후 우측 상단의 `로그인`을 클릭해 네이버 아이디로 로그인

![naver_1](https://woensug-choi.github.io/ChatGee/assets/images/naver_1.png)

### 어플리케이션 등록
- 상단의 `Application`에서 `어플리케이션 등록`을 클릭
- 약관동의 -> 계정 정보 등록 (휴대폰 인증) -> 애플리케이션 등록 절차를 완료
- 마지막 등록하기 단계에서 `사용 API`에 `검색`은 필수로 넣어주시고 추가로 함께 신청해두고 싶은 것을 골라넣어주세요. (추후에도 추가 신청 가능)
- `비로그인 오픈 API 서비스 환경` 에서는 `WEB 설정`을 선택하고 `웹 서비스 URL`에 `http://naver.com`을 입력 (아무거나 입력하는 것이므로 상관없습니다. 네이버 로그인을 사용할 경우에만 중요한 내용입니다.)

![naver_2](https://woensug-choi.github.io/ChatGee/assets/images/naver_2.png)

#### 어플리케이션 정보 확인
  - 등록을 완료하시면 어플리케이션 `Client ID`와 `Client Secret`이 발급. 이 정보는 추후에 사용할 예정

![naver_3](https://woensug-choi.github.io/ChatGee/assets/images/naver_3.png)

#### 사용량 확인
  - 어플리케이션 정보 확인 페이지 아래로 스크롤하시면 사용량을 볼수 있는 곳이 있습니다. 검색의 경우 매일 25000건이 무료로 제공

![naver_4](https://woensug-choi.github.io/ChatGee/assets/images/naver_4.png)


<br /><br />

이상 사전준비사항 완료입니다! 수고하셨습니다! 🎉🎉🎉