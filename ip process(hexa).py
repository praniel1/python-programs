import binascii

def comple(a):
    str = ""
    for bit in a:
        if bit == "1":
            str+="0"
        else:
            str+="1"
    return str

def addzero(arr):
    a = ""
    if len(arr)<16:
        diff = 16-len(arr)
        for num in range(diff):
            a+="0"
        a+=arr
    else:
        a=arr
    return a

dd="4500 003c 1c46 4000 4006 b1e6 ac10 0a63 ac10 0a0c"
data = "4500003c1c46400040060000ac100a63ac100a0c"
# version = int(data[:1])
# head_len = int(data[1:2])
# tos = data[2:4]
# tl = data[4:8]
# iden = data[8:12]
# fragment = data[12:16]
# ttl = data[16:18]
# protocol = data[18:20]
# sen_checksum = data[20:24]
# source = data[24:32]
# des = data[32:40]
# print "1011000111100110"

six1 = bin(int(data[:4],16))#convert 4characters to binary
six1 = six1[2:]
six1 = addzero(six1)
print six1

six2 = bin(int(data[4:8],16))
six2 = six2[2:]
six2 = addzero(six2)
print six2

six3 = bin(int(data[8:12],16))
six3 = six3[2:]
six3 = addzero(six3)
print six3

six4 = bin(int(data[12:16],16))
six4 = six4[2:]
six4 = addzero(six4)
print six4

six5 = bin(int(data[16:20],16))
six5 = six5[2:]
six5 = addzero(six5)
print six5

six6 = bin(int(data[20:24],16))
six6 = six6[2:]
six6 = addzero(six6)
print six6

six7 = bin(int(data[24:28],16))
six7 = six7[2:]
six7 = addzero(six7)
print six7

six8 = bin(int(data[28:32],16))
six8 = six8[2:]
six8 = addzero(six8)
print six8

six9 = bin(int(data[32:36],16))
six9 = six9[2:]
six9 = addzero(six9)
print six9

six10 = bin(int(data[36:40],16))
six10 = six10[2:]
six10 = addzero(six10)
print six10

# s =bin(int(six1,2) + int(six2,2)+int(six3,2)+int(six4,2)+int(six5,2)+int(six6,2)+int(six7,2)+int(six8,2)+int(six9,2)+int(six10,2))
# s = s[2:]
# print s
#
# s_com = comple(s)
# print s_com
# int_check_sum = int(sen_checksum,16) # convert sender checksum to decimal
# print int_check_sum
# s = int(data[:8],16)+int(data[8:16],16)+int(data[16:24],16)+int(data[24:32],16)+int(data[32:40],16) # add datas
# s_bin = bin(s) # convert data to binary
# s_bin2 = s_bin[2:]
# print s
# print s_bin2
# complement = comple(s_bin2) # take 1's complement
# print complement
# com_val = int(complement,2)
# print com_val
# print complement
# print "version : "+str(version)
# print "head length : "+str(head_len)
# print "type of service : "+tos
# print "Total length : "+tl
# print "Identification : "+iden
# print "Fragmentation : "+fragment
# print "Time to live : "+ttl
# print "Protocol : "+protocol
# print "head check sum : "+sen_checksum
# print "souce address : "+source
# print "Destination address : "+des
# print int_check_sum
