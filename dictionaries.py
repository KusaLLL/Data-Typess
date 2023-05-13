names = ['a','b','c','a','a'] #list with duplicates
count = {} #empty dictionary

for name in names: #itarate through names variable
    if name not in count: # chech is it not in thw list
        count[name] = 1 #if not add a counter 1
    else:
        count[name] += 1 #if do add an increment

print(count) #print

d = {"john":40, "peter":45}
print(list(d.keys()))
