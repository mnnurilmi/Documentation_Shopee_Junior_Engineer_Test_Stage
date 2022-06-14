text = list('abacc')
print(text)

found_not_duplicate =False
for idx,cha in enumerate(text):
    duplicate_cha = []
    for idx_check,check_cha in enumerate(text):
        if cha in (duplicate_cha):
            continue
        if cha == check_cha and idx != idx_check:
            duplicate_cha.append(cha)
            continue
        if idx_check == len(text)-1:
            print(idx)
            found_not_duplicate = True
            break
    if found_not_duplicate == True:
        break
    elif(idx == len(text)-1):
        print(-1)


