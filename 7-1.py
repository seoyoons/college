def sayHello(name, age):
  if age < 10:
    print("안녕, " + name)       # 10살 미만이면 안녕+이름이 출력
  elif age <=20 and age >=10:
      print("안녕하세요, " + name)    # 10살에서 20살 사이면 안녕하세요+이름 출력
  else:
      print("안녕하십니까, " + name)   # 그 외, 안녕하십니까+이름

sayHello("태희", 20)
sayHello("정수", 6)
sayHello("세영", 40)
sayHello("철수", 10)
