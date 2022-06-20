text='abca'
found_not_duplicate = False
for idx,char in enumerate(text):
    if text.count(char) > 1:
        continue
    elif(text.count(char)) ==1 :
        print(idx)
        found_not_duplicate = True
        break
if found_not_duplicate == False:
    print(-1)

