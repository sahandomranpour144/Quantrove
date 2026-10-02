@echo off
setlocal
cd /d "%~dp0"
powershell -ExecutionPolicy Bypass -File "%~dp0sync-company.ps1" %*
if errorlevel 1 (
    echo.
    echo Synchronization encountered an issue.
    pause
)
