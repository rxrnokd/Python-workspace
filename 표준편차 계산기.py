#표준편차 계산기

a = []
c = 0
term  = int(input('항을 입력하세요: '))

for i in range(1, term + 1):
    a.append(float(input('값을 일력 하시오: ')))

b = sum(a)/len(a)
print(f'평균: {b:.2f}')

for i in range(0, term):
    c += ((a[i] - b)**2)

c /= (term -1)
c **= 0.5

print(f'표준편차: {c:.4f}')    
    
