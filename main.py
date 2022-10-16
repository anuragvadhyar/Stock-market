import csv
import datetime
import random

file=open('eps.csv')
type(file)
csvreader=csv.reader(file)
header=[]
header=next(csvreader)
rows=[]
for row in csvreader:
        rows.append(row)
#print(rows)
file2=open('prices.csv')
csvreader2=csv.reader(file2)
header2=[]
header2=next(csvreader2)
rows2=[]
state=0
temp=0
temp2=0
q_table=[]
env_matrix=[]


for row3 in csvreader2:
        rows2.append(row3)

for x in rows2:
    q_table.append([0,0])
def six_months_price(date):
    global temp
    global temp2
    temp = 0
    temp2 = 0
    x = date.split('-')
    date2 = x[2] + '-' + x[1] + '-' + x[0]

    theday = datetime.date(*map(int, date2.split('-')))
    prevday = theday - datetime.timedelta(days=180)
    prevday = str(prevday)
    y = prevday.split('-')
    date3 = y[2] + '-' + y[1] + '-' + y[0]
    date3 = str(date3)
    if ((getstockprice(date3))>(getstockprice(date))):
        temp=1
        return 1

    elif (getstockprice(date3)<=  getstockprice(date) ):
        temp2 = 1

        return 0

    else:
        return -1





def eps_growth(a,b):
    eps1=0
    eps2=0
    for i in rows:
        if (i[0]==a):

            eps1=i[1]
        if (i[0]==str(b)):
            eps2=i[1]

    if(not eps1 or not eps2):
        return -1

    if (eps1>eps2):
        return 1
        #buy
    elif (eps2>eps1):
        return 0

def last_two_quarters_eps(date):
    x=date.split('-')
    x[0] =int(x[0]) #date
    x[1] =int(x[1]) #'month
    x[2] =int(x[2]) #'''year'''
    y=[0,0,0]
    z=[0,0,0]
    if (x[1] > 3 and x[1]<6):
        y[1] = 3
        y[0] = 31
        y[2] = x[2]
        z[1] = 12
        z[0] = 31
        z[2] = x[2]-1
    elif(x[1]>6 and x[1]<9):
            y[1]=6
            y[0]=30
            y[2]=x[2]
            z[1] = 3
            z[0] = 31
            z[2] = x[2]
    elif(x[1]>9 and x[1]<12):
        y[1]=9
        y[0]=30
        y[2]=x[2]
        z[1] = 6
        z[0] = 30
        z[2] = x[2]
    elif(x[1]<4):
        y[1]=12
        y[0]=31
        y[2]=x[2]-1
        z[1] = 9
        z[0] = 30
        z[2] = x[2]-1

    for i in range(3):
        if y[i]<10:
            y[i]='0'+str(y[i])
        else:
            y[i] = str(y[i])

        if z[i]<10:
            z[i]='0'+str(z[i])

        else:
            z[i]=str(z[i])
    y="-".join(y)
    z="-".join(z)

    return eps_growth(y,z)


def stock_decrease_fifteen(a):
    x=-1000
    y=True
    for i in a:
        if getstockprice(i)>x:
            x=getstockprice(i)
        else:
            return -1


    return 1

def stock_growth(a,b):
    stock_price1 = 0
    stock_price2 = 0
    for j in rows2:
        if (j[0] == a):
            stock_price1 = j[1]
        if (j[0] == str(b)):
            stock_price2 = j[1]

    if (not stock_price1 or not stock_price2):
        return -1

    if (stock_price1 > stock_price2):
        return 1
        # buy
    elif (stock_price2 > stock_price1):
        return 0

def getstockprice(a):
    stock_price1 = 0



    for j in rows2:


        if (j[0] == a):

            stock_price1 = float(j[1])

            return stock_price1
    return -1


def getnextstate(current_pos,action,date):
    if action==0:
        a=buy(date)
        return a[1]
    elif action==1:
        b=sell(date)
        return b[1]
    else:
        return current_pos

def isgoalerached(current_pos):
    return (current_pos==9 or current_pos==12)



def last_two_days(date):
    x = date.split('-')
    x[0] = int(x[0])  # date
    x[1] = int(x[1])  # 'month
    x[2] = int(x[2])  # '''year'''

    if(x[1] in [1,3,5,7,8,10,12]):

        if (x[0]>=3 and x[0]<=31):


            date1=str(x[0]-1)+'-'+str(x[1])+'-'+str(x[2])
            date2 = str(x[0] - 2) + '-' + str(x[1]) + '-' + str(x[2])
        elif (x[0]<3 and (x[1]-1)in [1,3,5,7,8,10,12]):

            if (x[0]==2 and (x[1]-1)!=2):

                date1=str(x[0]-1)+'-'+str(x[1])+'-'+str(x[2])
                if (x[1]==1):
                    date2 = str(31) + '-' + str(12) + '-' + str(x[2]-1)
                else:
                    date2 = str(31) + '-' + str(x[1]-1) + '-' + str(x[2])
            elif (x[0] == 2 and (x[1] - 1)==2):
                if x[2]%4==0:
                    date1 = str(x[0] - 1) + '-' + str(x[1]) + '-' + str(x[2])
                    date2 = str(29) + '-' + str(x[1]-1) + '-' + str(x[2])
                else:
                    date1 = str(x[0] - 1) + '-' + str(x[1]) + '-' + str(x[2])
                    date2 = str(28) + '-' + str(x[1] - 1) + '-' + str(x[2])
            else:
                if(x[0]==1 and (x[1]-1)!=2):

                    if (x[1]==1):
                        date1 = str(31) + '-' + str(12) + '-' + str(x[2]-1)
                        date2 = str(30) + '-' + str(12) + '-' + str(x[2]-1)
                    else:
                        date1 = str(30) + '-' + str(x[1]-1) + '-' + str(x[2])
                        date2 = str(29) + '-' + str(x[1]-1) + '-' + str(x[2])
                elif (x[0] == 1 and (x[1] - 1)==2):
                    if x[2]%4==0:
                        date1 = str(29) + '-' + str(x[1]-1) + '-' + str(x[2])
                        date2 = str(28) + '-' + str(x[1]-1) + '-' + str(x[2])
                    else:
                        date1 = str(28) + '-' + str(x[1]-1) + '-' + str(x[2])
                        date2 = str(27) + '-' + str(x[1] - 1) + '-' + str(x[2])

        elif (x[0] < 3 and (x[1] - 1) in [2,4,6,9,11,0]):

            if (x[0]==2):
                date1=str(x[0]-1)+'-'+str(x[1])+'-'+str(x[2])
                if (x[1]-1!=2):
                    date2 = str(31) + '-' + str(x[1]-1) + '-' + str(x[2])
                else:
                    if x[2]%4==0:
                        date2 = str(29) + '-' + str(x[1] - 1) + '-' + str(x[2])
                    else:
                        date2 = str(28) + '-' + str(x[1] - 1) + '-' + str(x[2])

            elif(x[0]==1):

                if ((x[1]-1)!=2):
                    if x[1]!=1:
                        date1 = str(30) + '-' + str(x[1]-1) + '-' + str(x[2])
                        date2=str(29) + '-' + str(x[1]-1) + '-' + str(x[2])
                    else:
                        date1 = str(31) + '-' + str(12) + '-' + str(x[2]-1)
                        date2 = str(30) + '-' + str(12) + '-' + str(x[2]-1)

                else:
                    if (x[2]%4==0):

                        date1 = str(29) + '-' + str(x[1] - 1) + '-' + str(x[2])
                        date2 = str(28) + '-' + str(x[1] - 1) + '-' + str(x[2])
                    else:
                        date1 = str(28) + '-' + str(x[1] - 1) + '-' + str(x[2])
                        date2 = str(27) + '-' + str(x[1] - 1) + '-' + str(x[2])


    else:
        if (x[1]!=2):
            if (x[0] >= 3 and x[0] <= 30):
                date1 = str(x[0] - 1) + '-' + str(x[1]) + '-' + str(x[2])
                date2 = str(x[0] - 2) + '-' + str(x[1]) + '-' + str(x[2])
            else:
                if x[0]==2:
                    date1 = str(x[0] - 1) + '-' + str(x[1]) + '-' + str(x[2])
                    date2 = str(31) + '-' + str(x[1]-1) + '-' + str(x[2])
                else:
                    date1 = str(31) + '-' + str(x[1]-1) + '-' + str(x[2])
                    date2 = str(30) + '-' + str(x[1] - 1) + '-' + str(x[2])

        else:
            if x[2]%4==0:
                if (x[0] >= 3 and x[0] <=29 ):
                    date1 = str(x[0] - 1) + '-' + str(x[1]) + '-' + str(x[2])
                    date2 = str(x[0] - 2) + '-' + str(x[1]) + '-' + str(x[2])
                else:
                    if x[0]==2:
                        date1 = str(x[0] - 1) + '-' + str(x[1]) + '-' + str(x[2])
                        date2 = str(31) + '-' + str(x[1] - 1) + '-' + str(x[2])
                    else:
                        date1 = str(31) + '-' + str(x[1] - 1) + '-' + str(x[2])
                        date2 = str(30) + '-' + str(x[1] - 1) + '-' + str(x[2])

            else:
                if (x[0] >= 3 and x[0] <=28 ):
                    date1 = str(x[0] - 1) + '-' + str(x[1]) + '-' + str(x[2])
                    date2 = str(x[0] - 2) + '-' + str(x[1]) + '-' + str(x[2])
                else:
                    if x[0]==2:
                        date1 = str(x[0] - 1) + '-' + str(x[1]) + '-' + str(x[2])
                        date2 = str(31) + '-' + str(x[1] - 1) + '-' + str(x[2])
                    else:
                        date1 = str(31) + '-' + str(x[1] - 1) + '-' + str(x[2])
                        date2 = str(30) + '-' + str(x[1] - 1) + '-' + str(x[2])
    y = date1.split('-')
    y[0] = int(y[0])  # date
    y[1] = int(y[1])  # 'month
    y[2] = int(y[2])  # '''year'''
    z = date2.split('-')
    z[0] = int(z[0])  # date
    z[1] = int(z[1])  # 'month
    z[2] = int(z[2])  # '''year'''
    for i in range(3):
        if y[i]<10:
            y[i]='0'+str(y[i])
        else:
            y[i] = str(y[i])

        if z[i]<10:
            z[i]='0'+str(z[i])

        else:
            z[i]=str(z[i])
    y="-".join(y)
    z="-".join(z)





    return stock_growth(y,z)


def get_last_fifteen_days_stock(date):
    x = date.split('-')
    date2=x[2]+'-'+x[1]+'-'+x[0]
    dates=['' for i in range(0,15)]

    for i in range(1,16):
        theday = datetime.date(*map(int, date2.split('-')))
        prevday = theday - datetime.timedelta(days=i)
        prevday=str(prevday)

        y=prevday.split('-')
        date3=y[2]+'-'+y[1]+'-'+y[0]
        date3=str(date3)

        dates[i-1]=date3


    return stock_decrease_fifteen(dates)





initialinvestment=500000
buy_reward=0
sell_reward=0
stocksinhand=0
inhandmoney=500000
count=0
count2=0
next_state=0

def buy(date):
    global initialinvestment
    global inhandmoney
    global stocksinhand
    global count
    global buy_reward
    global state
    global next_state
    global temp2
    temp2 = 0
    price=getstockprice(date)
    #print("buy price",price)
    if price<0:
        return -1
    else:
        if temp2==0:
            total=100*price
        else:
            total=1000*price
        if inhandmoney>=total:
            if temp2==0:
                stocksinhand+=100
            else:
                stocksinhand+=1000
            inhandmoney-=total

            count+=1

    if count>1:
        if (((inhandmoney+(stocksinhand*price))>initialinvestment)):
            #print('reward')
            buy_reward=10
        else:
            buy_reward=-10


    return [buy_reward,next_state]


def sell(date):
    global initialinvestment
    global inhandmoney
    global stocksinhand
    global count2
    global sell_reward
    global temp
    global next_state
    temp = 0
    price = getstockprice(date)

    if price<0:
        return -1
    else:
        if temp==0:
            if stocksinhand>=100:
                total = 100 * price
                stocksinhand -= 100
            else:
                total=0
        else:
            total=0.5*stocksinhand*price
            stocksinhand//=2

    #print("inhandmoney",inhandmoney)
    inhandmoney+=total
   # print("sell inhand", inhandmoney, total)


    if ((inhandmoney + (stocksinhand * price) > initialinvestment)):
        sell_reward =10
       # print('sell')
        if ((inhandmoney + (stocksinhand * price) - initialinvestment) >= 0.1 * initialinvestment):
            next_state = 1
        elif ((inhandmoney + (stocksinhand * price) - initialinvestment) >= 0.2 * initialinvestment):
            next_state = 2
        elif ((inhandmoney + (stocksinhand * price) - initialinvestment) >= 0.3 * initialinvestment):
            next_state = 3
        elif ((inhandmoney + (stocksinhand * price) - initialinvestment) >= 0.4 * initialinvestment):
            next_state = 4
        elif ((inhandmoney + (stocksinhand * price) - initialinvestment) >= 0.5 * initialinvestment):
            next_state = 5
        elif ((inhandmoney + (stocksinhand * price) - initialinvestment) >= 0.6 * initialinvestment):
            next_state = 6
        elif ((inhandmoney + (stocksinhand * price) - initialinvestment) >= 0.7 * initialinvestment):
            next_state = 7
        elif ((inhandmoney + (stocksinhand * price) - initialinvestment) >= 0.8 * initialinvestment):
            next_state = 8
        elif ((inhandmoney + (stocksinhand * price) - initialinvestment) >= 0.9 * initialinvestment):
            next_state = 9


    else:
        sell_reward=-10

        if ((inhandmoney + (stocksinhand * price) - initialinvestment) <= 0.1 * initialinvestment):
            next_state = 10
        elif ((inhandmoney + (stocksinhand * price) - initialinvestment) <= 0.2 * initialinvestment):
            next_state = 11
        elif ((inhandmoney + (stocksinhand * price) - initialinvestment) <= 0.3 * initialinvestment):
            next_state = 12

    return ([sell_reward,next_state])

for c in rows2:
    env_matrix.append([0,0])
    #a=buy(c[0])
    #b=sell(c[0])
    #env_matrix.append([a[0],b[0]])


learning_rate=0.1
discount=0.9

current_position = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
s=0
for x in env_matrix:
    s+=1
#for _ in range(1000):

    #current_position=random.choice(range(0,s))
    #current_state=random.choice([0,1,2,3,4,5,6,7,8,9,10,11])

current_position = 0  # random.choice(range(0, s))
for i in rows2:




    actio =random.choice([0,1]) #0:buy,1:sell,2:hold
    if i[0]!='30-12-2013':
        nxt_st =current_position+1
    if (actio ==0):
        env_matrix[current_position][actio] = (buy(i[0]))[0]
    else:
        env_matrix[current_position][actio]=(sell(i[0]))[0]

    print(current_position)
    print(actio)
    print(nxt_st)

    q_table[current_position][actio] = q_table[current_position][actio] + learning_rate * (
                        env_matrix[current_position][actio] +
                        discount * max(q_table[nxt_st]) - q_table[current_position][actio])

    current_position=nxt_st
    print('Episode done')


print(inhandmoney,' ',stocksinhand)
print(q_table)
print(env_matrix)
'''def getstate(date):
    x=last_two_quarters_eps(date)
    y=last_two_days(date)
    z=get_last_fifteen_days_stock(date)
    a=six_months_price(date)
    global state
    global buy_rep
    global sell_rep

    if ((x==1 or y==1) or a==0):
        buy(date)
        q_table[state][buy_rep] = q_table[state][buy_rep] + learning_rate * (
                state*buy_reward +
                discount * max(q_table[next_state]) - q_table[state][buy_rep])

        state = next_state


    else:
        if ((x==0 or z==1) or a==1):
            sell(date)
            q_table[state][sell_rep] = q_table[state][sell_rep] + learning_rate * (
                    state * sell_reward +
                    discount * max(q_table[next_state]) - q_table[state][sell_rep])

            state = next_state

        else:
            return 2'''

#print(rows2)

#print(rows2)
'''for i in rows2:

    #if (i[0]!='06-02-2010' and i[0]!='07-01-2012' and i[0]!='03-03-2012' and i[0]!='08-09-2012' and i[0]!='11-11-2012'):
        getstate(i[0])


print(inhandmoney,' ',stocksinhand)'''








'''for row2 in csvreader2:
    if (last_two_quarters_eps(row2[0])==1 or last_two_quarters_eps(row2[0])==-1):
        if'''



