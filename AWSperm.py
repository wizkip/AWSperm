#Here we will just do a simple code

from itertools import permutations

def AWSperm(str):

    permlist = permutations(str)

    #Iterate through the LIST
    for perm in list(permlist):
        print(''.join(perm))


if __name__ == "__main__":

    str = "AWS"
    AWSperm(str)

    
    