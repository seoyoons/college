# 반복문 : for, while
# break, Continue

i = 0
for i in range(5):            # i는 몇번째인지 i라는 변수에 넣음. range(5)는 5번 반복
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야. 그냥 있어.")

  if i == 1:
    continue

    print("원이: 안녕 철수, 영희야!")

i = 0
for i in range(100):
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야. 그냥 있어.")
  i = i + 1 

  if i > 2:
    break

i = 0 
while i < 3:           # i가 3보다 작으면
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야. 그냥 있어.")
  i = i + 1 

i = 0
while True:          # 무한 루프
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야. 그냥 있어.")
  i = i + 1 

  if i > 2:
    break

i = 0
while 1 < 3:
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야. 그냥 있어.")
  i = i + 1 
  
  while True:       # 무한루프
    print(i)
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야. 그냥 있어.")
    i = i + 1
   

# Break문

for i in range(100):
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야. 그냥 있어.")

  if i > 2:
    break

# continue

for i in range(3):
  print(i)
  print("철수: 안녕 영희야 뭐해?")
  print("영희: 안녕 철수야. 그냥 있어.")

  if i == 1:     # 1을 만나는 곳에는 아래 문장을 출력하지 않는다.
    continue     # 컨티뉴를 만나면 루프에 첫번째 라인으로 돌아간다.

    print("정수: 어이 친구들. 안녕.")
