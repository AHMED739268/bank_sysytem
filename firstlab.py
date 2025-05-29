vowels=['a', 'e', 'i', 'o','u']
# print(len(vowels))
#
#
# numberlist=[1,5,8,2,3,4]
# numberlist.sort()
# print (numberlist)
# numberlist.reverse()
# print (numberlist)
#
#
# mystring='iti give me all information i want to know thanks iti'
# print (mystring.count('iti'))
#
# testword='ahmedeeeeeeeeeeeedsd'
#
# def filter(word):
#     if (word==''):
#         return ''
#
#     else:
#         if(word[0] in vowels):
#            return filter(word[1:])
#         else:
#            return word[0]+filter(word[1:])
#
# print(filter(testword))


# fetchindex='ahmed mohamed abdallah'
# print(fetchindex.index('d'))


#

# biglist=[]
# num=3
# i=1
# while(i<=num):
#     smalllist = []
#     for j in range(0,i):
#         j+=1
#         smalllist.append(i*j)
#     biglist.append(smalllist)
#     i+=1
# print(biglist)

#
#
# num=4
# i=1
# while(i<=num):
#
#     for a in range(num - i):
#         print("  ", end='')
#     for j in range(0, i):
#         print(' '+'*',end='')
#         #that is behavoir in python in print() function it make \n
#     print()
#     i += 1
