
import random
List=['yashvant','akash','samarth','umesh','shiv','swapnil','tanishq','sanika','krishna','anagha','hemant','rushikesh karkhane','abhi','anand','murnal','nilesh','anuja','pooja','rameshwar','renuka kulkarni','renuka deshmukh','samir','tabish','sonali','vaibhav','yash','mayank','atharva','tejas gadhe','anand bawaskar','rushikesh kulkarni','faizan','prashant','divya','sahil','shivdatt','amit','aniket','rohan','tejas meshram','yogesh','kushi','shreya','dhanashree','suyog','rupali','bharti','pranjali','tejas misal','manisha','gauravi','siddhi','pratiksha']
friends_level=('are friends','you need to spend more time for becoming Best friends','are best friends',': for checking, Check whether he saved you No. or Not')
your_name=input("Enter Your Name: ")
friend_name=input("Enter Group Member Name :").lower()
def check_group_friends():
    if friend_name in List: #checking whether the friend_name in group or not
        level=random.choice(friends_level) #randomly getting a string from friends_level 
        return f"{your_name} and {friend_name} {level}"
    else:
        return "ASk him to Join Group "

print(check_group_friends())