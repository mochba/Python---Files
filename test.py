t = ['0.8475', '0.6178', '0.6961', '0.7565', '0.7626', '0.7556', '0.7002', '0.7615', '0.7601', '0.7605', '0.6959', '0.7606', '0.7559', '0.7605', '0.6932', '0.7558', '0.6526', '0.6948', '0.6528', '0.7002', '0.7554', '0.6956', '0.6959', '0.7556', '0.9846', '0.8509', '0.9907']
# print(t)
# v= 0.0
# for i in t:
#     float(i)
#     v = v + i
# print(v)

value = 0.0
count = 0
# t = ['4.3','6.7','10.10']
print(t)
for i in range(0,len(t)):
    value = t[i]
    fv = float(value)
    print(fv)
    value = float(value) + fv
    count = count +1 
print(value)
print(value/count)
    