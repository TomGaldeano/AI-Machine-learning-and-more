def merge(seq, start, mid, stop):
    lst = []
    low = start
    high = mid
    while low<mid and high<stop:
        if seq[low] < seq[high]:
            lst.append(seq[low])
            low += 1
        else:
            lst.append(seq[high])
            high +=1
    # add missing elements till mid if they are higher than those in start to mid
    while low < mid:
        lst.append(seq[low])
        low +=1
    i = 0
    # no need to add the elements from higher to stop as those are already sortedand in place
    while i<len(lst):
        seq[start+i]=lst[i]
        i +=1

def mergeSortRecursive(seq,start,stop):
    if start >= stop-1:
        return
    mid = (start+stop)//2
    mergeSortRecursive(seq,start,mid)
    mergeSortRecursive(seq,mid,stop)
    merge(seq,start,mid,stop)

def mergeSort(seq):
    mergeSortRecursive(seq,0,len(seq))

if __name__ == "__main__":
    a = [4,2,3,1]
    mergeSort(a)
    print(a)
    a = [4,3,2,1]
    mergeSort(a)
    print(a)