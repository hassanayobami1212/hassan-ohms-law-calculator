# Ohm's Law and Power Calculator

## What it does
This Python program calculates voltage, current, resistance or electrical power from two known electrical values. It uses a menu so the user can choose what to calculate, and it keeps running until the user quits.

## How to run it
1. Install Python 3.
2. Download `ohms_law.py`.
3. Open a terminal in the folder containing the file.
4. Run:

```bash
python ohms_law.py
```

## Sample output

```text
====================================
   OHM'S LAW AND POWER CALCULATOR
====================================

What would you like to calculate?
1. Voltage (V)
2. Current (I)
3. Resistance (R)
4. Power (P)
5. View calculation history
6. Quit
Enter your choice (1-6): 1

Choose the two values you already know:
1. Voltage and current (V and I)
2. Voltage and resistance (V and R)
3. Current and resistance (I and R)
4. Power and current (P and I)
5. Power and voltage (P and V)
6. Power and resistance (P and R)
Enter your choice (1-6): 3
Enter current (A): 2
Enter resistance (Ω): 5

--- RESULT ---
Voltage = 10.00 volts (V)
```

## My own twist
I added a calculation history feature. The user can choose option 5 to review all results calculated during the current session. This makes it easier to compare results without restarting the program.

## What I learned
I practised using Python functions, loops, if/elif/else decisions, dictionaries, lists, user input, number conversion and error handling. I also practised applying Ohm's Law and electrical power formulas in a small program.

## Author
Hassan Abdulsubur Ayobami  
ND1 Mechatronics Engineering, Yaba College of Technology (YABATECH)
