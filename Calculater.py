class Subject:
    gradeList = ['A','B','C','D','F','A+','B+','C+','D+'];
    def __init__(this,name = "",credit = 0,grade = ""):
        this.name = name
        this.credit = credit
        if grade not in gradeList:
            raise Exception("Unexpected Grade")
        this.grade = grade

    def __repr__(this):
        return f"[{this.name}] {str(this.credit)}학점: {this.grade}"

    def __str__(this):
        return f"[{this.name}] {str(this.credit)}학점: {this.grade}"

    @staticmethod
    def Str2FloatGrade(grade):
        if grade not in gradeList:
            raise Exception("Unexpected Grade")
        return 0.0 if(grade=="F") else 68.5-ord(grade[0])+len(grade)*0.5

    def GetFloatGrade(this):
        return Subject.Str2FloatGrade(this.grade)

def Input_Advanced(prompt = "",checkList = [],blackList = [],formatType = str):
    inputString = input(prompt)
    if inputString in blackList:
        raise Exception("Unpermitted Input " + inputString)
    if inputString not in checkList and checkList != []:
        raise Exception("Unexpected Input " + inputString)

    return formatType(inputString)

def InputSubject(arr):

    subjectName = Input_Advanced("과목명을 입력하세요:\n",blackList = [""])
    subjectCredit = Input_Advanced("학점을 입력하세요:\n",["1","2","3"],[""],int)
    subjectGrade = Input_Advanced("평점을 입력하세요:\n",blackList = [""])

    if subjectName in arr:
        if arr[subjectName].GetFloatGrade() < Subject.Str2FloatGrade(subjectGrade):
            arr[subjectName] = Subject(subjectName,subjectCredit,subjectGrade)
    else:
        arr[subjectName] = Subject(subjectName,subjectCredit,subjectGrade)

    print("입력되었습니다.")

def PrintCalculatedInfo(arr):
    total = sum(map(lambda x: x.credit,arr))
    average = sum(map(lambda x: x.credit*x.GetFloatGrade(),arr))/total
    print(f"{str(total)}학점 (GPA: {average})")

subjectDict = dict()

workType = 0

while workType != 5:
    
    workType = ord((input("작업을 선택하세요.\n1. 입력\n2. 출력\n3. 조회\n4. 계산\n5. 종료\n")+" ")[0])-ord("0");
    print("\n")

    if workType == 1:
        try:
            InputSubject(subjectDict)
        except Exception:
            print("잘못된 입력입니다.")

    elif workType == 2:
        for subject in subjectDict.values():
            print(subject)

    elif workType == 3:
        subjectName = input("과목명을 입력하세요:\n")
        if subjectName in subjectDict:
            print(subjectDict[subjectName])
        else:
            print("해당하는 과목이 없습니다.")

    elif workType == 4:
        print("제출용:",end = " ")
        PrintCalculatedInfo(list(filter(lambda x:x.grade != "F",subjectDict.values())))

        print("열람용:",end = " ")
        PrintCalculatedInfo(subjectDict.values())

    print("\n")