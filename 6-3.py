# 4)
a = "정수"
b = " 태희"
c = "환준"
d = "세영"


def chat(name1,name2):       # 함수들이 인자라는 것을 받음
  print("%s: 안녕? 넌 몇살이니?" % name1)
  print("%s: 나? 나는 20살이야!" % name2)

chat(a,b)
chat(c,d)


# 5)
def chat(name1, name2, age):              # 함수들이 인자라는 것을 받음
  print("%s:안녕? 넌 몇살이니?" % name1)
  print("%s:나? 나는 %d" % (name2, age) + "살이야")

a = "정수"
b = " 태희"
c = "환준"
d = "세영"


chat(a,b,20)
chat(c,d,30)
