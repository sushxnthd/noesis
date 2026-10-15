# Run176 raw first-failure clocks (all 128 evaluations)
Frozen width/seed order: widths 3 then 7; seeds 400..415 in each row. Word order: 1011001010, 1011010100, 001001010111, 100101110100. Zero means no failure within 8192 cycles. Prefix 000000, threshold abs(error)>0.1, float64.

width 3, word 1011001010
actual: 99 0 32 0 0 6280 1789 0 0 4593 0 0 0 1 265 0
affine: 99 0 32 0 0 6280 1789 0 0 4593 0 0 0 1 265 0
baseline32: 100 0 32 0 0 6231 1780 0 0 4631 0 0 0 1 261 0

width 3, word 1011010100
actual: 107 0 33 0 0 6708 1872 0 0 4917 0 0 0 1 309 0
affine: 107 0 33 0 0 6708 1872 0 0 4917 0 0 0 1 309 0
baseline32: 107 0 33 0 0 6652 1861 0 0 4961 0 0 0 1 303 0

width 3, word 001001010111
actual: 58 6315 20 0 5546 3728 1166 0 0 2701 0 0 0 1 116 0
affine: 58 6315 20 0 5546 3728 1166 0 0 2701 0 0 0 1 116 0
baseline32: 58 6362 20 0 5605 3707 1161 0 0 2717 0 0 0 1 116 0

width 3, word 100101110100
actual: 80 0 26 0 0 5072 1459 0 0 3706 0 0 0 1 206 0
affine: 80 0 26 0 0 5072 1459 0 0 3706 0 0 0 1 206 0
baseline32: 80 0 26 0 0 5033 1451 0 0 3735 0 0 0 1 203 0

width 7, word 1011001010
actual: 0 24 0 0 6 0 8 0 0 2625 0 6 14 5 1029 0
affine: 0 24 0 0 6 0 8 0 0 2625 0 6 14 5 1580 0
baseline32: 0 24 0 0 6 0 7 0 0 2654 0 6 14 5 274 0

width 7, word 1011010100
actual: 0 24 0 0 6 0 9 0 0 2877 0 7 16 6 1505 0
affine: 0 24 0 0 6 0 9 0 0 2877 0 7 16 6 1628 0
baseline32: 0 24 0 0 6 0 8 0 0 2911 0 6 16 6 485 0

width 7, word 001001010111
actual: 0 17 0 0 5 0 4 0 0 1407 0 3 7 3 7 0
affine: 0 17 0 0 5 0 4 0 0 1407 0 3 7 3 7 0
baseline32: 0 17 0 0 5 0 4 0 0 1417 0 3 7 3 7 0

width 7, word 100101110100
actual: 0 20 0 0 5 0 6 0 0 2096 0 5 11 4 45 0
affine: 0 20 0 0 5 0 6 0 0 2096 0 5 11 4 45 0
baseline32: 0 20 0 0 5 0 6 0 0 2118 0 5 11 4 44 0

Gate abstentions (all other rows accepted): width3 seed413 on words 001001010111 and 100101110100; width7 seed414 on word 100101110100. First32 gate accepted 125/128. First late switches on the two accepted clock mismatches: 781 and 1232.
Full raw error magnitudes, checkpoint SHA256s, code and numerical traces are in Run176 local reproducibility package.