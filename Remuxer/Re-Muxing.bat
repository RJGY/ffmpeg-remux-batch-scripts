@echo off
title Hanabi ^| Re-Muxing
cls
cd %~dp0
call .\env\Scripts\activate.bat
py ./src/remux.py %*
pause