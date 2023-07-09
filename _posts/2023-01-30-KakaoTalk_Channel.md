---
title: 카카오톡 채널 설정
author: Woen-Sug Choi
date: 2023-03-28
last-modified-at: 2023-04-23
layout: post
---



# 카카오톡 채널 신설 및 챗봇 등록 매뉴얼

두 단계를 통해 챗지 서버와 카카오톡 채널을 연동합니다.

- [카카오톡 채널 신설 및 챗봇 등록 매뉴얼](#카카오톡-채널-신설-및-챗봇-등록-매뉴얼)
  - [플러스 채널 생성](#플러스-채널-생성)
    - [카카오톡 비즈니스 계정 생성](#카카오톡-비즈니스-계정-생성)
    - [카카오톡 채널 생성](#카카오톡-채널-생성)
  - [챗봇 계정 생성](#챗봇-계정-생성)
    - [챗봇 관리자센터 오픈베타 참여신청](#챗봇-관리자센터-오픈베타-참여신청)
    - [챗봇 생성](#챗봇-생성)
    - [스킬 생성](#스킬-생성)
    - [시나리오 설정](#시나리오-설정)
    - [채널 연결](#채널-연결)
    - [제너릭 메뉴 설정](#제너릭-메뉴-설정)
    - [챗봇 배포](#챗봇-배포)
    - [콜백응답 설정](#콜백응답-설정)

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
![fig-8](https://woensug-choi.github.io/ChatGee/assets/images/8.jpg)

### 챗봇 생성

- 오픈베타에 승인되고 나면, `챗봇 관리자센터`로 들어가서 오른쪽 상단의 `+ 봇 만들기`를 클릭합니다.
  - `카카오톡 챗봇`과 `보이스 챗봇` 중 `카카오톡 챗봇`을 클릭합니다.
  - 챗봇 이름을 입력합니다. 언제든지 수정 가능한 이름입니다.

![fig-11](https://woensug-choi.github.io/ChatGee/assets/images/11.jpg)

### 스킬 생성

- 새로운 챗봇을 생성한 후 먼저 왼쪽 탭에서 `스킬`을 설정합니다.
  - `스킬`은 카카오톡과 챗지 서버가 서로 통신하도록 다리를 이어줍니다.

![fig-14](https://woensug-choi.github.io/ChatGee/assets/images/14.jpg)

- `스킬` 설정 화면에서 오른쪽 상단 `생성` 버튼을 클릭합니다.
  - 상단 `뒤로가기` 버튼 옆에 스킬 이름, 중간에 설명을 추가합니다.
  - `URL`부분에 챗지 서버를 구동 했을때 나타났던, `https://복잡한-숫자-주소.ngrok-free.app/prompt` 를 입력합니다. 이때, 끝에 `/prompt`가 있는 것을 주의해 주시기 바랍니다.
  - `스킬`을 통해 챗지 서버와 정상적인 통신이 되는지 `스킬 테스트`를 통해 확인합니다.
    - 요청할 파라메터에 `prompt`를 입력하고 `안녕안녕`이라는 예시를 입력후, `스킬서버로 전송`을 클릭해 통신을 시도해봅니다.
    - 응답이 정상적으로 오지 않는다면 먼저,
      - 챗지 서버가 살아있는지 확인합니다. `https://복잡한-숫자-주소.ngrok-free.app/local_test` 에 다시 접속해봅니다.
      - 서버가 꺼져 있거나 다른 문제가 있다면, 다시 서버를 구동해야 합니다.
      - 검정 `cmd` 창을 종료하고 다시 `ChatGee`를 실행해 새로운 `https://복잡한-숫자-주소.ngrok-free.app/prompt` 를 발급받습니다.
  - 입력을 완료했으면 오른쪽 상단의 `저장`을 클릭해 저장합니다.
  
![fig-16](https://woensug-choi.github.io/ChatGee/assets/images/16.jpg)
![fig-check](https://woensug-choi.github.io/ChatGee/assets/images/check.jpg)

### 시나리오 설정

- `스킬`을 설정했으면, 다시 왼쪽 탭에서 `시나리오`을 설정합니다.
  - 시나리오에서 `폴백 블록`을 선택합니다.
  - 시나리오 설정에서 사용할 변수를 활성화하기 위해 오른쪽 상단의 `봇 테스트` 왼쪽의 `"엔티티`를 클릭하고 위 탭에서 `시스템 엔티티` 그중 아래에서 `@sys.text`를 활성화합니다.

![fig-12](https://woensug-choi.github.io/ChatGee/assets/images/12.jpg)
![fig-13](https://woensug-choi.github.io/ChatGee/assets/images/13.jpg)

- `폴백 블록`의 일반 파라메터를 설정합니다.
  - 파라메터 설정에서 일반 파라메터를 추가하는 `+` 버튼을 누르고, 아래와 같이 `prompt` 파라메터를 설정합니다.
    - 파라메터명에 `prompt`, 엔티티는 `sys.text`를 선택, `값`에는 `$prompt`를 입력합니다. 여기서 `$`는 달러 표시 입니다.

![fig-17](https://woensug-choi.github.io/ChatGee/assets/images/17.jpg)
![fig-18](https://woensug-choi.github.io/ChatGee/assets/images/18.jpg)
![fig-21](https://woensug-choi.github.io/ChatGee/assets/images/21.jpg)

- 일반 봇 응답 모두 삭제 후 `스킬`응답으로 설정
  - 파라메터 설정의 오른쪽 `스킬 검색/선택`에서 이전에 생성한 `스킬`을 선택합니다.
  - 폴백 블록의 아래 봇 응답에서 일반 봇 응답을 모두 지우고 챗지의 응답오류 메세지를 하나만 입력합니다.
  - 그리고, 제일 마지막의 응답추가에서 `스킬데이터` 응답으로 설정합니다.

![fig-18](https://woensug-choi.github.io/ChatGee/assets/images/18.jpg)
![fig-19](https://woensug-choi.github.io/ChatGee/assets/images/19.jpg)
![fig-20](https://woensug-choi.github.io/ChatGee/assets/images/20.jpg)

### 채널 연결

- 챗봇을 플러스 채널과 연결
  - 챗봇의 왼쪽 탭 중 `설정`에서 `카카오톡 채널 연결`에 이전에 생성한 플러스 채널을 연결합니다.

![fig-22](https://woensug-choi.github.io/ChatGee/assets/images/22.jpg)
![fig-23](https://woensug-choi.github.io/ChatGee/assets/images/23.jpg)

### 제너릭 메뉴 설정

- 제너릭 메뉴 설정
  - `📓 사용설명서` 및 `💫 새로운 시작`은 시나리오에서 설정 가능합니다.
  - 시나리오 설정 화면에서 `+ 시나리오` 버튼 아래 회색으로 작게 `시나리오 설정`이 있습니다. 여기를 누르시면 다음과 같은 화면이 나옵니다.
  - 여기서 봇 제너릭 메뉴 설정을 활성화 하고 메뉴를 설정합니다.
  
![fig-generic-menu](https://woensug-choi.github.io/ChatGee/assets/images/generic_menu.jpg)
![fig-generic-menu-addbutton](https://woensug-choi.github.io/ChatGee/assets/images/generic_menu_addButton.jpg)

### 챗봇 배포

- 이제 모든 설정이 끝났습니다! 마지막으로 챗봇을 `배포`합니다.
  - 왼쪽 탭의 `배포`에서 오른쪽 상단 `배포` 버튼을 클릭합니다.
  - 설정된 값이 `배포`됩니다. 이제 앞서 만든 플러스 채널에서 카카오톡에서 챗지와 대화가 가능합니다!
    - 접속 주소는 `카카오톡 채널 관리자센터`에서 왼쪽 탭 중 `채널 홍보` 탭에서 확인가능합니다.
  - 챗지 서버에서 띄운 검정 `cmd`창을 종료하거나 재시작하면 `스킬`서버의 주소(`https://이상한영문.lhr.life/prompt`)가 변경됩니다.
    - 변경된 경우 다시 챗봇의 `스킬`에서 주소를 변경하고, 꼭!! 다시 배포해 주셔야 다시 작동합니다.

![fig-deploy](https://woensug-choi.github.io/ChatGee/assets/images/deploy.jpg)
![fig-deploy-done](https://woensug-choi.github.io/ChatGee/assets/images/deploy_done.jpg)


### 콜백응답 설정

- 카카오톡 서버의 5초 내 응답 제한
  - 카카오톡 서버는 5초안에 챗지서버가 응답을 하지 않으면 연결을 끊어버립니다.
  - 기본적인 챗지서버의 설정은 응답이 지연되면 `생각 다했니?`를 응답해 사용자가 백그라운드에서 저장된 응답을 받을 수 있도록 구성되어 있습니다.
- 카카오톡 콜백응답 기능
  - 5초 이후에 응답을 보내는 기능이 `콜백응답`기능입니다. 해당 기능은 카카오톡측에 직접 메일을 보내 승인을 받아야 합니다.
  - 숨겨진 Callback API 문서 : <a href="https://i.kakao.com/docs/skill-callback-dev-guide" target="_blank">https://i.kakao.com/docs/skill-callback-dev-guide</a>
  > Callback API 사용을 위해서는 챗봇관리자센터에 등록된 챗봇을 AI 챗봇으로 전환해야 합니다. 전환을 원하시는 경우, 이메일을 통해서 전환 신청 해주시기 바랍니다.
  > - botbiz@kakaocorp.com
  > - 제목과 간단한 서비스 소개
  > - 봇ID
  - 승인에 추가적으로 몇일이 소요되며, 승인 후 콜백기능을 설정할 수 있습니다.

- 콜백 승인 후 `챗봇 관리자센터`의 `시나리오`의 `폴백플롯`에서 우상단의 `초기화`버튼 옆 ...버튼에 `Callback 설정`이 옵션이 생성되어 있습니다. 여기서 On으로 설정 후 저장하고 배포하시면됩니다. Callback 기능은 최근에 추가된 기능이어서 `챗봇 관리자센터`에서 테스트가 불가능하고 배포 후 직접 카카오톡을 통해서만 구동 가능합니다.

![callback-setting](https://woensug-choi.github.io/ChatGee/assets/images/callback-setting-option.jpg)