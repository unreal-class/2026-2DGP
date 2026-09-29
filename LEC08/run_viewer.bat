@echo off
cd /d "%~dp0"
python animation_viewer.py
if errorlevel 1 pause
