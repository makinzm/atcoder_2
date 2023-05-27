i_hs, i_ms = list(map(int,input().split()))

conv_2 = lambda x: "0"+x if len(x)==1 else x

def forward(h: str,m: str):
    h,m = int(h),int(m)
    if m < 59:
        return (h, m+1)
    else:
        if h == 23:
            h = -1
        return (h+1, 0)

hs = conv_2(str(i_hs))
ms = conv_2(str(i_ms))

flag = False

while(True):
    if hs[0] == "0" or hs[0] == "1":
        if int(hs[1]) < 6:
            print(i_hs, i_ms)
            flag = True
        else:
            i_hs, i_ms = forward(hs,ms)
            hs = conv_2(str(i_hs))
            ms = conv_2(str(i_ms))
    elif hs[0] == "2":
        if int(ms[0]) < 4:
            print(i_hs, i_ms)
            flag = True
        else:
            i_hs, i_ms = forward(hs,ms)
            hs = conv_2(str(i_hs))
            ms = conv_2(str(i_ms))
    if flag:
        break
