# A Dynamic Programming based Python Program
# to solve the Constrained Optimization Problem faced by Bitcoin Miners
# Returns the maximum transactions fees that a solo miner can receive for a winning block

def bitcoinMaximization(block_size, transaction_size, fees, mempool):
    K = [[0 for x in range(block_size + 1)] for x in range(mempool + 1)]

    # Build table K[][] in bottom up manner
    for i in range(mempool + 1):
        for w in range(block_size + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif transaction_size[i - 1] <= w:
                K[i][w] = max(fees[i - 1] + K[i - 1][w - transaction_size[i - 1]],  K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[mempool][block_size]

# Main program feeds the transactions available in mempool for miner to select
if __name__== "__main__":
    mining_fees_in_bitcoin = [0.0887, 0.1856, 0.2307, 0.1522, 0.0532, 0.0250, 0.1409, 0.2541, 0.1147, 0.2660, 0.2933, 0.0686]
    transaction_size_in_bytes = [57247, 98732, 134928, 77275, 29240, 15440, 70820, 139603, 63718, 143807, 190457, 40572]
    #maximum_block_size = 500000
    maximum_block_size = 1000000
    available_transactions_in_mempool = len(transaction_size_in_bytes)
    block_reward = 12.5
    max_gas_collectable = bitcoinMaximization(maximum_block_size, transaction_size_in_bytes, mining_fees_in_bitcoin, available_transactions_in_mempool)
    print (f'Max Transaction Fees a Miner gets from given Mempool of Transations is approximately: {str(round(max_gas_collectable, 4))}')
    print (f'Max Block Reward for Winning Block is set at: {block_reward}')
    print (f'Total Possible Reward for next Block: {block_reward + max_gas_collectable} ')
