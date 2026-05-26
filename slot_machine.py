import random
import numpy as np

MAXLINES = 3
MINLINES = 1
MAXBET = 100
MINBET = 5

ROWS = 3
COLUMNS = 3

symbol_counts = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(col):
    transposed = np.transpose(col)
    for row in transposed:
        print(" | ".join(row))
    return transposed

def winnings(columns, lines, bet, values):
    total_winnings = 0
    winning_lines = []
    
    transposed = np.transpose(columns)
    
    for line_idx in range(lines):
        symbols_in_line = list(transposed[line_idx])
        
        # Check if all symbols in the line match
        if all(symbol == symbols_in_line[0] for symbol in symbols_in_line):
            symbol = symbols_in_line[0]
            line_winnings = values[symbol] * bet
            total_winnings += line_winnings
            winning_lines.append((line_idx + 1, symbol, line_winnings))
    
    return total_winnings, winning_lines

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $").strip()
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter a valid deposit amount")
        else:
            print("Enter a valid digit")
    return amount
    
def get_number_of_lines():
    while True:
        lines = input("Enter how many lines you want to bet on (1 - " + str(MAXLINES) + ")? ").strip()
        if lines.isdigit():
            lines = int(lines)
            if MINLINES <= lines <= MAXLINES:
                break
            else:
                print(f"Enter lines between {MINLINES} - {MAXLINES}")
        else:
            print("Enter a valid digit")
    return lines

def get_bet_amount():
    while True:
        bet = input("Enter how much you want to bet (" + str(MINBET) + " to " + str(MAXBET) + "): $").strip()
        if bet.isdigit():
            bet = int(bet)
            if MINBET <= bet <= MAXBET:
                break
            else:
                print(f"Enter between {MINBET} to {MAXBET}")
        else:
            print("Enter a valid digit")
    return bet

def main():
    balance = deposit()
    
    while True:
        line = get_number_of_lines()

        while True:
            bet = get_bet_amount()
            total_bet = bet * line
            if total_bet > balance:
                print(f"You do not have enough balance. Your current balance is ${balance}")
            else:
                break
        
        balance -= total_bet
        print(f"\nYou are betting ${bet} on {line} lines. Total bet = ${total_bet}")
        print("=" * 40)
        
        slots = get_slot_machine_spin(ROWS, COLUMNS, symbol_counts)
        print_slot_machine(slots)
        
        total_winnings, winning_lines = winnings(slots, line, bet, symbol_value)
        
        if winning_lines:
            print("=" * 40)
            print("WINNING LINES:")
            for line_num, symbol, payout in winning_lines:
                print(f"Line {line_num}: {symbol} x {bet} = ${payout}")
            print(f"Total Winnings: ${total_winnings}")
        else:
            print("=" * 40)
            print("No winning lines!")
        
        balance += total_winnings
        print(f"Current Balance: ${balance}")
        print("=" * 40)
        
        if balance == 0:
            print("You are out of money!")
            break
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print(f"Thanks for playing! Final balance: ${balance}")
            break

if __name__ == "__main__":
    main()