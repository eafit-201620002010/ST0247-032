#Fuerza Bruta


# 1
def punto1(start, nums, target):
    if start==len(nums):
        return target==0
    return punto1(start+1,nums,target-nums[start]) or punto1(start+1,nums,target)


# 2
def punto2(s):
    return punto2_aux("",s)

def punto2_aux(base, s):
    if len(s) == 0:
        print(base)
    else:
        for i in range(len(s)):
            punto2_aux(base+s[i], s[:i]+s[i+1:])


