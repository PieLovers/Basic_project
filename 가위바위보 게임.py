import random  # 랜덤 불러옴

choices = ["가위", "바위", "보"]  # 선택지 목록

while True:  # 반복겜
    user = input("가위, 바위, 보 중 하나를 입력하세요 : ")  # 사용자 입력 받기
    if user not in choices:  # 틀린 입력이라면
        print("잘못된 입력입니다.") # 틀렸다고 말하고
        continue  # 다시 입력 받기

    pc = random.choice(choices)  # 컴퓨터의 선택
    print("컴퓨터:", pc)

    # 비기는 경우
    if user == pc:  
        print("비겼습니다.")
    
    # 사용자가 이기는 경우
    elif (user == "가위" and pc == "보") or (user == "바위" and pc == "가위") or (user == "보" and pc == "바위"):
        print("축하합니다! 이겼습니다.")

    else:  # 사용자가 지는 경우
        print("졌습니다.")

    # 한 판 더?
    if input("한 판 더? (y/n): ").strip().lower() != "y":
        break  # y가 아니면 끝

