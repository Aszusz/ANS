alphabet = {
    'A': 0.1,
    'B': 0.3,
    'C': 0.6}

table_size = 2 ** 10

symbol_appearances = {
    symbol: round(probability * table_size)
    for symbol, probability
    in alphabet.items()}


def correct_symbol_appearances():
    if sum(symbol_appearances.values()) < table_size:
        index = max(symbol_appearances.items())[0]
        symbol_appearances[index] += 1


correct_symbol_appearances()


def generate_spread_fast():
    step = (table_size >> 1) + (table_size >> 3) + 3
    mask = table_size - 1
    position = 0
    spread_table = [None] * table_size
    for symbol, probability in alphabet.items():
        for i in range(0, symbol_appearances[symbol]):
            spread_table[position] = symbol
            position = (position + step) & mask
    return spread_table


print(generate_spread_fast())
