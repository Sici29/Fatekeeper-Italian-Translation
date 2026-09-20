@echo off
setlocal
cd /d "%~dp0"

if exist "Fatekeeper-Italian-Translation.exe" (
  "Fatekeeper-Italian-Translation.exe" restore %*
  pause
  exit /b %ERRORLEVEL%
)

if exist "tools\fatekeeper_it_installer.py" (
  python "tools\fatekeeper_it_installer.py" restore %*
  pause
  exit /b %ERRORLEVEL%
)

echo Eseguibile o script di installazione non trovato.
pause
exit /b 1
