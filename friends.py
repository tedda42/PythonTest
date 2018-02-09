fr = open('listin.txt', 'r')
f = int(fr.readline().strip())
friends = {}
maxFriends = 0
for i in range(f):
    v = fr.readline().split()
    # print v
    for j in range(0, 2):
        if (v[j] in friends):
            friends[v[j]] = friends[v[j]] + 1
        else:
            friends[v[j]] = 1
        if (friends[v[j]] > maxFriends):
            maxFriends = friends[v[j]]
answer = []
for k in friends:
    if (friends[k] == maxFriends):
        answer.append(int(k))
answer.sort()
w = open('listout.txt', 'w')
for a in answer:
    w.write(str(a) + '\n')
