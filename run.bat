@echo off
setlocal ENABLEDELAYEDEXPANSION

REM Change to the directory of this script
cd /d "%~dp0"

REM Ensure Node.js exists
where node >nul 2>nul
if errorlevel 1 (
  echo Node.js is not installed or not in PATH.
  echo Please install Node.js from https://nodejs.org/ and try again.
  pause
  exit /b 1
)

REM Install dependencies if node_modules is missing
if not exist node_modules (
  echo Installing dependencies...
  call npm install
  if errorlevel 1 (
    echo Failed to install dependencies.
    pause
    exit /b 1
  )
)

REM Optional: set a default PORT if not provided
if "%PORT%"=="" set PORT=3000

echo Starting server on port %PORT% ...
echo (Close this window to stop the server)

node server.js

echo.
echo Server stopped.
pause



