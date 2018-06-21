import numpy
with open('C://Users//10111//documents//GitHub//HuffmanCoding//compressed','r') as compressed:
    data = compressed.read()
bits = numpy.unpackbits(data)
print(bits)
print('done')