
# coding: utf-8

# # Pandas for Data Analysis

# In[ ]:

#Dataframe = Collection of Series(row series & col series)


# In[17]:

import pandas as pd
import numpy as np

#.1. DataFrame Creation (Part_1)
df = pd.DataFrame(data = np.random.randn(5,5),index = ['R0','R1','R2','R3','R4'],columns = ['A','B','C','D','E'])

#Col indexing
df[['C','A']]                              #dataframe access
df['new'] = df['A'] * df['B'] - df['C']    #creating new col
df.drop('new', axis = 1, inplace = True)   #delete col (inplace = remove permanently)
df.drop('R4',axis = 0,inplace = True)      #delete row 
print(df, df.shape)

#Row indexing
df.loc[['R2','R3']]                        #labelled index
df.iloc[0]                                 #integer index

#Subset indexing
df.loc['R0','A']                           #df.loc(row,col)
df.loc[['R0','R3'],['B','E']]


# In[128]:

#.2.Conditional Selection (Part_2)
#Singular
booldf = df > 0                        #shows T/F matrix
df[booldf]                             #shows NnN values
df[df > 0]
df[df['B'] > 0]                        #return R/C with true values
df[df['E'] > 0][['A','B','C']]         #conditional col selection + cols

#Multiple
df[ (df['E'] > 0) | (df['D'] > 1)]     #use '&,|' insteadof 'and,or' for multiple conditions 

# Setting and Resetting index
df.reset_index()                       #reset index to num vals
newind = 'CA NY IN SL SA'.split()
df.set_index('States')                 #add inplace = True to replace
print('')


# In[132]:

#.3. MultiLevel index & index hierarchy (Part_3)

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
hier_index

dtf = pd.DataFrame(data = np.random.randn(6,3),index = hier_index,columns = ['TN','MH','RJ'])
dtf.loc['G1'].loc[2]                                #multilevel indexing

dtf.index.names = ['Groups','Num']                  #assign names to index
dtf.loc['G2'].loc[2]['MH']

#Cross Section
dtf.xs(2,level = 'Num')
print('')


# In[234]:

#.4. Missing Data in Pandas (fillna() & dropna())
dic = {'A':[0,2,3],'B':[5,6,np.nan],'C':[9,4,np.nan]}
df1 = pd.DataFrame(dic)

#Drop missing vals
df1.dropna()                       #drop all NaN
df1.dropna(axis = 1)               #drop cols NaN
df1.dropna(axis = 1,thresh = 2)

#Fill Missing vals
df1.fillna(value = 'num')                    #fill all NaN
df1['C'].fillna(value = df1['C'].mean())     #fill cols NaN


#--------------------------------------------------------------------------
#.5. Grouping Data in Pandas
data = {'Company':['Slack','Twitter','Google','Slack','Amazon','Google'],
       'Person':['Larry','Mark','Turing','Amy','Jeff','Shuttle'],
       'Sales':[123,789,875,258,663,919]}

df2 = pd.DataFrame(data)
grp.sum().loc['Google']
grp.mean().loc['Slack']

df2.groupby('Company').sum().loc['Slack']                 #1-liner's
df2.groupby('Company').describe().transpose()['Google']   #1-liner's


#--------------------------------------------------------------------------
#.6. Merging Joining and Concatenating
#Concatenating
df3 = pd.DataFrame(data = np.random.randn(4,4),index = [1,2,3,4],columns = ['A','B','C','D'])
df4 = pd.DataFrame(data = np.random.randn(4,4),index = [5,6,7,8],columns = ['A','B','C','D'])
df5 = pd.DataFrame(data = np.random.randn(4,4),index = [9,10,11,12],columns = ['A','B','C','D'])
pd.concat([df3,df4,df5])

#Merging(Joins in SQL on any col)
left = pd.DataFrame({'Key':['k0','k1','k2'],'A':[1,2,5],'C':[9,3,4]})
right = pd.DataFrame({'Key':['k0','k1','k3'],'B':[6,8,7],'D':[6,6,6]})
pd.merge(left,right,how='right', on='Key')                   #how = inner/outer/left/right

#Joining(on index)
lt = pd.DataFrame({'AS':[88,99,44],'SW':[22,11,77],'PP':[85,74,25]},index = ['L0','L1','L2'])
rt = pd.DataFrame({'SA':[88,99,44],'WS':[22,11,77],'LL':[85,74,25]},index = ['L0','L1','L2'])
lt.join(rt)
lt.join(rt, how='outer')                            #how = inner/outer/left/right


# In[276]:

# .7. Pandas Operations
df6 = pd.DataFrame({'col1':[55,88,99,67,43,76],'col2':[11,999,888,55,77,11],'col3':['yaay','pq09r','bob','yaoy','ymmy','bob']})

df6.head(3)
df6.tail(1)
df6['col2'].unique()                   #returns unique
df6['col2'].nunique()                  #count of unique
df6['col3'].value_counts()             #count of each val
df6.sort_values('col3')                #sorting
df6.isnull()                           #find null vals
df6['col3'].apply(len)                 #apply inbuilt or user-defined func/lambda exp
df6['col1'].apply(lambda x : x * x)

#Attributes
df6.columns
df6.values
df6.index


#Pivot Tables
df7 = pd.DataFrame({'A':['foo','foo','foo','bar','bar','bar'],'B':['one','one','two','two','one','two'],
                   'C':['x','y','x','y','x','y'],'D':[1,9,5,7,4,2]})

df7.pivot_table(values='D', index =['A','B'], columns='C')    #create pivot table


# In[305]:

#.8.Data Input and Output in Pandas
#Pandas Can Read data from - CSV, Excel,SQL,HTML 

#R/W from CSV
df8 = pd.read_csv('../resources/data/samples/iris/iris.csv')
df8.to_csv('my_data',index = False)
df9 = pd.read_csv('my_data')

#Read from Excel
#pd.read_excel('file_name.xlsx',sheetname = 'sheet_name')
#df9.to_excel('file_name.xlsx',sheet_name = 'sheet_name')

#Read from HTML
htm = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
htm[0]

print('f')


# In[295]:

get_ipython().system(u'pip3 install ')

