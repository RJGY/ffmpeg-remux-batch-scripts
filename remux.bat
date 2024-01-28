@echo off
title Hanabi ^| Remuxer
cls
cd %~dp0
call .\env\Scripts\activate.bat
py ./src/remux.py %*
pause