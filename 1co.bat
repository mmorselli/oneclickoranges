@echo off
cd /d %~dp0

IF NOT EXIST .\1co\Configs\.env (
    echo Please put your .env file in .\1co\Configs\.env
    PAUSE
    EXIT /B
)


REM uncomment the two line below to debug
REM .\1co\Python\python.exe .\1co\App\main.py
REM PAUSE

START "" .\1co\Python\pythonw.exe .\1co\App\main.py