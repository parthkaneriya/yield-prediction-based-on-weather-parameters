import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import LinearRegression


file=pd.read_excel(r"D:\Analytics in Agri\project\parameter.xls")

data = ["BSS*MAXT44", "BSS*MAXT45","BSS*MAXT46","BSS*MAXT47","BSS*MAXT48","BSS*MAXT49","BSS*MAXT50",	"BSS*MAXT51","BSS*MAXT52",	"BSS*MAXT1",	"BSS*MAXT2",	"BSS*MAXT3",	"BSS*MAXT4",	"BSS*MAXT5", "BSS*MAXT6", "BSS*MAXT7",	"BSS*MAXT8",	"BSS*MAXT9",	"BSS*MAXT10",	"BSS*MAXT11","BSS*MINT44",	"BSS*MINT45",	"BSS*MINT46",	"BSS*MINT47",	"BSS*MINT48", "BSS*MINT49",	"BSS*MINT50",	"BSS*MINT51",	"BSS*MINT52",	"BSS*MINT1",	"BSS*MINT2",	"BSS*MINT3"	,"BSS*MINT4",	"BSS*MINT5",	"BSS*MINT6",	"BSS*MINT7",	"BSS*MINT8",	"BSS*MINT9",	"BSS*MINT10", "BSS*MINT11", "BSS*RH1 44",	"BSS*RH1 45",	"BSS*RH1 46",	"BSS*RH1 47",	"BSS*RH1 48",	"BSS*RH1 49",	"BSS*RH1 50",	"BSS*RH1 51",	"BSS*RH1 52"	,"BSS*RH1 1",	"BSS*RH1 2",	"BSS*RH1 3"	,"BSS*RH1 4",	"BSS*RH1 5",	"BSS*RH1 6"	,"BSS*RH1 7",	"BSS*RH1 8",	"BSS*RH1 9",	"BSS*RH1 10"	,"BSS*RH1 11","BSS*RH2 44",	"BSS*RH2 45","BSS*RH2 46",	"BSS*RH2 47"	,"BSS*RH2 48"	,"BSS*RH2 49"	,"BSS*RH2 50",	"BSS*RH2 51"	,"BSS*RH2 52"	,"BSS*RH2 1"	,"BSS*RH2 2"	,"BSS*RH2 3"	,"BSS*RH2 4"	,"BSS*RH2 5",	"BSS*RH2 6"	,"BSS*RH2 7",	"BSS*RH2 8",	"BSS*RH2 9"	,"BSS*RH2 10"	,"BSS*RH2 11","BSS*VP1 44",	"BSS*VP1 45"	,"BSS*VP1 46",	"BSS*VP1 47",	"BSS*VP1 48",	"BSS*VP1 49"	,"BSS*VP1 50"	,"BSS*VP1 51"	,"BSS*VP1 52"	,"BSS*VP1 1"	,"BSS*VP1 2"	,"BSS*VP1 3"	,"BSS*VP1 4",	"BSS*VP1 5",	"BSS*VP1 6"	,"BSS*VP1 7"	,"BSS*VP1 8"	,"BSS*VP1 9",	"BSS*VP1 10",	"BSS*VP1 11","BSS*VP2 44",	"BSS*VP2 45"	,"BSS*VP2 46"	,"BSS*VP2 47"	,"BSS*VP2 48"	,"BSS*VP2 49",	"BSS*VP2 50"	,"BSS*VP2 51",	"BSS*VP2 52"	,"BSS*VP2 1"	,"BSS*VP2 2",	"BSS*VP2 3",	"BSS*VP2 4"	,"BSS*VP2 5"	,"BSS*VP2 6"	,"BSS*VP2 7",	"BSS*VP2 8"	,"BSS*VP2 9"	,"BSS*VP2 10"	,"BSS*VP2 11","MAXT*MINT44"	,"MAXT*MINT45"	,"MAXT*MINT46"	,"MAXT*MINT47"	,"MAXT*MINT48"	,"MAXT*MINT49"	,"MAXT*MINT50"	,"MAXT*MINT51",	"MAXT*MINT52"	,"MAXT*MINT1"	,"MAXT*MINT2",	"MAXT*MINT3"	,"MAXT*MINT4"	,"MAXT*MINT5"	,"MAXT*MINT6",	"MAXT*MINT7",	"MAXT*MINT8",	"MAXT*MINT9",	"MAXT*MINT10"	,"MAXT*MINT11","MAXT*RH1 44",	"MAXT*RH1 45"	,"MAXT*RH1 46"	,"MAXT*RH1 47",	"MAXT*RH1 48",	"MAXT*RH1 49"	,"MAXT*RH1 50"	,"MAXT*RH1 51"	,"MAXT*RH1 52"	,"MAXT*RH1 1"	,"MAXT*RH1 2",	"MAXT*RH1 3"	,"MAXT*RH1 4",	"MAXT*RH1 5"	,"MAXT*RH1 6"	,"MAXT*RH1 7"	,"MAXT*RH1 8",	"MAXT*RH1 9",	"MAXT*RH1 10",	"MAXT*RH1 11","MAXT*RH2 44",	"MAXT*RH2 45"	,"MAXT*RH2 46"	,"MAXT*RH2 47",	"MAXT*RH2 48"	,"MAXT*RH2 49"	,"MAXT*RH2 50"	,"MAXT*RH2 51",	"MAXT*RH2 52"	,"MAXT*RH2 1"	,"MAXT*RH2 2"	,"MAXT*RH2 3"	,"MAXT*RH2 4"	,"MAXT*RH2 5",	"MAXT*RH2 6",	"MAXT*RH2 7",	"MAXT*RH2 8",	"MAXT*RH2 9"	,"MAXT*RH2 10"	,"MAXT*RH2 11","MAXT*VP1 44","MAXT*VP1 45",	"MAXT*VP1 46",	"MAXT*VP1 47",	"MAXT*VP1 48"	,"MAXT*VP1 49"	,"MAXT*VP1 50"	,"MAXT*VP1 51"	,"MAXT*VP1 52"	,"MAXT*VP1 1"	,"MAXT*VP1 2",	"MAXT*VP1 3",	"MAXT*VP1 4",	"MAXT*VP1 5",	"MAXT*VP1 6",	"MAXT*VP1 7",	"MAXT*VP1 8","MAXT*VP1 9",	"MAXT*VP1 10",	"MAXT*VP1 11","MAXT*VP2 44",	"MAXT*VP2 45",	"MAXT*VP2 46",	"MAXT*VP2 47",	"MAXT*VP2 48"	,"MAXT*VP2 49",	"MAXT*VP2 50",	"MAXT*VP2 51",	"MAXT*VP2 52",	"MAXT*VP2 1"	,"MAXT*VP2 2"	,"MAXT*VP2 3"	,"MAXT*VP2 4"	,"MAXT*VP2 5"	,"MAXT*VP2 6"	,"MAXT*VP2 7",	"MAXT*VP2 8",	"MAXT*VP2 9"	,"MAXT*VP2 10"	,"MAXT*VP2 11","MINT*RH1 44",	"MINT*RH1 45",	"MINT*RH1 46",	"MINT*RH1 47",	"MINT*RH1 48",	"MINT*RH1 49",	"MINT*RH1 50"	,"MINT*RH1 51",	"MINT*RH1 52"	,"MINT*RH1 1"	,"MINT*RH1 2",	"MINT*RH1 3",	"MINT*RH1 4"	,"MINT*RH1 5"	,"MINT*RH1 6",	"MINT*RH1 7"	,"MINT*RH1 8",	"MINT*RH1 9",	"MINT*RH1 10"	,"MINT*RH1 11","MINT*RH2 44",	"MINT*RH2 45"	,"MINT*RH2 46",	"MINT*RH2 47",	"MINT*RH2 48",	"MINT*RH2 49"	,"MINT*RH2 50"	,"MINT*RH2 51",	"MINT*RH2 52",	"MINT*RH2 1",	"MINT*RH2 2"	,"MINT*RH2 3",	"MINT*RH2 4"	,"MINT*RH2 5"	,"MINT*RH2 6",	"MINT*RH2 7",	"MINT*RH2 8",	"MINT*RH2 9",	"MINT*RH2 10"	,"MINT*RH2 11","MINT*VP1 44",	"MINT*VP1 45"	,"MINT*VP1 46",	"MINT*VP1 47"	,"MINT*VP1 48",	"MINT*VP1 49"	,"MINT*VP1 50"	,"MINT*VP1 51",	"MINT*VP1 52",	"MINT*VP1 1",	"MINT*VP1 2",	"MINT*VP1 3",	"MINT*VP1 4"	,"MINT*VP1 5"	,"MINT*VP1 6"	,"MINT*VP1 7"	,"MINT*VP1 8"	,"MINT*VP1 9",	"MINT*VP1 10",	"MINT*VP1 11","MINT*VP2 44",	"MINT*VP2 45",	"MINT*VP2 46"	,"MINT*VP2 47"	,"MINT*VP2 48",	"MINT*VP2 49"	,"MINT*VP2 50",	"MINT*VP2 51"	,"MINT*VP2 52"	,"MINT*VP2 1"	,"MINT*VP2 2"	,"MINT*VP2 3"	,"MINT*VP2 4"	,"MINT*VP2 5",	"MINT*VP2 6",	"MINT*VP2 7",	"MINT*VP2 8",	"MINT*VP2 9",	"MINT*VP2 10",	"MINT*VP2 11","RH1*RH2 44",	"RH1*RH2 45",	"RH1*RH2 46",	"RH1*RH2 47",	"RH1*RH2 48"	,"RH1*RH2 49",	"RH1*RH2 50",	"RH1*RH2 51",	"RH1*RH2 52",	"RH1*RH2 1",	"RH1*RH2 2"	,"RH1*RH2 3",	"RH1*RH2 4",	"RH1*RH2 5",	"RH1*RH2 6",	"RH1*RH2 7",	"RH1*RH2 8",	"RH1*RH2 9"	,"RH1*RH2 10",	"RH1*RH2 11","RH1*VP1 44",	"RH1*VP1 45",	"RH1*VP1 46",	"RH1*VP1 47",	"RH1*VP1 48"	,"RH1*VP1 49"	,"RH1*VP1 50",	"RH1*VP1 51",	"RH1*VP1 52",	"RH1*VP1 1",	"RH1*VP1 2",	"RH1*VP1 3",	"RH1*VP1 4",	"RH1*VP1 5",	"RH1*VP1 6",	"RH1*VP1 7",	"RH1*VP1 8"	,"RH1*VP1 9",	"RH1*VP1 10",	"RH1*VP1 11","RH1*VP2 44",	"RH1*VP2 45"	,"RH1*VP2 46"	,"RH1*VP2 47"	,"RH1*VP2 48",	"RH1*VP2 49",	"RH1*VP2 50",	"RH1*VP2 51",	"RH1*VP2 52"	,"RH1*VP2 1",	"RH1*VP2 2"	,"RH1*VP2 3",	"RH1*VP2 4"	,"RH1*VP2 5",	"RH1*VP2 6",	"RH1*VP2 7",	"RH1*VP2 8",	"RH1*VP2 9",	"RH1*VP2 10",	"RH1*VP2 11","RH2*VP1 44",	"RH2*VP1 45",	"RH2*VP1 46",	"RH2*VP1 47",	"RH2*VP1 48",	"RH2*VP1 49",	"RH2*VP1 50",	"RH2*VP1 51",	"RH2*VP1 52"	,"RH2*VP1 1"	,"RH2*VP1 2"	,"RH2*VP1 3",	"RH2*VP1 4",	"RH2*VP1 5",	"RH2*VP1 6",	"RH2*VP1 7",	"RH2*VP1 8",	"RH2*VP1 9",	"RH2*VP1 10",	"RH2*VP1 11","RH2*VP2 44",	"RH2*VP2 45",	"RH2*VP2 46",	"RH2*VP2 47",	"RH2*VP2 48"	,"RH2*VP2 49",	"RH2*VP2 50",	"RH2*VP2 51",	"RH2*VP2 52"	,"RH2*VP2 1",	"RH2*VP2 2"	,"RH2*VP2 3",	"RH2*VP2 4",	"RH2*VP2 5",	"RH2*VP2 6"	,"RH2*VP2 7",	"RH2*VP2 8",	"RH2*VP2 9",	"RH2*VP2 10"	,"RH2*VP2 11","VP1*VP2 44",	"VP1*VP2 45",	"VP1*VP2 46",	"VP1*VP2 47",	"VP1*VP2 48",	"VP1*VP2 49",	"VP1*VP2 50",	"VP1*VP2 51"	,"VP1*VP2 52",	"VP1*VP2 1",	"VP1*VP2 2",	"VP1*VP2 3",	"VP1*VP2 4",	"VP1*VP2 5",	"VP1*VP2 6",	"VP1*VP2 7",	"VP1*VP2 8",	"VP1*VP2 9",	"VP1*VP2 10",	"VP1*VP2 11"]

#creating multiplication column
#bss*maxt44 to bss*vp211    
for i in range(1,21):
    file[data[i-1]]=file.iloc[:,i+2]*file.iloc[:,i+22]

for i in range(1,21):
    file[data[19+i]]=file.iloc[:,i+2]*file.iloc[:,i+42]
    
for i in range(1,21):
    file[data[39+i]]=file.iloc[:,i+2]*file.iloc[:,i+62]
    
for i in range(1,21):
    file[data[59+i]]=file.iloc[:,i+2]*file.iloc[:,i+82]

for i in range(1,21):
    file[data[79+i]]=file.iloc[:,i+2]*file.iloc[:,i+102]
    
for i in range(1,21):
    file[data[99+i]]=file.iloc[:,i+2]*file.iloc[:,i+122]

#maxt*min44 to maxt*vp211
for i in range(1,21):
    file[data[119+i]]=file.iloc[:,i+22]*file.iloc[:,i+42]
    
for i in range(1,21):
    file[data[139+i]]=file.iloc[:,i+22]*file.iloc[:,i+62]

for i in range(1,21):
    file[data[159+i]]=file.iloc[:,i+22]*file.iloc[:,i+82]

for i in range(1,21):
    file[data[179+i]]=file.iloc[:,i+22]*file.iloc[:,i+102]
    
for i in range(1,21):
    file[data[199+i]]=file.iloc[:,i+22]*file.iloc[:,i+122]
#min*rh144 to mint*vp211
for i in range(1,21):
    file[data[219+i]]=file.iloc[:,i+42]*file.iloc[:,i+62]
    
for i in range(1,21):
    file[data[239+i]]=file.iloc[:,i+42]*file.iloc[:,i+82]
        
for i in range(1,21):
    file[data[259+i]]=file.iloc[:,i+42]*file.iloc[:,i+102]
    
for i in range(1,21):
    file[data[279+i]]=file.iloc[:,i+42]*file.iloc[:,i+122]
    
#rh1*rh244 to rh1*vp211
for i in range(1,21):
    file[data[299+i]]=file.iloc[:,i+62]*file.iloc[:,i+82]
    
for i in range(1,21):
    file[data[319+i]]=file.iloc[:,i+62]*file.iloc[:,i+102]

for i in range(1,21):
    file[data[339+i]]=file.iloc[:,i+62]*file.iloc[:,i+122]
    
#rh2*vp144 to rh2*vp211
for i in range(1,21):
    file[data[359+i]]=file.iloc[:,i+82]*file.iloc[:,i+102]
    
for i in range(1,21):
    file[data[379+i]]=file.iloc[:,i+82]*file.iloc[:,i+122]

#vp1*vp244 to vp1*vp211
for i in range(1,21):
    file[data[399+i]]=file.iloc[:,i+102]*file.iloc[:,i+122]



#creating sum of data column,ex Z10
data1=['Z10','Z20','Z30','Z40','Z50','Z60','Z70','Z120','Z130','Z140','Z150','Z160','Z170','Z230','Z240','Z250','Z260','Z270','Z340','Z350','Z360','Z370','Z450','Z460','Z470','Z560','Z570','Z670']
#creating zero value column
for k in range(0,28):
    file[data1[k]]=np.zeros(shape=(27,1)) 
"""
for k in range(0,28):        
    for i in range(0,27):
        for l in range(-17,523,20):
            x=l+20
            y=l+40
        for j in range(x,y):
            file[data1[k]][i]+=file.iloc[i,j]


"""
for i in range(0,27):
    for j in range(3,23):
        file[data1[0]][i]+=file.iloc[i,j]
        
for i in range(0,27):
    for j in range(23,43):
        file[data1[1]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(43,63):
        file[data1[2]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(63,83):
        file[data1[3]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(83,103):
        file[data1[4]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(103,123):
        file[data1[5]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(123,143):
        file[data1[6]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(143,163):
        file[data1[7]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(163,183):
        file[data1[8]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(183,203):
        file[data1[9]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(203,223):
        file[data1[10]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(223,243):
        file[data1[11]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(243,263):
        file[data1[12]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(263,283):
        file[data1[13]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(283,303):
        file[data1[14]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(303,323):
        file[data1[15]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(323,343):
        file[data1[16]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(343,363):
        file[data1[17]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(363,383):
        file[data1[18]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(383,403):
        file[data1[19]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(403,423):
        file[data1[20]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(423,443):
        file[data1[21]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(443,463):
        file[data1[22]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(463,483):
        file[data1[23]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(483,503):
        file[data1[24]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(503,523):
        file[data1[25]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(523,543):
        file[data1[26]][i]+=file.iloc[i,j]

for i in range(0,27):
    for j in range(543,563):
        file[data1[27]][i]+=file.iloc[i,j]


#to find corelation
corre=file.corr()[["YIELD"]]
corre=corre.drop(corre.index[562:])
corre=corre.transpose()
file=file.append(corre, ignore_index=True,sort=False)


#calculate sum product of correlation

data2=['Z11','Z21','Z31','Z41','Z51','Z61','Z71','Z121','Z131','Z141','Z151','Z161','Z171','Z231','Z241','Z251','Z261','Z271','Z341','Z351','Z361','Z371','Z451','Z461','Z471','Z561','Z571','Z671']
#creating zero value column
for k in range(0,28):
    file[data2[k]]=np.zeros(shape=(28,1)) 
  
#fhgfh    
for i in range(0,27):
    for j in range(3,23):
        file[data2[0]][i]+=file.iloc[i,j]*file.iloc[27,j]
        
for i in range(0,27):
    for j in range(23,43):
        file[data2[1]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(43,63):
        file[data2[2]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(63,83):
        file[data2[3]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(83,103):
        file[data2[4]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(103,123):
        file[data2[5]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(123,143):
        file[data2[6]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(143,163):
        file[data2[7]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(163,183):
        file[data2[8]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(183,203):
        file[data2[9]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(203,223):
        file[data2[10]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(223,243):
        file[data2[11]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(243,263):
        file[data2[12]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(263,283):
        file[data2[13]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(283,303):
        file[data2[14]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(303,323):
        file[data2[15]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(323,343):
        file[data2[16]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(343,363):
        file[data2[17]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(363,383):
        file[data2[18]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(383,403):
        file[data2[19]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(403,423):
        file[data2[20]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(423,443):
        file[data2[21]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(443,463):
        file[data2[22]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(463,483):
        file[data2[23]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(483,503):
        file[data2[24]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(503,523):
        file[data2[25]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(523,543):
        file[data2[26]][i]+=file.iloc[i,j]*file.iloc[27,j]

for i in range(0,27):
    for j in range(543,563):
        file[data2[27]][i]+=file.iloc[i,j]*file.iloc[27,j]
        

#train data
X_train=file.iloc[0:27,563:620]
Y_train=pd.DataFrame(file.iloc[0:27,1])

#test data
file1=pd.read_excel(r"D:\Analytics in Agri\project\testdata.xls")
data = ["BSS*MAX44", "BSS*MAXT45","BSS*MAXT46","BSS*MAXT47","BSS*MAXT48","BSS*MAXT49","BSS*MAXT50",	"BSS*MAXT51","BSS*MAXT52",	"BSS*MAXT1",	"BSS*MAXT2",	"BSS*MAXT3",	"BSS*MAXT4",	"BSS*MAXT5", "BSS*MAXT6", "BSS*MAXT7",	"BSS*MAXT8",	"BSS*MAXT9",	"BSS*MAXT10",	"BSS*MAXT11","BSS*MINT44",	"BSS*MINT45",	"BSS*MINT46",	"BSS*MINT47",	"BSS*MINT48", "BSS*MINT49",	"BSS*MINT50",	"BSS*MINT51",	"BSS*MINT52",	"BSS*MINT1",	"BSS*MINT2",	"BSS*MINT3"	,"BSS*MINT4",	"BSS*MINT5",	"BSS*MINT6",	"BSS*MINT7",	"BSS*MINT8",	"BSS*MINT9",	"BSS*MINT10", "BSS*MINT11", "BSS*RH1 44",	"BSS*RH1 45",	"BSS*RH1 46",	"BSS*RH1 47",	"BSS*RH1 48",	"BSS*RH1 49",	"BSS*RH1 50",	"BSS*RH1 51",	"BSS*RH1 52"	,"BSS*RH1 1",	"BSS*RH1 2",	"BSS*RH1 3"	,"BSS*RH1 4",	"BSS*RH1 5",	"BSS*RH1 6"	,"BSS*RH1 7",	"BSS*RH1 8",	"BSS*RH1 9",	"BSS*RH1 10"	,"BSS*RH1 11","BSS*RH2 44",	"BSS*RH2 45","BSS*RH2 46",	"BSS*RH2 47"	,"BSS*RH2 48"	,"BSS*RH2 49"	,"BSS*RH2 50",	"BSS*RH2 51"	,"BSS*RH2 52"	,"BSS*RH2 1"	,"BSS*RH2 2"	,"BSS*RH2 3"	,"BSS*RH2 4"	,"BSS*RH2 5",	"BSS*RH2 6"	,"BSS*RH2 7",	"BSS*RH2 8",	"BSS*RH2 9"	,"BSS*RH2 10"	,"BSS*RH2 11","BSS*VP1 44",	"BSS*VP1 45"	,"BSS*VP1 46",	"BSS*VP1 47",	"BSS*VP1 48",	"BSS*VP1 49"	,"BSS*VP1 50"	,"BSS*VP1 51"	,"BSS*VP1 52"	,"BSS*VP1 1"	,"BSS*VP1 2"	,"BSS*VP1 3"	,"BSS*VP1 4",	"BSS*VP1 5",	"BSS*VP1 6"	,"BSS*VP1 7"	,"BSS*VP1 8"	,"BSS*VP1 9",	"BSS*VP1 10",	"BSS*VP1 11","BSS*VP2 44",	"BSS*VP2 45"	,"BSS*VP2 46"	,"BSS*VP2 47"	,"BSS*VP2 48"	,"BSS*VP2 49",	"BSS*VP2 50"	,"BSS*VP2 51",	"BSS*VP2 52"	,"BSS*VP2 1"	,"BSS*VP2 2",	"BSS*VP2 3",	"BSS*VP2 4"	,"BSS*VP2 5"	,"BSS*VP2 6"	,"BSS*VP2 7",	"BSS*VP2 8"	,"BSS*VP2 9"	,"BSS*VP2 10"	,"BSS*VP2 11","MAXT*MINT44"	,"MAXT*MINT45"	,"MAXT*MINT46"	,"MAXT*MINT47"	,"MAXT*MINT48"	,"MAXT*MINT49"	,"MAXT*MINT50"	,"MAXT*MINT51",	"MAXT*MINT52"	,"MAXT*MINT1"	,"MAXT*MINT2",	"MAXT*MINT3"	,"MAXT*MINT4"	,"MAXT*MINT5"	,"MAXT*MINT6",	"MAXT*MINT7",	"MAXT*MINT8",	"MAXT*MINT9",	"MAXT*MINT10"	,"MAXT*MINT11","MAXT*RH1 44",	"MAXT*RH1 45"	,"MAXT*RH1 46"	,"MAXT*RH1 47",	"MAXT*RH1 48",	"MAXT*RH1 49"	,"MAXT*RH1 50"	,"MAXT*RH1 51"	,"MAXT*RH1 52"	,"MAXT*RH1 1"	,"MAXT*RH1 2",	"MAXT*RH1 3"	,"MAXT*RH1 4",	"MAXT*RH1 5"	,"MAXT*RH1 6"	,"MAXT*RH1 7"	,"MAXT*RH1 8",	"MAXT*RH1 9",	"MAXT*RH1 10",	"MAXT*RH1 11","MAXT*RH2 44",	"MAXT*RH2 45"	,"MAXT*RH2 46"	,"MAXT*RH2 47",	"MAXT*RH2 48"	,"MAXT*RH2 49"	,"MAXT*RH2 50"	,"MAXT*RH2 51",	"MAXT*RH2 52"	,"MAXT*RH2 1"	,"MAXT*RH2 2"	,"MAXT*RH2 3"	,"MAXT*RH2 4"	,"MAXT*RH2 5",	"MAXT*RH2 6",	"MAXT*RH2 7",	"MAXT*RH2 8",	"MAXT*RH2 9"	,"MAXT*RH2 10"	,"MAXT*RH2 11","MAXT*VP1 44","MAXT*VP1 45",	"MAXT*VP1 46",	"MAXT*VP1 47",	"MAXT*VP1 48"	,"MAXT*VP1 49"	,"MAXT*VP1 50"	,"MAXT*VP1 51"	,"MAXT*VP1 52"	,"MAXT*VP1 1"	,"MAXT*VP1 2",	"MAXT*VP1 3",	"MAXT*VP1 4",	"MAXT*VP1 5",	"MAXT*VP1 6",	"MAXT*VP1 7",	"MAXT*VP1 8","MAXT*VP1 9",	"MAXT*VP1 10",	"MAXT*VP1 11","MAXT*VP2 44",	"MAXT*VP2 45",	"MAXT*VP2 46",	"MAXT*VP2 47",	"MAXT*VP2 48"	,"MAXT*VP2 49",	"MAXT*VP2 50",	"MAXT*VP2 51",	"MAXT*VP2 52",	"MAXT*VP2 1"	,"MAXT*VP2 2"	,"MAXT*VP2 3"	,"MAXT*VP2 4"	,"MAXT*VP2 5"	,"MAXT*VP2 6"	,"MAXT*VP2 7",	"MAXT*VP2 8",	"MAXT*VP2 9"	,"MAXT*VP2 10"	,"MAXT*VP2 11","MINT*RH1 44",	"MINT*RH1 45",	"MINT*RH1 46",	"MINT*RH1 47",	"MINT*RH1 48",	"MINT*RH1 49",	"MINT*RH1 50"	,"MINT*RH1 51",	"MINT*RH1 52"	,"MINT*RH1 1"	,"MINT*RH1 2",	"MINT*RH1 3",	"MINT*RH1 4"	,"MINT*RH1 5"	,"MINT*RH1 6",	"MINT*RH1 7"	,"MINT*RH1 8",	"MINT*RH1 9",	"MINT*RH1 10"	,"MINT*RH1 11","MINT*RH2 44",	"MINT*RH2 45"	,"MINT*RH2 46",	"MINT*RH2 47",	"MINT*RH2 48",	"MINT*RH2 49"	,"MINT*RH2 50"	,"MINT*RH2 51",	"MINT*RH2 52",	"MINT*RH2 1",	"MINT*RH2 2"	,"MINT*RH2 3",	"MINT*RH2 4"	,"MINT*RH2 5"	,"MINT*RH2 6",	"MINT*RH2 7",	"MINT*RH2 8",	"MINT*RH2 9",	"MINT*RH2 10"	,"MINT*RH2 11","MINT*VP1 44",	"MINT*VP1 45"	,"MINT*VP1 46",	"MINT*VP1 47"	,"MINT*VP1 48",	"MINT*VP1 49"	,"MINT*VP1 50"	,"MINT*VP1 51",	"MINT*VP1 52",	"MINT*VP1 1",	"MINT*VP1 2",	"MINT*VP1 3",	"MINT*VP1 4"	,"MINT*VP1 5"	,"MINT*VP1 6"	,"MINT*VP1 7"	,"MINT*VP1 8"	,"MINT*VP1 9",	"MINT*VP1 10",	"MINT*VP1 11","MINT*VP2 44",	"MINT*VP2 45",	"MINT*VP2 46"	,"MINT*VP2 47"	,"MINT*VP2 48",	"MINT*VP2 49"	,"MINT*VP2 50",	"MINT*VP2 51"	,"MINT*VP2 52"	,"MINT*VP2 1"	,"MINT*VP2 2"	,"MINT*VP2 3"	,"MINT*VP2 4"	,"MINT*VP2 5",	"MINT*VP2 6",	"MINT*VP2 7",	"MINT*VP2 8",	"MINT*VP2 9",	"MINT*VP2 10",	"MINT*VP2 11","RH1*RH2 44",	"RH1*RH2 45",	"RH1*RH2 46",	"RH1*RH2 47",	"RH1*RH2 48"	,"RH1*RH2 49",	"RH1*RH2 50",	"RH1*RH2 51",	"RH1*RH2 52",	"RH1*RH2 1",	"RH1*RH2 2"	,"RH1*RH2 3",	"RH1*RH2 4",	"RH1*RH2 5",	"RH1*RH2 6",	"RH1*RH2 7",	"RH1*RH2 8",	"RH1*RH2 9"	,"RH1*RH2 10",	"RH1*RH2 11","RH1*VP1 44",	"RH1*VP1 45",	"RH1*VP1 46",	"RH1*VP1 47",	"RH1*VP1 48"	,"RH1*VP1 49"	,"RH1*VP1 50",	"RH1*VP1 51",	"RH1*VP1 52",	"RH1*VP1 1",	"RH1*VP1 2",	"RH1*VP1 3",	"RH1*VP1 4",	"RH1*VP1 5",	"RH1*VP1 6",	"RH1*VP1 7",	"RH1*VP1 8"	,"RH1*VP1 9",	"RH1*VP1 10",	"RH1*VP1 11","RH1*VP2 44",	"RH1*VP2 45"	,"RH1*VP2 46"	,"RH1*VP2 47"	,"RH1*VP2 48",	"RH1*VP2 49",	"RH1*VP2 50",	"RH1*VP2 51",	"RH1*VP2 52"	,"RH1*VP2 1",	"RH1*VP2 2"	,"RH1*VP2 3",	"RH1*VP2 4"	,"RH1*VP2 5",	"RH1*VP2 6",	"RH1*VP2 7",	"RH1*VP2 8",	"RH1*VP2 9",	"RH1*VP2 10",	"RH1*VP2 11","RH2*VP1 44",	"RH2*VP1 45",	"RH2*VP1 46",	"RH2*VP1 47",	"RH2*VP1 48",	"RH2*VP1 49",	"RH2*VP1 50",	"RH2*VP1 51",	"RH2*VP1 52"	,"RH2*VP1 1"	,"RH2*VP1 2"	,"RH2*VP1 3",	"RH2*VP1 4",	"RH2*VP1 5",	"RH2*VP1 6",	"RH2*VP1 7",	"RH2*VP1 8",	"RH2*VP1 9",	"RH2*VP1 10",	"RH2*VP1 11","RH2*VP2 44",	"RH2*VP2 45",	"RH2*VP2 46",	"RH2*VP2 47",	"RH2*VP2 48"	,"RH2*VP2 49",	"RH2*VP2 50",	"RH2*VP2 51",	"RH2*VP2 52"	,"RH2*VP2 1",	"RH2*VP2 2"	,"RH2*VP2 3",	"RH2*VP2 4",	"RH2*VP2 5",	"RH2*VP2 6"	,"RH2*VP2 7",	"RH2*VP2 8",	"RH2*VP2 9",	"RH2*VP2 10"	,"RH2*VP2 11","VP1*VP2 44",	"VP1*VP2 45",	"VP1*VP2 46",	"VP1*VP2 47",	"VP1*VP2 48",	"VP1*VP2 49",	"VP1*VP2 50",	"VP1*VP2 51"	,"VP1*VP2 52",	"VP1*VP2 1",	"VP1*VP2 2",	"VP1*VP2 3",	"VP1*VP2 4",	"VP1*VP2 5",	"VP1*VP2 6",	"VP1*VP2 7",	"VP1*VP2 8",	"VP1*VP2 9",	"VP1*VP2 10",	"VP1*VP2 11"]

for i in range(1,21):
    file1[data[i-1]]=file1.iloc[:,i+2]*file1.iloc[:,i+22]

for i in range(1,21):
    file1[data[19+i]]=file1.iloc[:,i+2]*file1.iloc[:,i+42]
    
for i in range(1,21):
    file1[data[39+i]]=file1.iloc[:,i+2]*file1.iloc[:,i+62]
    
for i in range(1,21):
    file1[data[59+i]]=file1.iloc[:,i+2]*file1.iloc[:,i+82]

for i in range(1,21):
    file1[data[79+i]]=file1.iloc[:,i+2]*file1.iloc[:,i+102]
    
for i in range(1,21):
    file1[data[99+i]]=file1.iloc[:,i+2]*file1.iloc[:,i+122]

#maxt*min44 to maxt*vp211
for i in range(1,21):
    file1[data[119+i]]=file1.iloc[:,i+22]*file1.iloc[:,i+42]
    
for i in range(1,21):
    file1[data[139+i]]=file1.iloc[:,i+22]*file1.iloc[:,i+62]

for i in range(1,21):
    file1[data[159+i]]=file1.iloc[:,i+22]*file1.iloc[:,i+82]

for i in range(1,21):
    file1[data[179+i]]=file1.iloc[:,i+22]*file1.iloc[:,i+102]
    
for i in range(1,21):
    file1[data[199+i]]=file1.iloc[:,i+22]*file1.iloc[:,i+122]
#min*rh144 to mint*vp211
for i in range(1,21):
    file1[data[219+i]]=file1.iloc[:,i+42]*file1.iloc[:,i+62]
    
for i in range(1,21):
    file1[data[239+i]]=file1.iloc[:,i+42]*file1.iloc[:,i+82]
        
for i in range(1,21):
    file1[data[259+i]]=file1.iloc[:,i+42]*file1.iloc[:,i+102]
    
for i in range(1,21):
    file1[data[279+i]]=file1.iloc[:,i+42]*file1.iloc[:,i+122]
    
#rh1*rh244 to rh1*vp211
for i in range(1,21):
    file1[data[299+i]]=file1.iloc[:,i+62]*file1.iloc[:,i+82]
    
for i in range(1,21):
    file1[data[319+i]]=file1.iloc[:,i+62]*file1.iloc[:,i+102]

for i in range(1,21):
    file1[data[339+i]]=file1.iloc[:,i+62]*file1.iloc[:,i+122]
    
#rh2*vp144 to rh2*vp211
for i in range(1,21):
    file1[data[359+i]]=file1.iloc[:,i+82]*file1.iloc[:,i+102]
    
for i in range(1,21):
    file1[data[379+i]]=file1.iloc[:,i+82]*file1.iloc[:,i+122]

#vp1*vp244 to vp1*vp211
for i in range(1,21):
    file1[data[399+i]]=file1.iloc[:,i+102]*file1.iloc[:,i+122]

#creating sum of data column,ex Z10
data1=['Z10','Z20','Z30','Z40','Z50','Z60','Z70','Z120','Z130','Z140','Z150','Z160','Z170','Z230','Z240','Z250','Z260','Z270','Z340','Z350','Z360','Z370','Z450','Z460','Z470','Z560','Z570','Z670']
#creating zero value column
for k in range(0,28):
    file1[data1[k]]=np.zeros(shape=(2,1)) 
    
#gudfhgh
for i in range(0,2):
    for j in range(3,23):
        file1[data1[0]][i]+=file1.iloc[i,j]
        
for i in range(0,2):
    for j in range(23,43):
        file1[data1[1]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(43,63):
        file1[data1[2]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(63,83):
        file1[data1[3]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(83,103):
        file1[data1[4]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(103,123):
        file1[data1[5]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(123,143):
        file1[data1[6]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(143,163):
        file1[data1[7]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(163,183):
        file1[data1[8]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(183,203):
        file1[data1[9]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(203,223):
        file1[data1[10]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(223,243):
        file1[data1[11]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(243,263):
        file1[data1[12]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(263,283):
        file1[data1[13]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(283,303):
        file1[data1[14]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(303,323):
        file1[data1[15]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(323,343):
        file1[data1[16]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(343,363):
        file1[data1[17]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(363,383):
        file1[data1[18]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(383,403):
        file1[data1[19]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(403,423):
        file1[data1[20]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(423,443):
        file1[data1[21]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(443,463):
        file1[data1[22]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(463,483):
        file1[data1[23]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(483,503):
        file1[data1[24]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(503,523):
        file1[data1[25]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(523,543):
        file1[data1[26]][i]+=file1.iloc[i,j]

for i in range(0,2):
    for j in range(543,563):
        file1[data1[27]][i]+=file1.iloc[i,j]



#to find corelation

file1=file1.append(corre, ignore_index=True,sort=False)

#creating zero value column
for k in range(0,28):
    file1[data2[k]]=np.zeros(shape=(3,1)) 

for i in range(0,2):
    for j in range(3,23):
        file1[data2[0]][i]+=file1.iloc[i,j]*file1.iloc[2,j]
        
for i in range(0,2):
    for j in range(23,43):
        file1[data2[1]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(43,63):
        file1[data2[2]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(63,83):
        file1[data2[3]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(83,103):
        file1[data2[4]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(103,123):
        file1[data2[5]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(123,143):
        file1[data2[6]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(143,163):
        file1[data2[7]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(163,183):
        file1[data2[8]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(183,203):
        file1[data2[9]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(203,223):
        file1[data2[10]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(223,243):
        file1[data2[11]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(243,263):
        file1[data2[12]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(263,283):
        file1[data2[13]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(283,303):
        file1[data2[14]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(303,323):
        file1[data2[15]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(323,343):
        file1[data2[16]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(343,363):
        file1[data2[17]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(363,383):
        file1[data2[18]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(383,403):
        file1[data2[19]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(403,423):
        file1[data2[20]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(423,443):
        file1[data2[21]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(443,463):
        file1[data2[22]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(463,483):
        file1[data2[23]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(483,503):
        file1[data2[24]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(503,523):
        file1[data2[25]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(523,543):
        file1[data2[26]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

for i in range(0,2):
    for j in range(543,563):
        file1[data2[27]][i]+=file1.iloc[i,j]*file1.iloc[2,j]

X_test=file1.iloc[0:2,563:620]
Y_test=pd.DataFrame(file1.iloc[0:2,1])


reg=LinearRegression().fit(X_train,Y_train)
y_pred=reg.predict(X_test)

error=mean_squared_error(Y_test,y_pred)
rscr=r2_score(Y_test,y_pred)

m=reg.coef_
c=reg.intercept_
