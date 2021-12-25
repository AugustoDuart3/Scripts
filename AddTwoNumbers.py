#solves https://leetcode.com/problems/add-two-numbers/
#expanded for n lists
import sys

listvector= [[9,9,9,9,9,9,9],[9,9,9,9]]           #[l1,l2,...,ln]
#first checks for constraints

#The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node value <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
NotInDigitRange=False
LengthOutOfRange=False
LeadingZero=False
for element in listvector:
    if len(element)<1 or len(element)>100:
        LengthOutOfRange=True
        break
    if len(element)>1 and element[-1]==0:
        LeadingZero=True
        break
    for number in element:
        if 0 > number or number > 9:
            NotInDigitRange=True
            break
    if NotInDigitRange: break

if NotInDigitRange or LengthOutOfRange or LeadingZero:
    print('Conditions not met!')
    sys.exit()

def reverseList(l):
    output=[]
    for element in l:
        output.insert(0,element)
    return output
def getIntFromList(l):
    numberString=''
    for element in l:
        numberString+=str(element)
    return int(numberString)


numbersToSum=[]
for l in listvector: numbersToSum.insert(0,getIntFromList(reverseList(l)))



total=0
for number in numbersToSum: total+=number

FinalList=list(str(total)) #a list of strings
num=0
for element in FinalList:
    FinalList[num]=int(element)
    num+=1
print(reverseList(FinalList))
