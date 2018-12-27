# VDLS 12/26/18 - Euclid's Algorithm - TAOCP Chapter 1.
# Given two positive integers m and n, find the greatest common divisor.

print("\n-----Euclid's Algorithm.-----\n")

# Flag to end the algorithm.
euclid_active = True
# Flag to check both numbers are positive.
pos_ints = False

# Euclid's Algorithm as a fuction.
def euclids_alg(m,n,euclid_active = True):
    # E0 Ensure m >= n.
    if n > m:
        t = m; m = n; n = t
    # E1 Find Remainder.
    r = m % n
    print(str(r))
    # E2 Is it Zero?
    if r == 0:
        # Yes? Then n is the result.
        print("The greatest common divisor is " + str(n))
        # Flag change to end algorithm.
        euclid_active = False
    else:
        # E3 Reduce.
        m = n; n = r

    return m, n, euclid_active

# User input check.
while not pos_ints:
    try:
        m = int(input("Enter an integer value for m:\t"))
        n = int(input("Enter an integer value for n:\t"))
    except ValueError:
        print("Only INTEGERS!!!")
    else:
        if (m or n) <= 0:
            print("Please enter numbers greater than zero...")
            continue
        else:
            # Flag change to end user input.
            pos_ints = True
            # Main algorithm lööp, bröther.
            while euclid_active:
                m, n, euclid_active = euclids_alg(m,n)

# TODO: Change Algorithm E so that all trivial replacements operations "m <- n" are avoided.