import timeit

coins = [50, 25, 10, 5, 2, 1]

# Жадібний алгоритм
def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            amount -= num_coins * coin
            result[coin] = num_coins
    return result

# Принцип динамічного програмування (Top-Down)
def find_min_coins_top_down(amount):
    memo = {}
    
    def dp(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return (0, {})
        min_count = float('inf')
        best_combination = {}
        for coin in coins:
            if n >= coin:
                count, combination = dp(n - coin)
                count += 1
                if count < min_count:
                    min_count = count
                    best_combination = combination.copy()
                    best_combination[coin] = best_combination.get(coin, 0) + 1
        memo[n] = (min_count, best_combination)
        return memo[n]
    
    _, result = dp(amount)
    return result

# Принцип динамічного програмування (Bottom-Up)
def find_min_coins_bottom_up(amount):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    prev_coin = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                prev_coin[i] = coin

    result = {}
    while amount > 0:
        coin = prev_coin[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    return result


amount = 113

print(f"Жадібний алгоритм для {amount}: {find_coins_greedy(amount)}")
print(f"Динамічне програмування (Top-Down): {amount}: {find_min_coins_top_down(amount)}")
print(f"Динамічне програмування (Bottom-Up): {amount}: {find_min_coins_bottom_up(amount)} \n")


# Набір тестових сум
test_amounts = [113, 1137]

# Порівняння швидкості
for amount in test_amounts:
    greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=100)
    top_down_time = timeit.timeit(lambda: find_min_coins_top_down(amount), number=100)
    bottom_up_time = timeit.timeit(lambda: find_min_coins_bottom_up(amount), number=100)
    
    print(f"Жадібний алгоритм для {amount}: {greedy_time:.6f} секунд(и)")
    print(f"Динамічне програмування (Top-Down) для {amount}: {top_down_time:.6f} секунд(и)")
    print(f"Динамічне програмування (Bottom-Up) для {amount}: {bottom_up_time:.6f} секунд(и) \n")