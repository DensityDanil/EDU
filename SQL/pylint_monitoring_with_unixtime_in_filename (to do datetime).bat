@echo off
for /f "tokens=1-3 delims=:." %%a in ("%TIME%") do set "time=%%a-%%b-%%c"
for /r %%i in (*.py) do (
    echo %%i >> output_%time%.txt
    pylint %%i >> output_%time%.txt
    echo. >> output_%time%.txt
)
