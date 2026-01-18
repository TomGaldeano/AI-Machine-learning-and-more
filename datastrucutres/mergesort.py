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

def merge2(seq, start, mid, stop):
    lst = seq[1]
    if stop > len(lst)-1:
        stop = len(lst)-1
    seq = seq[0]
    low = start
    high = mid+1
    i = start
    while low<mid+1 and high<stop:
        if seq[low] < seq[high]:
            lst[i] = seq[low]
            low += 1
            i +=1
        else:
            lst[i] = seq[high]        
            high +=1
            i+=1
    # add missing elements till mid if they are higher than those in start to mid
    if high == stop:
        while low <= mid and seq[low]<seq[high]:
            lst[i] = seq[low]
            low +=1
            i+=1
        lst[i] = seq[high]
        i+=1
    while low < mid+1:
        lst[i] = seq[low]
        low +=1
        i+=1
    while high < stop:
        lst[i] = seq[high]
        high +=1
        i+=1
    i = start
    # no need to add the elements from higher to stop as those are already sortedand in place
    while i<=stop and i<len(seq):
        seq[i]=lst[i]
        i +=1

def mergeSortRecursive2(seq,start,stop):
    if start >= stop:
        return 
    elif start == stop -1:
        if seq[0][start] > seq[0][stop]:
            seq[0][start]=seq[1][stop]
            seq[0][stop]=seq[1][start]
            seq[1][start]=seq[0][start]
            seq[1][stop]=seq[0][stop]
        return
    mid = (start+stop)//2
    mergeSortRecursive2(seq,start,mid)
    mergeSortRecursive2(seq,mid+1,stop)
    merge2(seq,start,mid,stop)

def mergeSort2(seq):
    lsts = [seq,seq.copy()]
    mergeSortRecursive2(lsts,0,len(seq)-1)

if __name__ == "__main__":
    a = [4,2,3,1,5]
    b = a.copy()
    mergeSort(a)
    mergeSort2(b)
    print(a)
    print(b)
    a = [4,3,2,1]
    b= a.copy()
    mergeSort(a)
    mergeSort2(b)
    print(a)
    print(b)
    a = [4,2,3,2,7,7,8,9]
    b= a.copy()
    mergeSort(a)
    mergeSort2(b)
    print(a)
    print(b)