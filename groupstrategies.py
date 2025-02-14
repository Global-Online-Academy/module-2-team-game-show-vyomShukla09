# YOU ONLY HAVE TO SUBMIT FUNCTIONS FOR WHICH
# YOU ARE THE DRIVER IN PAIR PROGRAMMING


# Here are some history variables to test your code on. Feel free to create your own.
hist1 = []
hist2 = [("split","steal")]
hist3 = [("split","split"),("steal","split"),("split,steal"),("split,split"),("steal,split")]
hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","split"),("split","split"),("steal","split")]

# Your team's 1st strategy (VYOM SHUKLA)
# Explanation of Strategy: Calculates the total split and percemtage split. Flips a coin from 0 - 1 and makes descion based off of that.
# 
import random
def luckIsEverything1(history):
    totalSplit = 0
    for i in range(len(history)):
        (me,them) = history[i]
        if them == "split":
            totalSplit += 1 

        if len(history) == 0:
            return "steal"
        else:
            percentageSplit = totalSplit/len(history)

        coin = random.uniform(0,1)

        if coin < percentageSplit:
            return "split"
        else:
            return "steal"

print(luckIsEverything1(history=hist4))

# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 
