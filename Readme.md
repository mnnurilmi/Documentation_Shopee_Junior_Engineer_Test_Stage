# Documentation for Shopee Junior Engineer Test Stage

So, this documentation aims to remind me or the reader when we are going to do the test stage for the shopee junior engineer position. The steps to get this position are as follows:
1. Test Stage
2. HR Call
3. End user interview

Because at the last commit the author was in the first step, the description of the test stages was divided into 2 sub-tests, namely 5 logic questions and 1 coding test.

## For the Logical Question
Topics may appear the same, including data structures, complexity of space and time, and algorithms (basic). Graphs, undirected graphs, trees, stacks, queues, hashes, and other related material can appear. We have to understand the basics of each material. This test will be held only 30 minutes

## For the Coding Test
Coding tests were performed randomly. Maybe one person and another get a different case. This test will be held in just 10 minutes. In my case I had a case that I had to build a function which should analyze the string in case of repeating characters, e.g. "aa.."/"bb..". If in that string all repeating characters, then the function should return "-1". If in the string there is a single character and it does not occur twice then the function must return the first index that satisfies the non-repeating criteria. For example
```
input:"aabbcc"
output: -1

input:"abacc"
output:1

input:"abca"
output:1
```
So, in this case, I can't meet all the expected outputs in 10 minutes. So, after the test finished, I tried to finish this coding test and it took me 50 minutes to complete. So, in this case, I'm 5 times slower to think of a proper way to solve this problem.

This is the last code I made
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
