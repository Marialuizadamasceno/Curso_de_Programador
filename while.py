paisA=80000
anoA=0.03
paisB=200000
anoB=0.015
contagem=0
while paisA<paisB:
    paisA+=paisA*anoA
    paisB+=paisB*anoB
    contagem+=1
print(contagem)