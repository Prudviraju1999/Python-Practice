n=int(input())
g_dict={}
for i in range(n):
    Pi,Ci=list(map(int,input().split()))
    g_dict[Pi]=Ci
items=list(g_dict.items())
items.sort()
r=""
for i in range(len(items)):
    n=len(items)-1
    Pi,Ci=items[i]
    
    if Pi==0 and Ci>0:
        r=" + "+str(Ci)+r
    if Pi==0 and Ci==0:
        r=""+r
    if Pi==0 and Ci<0:
        po_no=Ci*(-1)
        r=" - "+str(po_no)+r
        
    if Pi==1 and Ci>1:
        r=" + "+str(Ci)+"x"+r
    if Pi==1 and Ci==1:
        r=" + "+"x"+r
    if Pi==1 and Ci==0:
        r=""+r
    if Pi==1 and Ci<0:
        po_no=Ci*(-1)
        r=" - "+str(po_no)+"x"+r
        
    if n>Pi>1 and Ci>1:
        r=" + "+str(Ci)+"x^"+str(Pi)+r
    if n>Pi>1 and Ci==1:
        r=" + "+"x^"+str(Pi)+r
    if n>Pi>1 and Ci==0:
        r=""+r
    if n>Pi>1 and Ci<0:
        if Ci==(-1):
            r=" - "+"x^"+str(Pi)+r
        else:
            po_no=Ci*(-1)
            r=" - "+str(po_no)+"x^"+str(Pi)+r
        
    if Pi==n and Ci>1:
        r=str(Ci)+"x^"+str(Pi)+r
    if Pi==n and Ci==1:
        r="x^"+str(Pi)+r
    if Pi==n and Ci==0:
        r=""+r
    if Pi==n and Ci<0:
        if Ci==(-1):
            r=" - "+"x^"+str(Pi)+r
        else:
            po_no=Ci*(-1)
            r="-"+str(po_no)+"x^"+str(Pi)+r
        
print(r)
