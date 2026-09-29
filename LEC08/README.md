# Drill 8 — Character animation viewer

수업 자료의 `character.png`를 사용한 pico2d 애니메이션 뷰어입니다.
걷기, 달리기, 점프, 공격을 화면 중앙에서 순서대로 재생합니다.

## 실행

저장소 루트에서:

```powershell
python -m pip install -r LEC08/requirements.txt
python LEC08/animation_viewer.py
```

Windows에서는 `run_viewer.bat`를 더블클릭해도 됩니다.
종료: Escape 또는 창 닫기. 자동 재생 중 정지 구간에도 종료할 수 있습니다.
이미지 경로는 소스 파일 위치를 기준으로 하므로 다른 작업 폴더에서도 실행됩니다.

## 구현 내용 및 가산점 설명

| 동작 | 프레임 수 | 초당 프레임 |
| --- | ---: | ---: |
| 걷기 | 8 | 10 |
| 달리기 | 6 | 14 |
| 점프 | 10 | 12 |
| 공격 | 7 | 12 |

- 각 동작을 정확히 5회 재생한 후 **마지막 프레임에서 1초 정지**하고 다음 동작으로 넘어갑니다.
- 공격 다음에는 걷기로 돌아가며 사용자가 종료할 때까지 무한 반복합니다.
- 실제 경과 시간으로 프레임을 선택해 컴퓨터의 렌더링 속도와 재생 속도를 분리했습니다.
- 960 × 720 창 중앙에 표시하며 가장 작은 포즈도 화면 높이의 절반 이상입니다.
- **서로 다른 프레임 수 지원:** 메타데이터의 동작별 프레임 목록 길이를 사용합니다.
- **서로 다른 프레임 크기 지원:** 투명 여백을 제거한 가변 크기 스프라이트를 패킹하고,
  각 프레임의 사각형과 원래 위치 오프셋을 사용해 재생합니다. 단순한 고정 셀 나누기가 아닙니다.
- 원본 `character.png`는 단일 자세이므로 부위 분리와 회전으로 만든 컷아웃 방식입니다.
  손으로 다시 그린 자연스러운 관절 애니메이션과는 표현상의 차이가 있습니다.

## 재생성 및 검증

완성된 시트와 메타데이터를 포함하므로 일반 실행에는 재생성이 필요 없습니다.
Pillow는 재생성과 이미지 검증 도구에서만 사용합니다.

```powershell
python LEC08/generate_sheet.py
python LEC08/animation_viewer.py --check
python -m unittest discover -s LEC08 -v
python LEC08/animation_viewer.py --seconds 3
python LEC08/check_rendering.py
```

자동 테스트는 모든 프레임과 반복 횟수, 정지 경계, 장시간 경과 후 순환,
시트 복원 결과, 가변 크기 및 확대 시 화면 범위를 검증합니다.
`check_rendering.py --output 원하는경로.png`로 네 동작의 실제 SDL 렌더링을 저장할 수 있습니다.
