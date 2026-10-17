from fractions import Fraction

def exact(x):
    return Fraction.from_float(float(x))

def duplicate_row_identity(original_row, new_row):
    return list(map(exact, original_row)) == new_row[:-1] and new_row[-1] == 0

def readout_identity(original, augmented):
    return augmented[0] + augmented[-1] == exact(original[0]) and augmented[1:-1] == list(map(exact, original[1:]))
