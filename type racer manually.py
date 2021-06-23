import matplotlib.pyplot as plt
import time as t

mistakes=0
times=[]

print("This is a typing competition, you need to type \"computer\" word 5 times and check your evolution")
input("Enter to start: ")

while len(times)<5:
    start=t.time()
    word=input("enter the word: ")
    end=t.time()
    time_elapsed=end-start
    times.append(time_elapsed)

    if word.lower()!='computer':
        mistakes=mistakes+1

print("total mistake/(s) you commited= ",mistakes)
print("wait for your result")

t.sleep(3)

x=[1,2,3,4,5]
y=times
plt.plot(x,y)
legend=['1','2','3','4','5']
plt.xticks(x,legend)
plt.xlabel('Attempts')
plt.ylabel('Time in seconds')
plt.title('CHECK YOUR TYPING SPEED')
plt.show()
      
