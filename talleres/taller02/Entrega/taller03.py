#Fuerza Bruta


# 1
def punto1(start, nums, target):
    if start==len(nums):
        return target==0
    return punto1(start+1,nums,target-nums[start]) or punto1(start+1,nums,target)


# 2
def punto2(pre, pos, resultado):
	resultado.add(pre)
	if len(pos)==0 :
		return resultado
	return punto2(pre+pos[:1],pos[1:],resultado) and punto2(pre,pos[1:],resultado)

