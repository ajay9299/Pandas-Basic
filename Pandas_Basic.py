# Basic Of Pandas...
# Their are 3 data structures are availible 
# 1.Series(1-D) 2. Data frame(2-D) 3. Panel
import pandas as pd 
import numpy as np 


# Series data work
'''
lst = [1,2,3,4,5,6,7]
print(pd.Series(lst))
print(pd.Series(lst,index = ['A','B','C','D','E','F','G'])) # lable changing process...
print(pd.Series({'a':1,'b':2})) # data formation using dictionary 
'''
# Pandas Data frame work
'''
lst1 = np.arange(1,10,1)
print(pd.DataFrame(lst1))
dic = [{'Name':'Ajay','Roll_no':237,'Marks':300},{'Name':'Anil','Roll_no':239,'Marks':200},{'Name':'Mathur','Roll_no':256,'Marks':250}]
print(pd.DataFrame(dic,index=[1,2,3]))
'''

# Basic Operation For File Handling...
# We can pass ----> nrows, usecols,skiprows,index_col,header,head,tail in file reading columns...

# Handling missing values----------->

'''
Data = pd.read_csv('Data.csv')
print(Data.isnull().sum())
print(Data.isnull().sum().sum())
print(Data.dropna(axis = 0,how = 'any'))

print(Data.dropna(inplace = True))
'''

# Fillna values------>
'''
Data = pd.read_csv('Data.csv')
print(Data)
 print(Data.fillna(1))  # NaN values convert in 1
 print(Data.fillna({'indus':'8.9'}))
 print(Data.fillna(method = 'ffill')) # forword fill 
print(Data.fillna(method = 'bfill',limit =2)) # limit is = Number of NaN values
'''

# Replace values----->
'''
Data = pd.read_csv('Data.csv')
print(Data.replace(36.6,100))   # replace(Old_values,New_values)
print(Data) 
print(Data.replace([0.524,8.14],[1,2]))
'''

# Interpolate Values In Data-Frame
'''
Data = pd.read_csv('Data.csv') 
Data.interpolate(limit = 1, limit_direction ='backward', inplace = True)
print(Data)
'''

# loc Fun
'''
Data = pd.read_csv('Data.csv')
print(Data)
print(Data.loc[0])  # 0 index Raw Dataa extract from Data frame
print(Data.loc[17,'age']) # 17 Row , age colounm value
print(Data.loc[0:10,'age']) # From 0 index value to 10 index (row), Col_Name = 'age
print(Data.loc[Data['age']<45]) # Less values in Col_
   # iloc Fun()
print(Data.iloc[:,4])   # Print whole row with 4th colounm 
print(Data.iloc[[1,2,3]])  # Print Row using index values
'''
# Group By------------->
'''
Clas = pd.read_csv('Class.csv')
print(Clas)
gr1 = Clas.groupby(by = 'Section')
print(gr1.groups)
for Section, gu in gr1:  # Data showing
   print(Section)
   print(gu)
print(gr1.sum())
print(gr1.mean())
print(gr1.describe())
'''
# Merging ------------->

'''
Nof1 = pd.DataFrame({'ID':[1,2,3,4],'Class':[9,10,11,12]})
print(Nof1)
Nof2 = pd.DataFrame({'ID':[1,2,3,4],'Class':['A','B','C','D']})
print(pd.merge(Nof1,Nof2,on = 'ID',indicator=True))
'''

# concat--------->
'''
s_1 = pd.Series([1,2,3,4,5])
s_2 = pd.Series([6,7,8,9,10])
print(s_1)
print(s_2)
print(pd.concat([s_1,s_2],ignore_index = True)) # Series concatanation
d_1 = pd.DataFrame({'Name':['Ajay','Tushar','Mega'],'Roll':[234,202,300],'Sub':['Maths','Sanskrit','Sst']})
print(d_1)
d_2 = pd.DataFrame({'Name':['Hunny','Arnav','Rocky'],'Roll':[123,340,245],'Sub':['English','Supw','Hindi']})
print(d_2)
print(pd.concat([d_1,d_2],ignore_index = True,axis = 0,keys = ['First_Data','Second_Data']))  # Data Frame concatanation

'''
# Join()------>
'''
d_3 = pd.DataFrame({'Sr_1':[1,2,3,4,5],'ID_1':[11,12,13,14,15]})
print(d_3)
d_4 = pd.DataFrame({'Name':[5,6,7,8],'ID_2':[15,16,17,18]})
print(d_4)
print(d_3.join(d_4))
'''

# Append()----->

'''print(d_3.append(d_4,ignore_index= True))'''

# Pandas Pivot Table----->

'''
D_5 = pd.read_csv("Class.csv")
print(D_5)
print(D_5.pivot_table(index ='Name')) # Name columns become index
print(D_5.pivot_table(index = 'Name',columns='Marks')) # further classifiy based on Marks
print(D_5.pivot_table(index = 'Name',columns='Marks',fill_value = '_')) # replace NaN values with '_'
print(D_5.pivot_table(index = 'Name',columns='Marks',fill_value = '_', margins = True))
'''
# Melt()------->
'''
D_6  = pd.read_csv('Class.csv')
print(D_6)
print(pd.melt(D_6, id_vars=['Marks'])) # Horizontal data convert in Vertical Formate
'''
# Datetimeindex()
'''
D_6 = pd.read_csv('Class.csv',parse_dates =['Date'])
#print(D_6)
print(type(D_6.Date))
'''
















 

























