binary_data = b'\x00\xFF\x00\xFF'
import binascii
base64_data = binascii.b2a_base64(binary_data)
print(base64_data)