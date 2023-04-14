#!/bin/bash
echo "꼭 chatGee 폴더 내부에서 실행해주세요"

echo "1. HomeBrew Install"
$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)

echo $(brew --version)

echo "2. 파이썬 3.10.10 설치"
brew install python@3.10.10

echo "3. python pip upgrade"
python3 -m ensurepip --upgrade

echo "4. 파이썬 가상환경 설정 - 오래걸릴 수 있습니다."
pip3 install virtualenv

echo "4-1 파이썬 가상환경을 생성합니다."
python3 -m venv venv_chatgee

echo "4-2 파이썬 가상환경을 실행합니다."
source venv_chatgee/bin/activate

echo "4-3 requirements.txt 기반으로 chatGee 에 필요한 파일을 설치합니다."
pip3 install -r requirements.txt

exit 0

