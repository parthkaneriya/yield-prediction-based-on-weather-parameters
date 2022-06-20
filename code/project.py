import xlrd
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import LinearRegression

file=xlrd.open_workbook(r"C:\Users\student\Desktop\Analytics in Agri\project\Project_yieldprediction.xls")
sheet=file.sheet_by_index(0)

def value(start,stop):
    A=[]
    for i in range(start,stop):
        A.append(round((sheet.cell_value(i,24)),1))

    B=[]
    for i in range(start,stop):
        B.append(round((sheet.cell_value(i,25)),6))
    return(A,B)
    
Z10,Z11=value(1,28)
Z20,Z21=value(37,64)
Z30,Z31=value(73,100)
Z40,Z41=value(109,136)
Z50,Z51=value(145,172)
Z60,Z61=value(181,208)
Z70,Z71=value(217,244)
Z120,Z121=value(253,280)
Z130,Z131=value(289,316)
Z140,Z141=value(325,352)
Z150,Z151=value(361,388)
Z160,Z161=value(397,424)
Z170,Z171=value(433,460)
Z230,Z231=value(469,496)
Z240,Z241=value(505,532)
Z250,Z251=value(541,568)
Z260,Z261=value(577,604)
Z270,Z271=value(613,640)
Z340,Z341=value(649,676)
Z350,Z351=value(685,712)
Z360,Z361=value(721,748)
Z370,Z371=value(757,784)
Z450,Z451=value(793,820)
Z460,Z461=value(829,856)
Z470,Z471=value(865,892)
Z560,Z561=value(901,928)
Z570,Z571=value(937,964)
Z670,Z671=value(973,1000)


X_train=pd.DataFrame({'Z10':Z10,'Z11':Z11,'Z20':Z20,'Z21':Z21,'Z30':Z30,'Z31':Z31,'Z40':Z40,'Z41':Z41,'Z50':Z50,'Z51':Z51,'Z60':Z60,'Z61':Z61,'Z70':Z70,'Z71':Z71,
                'Z120':Z120,'Z121':Z121,'Z130':Z130,'Z131':Z131,'Z140':Z140,'Z141':Z141,'Z150':Z150,'Z151':Z151,'Z160':Z160,'Z161':Z161,'Z170':Z170,'Z171':Z71,
                'Z230':Z230,'Z231':Z231,'Z240':Z240,'Z241':Z241,'Z250':Z250,'Z251':Z251,'Z260':Z260,'Z261':Z261,'Z270':Z270,'Z271':Z271,
                'Z340':Z340,'Z341':Z341,'Z350':Z350,'Z351':Z351,'Z360':Z360,'Z361':Z361,'Z370':Z370,'Z371':Z371,
                'Z450':Z450,'Z451':Z451,'Z460':Z460,'Z461':Z461,'Z470':Z470,'Z471':Z471,
                'Z560':Z560,'Z561':Z561,'Z570':Z570,'Z571':Z571,
                'Z670':Z670,'Z671':Z671})


file2=pd.read_excel(r"C:\Users\student\Desktop\Analytics in Agri\project\Project_yieldprediction.xls")
Y_train=pd.DataFrame(file2.iloc[0:27,1])
"""
A10,A11=value(29,33)
A20,A21=value(65,69)
A30,A31=value(101,105)
A40,A41=value(137,141)
A50,A51=value(173,177)
A60,A61=value(209,213)
A70,A71=value(245,249)
A120,A121=value(281,285)
A130,A131=value(317,321)
A140,A141=value(353,357)
A150,A151=value(389,393)
A160,A161=value(425,429)
A170,A171=value(461,465)
A230,A231=value(497,501)
A240,A241=value(533,537)
A250,A251=value(569,573)
A260,A261=value(605,609)
A270,A271=value(641,645)
A340,A341=value(677,681)
A350,A351=value(713,717)
A360,A361=value(749,753)
A370,A371=value(785,789)
A450,A451=value(821,825)
A460,A461=value(857,861)
A470,A471=value(893,897)
A560,A561=value(929,933)
A570,A571=value(965,969)
A670,A671=value(1001,1005)

X_test=pd.DataFrame({'A10':A10,'A11':A11,'A20':A20,'A21':A21,'A30':A30,'A31':A31,'A40':A40,'A41':A41,'A50':A50,'A51':A51,'A60':A60,'A61':A61,'A70':A70,'A71':A71,
                'A120':A120,'A121':A121,'A130':A130,'A131':A131,'A140':A140,'A141':A141,'A150':A150,'A151':A151,'A160':A160,'A161':A161,'A170':A170,'A171':A71,
                'A230':A230,'A231':A231,'A240':A240,'A241':A241,'A250':A250,'A251':A251,'A260':A260,'A261':A261,'A270':A270,'A271':A271,
                'A340':A340,'A341':A341,'A350':A350,'A351':A351,'A360':A360,'A361':A361,'A370':A370,'A371':A371,
                'A450':A450,'A451':A451,'A460':A460,'A461':A461,'A470':A470,'A471':A471,
                'A560':A560,'A561':A561,'A570':A570,'A571':A571,
                'A670':A670,'A671':A671})
"""
X_test=pd.read_excel(r"C:\Users\student\Desktop\Analytics in Agri\hello.xls")
reg=LinearRegression().fit(X_train,Y_train)
y_pred=reg.predict(X_test)
y_pred=pd.DataFrame(np.array([3526.63,2995.18]))
Y_test=[2822,2585]
Y_test=pd.DataFrame(np.array(Y_test))
error=mean_squared_error(Y_test,y_pred)
rscr=r2_score(Y_test,y_pred)

coefficient=reg.coef_
intercept=reg.intercept_
