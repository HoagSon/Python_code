def swap_pairs(list):
    for i in range(0, len(list) -1, 2):
        list[i], list[i+1] = list[i+1], list[i]
    return list    

def avg_length(list):
    count = 0
    for i in range(0, len(list), 1):
        count += len(list[i]) 
    return count / len(list)

def palindrome_check(list):
    reversed = list[::-1]
    if list == reversed:
        return True
    return False

dictionary = {
    "banana": 1,
    "peach": 2,
    "nectarine": 3,
    "kiwi": 4,
    "apple": 5,
}

if __name__ == "__main__":
    list_1 = [10, 20, 30, 40, 50]
    list_2 = ["belt", "hat", "jelly", "bubble gum"]
    list_3 = ["alpha", "beta", "gamma", "delta", "gamma", "beta", "alpha"]
    print(swap_pairs(list_1))
    print(avg_length(list_2))
    print(palindrome_check(list_3))

