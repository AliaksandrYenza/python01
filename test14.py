def spy_game(nums):
    re = [ 7,0,0,'xy']
    for i in range(len(nums)-1, 1 , -1):
        if nums[i] == re[0]:
            re.pop(nums[i])
    return ("ss", nums)

print(spy_game([1,0,2,4,0,5,7]))