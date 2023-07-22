---
title: 실전개발 워크숍 필수 준비사항
author: Woen-Sug Choi
date: 2023-07-01
last-modified-at: 2023-07-01
layout: post
exclude: true
---

워크숍 참여를 환영합니다 🥳🎉
본 페이지는 직접 주소를 입력해 접속해야만 보실 수 있습니다!

> **📢 본 내용을 수행해두지 않으면 워크숍 시간 내 학습내용을 완수하기 어렵습니다**
> 
> **문의사항은 '워크숍 참여 멤버 오픈톡방'에서 문의해 주시기 바랍니다**
> - 실전개발 워크숍 참여멤버 오픈톡방 : [접속링크](https://open.kakao.com/o/goF68Ssf) (비밀번호 : `chatgee`)

<br>

## 목차

- [목차](#목차)
- [필요 프로그램 설치](#필요-프로그램-설치)
  - [파이썬 3.10 설치](#파이썬-310-설치)
  - [VSCode 설치](#vscode-설치)
- [카카오톡 플러스 채널 생성](#카카오톡-플러스-채널-생성)
  - [카카오톡 비즈니스 계정 생성](#카카오톡-비즈니스-계정-생성)
  - [카카오톡 채널 생성](#카카오톡-채널-생성)
- [카카오톡 챗봇 계정 생성](#카카오톡-챗봇-계정-생성)
  - [챗봇 관리자센터 오픈베타 참여신청](#챗봇-관리자센터-오픈베타-참여신청)
- [오라클 클라우드 평생무료 인스턴스 설정](#오라클-클라우드-평생무료-인스턴스-설정)
  - [오라클 클라우드 회원가입](#오라클-클라우드-회원가입)
  - [오라클 클라우드 로그인](#오라클-클라우드-로그인)
  - [오라클 클라우드 서버생성](#오라클-클라우드-서버생성)
  - [오라클 클라우드 서버 접속](#오라클-클라우드-서버-접속)
  - [오라클 클라우드 개발환경 설정](#오라클-클라우드-개발환경-설정)
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
  - 리눅스 : Ubuntu 22.04로 설치됬다면 이미 파이썬 3.10이 설치되어 있음
  - 윈도우 : [다운로드 링크](https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe)
    - 📢📢 윈도우 주의사항!! 아래 스크린샷과 같이 아래 `Add python.exe to PATH` 클릭 필수!
    - ADD PATH는 파이썬이 어느곳에서든지 실행되도록 설정하는 내용
  
      <img src="https://woensug-choi.github.io/ChatGee_Doc/assets/images/python1.jpg" style="height:270px;">

- 설치확인
  - 맥 & 리눅스
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

## 카카오톡 플러스 채널 생성

### 카카오톡 비즈니스 계정 생성
카카오 비즈니스 홈페이지에 접속하여 오른 쪽 상단 `로그인` 에서 카카오톡 비즈니스 계정을 생성, 로그인합니다.
- 카카오비즈니스 : <a href="https://business.kakao.com/" target="_blank">https://business.kakao.com/</a>
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

## 카카오톡 챗봇 계정 생성

- `챗봇 관리자센터`에 들어가려면 `OBT (오픈베타)` 신청을 해야합니다. 이 신청을 대게 3~5일 정도 소요되므로 미리 신청해 두시는게 좋습니다. 또한, 개인은 쉽게 승인이 되나 회사계정 또는 비즈니스는 까다로운 서류 절차를 진행해야 하므로 먼저 개인으로 전체적인 챗봇 개발과정을 진행해 보시는 것을 추천드립니다.

### 챗봇 관리자센터 오픈베타 참여신청

- `기업`과 `개인` 중 개인을 선택하고 앞서 생성한 카카오톡 채널의 URL을 입력합니다.
  - `채널 URL`은 `https://pf.kakao.com/_xaxaxaxax`와 같은 형태입니다.
  - `채널 URL`은 `채널 관리자 센터`의 왼쪽 탭들 중 `채널 홍보`에서 확인할 수 있습니다.
- 신청사유는 간단이 기입하셔도 문제 없었습니다.

![fig-9](https://woensug-choi.github.io/ChatGee/assets/images/9.jpg)

- 신청이 완료되면, `챗봇 관리자센터`로 들어가지고 다음과 같은 페이지를 보실 수 있습니다. 여기까지 하시면 워크숍 준비는 끝입니다! 곧 뵙겠습니다!

![fig-8](https://woensug-choi.github.io/ChatGee/assets/images/8.jpg)


## 오라클 클라우드 평생무료 인스턴스 설정

- 서버가 상시구동 되기 위한 온라인 컴퓨터로써 오라클 클라우드를 설정합니다
  - 오라클 클라우드 평생무료
    CPU코어 1개의 클라우드 컴퓨터를 2대까지 무료로 무기한으로 제공

### 오라클 클라우드 회원가입

- Step 1-1 <a href="https://www.oracle.com/kr/cloud/" target="_blank"> 오라클 클라우드 사이트 페이지 https://www.oracle.com/kr/cloud/</a> 에서 로그인 페이지 이동

![Prep_1_1](https://woensug-choi.github.io/ChatGee/assets/images/prep_1_1.png)

- Step 1-2 회원가입 진행

![Prep_1_2](https://woensug-choi.github.io/ChatGee/assets/images/prep_1_2.png)

- Step 1-3 메일주소 확인요청

![Prep_1_3](https://woensug-choi.github.io/ChatGee/assets/images/prep_1_3.png)

- Step 1-4 본인 메일에서 수신메일 검증 버튼 클릭

![Prep_1_4](https://woensug-choi.github.io/ChatGee/assets/images/prep_1_4.png)

- Step 1-5 넘어간 페이지에서,
  - Cloud Account Name : `계정이름`
  - Home Region : 한국(춘천) 서버
  
  - `여기서 설정한 계정이름은 로그인에 사용`!

- Step 1-6 체크박스 모두 동의 후 다음페이지 이동

![Prep_1_5](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_5.png)

- Step 1-7 넘어간 페이지에서,
  - `주소/전화번호 입력` (자세하진 않아도 정확해야 합니다)

![Prep_1_6](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_6.png)

- Step 1-8 다음으로 `신용카드 정보 등록` : 무료서버만 사용할 예정이나, 회원가입엔 신용카드정보가 필요
  - 신용카드 입력 중 문제가 생기면, 뭔가 꼬여서 고객센터 연락하라고 합니다. 이경우, 5분이상 후에 다시 메일에 온 메일인증 버튼 단계부터 다시 시도

![Prep_1_7](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_7.png)

- Step 1-9 신용카드 등록이 완료되면 `동의 체크박스 클릭` 후 회원가입 완료버튼 클릭
  - 자동으로 넘어간 페이지에서 기다리시면 오라클 로그인 페이지로 자동으로 넘어갑니다.

![Prep_1_8](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_8.png)

### 오라클 클라우드 로그인

- Step 2-1 앞서 설정한 `로그인용 계정이름`으로 로그인을 시작합니다.

![Prep_1_9](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_9.png)

- Step 2-2 다음으로 `메일주소`와 `비밀번호`로 최종 로그인합니다.

![Prep_1_10](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_10.png)

- Step 2-3 처음 로그인을 시도하면 `Secure Verification (보안인증)` 설정 페이지가 나타납니다
  - 클라우드 서버 계정을 해킹해 좀비피씨로 몇백~몇천만원어치 사용하는 경우가 빈번히 있었던 시절 이후 대부분 보안인증을 요구합니다.

- Step 2-4 버튼을 눌러 넘어가시면 `QR코드`가 나옵니다.
  - 앱스토어 또는 구글스토어에서 `Oracle Mobile Authenticator` 를 검색해 핸드폰에 설치하고 앱을 실행후 `계정추가(Add Account)`를 진행하면 나타나는 카메라로 QR코드를 인식하면 나오는 보안 OTP 번호로 보안인증을 수행합니다.
  - 완료후 다시 로그인합니다

![Prep_1_11](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_11.png)

- 로그인에 성공하면 다음과 같은 Dashboard 화면이 나옵니다.

![Prep_1_12](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_12.png)


### 오라클 클라우드 서버생성

  - 대쉬보드에서 먼저 오른쪽 위 지구본 버튼으로 한글로 변경합니다.
- 로그인에 후 대쉬보드에서 `인스턴스 컴퓨트`를 클릭해 이동합니다.

![Prep_1_13](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_13.png)


- 인스턴스 컴퓨트 페이지에서 먼저 왼쪽아래 `구획`에서 계정을 선택합니다.
- 그러면 `인스턴스 생성` 버튼이 보입니다. 클릭합니다.

![Prep_1_14](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_14.png)


- `인스턴스 이름`을 설정합니다.

![Prep_1_15](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_15.png)


- `이미지 및 구성` 항목의 `편집`을 클릭합니다.
- 기본 `평생무료` 이미지는 Standard E2.1.Micro라고 하는 일반 CPU의 코어 1개로 되어있습니다. 코어 1개는 아무래도 사용성이 떨어지니 새로 나온 ARM기반의 CPU 4개짜리로 변경하려합니다.
  - 이부분에서, CPU 4개짜리 ARM 인스턴스는 인기가 많아 마지막에 생성이 안되는 경우가 있습니다. 그런경우 다른 시간에 여러번 시도해서 뚫어놓으시면 좋습니다. 정말 안된다면, 기존의 Standard E2.1.Micro로 생성해 주시기 바랍니다. 다음 페이지에 이어서  CPU 4개짜리 ARM 설정방법을 설명합니다.

![Prep_1_15-1](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_15-1.png)

- `Change Shape`을 클릭해 인스턴스의 종류를 변경하는 페이지로 이동합니다.
  
![Prep_1_15-2](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_15-2.png)

- `Ampere` 타입 선택 후 `Standard.A1.Flex`를 체크합니다.

![Prep_1_15-3](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_15-3.png)

- `OCPU 수` 를 4로 설정합니다. 그 이상은 무료가 아닙니다.

![Prep_1_15-4](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_15-4.png)

- 다음으로 네트워킹을 설정합니다. 

![Prep_1_16](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_16.png)
![Prep_1_17](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_17.png)

- 다음으로 인스턴스에 접속하기 위한 `암호키 (전용키, 공용키 모두!)`를 다운받고 인스턴스를 `생성`합니다.

![Prep_1_18](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_18.png)


- 다운받은 암호키는 2개의 파일입니다
  - 전용키 예: `ssh-key-2023-06-08.key`
  - 고용키 예: `ssh-key-2023-06-08.key.pub`

- 로그인 암호가 파일의 형태로 되어있다고 생각하시면 됩니다. `해당 파일들을 분실하시면 만드신 인스턴스에 다시는 접속할 수 없습니다!` 분실하지 않도록 주의하시기 바랍니다!

- 페이지 최하단의 `생성` 버튼을 누르면 인스턴스 상태화면으로 넘어갑니다. `프로비전`(생성 중) 단계를 지나면 왼쪽의 그림 색이 초록색으로 변하며 완료됩니다.

- 여기서 생성한 인스턴스에 접속할 수 있는 `고정아이피`를 확인할 수 있습니다.

![Prep_1_19](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_19.png)

### 오라클 클라우드 서버 접속

- VSCode 실행, 설치하지 않으셨다면 아래 링크에서 다운받아 설치
  - 다운로드 링크 : <a href="https://code.visualstudio.com/download" target="_blank">https://code.visualstudio.com/download</a>

- 실행 후 '왼쪽 탭에서 `테트리스`(익스텐션) 검색 아이콘 클릭 -> `remote` 검색, `Remote-SSH` 설치

![Prep_1_20](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_20.png)

- `Remote-SSH`설치 완료 후 후, 왼쪽 아래 `><`파란버튼 (Remote SSH 연결 버튼) 클릭, `Connect to Host...`선택 후 `Configrure SSH Hosts...` 선택

![Prep_1_21](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_21.png)
![Prep_1_22](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_22.png)

- 제일 상단의 설정파일경로 선택 (운영체제 마다 경로가 상이)해 설정파일 열기
- 본인의 오라클 서버 `아이피주소`, `다운받은 Key 경로` 입력 (`Host oracle` `User opc`는 공통, `저장필수!!`)

![Prep_1_23](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_23.png)
![Prep_1_24](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_24.png)

- 설정파일 저장 후, VSCode 창의 가장 왼쪽 아래 코너의 `><`파란버튼 (Remote SSH 연결 버튼) 클릭, `oracle` 을 클릭하면 오라클 서버에 연결된 새로운 VS Code창이 나타남. 
- 새로 나타난 창에서 상단에 `Terminal` -> `New Terimal` 클릭
  
![Prep_1_25](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_25.png)
![Prep_1_26](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_26.png)

- 최종적으로 나타나는 VSCode 창은 다음과 같은 모습
- 왼쪽 아래에 파란버튼에 `oracle` 확인가능
- 오라클 서버에 접속한 명령어창(Terminal) 확인가능

![Prep_1_27](https://woensug-choi.github.io/ChatGee/assets/images/Prep_1_27.png)

### 오라클 클라우드 개발환경 설정

- 오라클 서버에 접속한 VSCode 상의 명령어창(Terminal)에서 아래 명령어들을 한줄 씩 순차적으로 입력 + Enter

  - 1 : 리눅스 패키지 목록 업데이트
    ```bash
    sudo dnf update -y
    ```

  - 2 : 파이썬 설치에 필요한 패키지 설치
    ```bash
    sudo dnf install -y curl gcc openssl-devel bzip2-devel libffi-devel zlib-devel wget make sqlite-devel 
    ```

  - 3 : 파이썬 소스코드 다운로드
    ```bash
    wget https://www.python.org/ftp/python/3.10.10/Python-3.10.10.tgz
    ```

  - 4 : 파이썬 소스코드 압축해제
    ```bash
    tar -xf Python-3.10.10.tgz
    ```

  - 5 : 파이썬 소스코드 폴더로 이동
    ```bash
    cd Python-3.10.10
    ```

  - 6 : 파이썬 소스코드 설치환경 설정
    ```bash
    ./configure --enable-optimizations --enable-loadable-sqlite-extensions
    ```

  - 7 : CPU4개를 이용해 컴파일 (약 10분 소요됩니다), 코어가 한개라면 마지막 숫자를 `1`로 변경
    ```bash
    make -j 4
    ```

  - 8 : 컴파일한 파이썬을 설치
    ```bash
    sudo make altinstall
    ```

  - 9 : 설치된 파이썬 버전 확인 (Python 3.10.10 으로 나오면 성공입니다.)
    ```bash
    python3.10 --version
    ```

  - 10 : 홈 폴더로 이동
    ```bash
    cd
    ```

  - 11 : 파이썬 소스코드 다운로드파일 삭제
    ```bash
    rm Python-3.10.10.tgz
    ```

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