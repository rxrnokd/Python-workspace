#백분율 오차 계산기

a = float(input('이론값을 입력하세요: '))
b = float(input('실험값을 입력하세요: '))
c = ((a - b)/a)*100
if c < 0:
    c *= -1
    print(f'백분율 오차: {c:.4f}')
else:
    print(f'백분율 오차: {c:.4f}')    
    
    
