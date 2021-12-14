import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)

a_student = pd.read_csv("d:\오픈소스 2차과제/학생수/일반고 학생수.csv")
b_student = pd.read_csv("d:\오픈소스 2차과제/학생수/자율고 학생수.csv")
c_student = pd.read_csv("d:\오픈소스 2차과제/학생수/특목고 학생수.csv")
d_student = pd.read_csv("d:\오픈소스 2차과제/학생수/특성화고 학생수.csv")

a_school = pd.read_csv("d:\오픈소스 2차과제/학교수/일반고 학교수.csv")
b_school = pd.read_csv("d:\오픈소스 2차과제/학교수/자율고 학교수.csv")
c_school = pd.read_csv("d:\오픈소스 2차과제/학교수/특목고 학교수.csv")
d_school = pd.read_csv("d:\오픈소스 2차과제/학교수/특성화고 학교수.csv")

a_teacher = pd.read_csv("d:\오픈소스 2차과제/교원수/시도별/일반고 시도별 교원수.csv")
b_teacher = pd.read_csv("d:\오픈소스 2차과제/교원수/시도별/자율고 시도별 교원수.csv")
c_teacher = pd.read_csv("d:\오픈소스 2차과제/교원수/시도별/특목고 시도별 교원수.csv")
d_teacher = pd.read_csv("d:\오픈소스 2차과제/교원수/시도별/특성화고 시도별 교원수.csv")

a_position_teacher = pd.read_csv("d:\오픈소스 2차과제/교원수/직위별/일반고 직위별 교원수.csv")
b_position_teacher = pd.read_csv("d:\오픈소스 2차과제/교원수/직위별/자율교 직위별 교원수.csv")
c_position_teacher = pd.read_csv("d:\오픈소스 2차과제/교원수/직위별/특목고 직위별 교원수.csv")
d_position_teacher = pd.read_csv("d:\오픈소스 2차과제/교원수/직위별/특성화고 직위별 교원수.csv")

student = pd.DataFrame()
all_student = pd.DataFrame()
student["년도"] = a_student["년도"]
all_student["년도"] = a_student["년도"]
all_student["총 학생 수"] = a_student["계"]+b_student["계"]+c_student["계"]+d_student["계"]
student["일반고 학생 수"] = a_student["계"]
student["자율고 학생 수"] = b_student["계"]
student["특목고 학생 수"] = c_student["계"]
student["특성화고 학생 수"] = d_student["계"]

figure1 = plt.figure()

ax1 = figure1.add_subplot()
ax1.set_ylabel('총 학생 수(백만명)')

student.plot.bar(x='년도', stacked=True, ax=ax1)

school1 = pd.DataFrame()
school2 = pd.DataFrame()
all_school = pd.DataFrame()
all_school["년도"] = a_school["년도"]
all_school["총 학교 수"] = a_school["계"]+b_school["계"]+c_school["계"]+d_school["계"]
school1["년도"] = a_school["년도"]
school1["일반고 학교 수"] = a_school["계"]
school2["년도"] = b_school["년도"]
school2["자율고 학교 수"] = b_school["계"]
school2["특목고 학교 수"] = c_school["계"]
school2["특성화고 학교 수"] = d_school["계"]

figure2 = plt.figure()

ax1 = figure2.add_subplot()
ax2 = ax1.twinx()
ax1.set_ylabel('일반고 학교 수(개)')
ax2.set_ylabel('그 외 학교 수(개)')

school1.plot.line(x='년도', color='red', ax=ax1)
school2.plot(x='년도', kind='line', ax=ax2)

teacher = pd.DataFrame()
teacher["년도"] = a_teacher["년도"]
teacher["일반고 전체 교직원 수"] = a_teacher["계"]
teacher["자율고 전체 교직원 수"] = b_teacher["계"]
teacher["특목고 전체 교직원 수"] = c_teacher["계"]
teacher["특성화고 전체 교직원 수"] = d_teacher["계"]

figure3 = plt.figure()

ax1 = figure3.add_subplot()
ax1.set_ylabel('교직원 수(명)')

teacher.plot.bar(x='년도', stacked=True, ax=ax1)

position_teacher1 = pd.DataFrame()
position_teacher2 = pd.DataFrame()
position_teacher3 = pd.DataFrame()
position_teacher4 = pd.DataFrame()
position_teacher1["년도"] = a_position_teacher["년도"]
position_teacher2["년도"] = b_position_teacher["년도"]
position_teacher3["년도"] = c_position_teacher["년도"]
position_teacher4["년도"] = d_position_teacher["년도"]
position_teacher1["일반고 교사 수"] = a_position_teacher["보직교사"]+a_position_teacher["교사"]
position_teacher1["일반고 기간제 교사 수"] = a_position_teacher["기간제교사"]
position_teacher2["자율고 교사 수"] = b_position_teacher["보직교사"]+b_position_teacher["교사"]
position_teacher2["자율고 기간제 교사 수"] = b_position_teacher["기간제교사"]
position_teacher3["특목고 교사 수"] = c_position_teacher["보직교사"]+c_position_teacher["교사"]
position_teacher3["특목고 기간제 교사 수"] = c_position_teacher["기간제교사"]
position_teacher4["특성화고 교사 수"] = d_position_teacher["보직교사"]+d_position_teacher["교사"]
position_teacher4["특성화고 기간제 교사 수"] = d_position_teacher["기간제교사"]

figure4 = plt.figure()

ax1 = figure4.add_subplot()
ax1.set_ylabel('교사 수(명)')

a_d_position_teacher = pd.merge(position_teacher1, position_teacher4)

a_d_position_teacher.plot.line(x='년도', ax=ax1)

figure5 = plt.figure()

ax1 = figure5.add_subplot()
ax1.set_ylabel('교사 수(명)')

b_c_position_teacher = pd.merge(position_teacher2, position_teacher3)
b_c_position_teacher.plot.line(x='년도', ax=ax1)

figure6 = plt.figure()
ax1 = figure6.add_subplot()
ax2 = ax1.twinx()
ax1.set_ylabel('학생 수(백만명)')
ax2.set_ylabel('학교 수(개)')
ax1.legend(loc='upper right')
ax2.legend(loc='lower right')

all_student.plot.line(x='년도', color='green', ax=ax1)
all_school.plot.line(x='년도', color='orange', ax=ax2)

plt.show()