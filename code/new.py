import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


file=pd.read_excel(r"D:\Analytics in Agri\project\parameter.xls")

data = ["BSS*MAXT44", "BSS*MAXT45","BSS*MAXT46","BSS*MAXT47","BSS*MAXT48","BSS*MAXT49","BSS*MAXT50",	"BSS*MAXT51","BSS*MAXT52",	"BSS*MAXT1",	"BSS*MAXT2",	"BSS*MAXT3",	"BSS*MAXT4",	"BSS*MAXT5", "BSS*MAXT6", "BSS*MAXT7",	"BSS*MAXT8",	"BSS*MAXT9",	"BSS*MAXT10",	"BSS*MAXT11","BSS*MINT44",	"BSS*MINT45",	"BSS*MINT46",	"BSS*MINT47",	"BSS*MINT48", "BSS*MINT49",	"BSS*MINT50",	"BSS*MINT51",	"BSS*MINT52",	"BSS*MINT1",	"BSS*MINT2",	"BSS*MINT3"	,"BSS*MINT4",	"BSS*MINT5",	"BSS*MINT6",	"BSS*MINT7",	"BSS*MINT8",	"BSS*MINT9",	"BSS*MINT10", "BSS*MINT11", "BSS*RH1 44",	"BSS*RH1 45",	"BSS*RH1 46",	"BSS*RH1 47",	"BSS*RH1 48",	"BSS*RH1 49",	"BSS*RH1 50",	"BSS*RH1 51",	"BSS*RH1 52"	,"BSS*RH1 1",	"BSS*RH1 2",	"BSS*RH1 3"	,"BSS*RH1 4",	"BSS*RH1 5",	"BSS*RH1 6"	,"BSS*RH1 7",	"BSS*RH1 8",	"BSS*RH1 9",	"BSS*RH1 10"	,"BSS*RH1 11","BSS*RH2 44",	"BSS*RH2 45","BSS*RH2 46",	"BSS*RH2 47"	,"BSS*RH2 48"	,"BSS*RH2 49"	,"BSS*RH2 50",	"BSS*RH2 51"	,"BSS*RH2 52"	,"BSS*RH2 1"	,"BSS*RH2 2"	,"BSS*RH2 3"	,"BSS*RH2 4"	,"BSS*RH2 5",	"BSS*RH2 6"	,"BSS*RH2 7",	"BSS*RH2 8",	"BSS*RH2 9"	,"BSS*RH2 10"	,"BSS*RH2 11","BSS*VP1 44",	"BSS*VP1 45"	,"BSS*VP1 46",	"BSS*VP1 47",	"BSS*VP1 48",	"BSS*VP1 49"	,"BSS*VP1 50"	,"BSS*VP1 51"	,"BSS*VP1 52"	,"BSS*VP1 1"	,"BSS*VP1 2"	,"BSS*VP1 3"	,"BSS*VP1 4",	"BSS*VP1 5",	"BSS*VP1 6"	,"BSS*VP1 7"	,"BSS*VP1 8"	,"BSS*VP1 9",	"BSS*VP1 10",	"BSS*VP1 11","BSS*VP2 44",	"BSS*VP2 45"	,"BSS*VP2 46"	,"BSS*VP2 47"	,"BSS*VP2 48"	,"BSS*VP2 49",	"BSS*VP2 50"	,"BSS*VP2 51",	"BSS*VP2 52"	,"BSS*VP2 1"	,"BSS*VP2 2",	"BSS*VP2 3",	"BSS*VP2 4"	,"BSS*VP2 5"	,"BSS*VP2 6"	,"BSS*VP2 7",	"BSS*VP2 8"	,"BSS*VP2 9"	,"BSS*VP2 10"	,"BSS*VP2 11","MAXT*MINT44"	,"MAXT*MINT45"	,"MAXT*MINT46"	,"MAXT*MINT47"	,"MAXT*MINT48"	,"MAXT*MINT49"	,"MAXT*MINT50"	,"MAXT*MINT51",	"MAXT*MINT52"	,"MAXT*MINT1"	,"MAXT*MINT2",	"MAXT*MINT3"	,"MAXT*MINT4"	,"MAXT*MINT5"	,"MAXT*MINT6",	"MAXT*MINT7",	"MAXT*MINT8",	"MAXT*MINT9",	"MAXT*MINT10"	,"MAXT*MINT11","MAXT*RH1 44",	"MAXT*RH1 45"	,"MAXT*RH1 46"	,"MAXT*RH1 47",	"MAXT*RH1 48",	"MAXT*RH1 49"	,"MAXT*RH1 50"	,"MAXT*RH1 51"	,"MAXT*RH1 52"	,"MAXT*RH1 1"	,"MAXT*RH1 2",	"MAXT*RH1 3"	,"MAXT*RH1 4",	"MAXT*RH1 5"	,"MAXT*RH1 6"	,"MAXT*RH1 7"	,"MAXT*RH1 8",	"MAXT*RH1 9",	"MAXT*RH1 10",	"MAXT*RH1 11","MAXT*RH2 44",	"MAXT*RH2 45"	,"MAXT*RH2 46"	,"MAXT*RH2 47",	"MAXT*RH2 48"	,"MAXT*RH2 49"	,"MAXT*RH2 50"	,"MAXT*RH2 51",	"MAXT*RH2 52"	,"MAXT*RH2 1"	,"MAXT*RH2 2"	,"MAXT*RH2 3"	,"MAXT*RH2 4"	,"MAXT*RH2 5",	"MAXT*RH2 6",	"MAXT*RH2 7",	"MAXT*RH2 8",	"MAXT*RH2 9"	,"MAXT*RH2 10"	,"MAXT*RH2 11","MAXT*VP1 44","MAXT*VP1 45",	"MAXT*VP1 46",	"MAXT*VP1 47",	"MAXT*VP1 48"	,"MAXT*VP1 49"	,"MAXT*VP1 50"	,"MAXT*VP1 51"	,"MAXT*VP1 52"	,"MAXT*VP1 1"	,"MAXT*VP1 2",	"MAXT*VP1 3",	"MAXT*VP1 4",	"MAXT*VP1 5",	"MAXT*VP1 6",	"MAXT*VP1 7",	"MAXT*VP1 8","MAXT*VP1 9",	"MAXT*VP1 10",	"MAXT*VP1 11","MAXT*VP2 44",	"MAXT*VP2 45",	"MAXT*VP2 46",	"MAXT*VP2 47",	"MAXT*VP2 48"	,"MAXT*VP2 49",	"MAXT*VP2 50",	"MAXT*VP2 51",	"MAXT*VP2 52",	"MAXT*VP2 1"	,"MAXT*VP2 2"	,"MAXT*VP2 3"	,"MAXT*VP2 4"	,"MAXT*VP2 5"	,"MAXT*VP2 6"	,"MAXT*VP2 7",	"MAXT*VP2 8",	"MAXT*VP2 9"	,"MAXT*VP2 10"	,"MAXT*VP2 11","MINT*RH1 44",	"MINT*RH1 45",	"MINT*RH1 46",	"MINT*RH1 47",	"MINT*RH1 48",	"MINT*RH1 49",	"MINT*RH1 50"	,"MINT*RH1 51",	"MINT*RH1 52"	,"MINT*RH1 1"	,"MINT*RH1 2",	"MINT*RH1 3",	"MINT*RH1 4"	,"MINT*RH1 5"	,"MINT*RH1 6",	"MINT*RH1 7"	,"MINT*RH1 8",	"MINT*RH1 9",	"MINT*RH1 10"	,"MINT*RH1 11","MINT*RH2 44",	"MINT*RH2 45"	,"MINT*RH2 46",	"MINT*RH2 47",	"MINT*RH2 48",	"MINT*RH2 49"	,"MINT*RH2 50"	,"MINT*RH2 51",	"MINT*RH2 52",	"MINT*RH2 1",	"MINT*RH2 2"	,"MINT*RH2 3",	"MINT*RH2 4"	,"MINT*RH2 5"	,"MINT*RH2 6",	"MINT*RH2 7",	"MINT*RH2 8",	"MINT*RH2 9",	"MINT*RH2 10"	,"MINT*RH2 11","MINT*VP1 44",	"MINT*VP1 45"	,"MINT*VP1 46",	"MINT*VP1 47"	,"MINT*VP1 48",	"MINT*VP1 49"	,"MINT*VP1 50"	,"MINT*VP1 51",	"MINT*VP1 52",	"MINT*VP1 1",	"MINT*VP1 2",	"MINT*VP1 3",	"MINT*VP1 4"	,"MINT*VP1 5"	,"MINT*VP1 6"	,"MINT*VP1 7"	,"MINT*VP1 8"	,"MINT*VP1 9",	"MINT*VP1 10",	"MINT*VP1 11","MINT*VP2 44",	"MINT*VP2 45",	"MINT*VP2 46"	,"MINT*VP2 47"	,"MINT*VP2 48",	"MINT*VP2 49"	,"MINT*VP2 50",	"MINT*VP2 51"	,"MINT*VP2 52"	,"MINT*VP2 1"	,"MINT*VP2 2"	,"MINT*VP2 3"	,"MINT*VP2 4"	,"MINT*VP2 5",	"MINT*VP2 6",	"MINT*VP2 7",	"MINT*VP2 8",	"MINT*VP2 9",	"MINT*VP2 10",	"MINT*VP2 11","RH1*RH2 44",	"RH1*RH2 45",	"RH1*RH2 46",	"RH1*RH2 47",	"RH1*RH2 48"	,"RH1*RH2 49",	"RH1*RH2 50",	"RH1*RH2 51",	"RH1*RH2 52",	"RH1*RH2 1",	"RH1*RH2 2"	,"RH1*RH2 3",	"RH1*RH2 4",	"RH1*RH2 5",	"RH1*RH2 6",	"RH1*RH2 7",	"RH1*RH2 8",	"RH1*RH2 9"	,"RH1*RH2 10",	"RH1*RH2 11","RH1*VP1 44",	"RH1*VP1 45",	"RH1*VP1 46",	"RH1*VP1 47",	"RH1*VP1 48"	,"RH1*VP1 49"	,"RH1*VP1 50",	"RH1*VP1 51",	"RH1*VP1 52",	"RH1*VP1 1",	"RH1*VP1 2",	"RH1*VP1 3",	"RH1*VP1 4",	"RH1*VP1 5",	"RH1*VP1 6",	"RH1*VP1 7",	"RH1*VP1 8"	,"RH1*VP1 9",	"RH1*VP1 10",	"RH1*VP1 11","RH1*VP2 44",	"RH1*VP2 45"	,"RH1*VP2 46"	,"RH1*VP2 47"	,"RH1*VP2 48",	"RH1*VP2 49",	"RH1*VP2 50",	"RH1*VP2 51",	"RH1*VP2 52"	,"RH1*VP2 1",	"RH1*VP2 2"	,"RH1*VP2 3",	"RH1*VP2 4"	,"RH1*VP2 5",	"RH1*VP2 6",	"RH1*VP2 7",	"RH1*VP2 8",	"RH1*VP2 9",	"RH1*VP2 10",	"RH1*VP2 11","RH2*VP1 44",	"RH2*VP1 45",	"RH2*VP1 46",	"RH2*VP1 47",	"RH2*VP1 48",	"RH2*VP1 49",	"RH2*VP1 50",	"RH2*VP1 51",	"RH2*VP1 52"	,"RH2*VP1 1"	,"RH2*VP1 2"	,"RH2*VP1 3",	"RH2*VP1 4",	"RH2*VP1 5",	"RH2*VP1 6",	"RH2*VP1 7",	"RH2*VP1 8",	"RH2*VP1 9",	"RH2*VP1 10",	"RH2*VP1 11","RH2*VP2 44",	"RH2*VP2 45",	"RH2*VP2 46",	"RH2*VP2 47",	"RH2*VP2 48"	,"RH2*VP2 49",	"RH2*VP2 50",	"RH2*VP2 51",	"RH2*VP2 52"	,"RH2*VP2 1",	"RH2*VP2 2"	,"RH2*VP2 3",	"RH2*VP2 4",	"RH2*VP2 5",	"RH2*VP2 6"	,"RH2*VP2 7",	"RH2*VP2 8",	"RH2*VP2 9",	"RH2*VP2 10"	,"RH2*VP2 11","VP1*VP2 44",	"VP1*VP2 45",	"VP1*VP2 46",	"VP1*VP2 47",	"VP1*VP2 48",	"VP1*VP2 49",	"VP1*VP2 50",	"VP1*VP2 51"	,"VP1*VP2 52",	"VP1*VP2 1",	"VP1*VP2 2",	"VP1*VP2 3",	"VP1*VP2 4",	"VP1*VP2 5",	"VP1*VP2 6",	"VP1*VP2 7",	"VP1*VP2 8",	"VP1*VP2 9",	"VP1*VP2 10",	"VP1*VP2 11"]

#creating multiplication column
#bss*maxt44 to bss*vp211  
for k in range (0,6):
    for i in range(1,21):
        file[data[i-1+k*20]]=file.iloc[:,i+2]*file.iloc[:,i+22+k*20]
        
#maxt*min44 to maxt*vp211
for k in range (0,5):
    for i in range(1,21):
        file[data[i-1+k*20+120]]=file.iloc[:,i+22]*file.iloc[:,i+42+k*20]

#min*rh144 to mint*vp211
for k in range (0,4):
    for i in range(1,21):
        file[data[i-1+k*20+220]]=file.iloc[:,i+42]*file.iloc[:,i+62+k*20]        
        
#rh1*rh244 to rh1*vp211
for k in range (0,3):
    for i in range(1,21):
        file[data[i-1+k*20+300]]=file.iloc[:,i+62]*file.iloc[:,i+82+k*20]
        
#rh2*vp144 to rh2*vp211
for k in range (0,2):
    for i in range(1,21):
        file[data[i-1+k*20+360]]=file.iloc[:,i+82]*file.iloc[:,i+102+k*20]
        
#vp1*vp244 to vp1*vp211
for i in range(1,21):
    file[data[399+i]]=file.iloc[:,i+102]*file.iloc[:,i+122]
    
###############################
test=file[["YIELD","BSS*MAXT44", "BSS*MAXT45","BSS*MAXT46","BSS*MAXT47","BSS*MAXT48"]]
testcor=test.corr()[['YIELD']]
"""value of correlation betn 44,45,46,47 and yield is wrong(above column)""" 
file.set_index('Unnamed: 0',inplace=True)
col = file.columns[3:]
correlation = file.corr()[['YIELD']]
multi = file.mul(correlation.squeeze().values,axis='columns')
#index1=['Z10','Z20','Z30','Z40','Z50','Z60','Z70','Z120','Z130','Z140','Z150','Z160','Z170','Z230','Z240','Z250','Z260','Z270','Z340','Z350','Z360','Z370','Z450','Z460','Z470','Z560','Z570','Z670']


def new_data(df, i):
    N = i*20 
    new = df.T[2+N:22+N].sum(axis = 0) 
    col_name = "{}".format(i) 
    df[col_name] = new
    
for i in range(0,28): 
    new_data(multi, i) 
    new_data(file,i)

file_ = file.iloc[:,562:590]
file_.set_axis(['Z10','Z20','Z30','Z40','Z50','Z60','Z70',
                      'Z120','Z130','Z140','Z150','Z160','Z170','Z230',
                      'Z240','Z250','Z260','Z270','Z340','Z350','Z360',
                      'Z370','Z450','Z460','Z470','Z560','Z570','Z670'],
    inplace=True, axis=1)

multi_ = multi.iloc[:,562:590]
multi_.set_axis(['Z11','Z21','Z31','Z41','Z51','Z61','Z71','Z121','Z131','Z141','Z151','Z161','Z171','Z231','Z241','Z251','Z261','Z271','Z341','Z351','Z361','Z371','Z451','Z461','Z471','Z561','Z571','Z671'],
    inplace=True, axis=1)
aa = file.iloc[:,0]
aa=pd.DataFrame(aa)
newww=pd.concat([aa,file_,multi_],sort=True,axis=1)

corr = newww.corr()[['YIELD']].sort_values(['YIELD'])
corr = corr[corr['YIELD'] > 0.6]
corr = corr[corr['YIELD']<1]
para=corr.index
x_train=newww[para]
X = np.array(x_train)
Y = np.array(aa)

reg=LinearRegression().fit(X,Y)
coe=reg.coef_
intercept=reg.intercept_
y_pred=reg.predict(X)

error=mean_squared_error(Y,y_pred)
print("error:",error)

plt.scatter(Y,y_pred)
plt.show()
print('Variance score of train data: %.2f' % r2_score(Y, y_pred))
plt.plot(y_pred,'r-*')
plt.plot(Y,'b-^')
plt.gca().legend(('y_pred','y'))

#test data###########################################################################
file1=pd.read_excel(r"D:\Analytics in Agri\project\testdata.xls")

#creating multiplication column
#bss*maxt44 to bss*vp211  
for k in range (0,6):
    for i in range(1,21):
        file1[data[i-1+k*20]]=file1.iloc[:,i+2]*file1.iloc[:,i+22+k*20]
        
#maxt*min44 to maxt*vp211
for k in range (0,5):
    for i in range(1,21):
        file1[data[i-1+k*20+120]]=file1.iloc[:,i+22]*file1.iloc[:,i+42+k*20]

#min*rh144 to mint*vp211
for k in range (0,4):
    for i in range(1,21):
        file1[data[i-1+k*20+220]]=file1.iloc[:,i+42]*file1.iloc[:,i+62+k*20]        
        
#rh1*rh244 to rh1*vp211
for k in range (0,3):
    for i in range(1,21):
        file1[data[i-1+k*20+300]]=file1.iloc[:,i+62]*file1.iloc[:,i+82+k*20]
        
#rh2*vp144 to rh2*vp211
for k in range (0,2):
    for i in range(1,21):
        file1[data[i-1+k*20+360]]=file1.iloc[:,i+82]*file1.iloc[:,i+102+k*20]
        
#vp1*vp244 to vp1*vp211
for i in range(1,21):
    file1[data[399+i]]=file1.iloc[:,i+102]*file1.iloc[:,i+122]
    
file1.set_index('Unnamed: 0',inplace=True)
col1 = file1.columns[3:]
correlation1 = file.corr()[['YIELD']]
multi1 = file1.mul(correlation.squeeze().values,axis='columns')


def new_data(df, i):
    N = i*20 
    new = df.T[2+N:22+N].sum(axis = 0) 
    col_name = "{}".format(i) 
    df[col_name] = new
    
for i in range(0,28): 
    new_data(multi1, i) 
    new_data(file1,i)
    
file_test = file1.iloc[:,562:590]
file_test.set_axis(['Z10','Z20','Z30','Z40','Z50','Z60','Z70',
                      'Z120','Z130','Z140','Z150','Z160','Z170','Z230',
                      'Z240','Z250','Z260','Z270','Z340','Z350','Z360',
                      'Z370','Z450','Z460','Z470','Z560','Z570','Z670'],
    inplace=True, axis=1)

multi_test = multi1.iloc[:,562:590]
multi_test.set_axis(['Z11','Z21','Z31','Z41','Z51','Z61','Z71','Z121','Z131','Z141','Z151','Z161','Z171','Z231','Z241','Z251','Z261','Z271','Z341','Z351','Z361','Z371','Z451','Z461','Z471','Z561','Z571','Z671'],
    inplace=True, axis=1)
aa_test = file1.iloc[:,0]
aa_test=pd.DataFrame(aa_test)
newww_test=pd.concat([aa_test,file_test,multi_test],sort=True,axis=1)

X_test=newww_test[para]
X_test = np.array(X_test)
Y_test = np.array(aa_test)


reg=LinearRegression().fit(X,Y)
coe=reg.coef_
intercept=reg.intercept_
y_pred_test=reg.predict(X_test)
error_test=mean_squared_error(Y_test, y_pred_test)
print("error test : ",error_test)
print('Variance score of test data: %.2f' % r2_score(Y_test, y_pred_test))
