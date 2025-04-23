1. use generate_i2s_input.py to generate the digitized sinewave in .CSV format, set the freq, sample rates, bit width, sample size.
2. In digital pattern editor, create TDMS file and load the csv into the file.
3. the freq is for FSYNC, the acutal fblk for each line of the vector equals to freq*(bitwidth*number_of_slots+offset+padding)*2
