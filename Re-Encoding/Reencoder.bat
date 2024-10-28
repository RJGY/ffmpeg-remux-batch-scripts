@echo off
title Hanabi ^| Re-Encoder
cls
cd /D %~dp0
py ./src/reencoder.py %*
pause