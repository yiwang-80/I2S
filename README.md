1. use generate_i2s_input.py to generate the digitized sinewave in .CSV format, set the freq, sample rates, bit width, sample size. (the code use 0x00000000 as Zero, and 0xFFFFFFFF as FS)
2. In digital pattern editor, create TDMS file and load the csv into the file.
3. the freq is for FSYNC, the acutal fblk for each line of the vector equals to freq*(bitwidth*number_of_slots+offset+padding)*2
4. the blk is in "RH" format when PASI_BCLK_POL = 0 (default)
5. confirm the pattern loop count equals to sample size
6. confirm each slot length equals to bit width
