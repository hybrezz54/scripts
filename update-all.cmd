:: Updates all chocolatey and pip packages
choco upgrade all -y
timeout /t 10
python -m pip install --upgrade pip
timeout /t 10


REM FOR /F "tokens=* USEBACKQ" %a in ('pip list --outdated --format=freeze') DO (
REM     SET OUTPUT=%a
REM )
