# Documentation for Shopee Junior Engineer Test Stage

So, this documentation aims to reminder me or the reader when we will do test stage on shopee junior engineer position. The steps of to get this position as follows:
1. Test Stage
2. HR call
3. Final user interview

Since on the last commit, the writer is on first steps, the depicture of the test stage is devided on 2 sub test, that is 5 of logical questions and 1 coding test.

## For the Logical Question
The topics that may be appeared on the same test are data stucture, space and time complexity, and also agorithm (basic). The graphs, undirected graphs, tree, stack, quees, hash, and other related materials may be appeared. We must understood the fundamentals each materials. This test will be held just 30 minutes

## For the Coding Test
The coding test is randomed. Maybe one person and the another is difference. This test will be held just 10 minutes. On my case, i have a case that i must build a function that should analize a string if there was a repeatable character, e.g. "aa.."/"bb..". If in that string all of character is repeatable, than the function should return "-1". If in that string there were single character and not appear twice than the function should return the first index of that character was found.
For the example
```
input:"aabbcc"
output: -1

input:"abacc"
output:1

input:"abca"
output:1
```
So, in this case, i cant satisfy all of the expeted outputs in 10 minutes. So, after the test over, i've tried to solve this coding test and i got 50 minutes to solve it. So, in this case, i 5 times slower to thiking the proper way to solve this problem.

This is the final code that i've built
```
inp = "aabbcc"
# inp = "abca"
def isRepeating(inputs):
    z = list(inputs)
    z_dict = {}
    for el in range(len(z)):
        z_dict[el]=-1
    print(z_dict)
    for i in range(len(z)-1):
        key = z[i]
        for j in range(i+1,len(z)):
            pair = z[j]
            if key == pair:
                print("sama")
                z_dict[i] = 1
                z_dict[j] = 1  
    print(z_dict)       
    for key, value in z_dict.items():
        if value == -1:
            return key 
    return -1
print(isRepeating(inp))
```
### Code Explanation
In the above code, I used a list and dictionary data structure. The dictionary will store the list index and character state, because characters are represented by the list value index.

Firstly, I convert the input string parameter to a list. Then, I create a dictionary and I populate it with the key is the index of the list and the value is the state.

Secondly, for the first iteration, I iterate over the list up to index "length of list z minus one" because the comparison limit is at the last index and one before the last index. I set the "key" variable with the element of index i. After that, the element of index i will be compared with each element on the list. The pair variable is assigned a value represented by the element of index "j".

Thirdly, I compared the "key" and "pair" variables. If the keys are the same as the pair, then the dictionary that has the keys i and j will be assigned a value of 1. This state 1 indicates that the characters in both positions are the same.
Finally, I checked the dictionary value. If any key has a value of -1, then the function will return the dictionary key. Otherwise, the function will return -1 indicating all characters in the repeated string.
