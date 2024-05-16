print('서비스 만족도')
print(' 1: 매우 만족')
print(' 2: 만족')
print(' 3: 불만족')

satisfaction=input('서비스 만족도를 입력해주세요')

price=int(input('음식값을 입력해주세요'))

if satisfaction=='1' :
    tip=float(price*0.2)
    service='매우 만족'
elif satisfaction=='2' :
    tip=float(price*0.1)
    service='만족'
else : 
    tip=float(price*0.05)
    service='불만족'

print('서비스 만족도: %s, 팁: %d원' % (service, tip))    