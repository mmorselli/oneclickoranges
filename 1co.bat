@echo off
cd /d %~dp0

REM uncomment the two line below to debug
REM .\1co\Python\python.exe .\1co\App\gui.py
REM PAUSE

START "" .\1co\Python\pythonw.exe .\1co\App\gui.py

