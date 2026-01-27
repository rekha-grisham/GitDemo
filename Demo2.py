#Lists are Arrays - can contain any data t - int or string etc in one list
values=[1,2,'a','b',1.2,2.5]
print(values)
print(type(values))
print(values[0])
print(type(values[4]))
print(values[-1]) #last index
print((values[1:3]))
values.insert(1,'c')#adding a new value in the list
print(values)
values.append('d')#adding a new value at the end
print(values)
values[1]='C'
print(values)
values.remove(2)
print(values)
del values[2]
print(values)

#tuple is immutable but same as List. Means it cannot be chnaged or updated.Itis protected
val=(1,2,'a','b',1.2,'c')
print("tuple",val)
#val[0]=3 #cannot change the value after declaration.You will get error
print(val)

#Dictionary declaration=Key value pair.
#Indentations matter in python. every line should be indented correcftly.
dic={"a":1,"b":2,"c":3}
print(dic)
dic={"a":1,"b":2,"c":"THREE"}
print(dic["a"])

dic={}
print(dic)

dic["a"]="Rekha"
dic["b"]="H"
print(dic)

print("This is Git test")

