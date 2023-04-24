#!/bin/zsh

cleanup(){
    kill -9 `ps -ef | grep ' chatgee/run_server.py' | grep -v grep | awk '{print $2}'`
}

trap cleanup INT TERM

find_python(){
    for python in `which python3.10`
    do
        if [[ ! -f "$python" ]]; then continue; fi
        var=`$python -c 'import sys;print(sys.version_info.minor==10)' 2>&1`
        if [[ 'True' == $var  ]]
        then
            echo $python
            break
        fi
    done
    echo ""
}
check_python(){
    if [[ '' == $1  ]]
    then
        echo 
        echo Pyton 3.10 is not installed !
        exit 1
    else
        echo 
        echo Python 3.10 Installation Confirmed !
    fi
}
ngrok_yaml_path(){
   echo "/Users/"$USER"/Library/Application Support/ngrok/ngrok.yml"
}
check_ngrok(){
   if [[ -f "ngrok" ]]; then
       return 1
   fi
   arch=`uname -m`
   if [[ $arch != "arm64" ]]; then arch="amd64"; fi
   zip="ngrok-v3-stable-darwin-"$arch".zip"
   url="https://bin.equinox.io/c/bNyj1mQVY4c/"$zip

   echo "========== Downloading ngrok =========="
   curl -O $url
   unzip $zip 
}
check_token_and_api(){
    if [[ $1 == "YOUR_OPEN_AI_API_KEY" ]]; then
        echo ""
        echo "You should input OPEN_API \"API_KEY\" in settings.yaml"
        exit 1
    fi
    if [[ $2 == "YOUR_NGROK_TOKEN" ]]; then
        echo ""
        echo "You should input NGROK \"TOKEN\" in settings.yaml"
        exit 1
    fi
}

echo 
echo 
echo "========== ChatGee AI Chatbot =========="

if [[ ! -f "venv_chatgee/bin/activate" ]]; then
    python=$(find_python)
    check_python $python

    basename=$python:h
    pip=$basename/pip3.10

    if [[ `which $pip` == $pip ]]
    then
        echo pip3 Installation Confirmed !
    else
        $python -m ensurepip --upgrade > /dev/null 2>&1
    fi

    echo 
    echo "Initiate Virtual Environment for ChatGee"
    $python -m pip install --upgrade pip  > /dev/null 2>&1
    $pip install virtualenv > /dev/null 2>&1
    $python -m venv venv_chatgee > /dev/null 2>&1
fi

source venv_chatgee/bin/activate

check_ngrok

echo
echo "========= Virtual Environment =========="
echo
echo "(1/4) Install ChatGee Library"
# 가상환경을 source 했으니 경로가 상관이 없어졌다.
pip install -r requirements.txt > /dev/null 2>&1

open_api_key=`python -c "import yaml; stream=open('settings.yaml', 'r'); print(yaml.load(stream,yaml.FullLoader)['OPEN_AI']['API_KEY'])"`
ngrok_token=`python -c "import yaml; stream=open('settings.yaml', 'r'); print(yaml.load(stream,yaml.FullLoader)['NGROK']['TOKEN'])"`
check_token_and_api $open_api_key $ngrok_token

echo
echo "(2/4) Run ChatGee Server"
python chatgee/run_server.py > /dev/null 2>&1  &

echo
echo "(3/4) Reading settings.yaml file..."
port_number=`python -c "import yaml; stream=open('settings.yaml', 'r'); print(yaml.load(stream,yaml.FullLoader)['SERVER']['PORT_NUMBER'])"`

echo
echo "(4/4) Run ngrok"

./ngrok config add-authtoken $ngrok_token
./ngrok http $port_number

wait
