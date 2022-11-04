import copy

spaces = [0]*11
first_persons = [1,2,3,5,7,10]


def set_person(sp,first):
    for n in first:
        sp[n] = 1
    
    return sp

def next_time(persons):
    next_patern = copy.copy(persons)
    for now_position,val in enumerate(persons):
        if now_position == len(persons) - 1: #一番右側を調べる時
            if persons[0] == 0  and val == 1:
                next_patern[0] = 1
                next_patern[now_position] = 0
        else: #それ以外を調べる
            if persons[now_position + 1] == 0 and val == 1:
                next_patern[now_position + 1] = 1
                next_patern[now_position] = 0
        #print(now_position,next_patern)
        #print(now_position,persons)
    return next_patern

p = set_person(spaces,first_persons)

print(0)
print(p)
for i in range(10):
    print(i + 1)
    p = next_time(p)
    print(p)

