import csv
import pandas as pd
import matplotlib.pyplot as plt
with open('expense.csv','a',newline='') as f:
    write=csv.writer(f)
    write.writerow(['Date','Category','Amount'])
with open('income.csv','a',newline='') as f:
    write=csv.writer(f)
    write.writerow(['Date','Category','Amount'])
class budget:
    def __init__(self,balance=0):
        self.balance=0
    def expense(self):
        lt=['date','Category','Amount']
        for i in range(len(lt)):
            lt[i]=input(f'Enter {lt[i]}  ')
        lt[2]=int(lt[2])
        with open('expense.csv','a',newline='') as f:
            write=csv.writer(f)
            write.writerow(lt)
        self.balance-=int(lt[2])
        print(f"Your balance amount is {self.balance}")
    def income(self):
        lt=['date','Category','Amount']
        for i in range(len(lt)):
            lt[i]=input(f'Enter {lt[i]}  ')
        lt[2]=int(lt[2])

        with open('income.csv','a',newline='') as f:
            write=csv.writer(f)
            write.writerow(lt)
        self.balance+=int(lt[2])
        print(f"Your balance amount is {self.balance}")

    def analysis(self):
        df=pd.read_csv('expense.csv')
        category_sum=df.groupby('Category')['Amount'].sum()
        print(category_sum)
        category_sum.plot(kind='bar', color='skyblue')
        plt.xlabel('Expense Category')
        plt.ylabel('Total Spending Amount')
        plt.title('Total Spending Amounts by Category')
        plt.xticks(rotation=45)
        plt.show()
    def calculate_budget(self):
        df1=pd.read_csv('expense.csv')
        df2=pd.read_csv('income.csv')
        self.balance=(len(df2.head())==0)*df2['Amount'].sum()-(len(df1.head())==0)*df1['Amount'].sum()


obj=budget()
obj.calculate_budget()
while True:
    it=int(input('Enter 1 for expense\nEnter 2 for income\nEnter 3 for analysis\nEnter 4 for exiting\n'))
    if it==1:
        obj.expense()
    elif it==2:
        obj.income()
    elif it==3:
        obj.analysis()
    elif it==4:
        print('Exited Successfully...')
        break
    else:
        print('Wrong key pressed...')

    
