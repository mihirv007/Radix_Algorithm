box=[86,76,34,88,99]

# time complexity : O(n+d)
def radix_sort(array):
    
    less_significant_numbers=[]
    more_significant_numbers=[]
    for i in range(10):
        less_significant_numbers.append([])
        i+=1

    #buckets=[[] for i in range(1,10)]

    for j in range(10):
        more_significant_numbers.append([])
        i+=1

    for num in array:
        value=num%10
        less_significant_numbers[value].append(num)

    out=[]

    for numbers in less_significant_numbers:
        for item in numbers:
            out.append(item)

    
    for num in out:
        value=num//10
        more_significant_numbers[value].append(num)

    result=[]
    for numbers in more_significant_numbers:
        for item in numbers:
            result.append(item)

    return result


print(radix_sort(box))

    