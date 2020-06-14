import datetime

class Timeline:
    timeline=[]

    def __init__(self,member,text, time):
        self.member=member
        self.time=time
        self.text=text
        self.good_response=[]
        self.message=[]

    @staticmethod
    def input_timeline(member,text):
        time=datetime.datetime.now() #현재 시간 로드
        t=Timeline(member,text,time) #타임 라인 객체 생성
        Timeline.timeline.insert(0,t)
        return t #객체를 반환


    def input_message(self, member, message):
        self.message.append((member.id,message))

    def add_good_response(self,member):
        self.good_response.append(member.id)

    def show_story(self):
        print(self.member.id,"님의 게시물")
        print('내용:', self.text)
        print('작성 시간:', self.time)
        for p in self.good_response : print(p,'님이 이 글을 좋아합니다')
        for p,m in self.message : print(p,'님: ',m)
        print()

class Member:
    info=[]
    def __init__ (self,name,id,password,profile):
        self.id=id
        self.password=password
        self.name=name
        self.profile=profile

    @staticmethod
    def join(name,id,password,profile):
        m=Member(name, id, password,profile) #멤버 객체 생성
        Member.info.append(m) #데이터 베이스에 객체 추가
        return m

    @staticmethod
    def login(id, password):
        for _ in Member.info:
            if _.id==id and _.password==password:
                return _

    def update_member_name(self, name=""):
        self.name=name

    def update_member_profile(self,profile=""):
        self.profile=profile

    def update_member_password(self,password=""):
        self.password=password

    def show_member_info(self):
        print(self.id,'님의 프로필을 출력합니다.')
        print('이름 : ',self.name)
        print('프로필 : ',self.profile)

    @staticmethod
    def remove_member(member):
        print("정말 탈퇴하시겠습니까?")
        char=input("(Y/N)\n-->")
        if(char=='Y'):
            Member.info.remove(member)
        else:
            return 9;


def join_us():
    id=input("ID (e-mail) 입력해주세요: ")
    for _ in Member.info:
        if _.id==id:
            print("이미 존재하는 아이디 입니다.")
            return;
    name=input("이름을 입력해 주세요 : ")
    password=input("비밀번호를 입력해 주세요 : ")
    profile=input("본인을 설명해 주세요 : ")
    member=Member.join(name,id,password,profile)

    print(member.id,"님 환영합니다!")

def login_us():
    id=input("ID: ")
    password=input("Password: ")

    member=Member.login(id,password)
    if member!=None:
        print(member.id+"님이 로그인하셨습니다.")
        show_timeline()
    else:
        print("존재하지 않는 계정입니다.")
    return member

def write_story(member):
    text=input("게시글을 입력합니다: ")
    Timeline.input_timeline(member,text)

def write_message(member):
    index=int(input("댓글을 입력할 게시글을 선택합니다."))

    if index>=0 and index<len(Timeline.timeline):
        message=input("댓글을 입력합니다: ")
        story=Timeline.timeline[index]
        story.input_message(member,message)

    else:
        print("존재하지 않는 게시글입니다.")

def write_like(member):
    index=int(input("좋아요를 입력할 게시글을 선택합니다."))
    if index>=0 and index<len(Timeline.timeline):
        story=Timeline.timeline[index]
        story.add_good_response(member)
    else:print("존재하지 않는 게시글입니다.")

def show_members():
    print("회원 정보를 출력합니다.")
    for member in Member.info:
        member.show_member_info()

def update_member(member):
    while True:
        op=input("\n1.이름변경"+"(현재이름 : "+member.name+")"+"\n2.소개글 변경"+"(현재소개글 : "+member.profile+")"+"\n3.비밀번호 변경\n4.종료\n-->")
        if '1' in op:
            name=input("변경하실 이름을 입력해주세요 : ")
            member.update_member_name(name)
        elif '2' in op:
            profile=input("변경하실 소개글을 입력해주세요 : ")
            member.update_member_profile(profile)
        elif '3' in op:
            password=input("현재 비밀번호를 입력해주세요.")
            if(password==member.password):
                p_w=input("바꾸실 비밀번호를 입력해주세요.")
                member.update_member_password(p_w)
            else:
                print("비밀번호가 틀렸습니다!")
        else:break

def show_timeline():
    print("타임라인을 출력합니다.")
    for i,contents in enumerate(Timeline.timeline):
        print("index:",i)
        contents.show_story()

while True:
    menu=input("\n1:회원가입\n2:로그인\n3:회원리스트 출력\n4:종료\n-->")
    if '1' in menu:
        join_us()
    elif '2' in menu:
        member=login_us()
        if member==None:continue #로그인 실패시
        else:
            while True:
                menu=input('\n1:글작성\n2:댓글작성\n3:좋아요작성\n4:타임라인 보기\n5:회원정보수정\n6:회원탈퇴\n7:로그아웃\n-->')
                if '1' in menu: write_story(member)
                elif '2' in menu:write_message(member)
                elif '3' in menu:write_like(member)
                elif '4' in menu:show_timeline()
                elif '5' in menu:update_member(member)
                elif '6' in menu:
                    check=member.remove_member(member)
                    if(check!=9):
                        break
                else:break
    elif '3' in menu:show_members()
    else:break
