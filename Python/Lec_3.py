nums=[56,76,23,43,78,85,97]      # This is List [] use this brackets
print (len(nums))                # print length of list
print(nums)                      # print list
print(nums[0])                   # print index 0 index value
print(nums[0:5])                 # print 0 index to 5 index
nums[6]=90                       # change  one value
nums[2:5]=[25,85,63]             # change 2,3,4, index value

print (nums)
print(nums[-1])                  # print last index value 90
print(nums[-3])                  # print -3 index value 63
print (len(nums))

names=["Asha","Uma","Rama"]      # Inter  List
print (names)                    # print list
value =[nums,names]              # Add value
print (value)                    # print value

print (len(nums))                # print  Length
print(value[0])                  # print 0 index value nums
print(value[1])                  # print 1 index value names
print(value[0][1])               # print 0 index value number 76
print(value[1][2])               # print 1 index value names Rama

nums.append(100)                 # one no. add use append function
print(nums)
#nums.append([101,75])            # two no. add but print like this  [] brackets
#print (nums)                     # print list

nums.extend([101,75])            # use this function two no. add
print (nums)                     # print list

nums.insert(2,120)               # 2 index value change to 120
print (nums)

'''del nums[3]                      # delete 3 index value 63
print (nums)
del nums[3:5]                    # delete 4,5 index value 63 ,85
print (nums)'''

'''del nums
print(nums)
'''
nums.remove(120)               # remove 120
print (nums)

nums.pop(3)                   # delete 3 index value
print (nums)

nums.sort()                  # sorting list
print(nums)
nums.reverse()               # reverse list
print(nums)
