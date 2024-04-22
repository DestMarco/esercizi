def intesrsection(nums1:list [int], nums2:list[int])->list [int]:
    elements_comuni=[]
    for i in nums1:
        if i in nums2 and i not in elements_comuni:
            elements_comuni.append(i)
    return elements_comuni
nums1=[2,2,4,2,1]
nums2=[1,1,2,0,2,1,2]
risultato=intesrsection(nums1,nums2)
print(risultato)