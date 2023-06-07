# Function to find a pair in an array with a given sum using hashin

def findPair(nums, target):
    # create an empty dictionary
    d = {}
    # create a counter
    j = 0
    # create a message variable
    msn = ''
 
    # do for each element
    for i in range(0, len(nums), 1):

        #Conditional that checks the condition of the algorithm
        if target - nums[i] in d:

            # If the condition is met, the counter (j) is increased 
            # and the pair is assembled from the item that meets 
            # the condition stored in the dictionary and the item 
            # that allowed it to be entered in the conditional

            j=j+1
            msn=msn+'Pair found'+'('+str(nums[d.get(target - nums[i])])+','+str(nums[i])+')'+'\n'

        #Save all elements of the array in a dictionary (key: array value item, value: array position value item)        
        d[nums[i]] = i
        
    #If the j counter is different than 0 the condition was met at least once    
    if(j!=0):
        return msn
    
    #If the j counter is 0 the condition was never met at the time of running the code  
    else:
        msn='Pair not found'
        return msn 
 
if __name__ == '__main__':

    # Open the variables of 'variables.txt' file
    f = open('variables.txt', 'r');
    text = (f.readlines())

    #Get the content of line number 2 of the document
    numsStr = text[1]
    #Get the content of line number 4 of the document
    targetStr = text[3]

    #Change the content line to array
    nums = list(map(int, numsStr.split(" ")))

    #Change the content line to integer
    target = int(targetStr)

    msg = findPair(nums, target)
 
    print(msg)
