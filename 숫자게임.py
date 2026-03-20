import random  #랜덤 불러옴
anwer = random.randint(1, 100) #랜덤숫자의 범위 (1~100)
print("숫자 게임에 오신걸 환영합니다, 1부터 100까지의 숫자 중 하나를 맞춰보세요:)") #게임 시작 대사
while True: #조건이 참인 동안은 계속 반복
    guess = int(input("숫자를 입력하세요: ")) #사용자에게 숫자 입력받음, 여기서 문자열은 숫자로 변환. 입력 받은 숫자는 guess에 저장!
    if guess < anwer: #답이 입력한 숫자보다 크면
        print("업")
    elif guess > anwer: #답이 입력한 숫자보자 작으면
        print("다운") 
    else: #맞추면
        print("와!!!정답!!!")
        break
