import random  # 랜덤 불러옴

# 비밀번호에 사용할 문자들
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+"

# 비밀번호 생성 무한 루프
while True:
    # chars에서 12개 랜덤 선택
    random_password = "".join(random.sample(chars, 12))

    # 새로운 비밀번호
    print("새로운 비밀번호:", random_password)

    # 재생성 물어보기
    user_input = input("다시 생성하시겠습니까? (y/n): ").strip().lower()

    # 예스 아니면 바로 끝
    if user_input != "y":
        break