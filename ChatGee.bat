@echo off
echo.
echo.
echo ========== ChatGee AI Chatbot ==========

@REM ------- Install Python if not installed

if exist venv_chatgee\Scripts\activate.bat (
  goto :source_activate
) 

call:find_python 
call:check_python_exist
if "%python%" == "" (
    pause
    EXIT /B 0
)

call:find_pip

if "%pip_bin%" == "" (
  %python% -m ensurepip --upgrade > nul 2>&1
) else (
  echo pip3 Installation Confirmed !
  goto :init_venv
)

call:find_pip

:init_venv
echo.
echo Initiate Virtual Environment for ChatGee
%python% -m pip install --upgrade pip > nul 2>&1
%pip_bin% install virtualenv > nul 2>&1
%python% -m venv venv_chatgee > nul 2>&1

:source_activate
call venv_chatgee\Scripts\activate.bat > nul 2>&1

call :check_ngrok

@REM ----- Install ChatGee
echo.
echo ========= Virtual Environment ==========
echo.
echo (1/4) Install ChatGee Library
pip install -r requirements.txt > nul 2>&1

for /f "tokens=* USEBACKQ" %%F in (`.\yq.exe eval ".OPEN_AI.API_KEY" settings.yaml`) do (
  set "open_api_key=%%F"
)
for /f "tokens=* USEBACKQ" %%F in (`.\yq.exe eval ".NGROK.TOKEN" settings.yaml`) do (
  set "ngrok_token=%%F"
)

if "%open_api_key%" == "YOUR_OPEN_AI_API_KEY" (
  echo You should input OPEN_API "API_KEY" in settings.yaml
  pause
  EXIT /B 0
)
if "%ngrok_token%" == "YOUR_OPEN_AI_API_KEY" (
  echo You should input NGROK "TOKEN" in settings.yaml
  pause
  EXIT /B 0
)

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
echo "(4/4) Run ngrok"
.\ngrok.exe config add-authtoken %ngrok_token%
.\ngrok.exe http %port_number%

pause
goto :eof

:find_python
set "python="
for /f "tokens=* USEBACKQ" %%F in (`where python`) do (
  for /f "tokens=* USEBACKQ" %%G in (`%%F -c "import sys;print(sys.version_info.minor==10, end='')" 2^>^&1`) do (
    if "%%G" == "True" (
      set "python=%%F"
      goto :break0
    )
  )
)
:break0
EXIT /B 0
:check_python_exist
if "%python%" == "" (
  echo.
  echo Pyton 3.10 is not installed!. Please install with python-3.10.10.exe
) else (
  echo.
  echo Python 3.10 Installation Confirmed !
)
EXIT /B 0
:find_pip
set "pip_bin="
for %%F in (%python%) do set dirname=%%~dpF
for /f "tokens=* USEBACKQ" %%F in (`where pip`) do (
  echo %%F | findstr %dirname% >nul
  if not errorlevel 1 (
    set "pip_bin=%%F"
    goto :break1
  )
)
:break1
EXIT /B 0

:check_ngrok
if not exist ngrok.exe (
  echo ========== Downloading ngrok ==========
  curl -o ngrok-v3-stable-windows-amd64.zip https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip
  tar -xf .\ngrok-v3-stable-windows-amd64.zip
)
EXIT /B 0