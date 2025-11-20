import numpy as np
import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                    101, 104, 111, 112, 113, 114, 115, 116, 117, 118],
    "Name": ["Komal", "Isha", "Anvi", "Rohit", "Ramesh", "Ishwari", "Amit", "Sneha", "Kiran", "Mira",
             "Komal", "Rohit", "Nisha", "Vikram", None, "Pooja", "Tina", "Arjun", "Raj", "Sara"],
    "Age": [25, 28, None, 22, 35, 40, 29, 31, np.inf, 27,
            25, 22, 26, None, 30, -20, 45, 33, 36, 29],
    "Department": ["HR", "Finance", "IT", "IT", "HR", "Marketing", "Finance", "Finance", "IT", "HR",
                   "HR", "IT", "IT", "Finance", "Finance", "HR", "Marketing", None, "HR", "Finance"],
    "Salary": [35000, 40000000, 50000, 45000, None, 55000, 60000, -45000, 70000, np.inf,
               35000, 45000, None, 48000, 50, 51000, -99999, 42000, 62000, -52000],
    "Experience_Years": [2, 3, 5, 2, np.inf, 10, 7, 1, 12, 5,
                         2, 2, None, 4, -3, 8, 6, 5, 11, np.nan],
    "City": ["Mumbai", "Delhi", "Pune", "Chennai", "Kolkata", None, "Delhi", "Pune", "Chennai", "Kolkata",
             "Mumbai", "Chennai", "Delhi", "Pune", "Delhi", "Mumbai", "Kolkata", "Pune", "Pune", None]
}

df=pd.DataFrame(data)
print(df)
print(df.info())

print('Missing values in each column')
print(df.isnull().sum())

df.replace([np.inf,-np.inf],np.nan,inplace=True)
print('Converting infinity values into Nan')
print(df)



# df.fillna(df.mean(),inplace=True) ---->  We can't find mean of non numeric value

df.fillna(df.select_dtypes(include='number').mean(), inplace=True)   #numeric values with mean
    
df=df.astype({'Salary':'int','Age':'int','Experience_Years':'int'})  #making them int

df.fillna(df.select_dtypes(exclude='number').mode().iloc[0],inplace=True)  #non numeric values with   {.mode().iloc[] }
                                                                          #mode() = most frequent ocurring values 
                                                                          #iloc[row_idx,col_idx] = it return value present at given row and col index
                                                                          # iloc[0]= value at 0th row
        #We use both of them becoz mode can give multiple values as there can be 2 similar name twice so we also use iloc[]
print('missing fillup')
print(df)


# df.drop_duplicates(inplace=True) ---->It works if 100% rows match

# For specific  column
df.drop_duplicates(subset=['Name'],inplace=True)
print('Drop Duplicate')
print(df)

# For replacing negative values 
df['Salary']=np.where(df['Salary']<0,df['Salary'].median(),df['Salary'])
df['Age']=np.where(df['Age']<0,df['Age'].median(),df['Age'])
print('Replace negative with median')
print(df)


# ======================UPPER AND LOWER BOUND
# Salary_mode=df['Salary'].mode()   #mode return series not a single value so will use

Salary_mode=df['Salary'].mode().iloc[0]
Salary_std=df['Salary'].std()
lower_bound=Salary_mode-(3*Salary_std)
upper_bound=Salary_mode+(3*Salary_std)

#remove salary where it is too high and too low
df=df[(df['Salary']>=lower_bound) & (df['Salary']<=upper_bound)]
print(df)


# ----------------------Final step-----------------------------------------------
print('Cleaned Dataset')
df.reset_index(drop=True,inplace=True)
print(df)