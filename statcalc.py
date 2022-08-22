#####making a statistical calculator to make it easier for non professional people#####
from statistics import mode
import numpy as np

#making the main function for all main functions
def main():
    get_n()
    s_main()

#making it global for all variables
samples=[]


#getting all samples
def get_n():
    get_n.n = input("how many samples?")
    n= get_n.n
    n = int(n)
    while n > 0:
        try:
            get_X()
            sample = get_X.sample
            samples.append(sample)
            n -= 1
        except ValueError:
            pass

#getting each sample
def get_X():
    get_X.sample=[]
    sample = get_X.sample
    while True:
        N = input("N: ")
        try:
            
            N = int(N)
            break
        except ValueError:
            pass


    while N > 0:
        x = input("X: ")
        try:
            x = int(x)
            sample.append(x)
            N -= 1    
        except ValueError:
            print("that is not an integer!!!!")


    return sample

#it's the house of all secondary functions depending on the input of the user
def s_main():

    answer  =  input("1.mean \
                        2.mode\
                        3.median    \
                        4.standard dev \
                        What do you need to be done? \
                        Note:    You can type number or the name of method.")

    if answer.lower() == "mean" or answer == "1":
        mean()
    elif answer.lower() == "mode" or answer == "2":
        Themode()
    elif answer.lower() == "median" or answer == "3":
        median()       
    elif answer.lower() == "standard dev" or answer == "4":
        std()

#mean function    
def mean():
    meanArr=[]
    for sample in samples:
        mean =np.mean(sample)
        meanArr.append(mean)      
    i=1
    for Themean in meanArr:

        print(f"The mean of sample {i} is {Themean}")
        i+=1
#mode function
def Themode():
    modeArr=[]
    for sample in samples:
        themode = mode(sample)
        modeArr.append(themode)
    i= 1
    for themode in modeArr:
        print(f"The median of sample {i} is {themode}")
        i += 1
#median funtion
def median():
    medArr=[]
    for sample in samples:
        median = np.median(sample)
        medArr.append(median)
    i= 1
    for Themedian in medArr:
        print(f"The median of sample {i} is {Themedian}")
        i += 1


def std():
    stdArr=[]
    for sample in samples:
        thestd =np.std(sample)
        stdArr.append(thestd)      
    i=1
    for thestd in stdArr:

        print(f"The std of sample {i} is {thestd}")
        i+=1



main()