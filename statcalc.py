import numpy as np
<<<<<<< HEAD

def main ():

    print("main")

samples = []

# we are getting n 
def get_N():
    n = input("how many samples? ")






=======
import string

#making the main function for all functions
def main():
    get_n()


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
            break;
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
    
    

      
    
main()
>>>>>>> 6b0da53f36442f46f2a318bfc861a4d803b7b901
