#to check for duplicatee item and print them out ignore the extensions
listme2=["pawpaw.txt","tomato.txt","apple.mb","apple.mb","apple.mb","carrot.pg","goat.jpg","goatt.jpg","cashew.mb","cashew.mb","groundnut.jpg"]
opt=[]
duplicate=[]
for i in listme2:
    opt.append(i)
    if opt.count(i)>1: 
        duplicate.append(i)
        #print(duplicate)
    else:
        continue 
print(duplicate)

