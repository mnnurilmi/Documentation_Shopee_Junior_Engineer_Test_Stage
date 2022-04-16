def main():
    inputs = input("Please enter a string:")
    print(isRepeating(inputs))

def isRepeating(inputs):
    z = list(inputs)
    z_dict = {}
    for el in range(len(z)):
        z_dict[el]=-1
    # print(z_dict)
    for i in range(len(z)-1):
        key = z[i]
        for j in range(i+1,len(z)):
            pair = z[j]
            if key == pair:
                # print("sama")
                z_dict[i] = 1
                z_dict[j] = 1  
    # print(z_dict)       
    for key, value in z_dict.items():
        if value == -1:
            return key 
    return -1

if __name__=="__main__":
    main()