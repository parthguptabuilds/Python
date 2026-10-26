token="sec-9081-ALPHA"
print(token)
i_d=id(token)
print(i_d)

new=(token[:4]+"X"+token[5:])
print(new)
i_d2=id(new)
print(i_d2)

# this give error
# token[4]="X"
# print(token[4])