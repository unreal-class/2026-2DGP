@echo off
setlocal EnableExtensions EnableDelayedExpansion
chcp 65001 >nul

cd /d "%~dp0"

where git >nul 2>nul
if errorlevel 1 (
  echo Git was not found in PATH.
  pause
  exit /b 1
)

git rev-parse --is-inside-work-tree >nul 2>nul
if errorlevel 1 (
  echo This folder is not a Git repository.
  pause
  exit /b 1
)

echo.
echo Recent commits:
git log -5 --pretty=format:"%%h  %%ad  %%s" --date=short
if errorlevel 1 (
  echo Failed to read recent commits.
  pause
  exit /b 1
)
echo.
echo.

for /f "delims=" %%B in ('git branch --show-current') do set "BRANCH=%%B"
if not defined BRANCH (
  echo Could not determine the current branch.
  pause
  exit /b 1
)

set "HAS_CHANGES="
for /f "delims=" %%S in ('git status --porcelain') do set "HAS_CHANGES=1"

if defined HAS_CHANGES goto commit_changes
goto check_push

:commit_changes
echo Changes found.
echo.
echo Files to commit:
git status --short >nul
if errorlevel 1 (
  echo Failed to list files to commit.
  pause
  exit /b 1
)
for /f "tokens=1,*" %%A in ('git -c "core.quotePath=false" status --short') do (
  set "CHANGE_TYPE=[Changed]"
  if "%%A"=="??" set "CHANGE_TYPE=[New File]"
  if "%%A"=="A"  set "CHANGE_TYPE=[New File]"
  if "%%A"=="M"  set "CHANGE_TYPE=[Modified]"
  if "%%A"=="D"  set "CHANGE_TYPE=[Deleted]"
  if "%%A"=="R"  set "CHANGE_TYPE=[Renamed]"
  if "%%A"=="C"  set "CHANGE_TYPE=[Copied]"
  if "%%A"=="U"  set "CHANGE_TYPE=[Conflict]"
  echo   !CHANGE_TYPE! %%B
)
echo.
set /p "COMMIT_MESSAGE=Commit message: "
if not defined COMMIT_MESSAGE (
  echo Commit message is required.
  pause
  exit /b 1
)

git add -A
if errorlevel 1 (
  echo Failed to stage changes.
  pause
  exit /b 1
)

git commit -m "%COMMIT_MESSAGE%"
if errorlevel 1 (
  echo Failed to create commit.
  pause
  exit /b 1
)

:check_push
set "UPSTREAM="
for /f "delims=" %%U in ('git rev-parse --abbrev-ref --symbolic-full-name @{u} 2^>nul') do set "UPSTREAM=%%U"

if not defined UPSTREAM (
  echo No upstream branch found.
  call :select_remote
  if errorlevel 1 (
    pause
    exit /b 1
  )
  echo Pushing and setting upstream to !REMOTE!/%BRANCH%...
  git push -u "!REMOTE!" "%BRANCH%"
  goto finish
)

for /f "tokens=1,2" %%A in ('git rev-list --left-right --count "%UPSTREAM%...HEAD"') do (
  set "BEHIND=%%A"
  set "AHEAD=%%B"
)

if "%AHEAD%"=="0" (
  echo Nothing to push.
  pause
  exit /b 0
)

echo Pushing %AHEAD% commit(s) to %UPSTREAM%...
git push

:finish
if errorlevel 1 (
  echo Push failed.
  pause
  exit /b 1
)

echo Push complete.
pause
exit /b 0

:select_remote
set "REMOTE="
set "REMOTE_COUNT=0"
for /f "delims=" %%R in ('git remote') do (
  set /a REMOTE_COUNT+=1
  set "REMOTE_!REMOTE_COUNT!=%%R"
)

if "%REMOTE_COUNT%"=="0" (
  echo No Git remote found.
  echo Add one first, for example:
  echo   git remote add origin ^<url^>
  exit /b 1
)

if "%REMOTE_COUNT%"=="1" (
  set "REMOTE=!REMOTE_1!"
  echo Using remote !REMOTE!.
  exit /b 0
)

echo Available remotes:
for /l %%I in (1,1,%REMOTE_COUNT%) do echo   %%I. !REMOTE_%%I!
set /p "REMOTE_CHOICE=Select remote [1-%REMOTE_COUNT%]: "

if not defined REMOTE_CHOICE (
  echo Remote selection is required.
  exit /b 1
)

for /f "delims=0123456789" %%C in ("%REMOTE_CHOICE%") do (
  echo Invalid remote selection.
  exit /b 1
)

if %REMOTE_CHOICE% LSS 1 (
  echo Invalid remote selection.
  exit /b 1
)

if %REMOTE_CHOICE% GTR %REMOTE_COUNT% (
  echo Invalid remote selection.
  exit /b 1
)

set "REMOTE=!REMOTE_%REMOTE_CHOICE%!"
echo Using remote !REMOTE!.
exit /b 0
