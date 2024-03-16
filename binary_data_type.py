# Binary data type

# Immutable byteList
myList = [1, 5, 6, 8, 255]
listConvertToBytes = bytes(myList)
print(type(listConvertToBytes))

# Mutable byteArray
byteArrayList = [5, 10, 25, 40, 255]
convertByteArrayToBytes = bytearray(byteArrayList)
convertByteArrayToBytes[3] = 50  # replace the number of index [3]40 to 50
print(convertByteArrayToBytes[3])

'''
1. Bytes and ByteArray range should be 0-256
2. But 256 is not acceptable
3. So the last number of bytes and bytesArray is 255
4. Bytes are immutable
5. BytesArray is mutable
Important: Bytes used for compressing image and something like that
'''
