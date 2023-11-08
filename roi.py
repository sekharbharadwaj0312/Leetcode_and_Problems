def calculate_profit_loss(N, stocks, M, stock_prices, time_instance):
    realized_profit = 0
    unrealized_profit = 0

    for i in range(N):
        quantity, purchase_time, sell_time = stocks[i]
        current_price = stock_prices[i][time_instance - 1]

        if sell_time == 0:  # Stock not sold
            unrealized_profit += quantity * (current_price - stock_prices[i][purchase_time - 1])
        elif sell_time <= time_instance:  # Stock sold before or at the given time_instance
            realized_profit += quantity * (stock_prices[i][sell_time - 1] - stock_prices[i][purchase_time - 1])

    print(realized_profit)
    print(unrealized_profit)

# Read input
N = int(input())
stocks = [tuple(map(int, input().split())) for _ in range(N)]
M = int(input())
stock_prices = [list(map(int, input().split())) for _ in range(N)]
time_instance = int(input())

# Calculate and print profits
calculate_profit_loss(N, stocks, M, stock_prices, time_instance)
