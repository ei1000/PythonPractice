value_range = 1023
reference_range = 5.00
true_range = reference_range/value_range

input_range = float(input("Input bits: "))
output_range = input_range*true_range

print("V_DAC(%.0f) -> %.2f" % (input_range, output_range))