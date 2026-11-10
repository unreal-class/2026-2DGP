# Drill 8 — pico2d 애니메이션 뷰어

사용자가 제공한 강의 예제의 반복문, `clip_draw()`, `delay(0.05)`를 기준으로 작성했습니다.
외부 라이브러리는 pico2d만 사용합니다. `os`는 이미지 경로 처리를 위한 파이썬 기본 모듈입니다.

## 실행

```powershell
python -m pip install pico2d
python LEC08/animation_viewer.py
```

또는 `run_viewer.bat`를 실행합니다. ESC 또는 창 닫기로 종료합니다.

## 재생 방식

- 수업 자료 `Labs/LEC08_Animation/animation_sheet.png`와 `grass.png`를 사용합니다.
- 시트는 `character.png`와 같은 캐릭터의 좌우 걷기·좌우 달리기, 총 4개 action입니다.
- 각 행은 8프레임이며 `frame * 100`, `action * 100`으로 자를 위치를 정합니다.
- 800 × 600 화면 중앙 `(400, 300)`에서 100 × 100 프레임을 500 × 500으로 확대합니다.
- 각 action은 5회 재생 후 마지막 프레임에서 1초 정지합니다.
- 네 action을 차례대로 무한 반복합니다.
- 프레임 크기와 개수가 일정한 수업용 시트이므로 가변 크기·개수 가산점 구현은 포함하지 않습니다.

이미지는 제공된 수업 자료이며 원본의 권리는 원저작자에게 있습니다.
