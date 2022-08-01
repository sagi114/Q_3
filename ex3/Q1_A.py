def permute(A):
    size_A = len(A)
    if size_A==0:
        return
    if size_A==1:
        new_list=[]
        new_list.append(A[0])
        return new_list
    if size_A>1:
        char=A[0]
        a=list(A)
        a.remove(char)
        A =''.join(a)
        new_list=permute(A)
        size_l=len(new_list)
        list_of_list=[]

        for n_l in new_list:
            for n in range(size_A):
                tmp_new_list=list(n_l)
                tmp_new_list.insert(n,char)
                list_of_list.append(tmp_new_list)
        return list_of_list
if __name__ == '__main__':
    print(permute('abc'))