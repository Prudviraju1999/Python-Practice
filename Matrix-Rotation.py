def rotate_matrix(g_matrix):
    t_matrix=[]
    for i in range(n):
        col=[]
        for j in range(n):
            row=n-j-1
            col.append(g_matrix[row][i])
        t_matrix.append(col)
    return t_matrix


n=int(input())
i_matrix=[]
for i in range(n):
    g_row=list(map(int,input().split()))
    i_matrix.append(g_row)
ini_matrix=i_matrix.copy()
g_matrix=i_matrix.copy()
#print(g_matrix)
co=0
    
for j in range(8):
    input_str=input()
    if input_str!="-1":
        input_condition_list=input_str.split()
        initial_char=input_condition_list[0]
        if initial_char=="R":
            s=int(input_condition_list[1])
            r_by=(s/90)%4
            for i in range(int(r_by)):
                g_matrix=rotate_matrix(g_matrix)
                #print(g_matrix)
                co+=1

        if initial_char=="U":
            n_list=input_condition_list[1:]
            x,y,z=list(map(int,n_list))
            ini_matrix=i_matrix
            ini_matrix[x][y]=z
            #print(ini_matrix)
            for b in range(co):
                ini_matrix=rotate_matrix(ini_matrix)
            g_matrix=ini_matrix
            #print(ini_matrix)

        if initial_char=="Q":
            num_list=input_condition_list[1:]
            k,l=list(map(int,num_list))
            print(g_matrix[k][l])
        
    else:
        break
