@echo off
title Hanabi ^| Re-Muxing
cls
cd %~dp0
py ./src/remux.py %*
pause