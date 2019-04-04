class assignment:
    # 생성자(정보저장)
    def __init__(self,name='',phone='',sex=''):
        self.name = name
        self.phone = phone
        self.sex = sex
    # 출력
    def __str__(self):
        return "이름은 {}, 전화번호는 {}, 성별은 {} 입니다." .format(self.name,self.phone,self.sex)

# 리스트로 여러개의 데이터를 저장합니다
phone_book_list = []
while(1):

    # name 입력
    name = input('이름을 입력하세요 : ')
    
    # 그만이 입력된다면 while문을 종료합니다.
    if(name == '그만'):
        break
    
    # phone입력
    phone = input('전화번호를 입력하세요 : ')
    
    # sex입력
    sex = input('성별을 입력하세요 (male이나 female로 작성해주세요) : ')
    if(sex == 'male'):
        sex = 'male'
   
    elif(sex == 'female'):
        sex = 'female'
   
    else:
        sex = 'unknown'
    
    # 여러개의 생성자를 저장하기위해 리스트에 append시킵니다.
    phone_book_list.append( assignment(name,phone,sex) )
    
    # 리스트에 저장된 생성자의 개수만큼 출력하기위해 for문을 이용하여 출력합니다 
    for a in phone_book_list:
        print(a)

# 그만이 입력된 후 저장된 리스트의 값을 출력합니다
for a in phone_book_list:
    print(a)