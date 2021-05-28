#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import Tk, ttk, Label, Button, Text, END

reports = [
    {'이름' : '가영', '학년' : 1, '국어' : 90, '수학' : 22, '영어' : 33, '한국사' : 66, '통합과학' : 99},
    {'이름' : '나겸', '학년' : 3, '국어' : 90, '수학' : 23, '영어' : 90, '한국사' : 56, '통합과학' : 29},
    {'이름' : '다은', '학년' : 2, '국어' : 20, '수학' : 28, '영어' : 66, '한국사' : 66, '통합과학' : 94},
    {'이름' : '라희', '학년' : 3, '국어' : 44, '수학' : 90, '영어' : 77, '한국사' : 26, '통합과학' : 99}
]
  
selected_index = 0

def report_selected(event) : # 선택하면 반영되게끔
    global selected_index
    for item in treeTable.selection() :
        selected_index = int(treeTable.item(item, "text"))
    report = reports[selected_index]
    name = report['이름']
    grade = str(report['학년'])
    kor = str(report['국어'])
    math = str(report['수학'])
    eng = str(report['영어'])
    hist = str(report['한국사'])
    sci = str(report['통합과학'])
    
    text_Name.delete("1.0",END)
    text_Name.insert("end", name)
    text_Grade.delete("1.0",END)
    text_Grade.insert("end", grade)
    text_Kor.delete("1.0",END)
    text_Kor.insert("end", kor)
    text_Math.delete("1.0",END)
    text_Math.insert("end", math)
    text_Eng.delete("1.0",END)
    text_Eng.insert("end", eng)
    text_Hist.delete("1.0",END)
    text_Hist.insert("end", hist)
    text_Sci.delete("1.0",END)
    text_Sci.insert("end", sci)

def setTableItems() :
    treeTable.delete(*treeTable.get_children())
    for idx, report in enumerate(reports) :
        name = report['이름']
        grade = str(report['학년'])
        kor = str(report['국어'])
        math = str(report['수학'])
        eng = str(report['영어'])
        hist = str(report['한국사'])
        sci = str(report['통합과학'])
        treeTable.insert("", 'end', iid = None, text=str(idx), values=[name, grade, kor, math, eng, hist, sci])
    
def insert_report() :
    name = text_Name.get("1.0", END)
    grade = int(text_Grade.get("1.0", END))
    kor = int(text_Kor.get("1.0", END))
    math = int(text_Math.get("1.0", END))
    eng = int(text_Eng.get("1.0", END))
    hist = int(text_Hist.get("1.0", END))
    sci = int(text_Sci.get("1.0", END))
    report = { '이름' : name, '학년' : grade, '국어' : kor, '수학' : math, '영어' : eng, '한국사' : hist, '통합과학' : sci}
    reports.append(report)
    setTableItems()

def update_report() :
    global selected_index
    name = text_Name.get("1.0", END)
    grade = int(text_Grade.get("1.0", END))
    kor = int(text_Kor.get("1.0", END))
    math = int(text_Math.get("1.0", END))
    eng = int(text_Eng.get("1.0", END))
    hist = int(text_Hist.get("1.0", END))
    sci = int(text_Sci.get("1.0", END))
    selectedItem = reports[selected_index]
    selectedItem['이름'] = name
    selectedItem['학년'] = grade
    selectedItem['국어'] = kor
    selectedItem['수학'] = math
    selectedItem['영어'] = eng
    selectedItem['한국사'] = hist
    selectedItem['통합과학'] = sci
    setTableItems()
    
    
def delete_report() :
    global selected_index
    reports.pop(selected_index)
    setTableItems()


window = Tk()
window.title("성적관리 프로그램 v1.0")
window.geometry("1000x600")
window.resizable(0,0)
title = "9월 모의고사 성적결과"
title_feature = Label(window, text = title, font = ("Noto Sans KR Black", 20))
title_feature.pack(padx = 10, pady = 15) # 위치

#성적관리 화면에 표현
treeTable = ttk.Treeview(window)
treeTable["columns"] = ("name", "grade", "kor", "math", "eng", "hist", "sci")
treeTable.column("#0", width = 50)
treeTable.column("name", width = 100)
treeTable.column("grade", width = 50)
treeTable.column("kor", width = 100)
treeTable.column("math",width = 100)
treeTable.column("eng", width = 100)
treeTable.column("hist", width = 100)
treeTable.column("sci", width = 100)

# treeStationfares에는 순번, 정류장, 요금 표시
treeTable.heading("#0", text="No.")
treeTable.heading("name", text="이름")
treeTable.heading("grade", text="학년")
treeTable.heading("kor", text="국어")
treeTable.heading("math", text="수학")
treeTable.heading("eng", text="영어")
treeTable.heading("hist", text="한국사")
treeTable.heading("sci", text="통합과학")

treeTable.place(x = 100, y = 100, width=800, height=200)

treeTable.bind("<<TreeviewSelect>>", report_selected)

# button
btn_Insert = Button(window, text = "추가", command = insert_report, font = ("Noto Sans KR Medium", 14))
btn_Insert.place(x = 100, y = 350, width = 200, height = 30)
btn_Update = Button(window, text = "수정", command = update_report, font = ("Noto Sans KR Medium", 14))
btn_Update.place(x = 400, y = 350, width = 200, height = 30)
btn_Delete = Button(window, text = "삭제", command = delete_report, font = ("Noto Sans KR Medium", 14))
btn_Delete.place(x = 700, y = 350, width = 200, height = 30)

# label
label_Name = Label(window, text = "이름")
label_Name.place(x = 150, y = 430, width = 50, height = 25)
label_Grade = Label(window, text = "학년")
label_Grade.place(x = 250, y = 430, width = 50, height = 25)
label_Kor = Label(window, text = "국어")
label_Kor.place(x = 350, y = 430, width = 50, height = 25)
label_Math = Label(window, text = "수학")
label_Math.place(x = 450, y = 430, width = 50, height = 25)
label_Eng = Label(window, text = "영어")
label_Eng.place(x = 550, y = 430, width = 50, height = 25)
label_Hist = Label(window, text = "한국사")
label_Hist.place(x = 650, y = 430, width = 50, height = 25)
label_Sci = Label(window, text = "공통과학")
label_Sci.place(x = 750, y = 430, width = 50, height = 25)

text_Name = Text(window, width = 13, height = 1)
text_Name.place(x = 130, y = 460)
text_Grade = Text(window, width = 4, height = 1)
text_Grade.place(x = 260, y = 460)
text_Kor = Text(window, width = 8, height = 1)
text_Kor.place(x = 345, y = 460)
text_Math = Text(window, width = 8, height = 1)
text_Math.place(x = 445, y = 460)
text_Eng = Text(window, width = 8, height = 1)
text_Eng.place(x = 545, y = 460)
text_Hist = Text(window, width = 8, height = 1)
text_Hist.place(x = 645, y = 460)
text_Sci = Text(window, width = 8, height = 1)
text_Sci.place(x = 745, y = 460)


setTableItems()

window.mainloop()

