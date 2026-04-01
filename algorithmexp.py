#Boyer-Moore Majority Voting Algorithm
nums=[2,2,4,2,3,6,2]
def BMMVA(arr : list) -> int:
    major = arr[0]
    count = 0
    #To find the candidate number
    for each in arr:
        if count==0:
            major = each
        if each == major:
            count +=1
        else:
            count -=1
    return major
#To check if this candidate number is the correct answer
def judgement(major,arr):
    if nums.count(major)>len(arr)/2:
        print("多数元素为："+str(major))
    else:
        print("不存在多数元素")
result = BMMVA(nums)
print(result)
judgement(result,nums)