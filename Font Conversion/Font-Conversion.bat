@echo off
title Hanabi ^| Font-Conversion
cls
cd /D %~dp0
py ./src/font_conversion.py %*
pause