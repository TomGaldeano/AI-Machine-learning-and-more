buckets = dict()
for i in range(256):
    buckets[chr(i)] = []

def charAt(s,i):
    if len(s) - 1 < i:
        return " "  
    return s[i]

def RadixSort(*args):
    elements = []
    max = 0
    for i in args:
        if len(i) > max:
            max = len(i)
        elements.append(str(i))
    return(recurse_radix(elements,max-1))

def recurse_radix(elements,size):
    if size == -1:
        return elements
    for i in elements:
        buckets[charAt(i,size)].append(i)
    ans = []
    i = 0
    while i < 256:
        while len(buckets[chr(i)]) > 0:
            ans.append(buckets[chr(i)].pop())
        i+=1
    return recurse_radix(ans,size-1)

def test():
    ordered = RadixSort("hello", "world","potato","apple","barnacle","hell")
    if ordered == ["apple","barnacle","hell","hello","potato","world"]:
        print("we did it")
    for i in ordered: 
        print(i)

if __name__ == "__main__":
    test()
