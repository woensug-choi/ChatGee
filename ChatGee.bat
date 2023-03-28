@echo off
echo.
echo.
echo ========== ChatGee AI Chatbot ==========

@REM ------- Install Python if not installed

where python3.10 > nul 2>&1

if %errorlevel% equ 0 (
    python -c "import platform; assert platform.python_version() == '3.10.10', 'Unexpected Python version'"
    echo.
    echo Python 3.10.10 Installation Confirmed !
) else (
    echo.
    echo Pyton 3.10.10 is not installed!. Please install with python-3.10.10.exe
)

@REM ----- Create Virtual Env For ChatGee

where pip > nul 2>&1

if %errorlevel% equ 0 (
    goto :pip_installed
) else (
    python -m ensurepip --upgrade > nul 2>&1
)

:pip_installed
echo.
echo Initiate Virtual Environment for ChatGee
python -m pip install --upgrade pip > nul 2>&1
pip install virtualenv > nul 2>&1
python -m venv venv_chatgee > nul 2>&1
call venv_chatgee\Scripts\activate.bat > nul 2>&1

@REM ----- Install ChatGee
echo.
echo ========== ChatGee AI Chatbot ==========
echo.
echo ========= Virtual Environment ==========
echo.
echo (1/4) Install ChatGee Library
pip install -r requirements.txt > nul 2>&1

@REM ---- RUN SERVEO TUNNEL
echo.
echo (2/4) Run ChatGee Server
start /b python chatgee/run_server.py > nul 2>&1

@REM ----- Read Port Number from settings.yaml file
echo.
echo (3/4) Reading settings.yaml file...
for /f "tokens=* USEBACKQ" %%F in (`.\yq.exe eval ".SERVER.PORT_NUMBER" settings.yaml`) do (
  set "port_number=%%F"
)

echo.
echo (4/4) Run Localhost.run Tunnel

setlocal enabledelayedexpansion

set "tempFile1=%TEMP%\tunnel_output_temp.txt"
set "tempFile2=tunnel_output.txt"

taskkill /im ssh.exe /f >nul 2>&1
start /b /min cmd /c "ssh -o StrictHostKeyChecking=no -R 80:127.0.0.1:%port_number% nokey@localhost.run > %tempFile1% 2>&1"

:wait_output
timeout /t 5 /nobreak >nul
if not exist %tempFile1% goto wait_output
copy %tempFile1% %tempFile2% >nul 2>&1

:parse_output
set "serveo_addr="
for /f "tokens=1,2,3" %%a in ('type %tempFile2% ^| findstr "tunneled with tls termination"') do (
    set "serveo_addr=https://%%a"
    goto serveo_found
)

:serveo_found
if not defined serveo_addr (
  timeout /t 5 /nobreak >nul
  goto parse_output
) else (
  echo.
  echo ===========    SUCCESS !!   ============
  echo.
  echo The ChatGee Server Address : %serveo_addr%
  echo The ChatGee Prompt Skill : %serveo_addr%/prompt
  echo.
  echo To test at local machine,
  echo Goto %serveo_addr%/local_test
  echo Or http://localhost:%port_number%/local_test
  echo.
  echo If none of above works, it could be firewall problem
  echo.
  echo Change settings.yaml for system prompts and other settings.
)

pause