@echo off
setlocal enabledelayedexpansion

where python > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b 1
)

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo You need administrator permissions to run this script.
    pause
    exit /b 1
)

for %%F in (app.py) do set "app_path=%%~dpF"

set "install_path=%UserProfile%\AppData\Local\Programs\TaskCreator"

mkdir "!install_path!" > nul 2>&1
if %errorlevel% neq 0 (
    echo Failed to create the installation folder. Check permissions.
    pause
    exit /b 1
)

copy "!app_path!app.py" "!install_path!" > nul
if %errorlevel% neq 0 (
    echo Failed to copy the 'app.py' file to the installation folder.
    pause
    exit /b 1
)

set "task_creator_bat_path=!install_path!\TaskCreator.bat"

(
    echo @echo off
    echo python "!app_path!app.py" %%*
) > "!task_creator_bat_path!"

set "new_path=!install_path!;%PATH%"
setx PATH "!new_path!" /M > nul 2>&1
if %errorlevel% neq 0 (
    echo Failed to update the PATH environment variable. Check permissions.
    pause
    exit /b 1
)

echo Setup completed. You can now run 'taskcreator' in CMD or PowerShell to start the application.
pause

endlocal
