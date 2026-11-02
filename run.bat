@echo off
title Gemini Watermark Remover
echo ========================================================
echo   Gemini Watermark Remover (100%% Local ^& Private)
echo ========================================================
echo.
echo Starting local web server on port 8080...
echo Opening in your default browser...
echo.

start "" http://localhost:8080
python -m http.server 8080

pause
