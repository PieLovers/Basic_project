import random
#로또 번호 생성기
print("로또 번호를 생성해 드릴게요!")
def generate_lotto_numbers():
    numbers = random.sample(range(1, 46), 6) # 1부터 45까지의 숫자 중에서 6개를 랜덤으로 선택
    numbers.sort() # 번호를 오름차순으로 정렬
    return numbers
lotto_numbers = generate_lotto_numbers() # 로또 번호 생성
print("생성된 로또 번호:", lotto_numbers) # 생성된 로또 번호 출력
