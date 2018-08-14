import random
import os
#from os.path import isfile,join
#onlyfiles=[f for f in listdir(C:\Users\lenovo\Desktop\internbatch\game\kbc\categories) if isfile(join(mypath, f))]

os.system('cls')

name=input('Enter your name:')
print('\n\nWelcome to the trivia game\nRule #1:Right Score +10\nRule #2:Wrong Score -5')


ls=list(os.walk('.\categories'))

ls=ls[0][2]

os.system('cls')

print('Choose your category:')

for i in range(0,len(ls)):
    print('\t{}. {}'.format(i,ls[i]))

x=int(input('Enter your choice:'))


f=open('C:\\Users\\lenovo\\Desktop\\internbatch\\game\\kbc\\categories\\'+ls[x],'r',encoding='utf-8')

data=f.read()
f.close()
s=data


ls=s.split('\n\n#')


questions={}

count=0

for i in ls:
    ls2=i.split('\n')
    questions[count]=ls2
    count+=1


#questions={
 #       '1':['Q.2+3=?','a:4','b:5','c:6','b'],
  #      '2':['Q.5+3/3','a:4','b:5','c:6','c'],
   #     '3':['Q.Highest peak of world','a:Mount Everest','b:Mount Baton','c:MountValley','a'],
                
    #    }




l=[var for var in range(0,len(ls))]

num=int(input('\nEnter number of questions you want(max({}):-)'.format(len(l))))

os.system('cls')
print('Get ready for blast')


while input('\n\nWhenever you are ready press any key:'):
    
    random.shuffle(l)
    answerls=[]
    questionls=[]
    marks=0
    for i in range(0,num):
        os.system('cls')
        ans=questions[l[i]][1].split(' ')
        ans=ans[1]
        chckans=0
        #print(len(questions[l[i]]))
        if(len(questions[l[i]])==6):
            print("\n\n",questions[l[i]][0])
            
            questionls.append(questions[l[i]][0])
            
            print("",questions[l[i]][2])
            print("",questions[l[i]][3])
            print("",questions[l[i]][4])
            print("",questions[l[i]][5])
            for jk in range(2,6):
                s=questions[l[i]][jk].split(' ')
                if s[1]==ans:
                    chckans=s[0]

        else:
            print("\n\n",questions[l[i]][0])
            questionls.append(questions[l[i]][0])
            print("",questions[l[i]][2])
            print("",questions[l[i]][3])
            for jk in range(2,4):
                s=questions[l[i]][jk].split(' ')
                if s[1]==ans:
                    chckans=s[0]

        x=input(' Enter your choice:')
        
        answerls.append(chckans)

        if(x==chckans):
            marks=marks+10
        else:
            marks=marks-5

    os.system('cls')

    print('\n\n{},Your score is:{}'.format(name,marks))
    print('The answers are as follows:')
    for i in range(len(answerls)):
        print('{}\nAns. {}\n\n'.format(questionls[i],answerls[i]))



