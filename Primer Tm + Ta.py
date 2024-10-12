# Primer Tm and Ta calculation

# Loop for two primer sets

for i in range (2):

# Enter the forward primer

    forward_primer = input("Please enter your forward primer:\n")

# Initialise the nucleotide count of the forward primer

    A = 0
    T = 0
    C = 0
    G = 0

# Obtain the nucleotide count of the forward primer

    for nucleotide in forward_primer:
        if nucleotide == "A":
            A += 1
        elif nucleotide == "T":
            T += 1
        elif nucleotide == "C":
            C += 1
        elif nucleotide == "G":
            G += 1

# Calculate the forward primer Tm

    forward_primer_Tm = 2*(A+T)+4*(G+C)

# Output the forward primer Tm

    print("The forward primer Tm is:", str(float(forward_primer_Tm)) + "°C")

# Enter the reverse primer

    reverse_primer = input("Please enter your reverse primer:\n")

# Initialise the nucleotide count of the reverse primer

    A = 0
    T = 0
    C = 0
    G = 0

# Obtain the nucleotide count of the reverse primer

    for nucleotide in reverse_primer:
        if nucleotide == "A":
            A += 1
        elif nucleotide == "T":
            T += 1
        elif nucleotide == "C":
            C += 1
        elif nucleotide == "G":
            G += 1

# Calculate the reverse primer Tm

    reverse_primer_Tm = 2*(A+T)+4*(G+C)

# Output the reverse primer Tm

    print("The reverse primer Tm is:", str(float(reverse_primer_Tm)) + "°C")

# Initialise the lower primer Tm

    lower_primer_Tm = 0

# Define the lower primer Tm

    if forward_primer_Tm > reverse_primer_Tm:
        lower_primer_Tm = reverse_primer_Tm
    elif forward_primer_Tm < reverse_primer_Tm:
        lower_primer_Tm = forward_primer_Tm
    elif forward_primer_Tm == reverse_primer_Tm:
        lower_primer_Tm = forward_primer_Tm

# Output the lower primer Tm

    print("The lower primer Tm is:", str(float(lower_primer_Tm)) + "°C")

# Enter the PCR product sequence

    PCR_product = input("Please enter your PCR product:\n")

# Initialise the nucleotide count of the PCR product

    A = 0
    T = 0
    C = 0
    G = 0

# Obtain the nucleotide count of the PCR product

    for nucleotide in PCR_product:
        if nucleotide == "A":
            A += 1
        elif nucleotide == "T":
            T += 1
        elif nucleotide == "C":
            C += 1
        elif nucleotide == "G":
            G += 1
        
# Calculate the PCR product Tm

    PCR_product_Tm = 64.9+41*(G+C-16.4)/(A+T+G+C)

# Output the PCR product Tm

    print("The PCR product Tm is:", str(round(PCR_product_Tm, 1)) + "°C")

# Calculate the primer Ta

    PCR_product_Tm = 64.9+41*(G+C-16.4)/(A+T+G+C)

    primer_Ta = 0.3*lower_primer_Tm+0.7*PCR_product_Tm-14.

# Output the primer Ta

    print("The primer Ta is", str(round(primer_Ta, 1)) + "°C")
