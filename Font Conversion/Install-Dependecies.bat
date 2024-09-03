@echo off

:: Install FontTools using pip
pip install fonttools

:: Check if installation was successful
if %errorlevel%==0 (
  echo FontTools installed successfully!
) else (
  echo Error installing FontTools: %errorlevel%
)

:: Install Brotli using pip
pip install brotli

if if %errorlevel%==0 (
  echo Brotli installed successfully!
) else (
  echo Error installing Brotli: %errorlevel%
)

pause