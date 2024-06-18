immutable_var=10,20,30,False,'street',[10,20,30]
immutable_var1=(10,20,30,False,'street',[10,20,30])
immutable_var2=tuple([10,20,30,False,'street',[10,20,30]])
print(immutable_var)
print(immutable_var1)
print(immutable_var2)
#immutable_var[4]='home' # В кортеже не поддерживается обращение по элементам,так как он хранит ссылки на объект.
#print(immutable_var)
mutable_list=[10,20,30,"home","street"]
print(mutable_list)
mutable_list[1]=40
mutable_list.append('broomstick')
mutable_list.extend('shovel')
mutable_list.extend([False])
mutable_list.remove(10)
print(mutable_list)
