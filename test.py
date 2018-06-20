import struct
bits = '11000011'
int_value = int(bits[::-1], base=2)
bin_array = struct.pack('i', int_value)
with open('compressed.txt','wb') as output:
    output.write(bin_array)