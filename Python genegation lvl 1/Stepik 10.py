'''
st_in = input()
st_out = ''
for i in range(len(st_in)):
    if i % 3 == 0:
        continue
    st_out += st_in[i]
print(st_out)
'''
'''
print(input().replace("1", "one"))
'''
'''
st_in = input()
st_out = ''
for i in st_in:
    if i == '@':
        continue
    st_out += i
print(st_out)
'''
'''
st = input()
i_1 = st.find('f')
if i_1 == -1:
    print(-2)
else:
    st = st[i_1 + 1:]
    i_2 = st.find('f')
    if i_2 == -1:
        print(-1)
    else:
        i_2 += 1 + i_1
        print(i_2)
'''

st = input()
i_1 = st.find('h')
i_2 = st.rfind('h')
print(st[:i_1]+st[i_2:i_1:-1]+st[i_2:])
