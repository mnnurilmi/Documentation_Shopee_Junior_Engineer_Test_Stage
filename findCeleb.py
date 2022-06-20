"""
Find the Celebrity

There is gathering of N people labeled from 1 to N. Among these pople, there might be one Celebrity. A Celebrity is someone who:
    1.Dosn't know anyone in the gathering
    2.Is known by everyone else in gethering
Given the information of list A knows B, return the index of the Celebrity. If there is no Celebrity, return -1 
Example 
input:
    3
    2
    1 3
    2 3
output 
3
Explanation
Everyone other than 3 (1,2) knows 3, but 3 does not know anyone, so 3 is Celebrity
"""
input = [[3,5],[2],[1,5],[2,5],[4,5],[5,3]]
peoples = []
for idx, pair in enumerate(input):
    for idx_pair, people in enumerate(pair):
        if people not in peoples :
            peoples.append(people)
celeb_found = False
for people in peoples:
    known=0
    for idx, pair in enumerate(input):
            if len(pair)==1:
                continue
            elif pair[1] == people: 
                known+=1
            elif pair[0] == people:
                known-=1
    if known == len(peoples) - 1:
        celeb_found =True
        print(people)
        break
if celeb_found == False:
    print(-1)




        

