#---------------1--------------------

sentence=" arora is malayalam madam "
words=sentence.split()

count =sum(word==word[::-1] for word in words)
print(count)



#------------------2------------------------

numbers=[int(x) for x in input("Enter number separated by spaces ").split()]

numbers.sort()

mean=sum(numbers)/len(numbers)
n=len(numbers)
if n%2==0:
    median=(numbers[n//2-1]+numbers[n//2])/2
else:
    median=numbers[n//2]


mode=max(numbers,key=numbers.count)

    
print(mean)
print(median) 
print(mode)   

#-----------3------------------------
coursecodes=input("Enter course code ").split()
coursename=input("Enter course name").split()

combinedlist=[f"{code}:{name}"for code,name in zip(coursecodes,coursename)]
print(combinedlist)

#------------------------------4--------------------------------


singers = {name for name in input("Enter names of singers separated by spaces: ").split()}
dancers = {name for name in input("Enter names of dancers separated by spaces: ").split()}


all_artists = singers.union(dancers)  # All artists (singers and dancers)
allrounders = singers.intersection(dancers)  # Singers who are also dancers
dancers_not_singers = dancers.difference(singers)  # Dancers but not singers
singers_not_dancers = singers.difference(dancers)  # Singers but not dancers
exclusive_dancers_singers = dancers.symmetric_difference(singers)  # Either dancers or singers but not both


print(f"All artists: {all_artists}")
print(f"Allrounders: {allrounders}")
print(f"Dancers but not singers: {dancers_not_singers}")
print(f"Singers but not dancers: {singers_not_dancers}")
print(f"Exclusive dancers or singers: {exclusive_dancers_singers}")
