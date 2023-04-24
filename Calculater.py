def Str2FloatGrade(grade):
    return 0.0 if(grade=="F") else 68.5-ord(grade[0])+len(grade)*0.5

def InputSubjectInfo(nameDict,infoList):
    subjectName = input("과목명을 입력하세요:\n")
    subjectCredit = int(input("학점을 입력하세요:\n"))
    subjectGrade = input("평점을 입력하세요:\n")

    if subjectName in nameDict.values():
        key = [k for k, v in nameDict.items() if v == subjectName][0]
        for i in range(len(infoList)): 
            if infoList[i][0] == key and Str2FloatGrade(infoList[i][2])<Str2FloatGrade(subjectGrade):
                infoList[i] = (key,subjectCredit,subjectGrade)

    else:
        key = len(nameDict)
        nameDict[key] = subjectName
        infoList.append((key,subjectCredit,subjectGrade))

    print("입력되었습니다.")

def PrintSubjectListInfo(nameDict,infoList):
    for i in range(0,len(infoList)):
        print(f"[{nameDict[infoList[i][0]]}] {str(infoList[i][1])}학점: {infoList[i][2]}")

def PrintCalculatedInfo(list):
    total = sum(map(lambda x: x[1],list))
    average = sum(map(lambda x: x[1]*Str2FloatGrade(x[2]),list))/total
    print(f"{str(total)}학점 (GPA: {average})")

subjectNameDict = dict()
subjectInfoList = list()

workType = 0

while workType != 3:
    workType = int(input("작업을 선택하세요.\n1. 입력\n2. 출력\n3. 계산\n"))
    print("\n")

    if workType == 1:
        InputSubjectInfo(subjectNameDict,subjectInfoList)

    elif workType == 2:
        PrintSubjectListInfo(subjectNameDict,subjectInfoList)

    print("\n")

print("제출용:",end = " ")
PrintCalculatedInfo(list(filter(lambda x:x[2] != "F",subjectInfoList)))

print("열람용:",end = " ")
PrintCalculatedInfo(subjectInfoList)