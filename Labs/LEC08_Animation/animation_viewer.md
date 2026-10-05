# Drill #8 애니메이션 뷰어

실행: `python animation_viewer.py` (pico2d 필요)

- 대기 6프레임, 달리기 8프레임, 공격 14프레임, 쓰러짐 10프레임
- 화면 중앙에서 7배 확대 표시 (대기 자세 높이 322px, 화면 높이 600px)
- 각 애니메이션을 5회 재생한 다음 마지막 프레임에서 1초 정지, 전체 순서 무한 반복
- ESC 또는 창 닫기 버튼으로 종료

## 제출할 때 추가점수 설명

프레임마다 가로·세로 크기와 배치가 다른 스프라이트 시트를 사용했습니다. JSON의 각 프레임 좌표와 크기로 이미지를 자르고, 잘려 나간 투명 여백의 위치를 복원해 캐릭터가 흔들리지 않게 표시했습니다. 또한 애니메이션별 실제 프레임 수를 읽어서 6·8·14·10프레임의 서로 다른 길이를 지원합니다.

## 스프라이트 출처

- [Phaser examples — knight.png](https://github.com/phaserjs/examples/blob/master/public/assets/animations/knight.png)
- [Phaser examples — knight.json](https://github.com/phaserjs/examples/blob/master/public/assets/animations/knight.json)
- [원본 저장소의 에셋 이용 안내](https://github.com/phaserjs/examples#license)

원본 PNG와 JSON을 수정하지 않고 수업용 뷰어에 사용했습니다.
