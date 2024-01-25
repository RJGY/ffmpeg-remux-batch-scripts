@echo off
title Remuxer
cls
cd %~dp0
call .\env\Scripts\activate.bat
python ./main.py %*
pause