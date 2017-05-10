

def mergeSort(numList):
    n = len(numList)
    if n > 1 :
        m = n // 2
        subList1, subList2 = numList[:m], numList[m:]
        mergeSort(subList1)
        mergeSort(subList2)
        merge(subList1,subList2,numList)

def merge(subList1,subList2,numList):
    n1, n2 ,n3= len(subList1), len(subList2), len(numList)
    index1, index2, index3 = 0, 0, 0
    while index1 < n1 and index2 < n2 :
        if subList1[index1] <= subList2[index2] :
            numList[index3] = subList1[index1]
            index1 += 1
        else :
            numList[index3] = subList2[index2]
            index2 += 1
        index3 += 1
    while index1 < n1 :
        numList[index3] = subList1[index1]
        index3 += 1
        index1 += 1
    while index2 < n2 :
        numList[index3] = subList2[index2]
        index3 += 1
        index2 += 1

def main():
    numList = [3,5,3,1,6,8,4]
    mergeSort(numList)
    print(numList)

if __name__ == "__main__" :
    main()


