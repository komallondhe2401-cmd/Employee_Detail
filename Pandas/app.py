import pandas as pd
# df=pd.read_csv("sales_data_sample.csv",encoding="latin1")

# print(df)

data={
    "Name":['Komal','Isha','Anvi','Rohit','Isha','Iswari'],
    "Age":[20,18,3,23,18,32],
    "City":['Ankleshwar','Bharuch','Mumbai','Lucknow',None,'Chennai'],
    "Salary":[30000,40000,25000,34000,None,45000]
}

df=pd.DataFrame(data)
# print(df) 

# df.to_csv("Data.csv",index=False)


# printing few lines
print("Dispaly starting of 10 rows of data")
print(df.head(5))
print(df.info())
print(df.describe())

# ALL THE OTHER COMMAND
print('Print shape of data')
print('Shape:{df.shape}')

# Column
single_column=df['Name']
print('Name column values')
print(single_column)

multiple_col=df[['Name','Age']]
print('name and age column values')
print(multiple_col)

#filter
single_filter=df[df['Age']>20]
print('Age>20')
print(single_filter)

multiple_filter=df[(df['Age']>20) & (df['Salary']>30000)]
print('age>20 and salary > 30000')
print(multiple_filter)

or_filter=df[(df['Age']>25) | (df['Salary']>25000)]
print(' age>25 or salary >25000 ')
print(or_filter)

# adding column
df['bonus']=df['Salary']*0.1
print('Added bonus column')
print(df)

#insert function
df.insert(0,'Emp_ID',[1,2,3,4,5,6]) 
print('Insert Emp_ID')
print (df)

# /updating
df.loc[0,'Salary']=70000  #df.loc[row_idx,col_name]=value
print('updated value of 0th row and salary column with 70000')
print(df)

# updating more than 1 value
df['Salary']=df['Salary']*1.05
print('Update everyones salary')
print(df)

# removing columns
df.drop(columns=['City'],inplace=True)
print('Print data after droping city column')
print(df)





# ------------------------------Data handling and cleaning-------------------------------
# return null value or not
print('Check for null values')
print(df.isnull())

# no of null values
print('Number of null values')
print(df.isnull().sum())

# drop null values
# df.dropna(inplace=True)
# print(df)

# df.dropna(axis=0,inplace=True)      #removed the none rows
# print(df)

# df.dropna(axis=1,inplace=True)      #removed the none columns , here age, salary,bonus
# print(df)

# fill with default value
#  df.dropna(0,inplace=True)

df['Age'].fillna(df['Age'].mean(),inplace=True)
print('Fill the none value of age with mean age')
print(df)

# Interpolation
df['Salary'] = df['Salary'].interpolate(method='linear')
print('print none salary values by estimated value using linear method')
print(df)

# Sorting
df.sort_values(by='Age',ascending=True,inplace=True)
print('Sorted age')
print(df)

df.sort_values(by=['Age','Salary'],ascending=[True,True],inplace=True)
print('acending sort age and descending sort salary')
print(df)

# Aggregation
avg_salary=df['Salary'].mean()
print(avg_salary)

# Grouping
grouped=df.groupby('Age')['Salary'].sum()
        # ('Age') col name by which group will be made        ['Salary']values will be taken from this column name
print(grouped)

grouped1=df.groupby(['Age','Name'])['Salary'].sum()
print(grouped1)



# =================================================================
# Merge
df_customer=pd.DataFrame({
    'Customer_ID':[1,2,3],
    'Name':['Ramesh','Suresh','Rahul']
})

df_order=pd.DataFrame({
    'Customer_ID':[1,2,4],
    'order_price':[100,120,500]
})

df_merged=pd.merge(df_customer,df_order,on='Customer_ID',how="inner")
print('Inner join')
print(df_merged)


df_merged=pd.merge(df_customer,df_order,on='Customer_ID',how="outer")
print('Outer join')
print(df_merged)

# Concatination
df_concat=pd.concat([df_customer,df_order],axis=0,ignore_index=True)

print(df_concat)

df_concat=pd.concat([df_customer,df_order],axis=1,ignore_index=True)
print(df_concat)






# ===================TASK=================

Customer_profile=pd.DataFrame({
    'Customer_ID':[1001,1002,1003,1004,1005],
    'Name':["Isha","Rashi","Kalyani",None,"Riya"]
})

Transaction_history=pd.DataFrame({
    'Customer_ID':[1001,1002,1003,1004,1006],
    'Order_ID':[10004,10002,None,10006,10007],
    'Order_price':[225, 45 , 525 , 825 ,None]
})

# Merge
df_merge=pd.merge(Customer_profile,Transaction_history,on='Customer_ID',how='inner')
print('Inner join')
print(df_merge)

df_merge=pd.merge(Customer_profile,Transaction_history,on='Customer_ID',how='outer')
print('Outer join')
print(df_merge)

df_merge=pd.merge(Customer_profile,Transaction_history,on='Customer_ID',how='left')
print('Left join')
print(df_merge)

df_merge=pd.merge(Customer_profile,Transaction_history,on='Customer_ID',how='right')
print('right join')
print(df_merge)

# concatination
df_concat=pd.concat([Customer_profile,Transaction_history],axis=0,ignore_index=True)
print('df_concatination')
print(df_concat)

df_concat=pd.concat([Customer_profile,Transaction_history],axis=1,ignore_index=True)
print('df_concatination')
print(df_concat)
