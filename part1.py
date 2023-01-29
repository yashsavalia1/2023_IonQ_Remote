
def encoder(image):
    pass

def decoder(histogram):
    # count up in binary up to number of pixels
    # for each pixel, look at first qubit (0 and 1)
    # get counts for 0... and 1...
    # expectation value of 0 gives you a number in range 0 - 1
    # this number corresponds to the intensity of the pixel
    n = len(list(histogram.keys())[0]) - 1
    image = np.zeros(2**n)
    for i in range(2**n):
        state_0 = format(i, f'0{n+1}b')
        state_1 = format(i+2**n, f'0{n+1}b')
        count_0 = histogram[state_0] if state_0 in histogram else 0 
        count_1 = histogram[state_1] if state_1 in histogram else 0
        intensity = count_1 / (count_0 + count_1)
        image[i] = intensity
    image.shape = (int(np.sqrt(2**n)), int(np.sqrt(2**n)))
    return image

def run_part1(image):
    pass