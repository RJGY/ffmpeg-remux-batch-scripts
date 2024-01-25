:: Run me only once to install python packages needed for the project
:: Check for Python Installation
cls
@echo off
py --version 3>NUL
if errorlevel 0 goto pyInstalled
python --version 3>NUL
if errorlevel 1 goto errorNoPython

:: Install PIP
echo Installing PIP
python -m ensurepip --upgrade

:: Install Python Virtual Environment
echo Installing Python Virtual Environment
python -m pip install virtualenv
python -m venv env

:: Activate Python Virtual Environment
echo Activating Python Virtual Environment
call .\env\Scripts\activate.bat

:: Install Python Packages
echo Installing Python Packages
python -m pip install -r requirements.txt

:: Once done, exit the batch file -- skips executing the errorNoPython section
echo Done
pause
goto:eof

:pyInstalled
:: Python is installed.
py -m pip --version > NUL
if errorlevel 0 goto hasPyPIP

:: Install PIP
echo Installing PIP
py -m ensurepip --upgrade

:hasPyPIP
:: Install Python Virtual Environment
echo Installing Python Virtual Environment
py -m pip install virtualenv
py -m venv env

:: Activate Python Virtual Environment
echo Activating Python Virtual Environment
call .\env\Scripts\activate.bat

:: Install Python Packages
echo Installing Python Packages
py -m pip install -r requirements.txt

:: Once done, exit the batch file -- skips executing the errorNoPython section
echo Done
pause
goto:eof


:: Error
:errorNoPython
echo.
echo Error^: Python not installed
