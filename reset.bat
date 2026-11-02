@echo off
chcp 65001 >nul
echo.
echo === 변경/추가된 파일 목록 ===
git status --short
echo.

set /p confirm=진짜로 리셋하겠습니까? 커밋되지 않은 모든 변경사항이 삭제됩니다. (y/N): 

if /i "%confirm%"=="y" (
    git reset --hard HEAD
    git clean -fd
    echo.
    echo 리셋 완료: 최신 커밋 상태로 되돌렸습니다.
) else (
    echo.
    echo 취소되었습니다.
)

pause