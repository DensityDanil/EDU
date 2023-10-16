for /r %i in (*.py) do (
    echo %i >> output.txt
    pylint %i >> output.txt
    echo. >> output.txt
)
