@echo off
title Hanabi ^| Upscaler
cls
cd /D %~dp0
py ./src/upscaler.py %*
pause