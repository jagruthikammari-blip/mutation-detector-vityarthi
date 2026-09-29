# mutation-detector-vityarthi
 simple Python program that calculates the required volume of stock solution using the dilution equation:

**C1 × V1 = C2 × V2**

## What it does

The program calculates:

- **V1** — volume of stock solution required
- **Diluent volume** — volume of water/buffer to add
- **Final volume** — desired total volume

## Example

The example in the program uses:

- Stock concentration (C1): 10 M
- Desired concentration (C2): 2 M
- Final volume (V2): 500 mL

The program calculates:

- Stock solution needed: 100.00 mL
- Diluent needed: 400.00 mL
- Total final volume: 500.00 mL

## Requirements

- Python 3.x
- No external Python libraries are required.

## How to run

1. Install Python 3.
2. Open a terminal in this project folder.
3. Run:

```bash
python main.py
```

## Formula

The program uses:

```text
C1 × V1 = C2 × V2
```

and rearranges it to:

```text
V1 = (C2 × V2) / C1
```

## Validation

The program checks that:

- C1 is greater than zero.
- C2 does not exceed C1.

## Project structure

```text
dilution-calculator/
├── main.py
├── README.md
└── .gitignore
```
