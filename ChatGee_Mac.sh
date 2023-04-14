#!/bin/zsh

cleanup(){
    kill -9 `ps -ef | grep ' chatgee/run_server.py' | grep -v grep | awk '{print $2}'`
}

trap cleanup INT TERM

echo 
echo 
echo "========== ChatGee AI Chatbot =========="

for python in `where python3.10`
do
    var=`$python --version 2>&1`
    parts=(${(@s:.:)var})
    if [[ '10' == $parts[2]  ]]
    then
        break
    fi
    python=''
done
if [[ '' == $python  ]]
then
    echo 
    echo Pyton 3.10 is not installed!.
    exit 1
else
    echo 
    echo Python 3.10 Installation Confirmed !
fi

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
source venv_chatgee/bin/activate

echo
echo "========== ChatGee AI Chatbot =========="
echo
echo "========= Virtual Environment =========="
echo
echo "(1/4) Install ChatGee Library"
# 가상환경을 source 했으니 경로가 상관이 없어졌다.
pip install -r requirements.txt > /dev/null 2>&1

echo
echo "(2/4) Run ChatGee Server"
python chatgee/run_server.py > /dev/null 2>&1  &

echo
echo "(3/4) Reading settings.yaml file..."
port_number=`python -c "import yaml; stream=open('settings.yaml', 'r'); print(yaml.load(stream,yaml.FullLoader)['SERVER']['PORT_NUMBER'])"`

echo
echo "(4/4) Run Localhost.run Tunnel"
ssh -o StrictHostKeyChecking=no -R 80:127.0.0.1:$port_number nokey@localhost.run

wait
