def count_split_ways(n):
    # 初始化拆分方式计数
    ways = 0

    # 情况1：a和b都是3的倍数
    ways += n // 3

    # 情况2：只有一个数是3的倍数
    for x in range(1, n // 3 + 1):
        if (n - 3 * x) % 3 == 0:
            ways += 1

    return ways

n = int(input("请输入正整数 n："))
result = count_split_ways(n)
print("有", result, "种拆分方式满足条件.")
