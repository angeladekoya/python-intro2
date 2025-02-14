listfruit= ["orange","orange","orange","apple","apple","apple","apple","apple","apple","pineapple","mango","pawpaw","groundnut"]
print(listfruit)
for i in listfruit:
    if i=="orange":
        print(i)
    listfruit.remove(i)
    print(listfruit)


