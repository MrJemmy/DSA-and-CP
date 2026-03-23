# binary treated as int
x = 0b10 
x = 6 + x
print(x)

# real binary with 0b
y = bin(-x)
print(y)

# binary to decimal
z = int(y, 2)
print(z)

# -10 => 10 ignore -ve
# 1's complement which is ~ binary not opration on 10
# add 1 result in binary for -10

xx = 10
not_xx = ~xx
print(f"~{xx}:", not_xx)
not_xx_plus_one = not_xx + 1
result = 0
size = 8
power = 1
while(size):
    bit = not_xx_plus_one & 1
    not_xx_plus_one >>= 1
    result = (bit*power) + result
    power *= 10
    size -= 1
print(result)
# print(int(str(result), 2)) : it does not convert into int
    

# 11110110 => -10
# conver to int
# 00001001 not
# -1 
# 00001010


# yy = 11110110 # => 00001010
yy = 1010
result = 0
power = 1
while(yy!=0):
    temp = int(yy / 10) # remoce last digit
    bit = yy - 10 * temp #  yy % 10
    yy = temp
    if bit == 1:
        result = (bit * power) + result
    power *= 2

print(result)
