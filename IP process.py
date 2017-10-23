data = "0100010100000000000000011101101000000111100011000100000000000000010000000000011000100101011100010000101000001010011001010100000111001011100000111101000101010010"
version = data[:4]
head_len = data[4:8]
type = data[8:16]
total_length = data[16:32]
indentification = data[32:64]
flag = data[32:35]
f_offset = data[35:64]
ttl = data[64:72]
protocol = data[72:80]
check_sum = data[80:96]
source = data[96:128]
des = data[128:160]
print version
print head_len
print type
print total_length
print indentification
print flag
print f_offset
print ttl
print protocol
print check_sum
print source
print des