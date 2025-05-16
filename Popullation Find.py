#To find last 10 years population of a village

curr_pop = 10000

for i in range(10,0,-1):
    print(i, curr_pop)
    curr_pop = curr_pop - 0.1*curr_pop
