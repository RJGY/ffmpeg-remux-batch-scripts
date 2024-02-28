:: Run me only once to install python packages needed for the project
:: Check for Python Installation
cls
@echo off
:: Create Folders
echo Creating folders
if not exist ".\Default Output" mkdir ".\Default Output"
if not exist ".\Font Conversion" mkdir ".\Font Conversion"
if not exist ".\Metadata Removal" mkdir ".\Metadata Removal"
if not exist ".\Re-Encoding" mkdir ".\Re-Encoding"
if not exist ".\Remuxer" mkdir ".\Remuxer"
if not exist ".\Upscaler" mkdir ".\Upscaler"
if not exist ".\Video to GIF" mkdir ".\Video to GIF"

py --version 3>NUL
if errorlevel 0 goto pyInstalled
python --version 3>NUL
if errorlevel 1 goto errorNoPython

:pyInstalled
ffmpeg -version 3>NUL
if errorlevel 1 goto noFfmpeg
:: Once done, exit the batch file -- skips executing the errorNoPython section
echo Done.
pause
goto:eof

:: Error
:noFfmpeg
echo.
echo ERROR^: FFmpeg not installed.
pause
goto:eof

:: Error
:errorNoPython
echo.
echo ERROR^: Python not installed.
pause