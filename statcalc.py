#####making a statistical calculator to make it easier for non professional people#####
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
            if n >= 3:
                print("you can't make more than 2")
                break
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
                        3.median\
                        What do you need to be done?     ")

    if answer.lower() == "mean" or answer == "1":
        mean()
    elif answer.lower() == "mode" or answer == "2":
        mode()
    else:
        median()       


#mean function    
def mean():
    meanArr=[]
    for sample in samples:
            mean= np.mean(sample,axis=0)
            meanArr.append(mean)
            return meanArr
    print(meanArr)    

#mode function
def mode():
    print("mode")

#median funtion
def median():
    print("this is median")


main()