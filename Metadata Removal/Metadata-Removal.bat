@echo off
title Hanabi ^| Metadata-Removal
cls
cd /D %~dp0
py ./src/metadata_removal.py %*
pause