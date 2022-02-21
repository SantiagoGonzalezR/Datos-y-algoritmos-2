'''
Antes de empezar con el codigo, quiero agradecer a Mariana Vasquez Escobar y a Pablo Maya Villegas por su ayuda en esto
Tengo consentimiento de usar este codigo, que contiene una logica casi identica a la de Mariana Vasquez Escobar
Y Pablo Maya Villegas ayudo a formular de manera correcta el output, puesto a que este aunque fuera una solucion correcta no se mostraba como se debia.
'''


from pickle import TRUE

#The starting function, this reads the inputs and generates both an Array that contains the list of topics as an array that contains the prohibited pairs
def main():
    n=int(input()) #This reads the three inputs, in the problem; t, p and s
    used=[] #This is the list that will be used as an output
    nCounter= 1
    while nCounter<=n:
        aux= input().split()
        t= int(aux[0]) #No. of topics
        p= int(aux[1]) #No. of prohibited pairs
        s= int(aux[2]) #No. of topics per speechl
        
        topicsList= [] #The list that contains a list of topics
        while t>0:
            topicsList.append(input().upper()) #Adds the topic to the list in upper case
            t=t-1

        
        prohibitedSet=set() #A set of prohibited pairs
        while p>0:
            splittedVar=input().upper().split() #This variable will save two words that should not be together

            #The next list is saving the tuples s-tuples combitations of the previous words and the s-tuples with the same words
            splittedList=permutation(splittedVar)

            #This loop is converting each s-tuple of splittedList to a string separated by empty spaces and saving them in the prohibitedList.
            while len(splittedList)>0:
                prohibitedSet.add(' '.join(splittedList.pop()))
            p=p-1

        
        topicsList.sort()
        topicsList.sort(key = len, reverse=True) #This sorts the list in descending length

        
        used.append('Set '+str(nCounter)+':') #Adding the Set #: to the output

        used=generator(topicsList, s, prohibitedSet, used) #This sends all the necessary information to the string so that it can be processed and generate a valid output

        used.append('')
        nCounter+=1

    printer(used) #This sends the output to a method that will print it
    
        


def generator(tl, s, banned, used):
    outter=[] #This is a temporary list that will help avoid errors when the amount of topics per speech are more than 2

    #If the number of topics in a speech is 1, we will return just the topics list without the banned ones
    if s==1:
        while len(tl)>0:
            aux=tl.pop(0)
            used.append(aux)
            
        return used

    if s==2:
        '''
        In this if and the next one, what I do is to make a pop (save the head and then remove it)
        so it won't repeat again in the next loops, because each loop makes all the possible permutations
        for that head, so is not necessary that ir remains in the list. More over, each loops iterates over
        a list that, of course, does not include the head: We have a list of 8 elementes (1-8), the 
        firstWord variables save the element [1], then the code remove it from the list (list = 2-8) and will
        start iterating over it; when the loop ends, we do the same with the remaining list: we take its head
        in firstWord=2 and when we remove the element from the list, it looks like list=3-8 and repeat the 
        process. This mechanism assures that there will not be repetitions of any kind.

        THE BACKTRACKING MECHANISM: Having the list of banned s-tuples, when the code creates a new s-tuple, 
        it compares it with all the elements of the banned list with the 'not in' command, if the s-tuple does not
        appears in 'banned' the it will be concatenated to the 'used' list and then the combination that makes the 
        s-tuple posible will be removed; on the contrary, if it finds that the s-tuple appears in the banned list, 
        it would not be stored and the combination that makes the s-tuple posible will be removed.
        '''
        while len(tl)>=s:
            firstWord=tl.pop(0) #The last tl word is the longest one, so I will start from here
            

            #The remaining list will be duplicated so I can manipulate to rotate the words and make the n-tuples.
            auxList=tl.copy()
            while len(auxList)>0:
                comparator=firstWord+" "+auxList[0]
                if comparator not in banned:
                    used.append(comparator)
                auxList.pop(0)
                
    else:
        outter=used.copy() #Here we make a copy of used (our output) so that we can still operate with used in the recursion without making
                           #a mistake
        while len(tl)>=s:
            used.clear()
            firstWord=tl.pop(0) #The last tl word is the longest one, so I will start from here
            
            #The remaining list will be duplicated so I can manipulate to rotate the words and make the n-tuples.
            auxList=tl.copy()
            auxList2=used.copy()
            #The next variable is the list of n-tuples that ver previously created by recursion
            prevList=generator(auxList, s-1,banned, auxList2).copy()

            while len(prevList)>0:
                #The next variables saves the generated permutations so they can be compared to the banned pairs
                '''
                This looks like a mess, I know, but it proves to be effective and fast in execution, there is probably an easier, less visually
                polluting method for this, but it works
                I'll explain how  it works, I manually make all possible combinations that are inside of each generated string, depending
                on the amount of topics per speech, and then I check if ANY of these is in the banned list, if it is, it is skipped, if it isn't
                it's put in the output list 
                '''
                generated=firstWord+" "+prevList[0]
                aux0=prevList[0].split()
                aux1=firstWord + " " + aux0[0]
                aux2=firstWord + " " + aux0[1]
                if(len(aux0)==2):
                    if aux1 not in banned and aux2 not in banned:
                        outter.append(generated)
                if(len(aux0)==3):
                    aux3=firstWord+" "+aux0[2]
                    aux4=aux0[0]+" "+aux0[2]
                    aux5=aux0[1]+" "+aux0[2]
                    if aux1 not in banned and aux2 not in banned and aux3 not in banned and aux4 not in banned and aux5 not in banned:
                        outter.append(generated)
                if(len(aux0)==4):
                    aux3=firstWord+" "+aux0[2]
                    aux4=firstWord+" "+aux0[3]
                    aux5=aux0[0]+" "+aux0[2]
                    aux6=aux0[0]+" "+aux0[3]
                    aux7=aux0[1]+" "+aux0[2]
                    aux8=aux0[1]+" "+aux0[3]
                    aux9=aux0[2]+" "+aux0[3]
                    if aux1 not in banned and aux2 not in banned and aux3 not in banned and aux4 not in banned and aux5 not in banned and aux6 not in banned and aux7 not in banned and aux8 not in banned and aux9 not in banned:
                        outter.append(generated)
                prevList.pop(0)
        used=outter.copy()
    return used
               
# The goal of this method is to organize the output, this was made with the help of Pablo Maya Villegas
def printer(used):
    s = "\n".join(used)
    print(s)
    used.clear()

#This method makes the permutation @line 32 
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    l = [] # empty list that will store current permutation

    for i in range(len(lst)):
       m = lst[i]

       # Extract lst[i] or m from the list. remainderLst is remaining list
       remainderLst = lst[:i] + lst[i+1:]

       # Generating all permutations where m is first element
       for p in permutation(remainderLst):
           l.append([m] + p)
    return l


main()