listObj = [{
    'Report Data':{'type':'type','Subtype':'Subtype','size':'size'},
    'Detect':{'type':'type','Subtype':'Subtype','size':'size'},
    'list1':{'type':['a','ab','abc']},
    'list2':{'type':['j','k','l','m']},
    'list3':{'type':["r"]},
    'list4':{'type':["u"]},
}]
#o/p should be :   a ab abc  j k l m ... ... ...
key_list=[]
answer=[]
for i in listObj:
    
    #rint(i)
   
    for k in i:
        key_list.append(k)
    for j in key_list[2::]:
        #print(i[j]["type"])
        answer.append(i[j]["type"])
print(answer[::])
real=" "
for i in answer:
    
    for j in i:
        real=real+ " " +j
print(real)




        
        
    