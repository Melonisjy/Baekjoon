a, b = map(int,input().split()) # 사과 a개와 오렌지 b개
c, d = map(int,input().split()) # 사과 c개와 오렌지 d개

A = a + d
B = b + c

print(min(A, B))