# RobotSW
Robot Software, use Python

## color.py
구성 함수: redcolor(), bluecolor(), greencolor(), sectioncolor() <- 추후 색이 정해지면 함수명이 바뀔 예정
RGB값으로 색을 검출하는 함수 
모든 함수의 lower, upper 수정 필요 (lower, upper: BGR 값으로 넣어야 함

return 
- 마스킹되어 사용자가 지정한 색의 부분을 제외한 다른 부분은 검은색으로 된 이미지 

## LineTracer.py <= main
LineTracing을 하고 
Triangle_Detection() 함수의 리턴 값이 0이상이면 멈추게 동작하도록 함
나중에 서버에서 사용자가 보낸 섹 정보를 받아서 그 색에 따라 color 함수를 불러야 함

return
- 없음

## Triangle_Detection.py
구성 함수: Triangle_Detection(), Direction_Check()
Triangle_Detection(): 외곽선을 검출한 후 근사화를 해서 꼭지점을 찾음 그 꼭지점이 몇 개인지에 따라 삼각형을 판별함
Direction_Check(): 삼각형의 꼭지점 좌표값으로 삼각형의 방향이 위인지 아래인지 판별함

return
- Triangle_Detection(): 삼각형이 아니면 0 삼각형이면 Direction_Check()의 리턴값
- Direction_Check(): 삼각형이 위이면 1 아래면 2
