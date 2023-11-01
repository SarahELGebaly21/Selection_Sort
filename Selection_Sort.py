def Swap(list, indexV1, indexV2):
    temp = list[indexV1]
    list[indexV1] = list[indexV2]
    list[indexV2] = temp
def SelectionSort(list):
    max =0
    for k in range(len(list)):
        if list[k]>max:
            max = list[k]
    max +=1
    for i in range(len(list)-1):
        min = max
        min_index = i
        for j in range(i,len(list)):
            if list[j] < min:
                min = list[j]
                min_index = j
        Swap(list, i, min_index)