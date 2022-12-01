# 선형 검색 알고리즘 (3_1) 을 보초법으로 수정

from typing import Any,Sequence
import copy

def seq_search(seq: Sequence, key:Any) -> int:
    """시퀀스 seq에서 key 와 일치하는 원소를 선형 검색(보초법)"""
    a = copy.deepcopy(seq) #copy seq 
    a.append(key)  # sentinel key append

    i=0
    while True:
        if a[i]==key:
            break
        i +=1
    return -1 if i == len(seq) else i 

if __name__=='__main__':
    num = int(input('원소수를 입력하세요: '))
    x= [None] * num 

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky=int(input('put the key: '))

    idx=seq_search(x, ky)

    if idx == -1:
        print(' 검색할 키 존재하지않음.')
    else:
        print(f' 검색값은 x[{idx}]에 있습니다. ')