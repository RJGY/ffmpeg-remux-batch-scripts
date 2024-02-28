cls
@echo off
:: Delete env folder if exists
echo Deleting Dependencies for Hanabi Utilities.

set /p DeleteOldFolders="Do you wish to safely delete the folders? This will not delete folders with files inside of them. Y/N"
if %DeleteOldFolders%==y (echo Deleting folders.) else (goto noDeleteFolder)

if exist ".\Default Output" rmdir ".\Default Output"
if exist ".\Font Conversion" rmdir ".\Font Conversion"
if exist ".\Metadata Removal" rmdir ".\Metadata Removal"
if exist ".\Re-Encoding" rmdir ".\Re-Encoding"
if exist ".\Remuxer" rmdir ".\Remuxer"
if exist ".\Upscaler" rmdir ".\Upscaler"
if exist ".\Video to GIF" rmdir ".\Video to GIF"

pause
goto:eof

:noFiles
echo ERROR^: Dependencies are not installed in your system.
pause
goto:eof

:noDelete
echo User input did not delete files. Exiting.
pause
goto:eof

:noDeleteFolder
echo User input did not delete folders. Exiting.
pause