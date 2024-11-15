@echo off
rem Batch script to open FakerSmith Identity Generator

set SCRIPT_PATH="fakersmith.py"

if exist %SCRIPT_PATH% (
    echo Starting FakerSmith Identity Generator...
    python %SCRIPT_PATH%
) else (
    echo Error: Could not find FakerSmith script in the current directory.
    pause
)

pause
