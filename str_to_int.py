str_num_tuple='1','2','3','4'
print("string number tuple is:",str_num_tuple)
num_list=[]
for num in str_num_tuple:
    num_list.append(int(num))
print("Number List:",num_list)
num_tuple=tuple(num_list)
print("Final Output:",num_tuple)
