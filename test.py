print(int(bin(10)[2:]))
bits = "01100010"
newbits = int(bits[::-1], 2).to_bytes(int(len(bits)/8), 'little')
with open('compressed','wb') as output:
    output.write(newbits)
    