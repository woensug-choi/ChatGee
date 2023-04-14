#!/bin/bash
echo "chatGee 시작 시 start 종료시 end 를 입력해주세요."
echo "localhost.run 을 통해 주소를 발급받습니다. 발급된 주소를 running_log.out 에서 확인해주세요."
if [ -f localhost_run.pid ]; then
    kill -9 `cat localhost_run.pid`
else
    nohup ssh -o StrictHostKeyChecking=no -R 80:localhost:6959 nokey@localhost.run > localhost_run_log.out 2>&1 & echo $! > localhost_run.pid
fi

echo "챗지 프로세스를 시작하겠습니다"
if [ "$1" = "start" ]; then
    if [ -f chatgee.pid ]; then
        kill -9 `cat chatgee.pid`
    else
        echo "챗지를 시작하겠습니다."
        nohup python3 ./chatgee/run_server.py > running_log.out 2>&1 & echo $! > chatgee.pid
    fi
else
    if [ -f chatgee.pid ]; then
        kill -9 `cat chatgee.pid`
        echo "챗지를 종료했습니다."
    fi
fi