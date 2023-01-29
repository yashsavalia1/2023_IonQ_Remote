import numpy as np

def encoder(image):
    image_ = image.reshape(len(image)*len(image))
    size = len(image_)
    n_ = np.ceil(np.log(len(image)) / np.log(2))
    n_qubits = (2*n_) + 1
    q = qiskit.QuantumRegister(3)
    qc = qiskit.QuantumCircuit(n_qubits)
    for i in range(n_qubits - 1):
        qc.h(i)
    qc.barrier()
    for i in range(2**(2*n_)):
        for j in range(n_qubits - 1):
            b = format(j, f'0{n_}b')
            for l in len(b):
                if b[l] == '0':
                    qc.x(l)

        qc.mcry(image_[len - i], np.arange(n_qubits - 1), n_qubits-1)
        
        
        for j in range(n_qubits - 1):
            b = format(j, f'0{n_}b')
            for l in len(b):
                if b[l] == '0':
                    qc.x(l)
        qc.barrier()
    return qc

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