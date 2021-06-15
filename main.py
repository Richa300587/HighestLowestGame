#Dictionary of 10 heighest earning Indian movies  and their ranking as per
from random import randint
dic={'Dangal': 1, 'Padmavaat': 10, 'Pk': 5, 'Secret Superstar': 4, 'Sanju': 9, '2.0': 5, 'Dhoom3': 12, 'Bahubali': 2, 'Sahoo': 16, 'Bajrangi Bhaijaan': 3}

def moviebyindex(i):
    movieslist=list(dic)
    return movieslist[i]


def comparison(i,j):
    if dic.get(moviebyindex(i)) < dic.get(moviebyindex(j)):
        return True
    else:
        return False

def finalgame():
    i=0
    j=1
    m=0
    while i<len(dic) and j<len(dic):
        first = moviebyindex(i)
        second = moviebyindex(j)
        print(f" first = {first}       second = {second}")
        yourchoice = input("'y' if first earned more than second else choose 'N'")
        if yourchoice != 'Y' and yourchoice != 'N':
            print("Wrong Input")
            yourchoice = input("'y' if {first} earned more than {second} else choose 'N'")
        if comparison(i,j)==True and yourchoice=='Y':
            m=m+1
            j=j+1
        elif comparison(i,j)==False and yourchoice=='N':
            m=m+1
            i=i+1
        else:
            print(f"wrong answer and game over with number of right attempt is {m}")
            break
        if i==len(dic) or j==len(dic):
            print("you got all answers right  Congratulations!")

finalgame()
def generator(i,t):
    j=randint(0,len(dic)-1)
    while i==j or t==j:
        j = randint(0, len(dic) - 1)
    return j

def finalgame2():
    i=0
    j=generator(i,i)
    m=0

    while j>0:
          first = moviebyindex(i)
          second = moviebyindex(j)
          print(f" first = {first}       second = {second}")
          yourchoice = input("'y' if first earned more than second else choose 'N'")
          if yourchoice != 'Y' and yourchoice != 'N':
            print("Wrong Input")
            yourchoice = input("'y' if {first} earned more than {second} else choose 'N'")
          if comparison(i,j)==True and yourchoice=='Y':
            m=m+1
            j=generator(j,i)
            i=generator(j,i)
          elif comparison(i,j)==False and yourchoice=='N':
            m=m+1
            i=generator(i,j)
            j=generator(i,j)
          else:
            print(f"wrong answer and game over with number of right attempt is {m}")
            break

finalgame2()



