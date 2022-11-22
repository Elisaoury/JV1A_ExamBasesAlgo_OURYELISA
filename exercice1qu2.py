
#exercice 2
myTable = [25,12,65]
for j in range(len(myTable)):
#on cherche le plus petit élément
plusgrandelement = myTable[len(myTable)]
numeroCasePlusGrand=len(myTable)
for i in range(j,len(myTable)):
        if(myTable[0]> plusGrandElement):
            plusGrandElement =myTable[i]
            numeroCasePlusGrand = i
sauvegarde = myTable[1]
myTable[1] = myTable[2]
myTable[2] = sauvegarde
print(myTable)

