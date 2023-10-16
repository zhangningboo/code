# https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/#
# Python3 program to find out maximum 
# value from a given sequence of coins 

# Returns optimal value possible that 
# a player can collect from an array 
# of coins of size n. Note than n 
# must be even 


def optimalStrategyOfGame(arr, n): 

    # Create a dp_table to store 
    # solutions of subproblems 
    dp_table = [[0] * n for _ in range(n)] 

    # Fill dp_table using above recursive 
    # formula. Note that the dp_table is 
    # filled in diagonal fashion 
    # (similar to http://goo.gl / PQqoS), 
    # from diagonal elements to 
    # dp_table[0][n-1] which is the result. 
    # dp_table[i][j] 含义：从第 i 堆到第 j 堆硬币区间内，先手能拿到的最大值
    for gap in range(n):
        for j in range(gap, n): 
            i = j - gap  # 使用gap控制填写顺序

            # Here x is value of F(i + 2, j), 
            # y is F(i + 1, j-1) and z is 
            # F(i, j-2) in above recursive 
            # formula
            if i + 2 <= j:  # 剩余的长度大于2
                x = dp_table[i + 2][j]  # 选 i，对手选 i + 1， 剩余区间是[i + 2, j]
                y = dp_table[i + 1][j - 1]  # 选 i，对手选 j， 剩余区间是[i + 1, j - 1]
                z = dp_table[i][j - 2]  # 选 j，对手选 j - 1， 剩余区间是[i, j - 2]
                # 因为有 gap 控制了填写顺序，计算dp_table[i][j]时，使用的值都已经计算过了
                dp_table[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
            elif i + 1 == j:  # 只剩余两个，取其中最大的一个
                dp_table[i][j] = max(arr[i], arr[j])
            elif i == j:  # 只剩余一个，没什么好选择的
                dp_table[i][j] = arr[i]                                                                                   
            
    return dp_table[0][n - 1]


# Driver Code 
arr1 = [8, 15, 3, 7] 
n = len(arr1) 
print(optimalStrategyOfGame(arr1, n)) 

arr2 = [2, 2, 2, 2] 
n = len(arr2) 
print(optimalStrategyOfGame(arr2, n)) 

arr3 = [20, 30, 2, 2, 2, 10] 
n = len(arr3) 
print(optimalStrategyOfGame(arr3, n)) 

# This code is contributed 
# by sahilshelangia 
