# 첨 시작 프린트 (선택지들)
print("단위 변환기")
print("1. m (미터) → km (키로미터)")
print("2. km (키로미터) → m (미터)")
print("3. m (미터) → cm (센티미터)")
print("4. cm (센티미터) → m (미터)")
print("5. mm (밀리미터) → cm (센티미터)")
print("6. cm (센티미터) → mm (밀리미터)")

while True:  # 무한 반복
    choice = input("원하는 변환을 선택하세요 (1-6): ").strip() # 1에서 6 사이 선택
    if choice not in ["1", "2", "3", "4", "5", "6"]: # 다른거 입력했으면
        print("잘못된 입력입니다.") # 틀렸다고 말하기
        continue  # 다시 입력

    if choice == "1": # 1번을 선택한 경우
        meters = float(input("미터 입력: ")) # 미터 입력받기
        kilometers = meters / 1000  # 1 m = 0.001 km, 미터 나누기 1000
        print(f"{meters} 미터 = {kilometers:.2f} 키로미터") # 결과 출력, 소수점 2자리까지 표시

    elif choice == "2": # 2번을 선택한 경우
        kilometers = float(input("키로미터 입력: ")) # 키로미터 입력받기
        meters = kilometers * 1000  # 1 km = 1000 m, 키로미터 곱하기 1000
        print(f"{kilometers} 키로미터 = {meters:.2f} 미터") # 결과 출력, 소수점 2자리까지 표시

    elif choice == "3": # 3번을 선택한 경우
        meters = float(input("미터 입력: ")) # 미터 입력받기
        centimeters = meters * 100  # 1 m = 100 cm, 미터 곱하기 100
        print(f"{meters} 미터 = {centimeters:.2f} 센티미터") # 결과 출력, 소수점 2자리까지 표시

    elif choice == "4": # 4번을 선택한 경우
        centimeters = float(input("센티미터 입력: ")) # 센티미터 입력받기
        meters = centimeters / 100  # 1 cm = 0.01 m, 센티미터 나누기 100
        print(f"{centimeters} 센티미터 = {meters:.2f} 미터") # 결과 출력, 소수점 2자리까지 표시

    elif choice == "5": # 5번을 선택한 경우
        millimeters = float(input("밀리미터 입력: ")) # 밀리미터 입력받기
        centimeters = millimeters / 10  # 1 mm = 0.1 cm, 밀리미터 나누기 10
        print(f"{millimeters} 밀리미터 = {centimeters:.2f} 센티미터") # 결과 출력, 소수점 2자리까지 표시

    elif choice == "6": # 6번을 선택한 경우
        centimeters = float(input("센티미터 입력: ")) # 센티미터 입력받기
        millimeters = centimeters * 10  # 1 cm = 10 mm, 센티미터 곱하기 10
        print(f"{centimeters} 센티미터 = {millimeters:.2f} 밀리미터") # 결과 출력, 소수점 2자리까지 표시

    # 그 외    
    else:
        print("잘못된 선택입니다.")

    # 재시도
    if input("다시 시도하시겠습니까? (y/n): ").strip().lower() != "y":
        break  # 예스 아니면 바로 끝
