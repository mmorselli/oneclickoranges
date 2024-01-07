@echo off
cd /d %~dp0\1co



powershell.exe -ExecutionPolicy Bypass -File .\scripts\install-python.ps1

PAUSE