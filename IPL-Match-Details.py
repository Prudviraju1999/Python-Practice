def get_points(val):
    po=0
    for o in val:
        if o=="win":
            po+=3
        if o=="loss":
            po+=0
        if o=="draw":
            po+=1
    return po

n=int(input())
if n==0:
    print("No Output")
else:
    g_dict={}                       #forming dict from input
    o_list=[]
    for i in range(n):
        term=input().split(";")
        t1,t2,o=term
        g_dict[t1]=()
        g_dict[t2]=()
        o_list.append(term)
    
    for i in range(n):
        term=o_list[i]
        t1,t2,o=term
        if o=="win":
            o1="win"
            o2="loss"
        if o=="loss":
            o1="loss"
            o2="win"
        if o=="draw":
            o1="draw"
            o2="draw"
        if t1 in g_dict:
            g_dict[t1]+=(o1,)
        if t2 in g_dict:
            g_dict[t2]+=(o2,)
        
    values=list(g_dict.values())
    keys=list(g_dict.keys())

    poits_dict={}                      #points dict from
    for i in range(len(keys)):
        val=list(values[i])
        points=get_points(val)
        poits_dict[keys[i]]=points     

    v=list(poits_dict.values())
    k=list(poits_dict.keys())
    v1=sorted(v)                      #points dict end

    for i in range(len(keys)):      #for printing Output
        j=len(keys)-i-1
        index=v.index(v1[j])
        kee=k[index]
        values=list(g_dict.values())
        keys=list(g_dict.keys())
        g_index=keys.index(kee)
        val=values[g_index]
        print("Team: "+k[index]+", Matches Played: "+str(len(val))+", Won: "+str(val.count("win"))+", Lost: "+str(val.count("loss"))+", Draw: "+str(val.count("draw"))+", Points: "+str(v[index]))
