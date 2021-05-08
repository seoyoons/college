x = 3
y = 1
z = 0

if x > 2 :
  print("Hello","\n")     # x가 2보다 크면 출력

if x > y :
  print("x는 y보다 크다.")    # x가 y보다 크면 출력

if x < y :
  print("x보다 y가 크다.")     # y가 x보다 크면 출력

if not x < y :
  print("x보다 y가 크지 않다.")    # y가 x보다 크지 않으면 출력

if x > z and x > y :
  print("y가 z보다 크고 x가 y보다 크다.")     # x가 z보다 크고 x가 y보다 크면 출력,  두 가지 모두 맞아야 출력

if z > y or x > y :
  print("z가 y보다 크거나 또는 x가 y보다 크다.")     # z가 y보다 크거나 x가 y보다 크면 출력, 둘 중 하나만 맞아도 출력
