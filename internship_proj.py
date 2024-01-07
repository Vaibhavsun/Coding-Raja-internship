import csv
import pandas as pd
# with open('C:\\Users\\hp\\Desktop\\data.csv.csv','a') as f:
#     write=csv.writer(f)
#     write.writerow(['ID','Task_Name','Description','Due Date','Priority','Status'])
df=pd.read_csv("C:\\Users\\hp\\Desktop\\data.csv.csv")
class task:
    def add(self):
        info=['ID','Task_Name','Description','Due Date','Priority','Status']
        for i in range(4):
            print(f'Enter {info[i+1]}',end=" ")
            info[i+1]=input()
        df=pd.read_csv('C:\\Users\\hp\\Desktop\\data.csv.csv')
        info[0]=0
        info[-1]='Not Completed'
        if info[4]=='High':
            df=pd.concat([pd.DataFrame([info],columns=df.columns),df]).reset_index(drop=True)
        elif info[4]=='Medium':
            dff=df.loc[df['Priority'].isin(['Medium','Low'])]
            if len(dff.head())==0:
                df=pd.concat([df,pd.DataFrame([info],columns=df.columns)]).reset_index(drop=True)
            else:
                id=dff.head().iloc[0,0]
                df=pd.concat([df.iloc[:id-1,:],pd.DataFrame([info],columns=df.columns),df.iloc[id-1:,:]]).reset_index(drop=True)
        else:
            df=pd.concat([df,pd.DataFrame([info],columns=df.columns)]).reset_index(drop=True)
        df['ID']=df.index+1
        df.to_csv('C:\\Users\\hp\\Desktop\\data.csv.csv',index=False)
        print('Updated Successfully...\n')
    def show(self):
        df=pd.read_csv('C:\\Users\\hp\\Desktop\\data.csv.csv')
        print(df.to_string(index=False))
        print('\n')
    def remove(self):
        print('Enter ID of task to be removed',end=" ")
        id=int(input())
        df=pd.read_csv('C:\\Users\\hp\\Desktop\\data.csv.csv')
        if len(df.loc[df['ID']==id])==0:
            print(" ID not Found")
        else:
            df=df.drop(index=id-1)
            df=df.reset_index(drop=True)
            df['ID']=df.index+1
            df.to_csv('C:\\Users\\hp\\Desktop\\data.csv.csv',index=False)
            print('Removed Succesfully...\n')
    def mark(self):
        print('Enter ID of task to be marked',end=" ")
        id=int(input())
        if len(df.loc[df['ID']==id])==0:
            print(" ID not Found")
        else:
            df.loc[df['ID']==id,'Status']='Completed'
            df.to_csv('C:\\Users\\hp\\Desktop\\data.csv.csv',index=False)
            print('Marked Sucessfully...\n')

obj=task()
while(True):
    it=int(input('''Enter 1 for adding the task\nEnter 2 for showing task\nEnter 3 for removing task\nEnter 4 for marking task\nEnter 5 for quiting\n'''))
    if (it==1):
        obj.add()
    elif (it==2):
        obj.show()
    elif (it==3):
        obj.remove()
    elif(it==4):
        obj.mark()
    else:
        print('Program Exited...')
        break
