from xmlrpc.client import boolean


print("For string:")
text1="halo,konmday"
text1_a=int ("123")#can convert string to int only number in string#if it is a letter or text we cant convert to int or float
text1_b=float("78")
text1_c=bool("Ty")
print(type(text1))
print(type(text1_a))
print(type(text1_b))
print(type(text1_c))
print("For integer:")
text2=90
text2_a=str(text2)
text2_b=float(text2)
text2_c=bool(text2)
print(type(text2))
print(type(text2_a))
print(type(text2_b))
print(type(text2_c))

print("For boolean:")
text3=True
text3_a=str(text3)
text3_b=float(text3)
text3_c=int(text3)
print(type(text3))
print(type(text3_a))
print(type(text3_b))
print(type(text3_c))


print("For float:")
text4=93.45
text4_a=str(text4)
text4_b=float(text4)
text4_c=bool(text4)
print(type(text4))
print(type(text4_a))
print(type(text4_b))
print(type(text4_c))
