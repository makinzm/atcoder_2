a = []
for i in range(9):
    a.append(list(map(int,input().split())))

def main():
    ans_set = set(list(range(1,10)))

    # BOX
    for i in range(3):
        for j in range(3):
            s = set()
            for ik in range(3):
                for jk in range(3):
                    s.add(a[3*i+ik][3*j+jk])
            # print(s)
            if ans_set != s:
                return False
    
    # horizon
    for i in range(9):
        s = set()
        for j in range(9):
            s.add(a[i][j])
        # print(s)
        if ans_set != s:
                return False
    
    # vertical
    for j in range(9):
        s = set()
        # print(s)
        for i in range(9):
            s.add(a[i][j])
        if ans_set != s:
                return False
    
    return True
        
print("Yes") if main() else print("No")