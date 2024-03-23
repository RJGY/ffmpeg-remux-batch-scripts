@echo off
title Hanabi ^| Re-Muxing
cls
cd /D %~dp0
py ./src/remux.py %*
pause