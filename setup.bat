@echo off
setlocal enabledelayedexpansion

for %%F in (app.py) do set "app_path=%%~dpF"

set "install_path=%ProgramFiles%\TaskCreator"

mkdir "!install_path!" > nul 2>&1

copy "!app_path!app.py" "!install_path!" > nul

set "task_creator_bat_path=!install_path!\TaskCreator.bat"
echo @echo off > "!task_creator_bat_path!" > nul
echo python "!app_path!app.py" %%* >> "!task_creator_bat_path!" > nul

set "new_path=!install_path!;%PATH%"
setx PATH "!new_path!" /M > nul 2>&1

echo Setup completed. Run 'taskcreator' in CMD or PowerShell to start the application.
pause

endlocal
