#python 3.7
#same problem as last script, only this version is "translated" to use classes

import sys

class Addition:
    def reverseList(l):
        output=[]
        for element in l: output.insert(0,element)
        return output
    def getIntFromList(l):
        numberString=''
        for element in l: numberString+=str(element)
        return int(numberString)
    def __init__(self,listvector):
        self.v=listvector
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

        #conditions are met at this point
        numbersToSum=[]
        for l in listvector: numbersToSum.insert(0,Addition.getIntFromList(Addition.reverseList(l)))

        total=0
        for number in numbersToSum: total+=number

        FinalList=list(str(total)) #a list of strings
        num=0
        for element in FinalList:
            FinalList[num]=int(element)
            num+=1

        self.result=Addition.reverseList(FinalList)


listvector1= Addition([[2,4,3],[5,6,4]])          #[l1,l2,...,ln]
print(listvector1.result)
