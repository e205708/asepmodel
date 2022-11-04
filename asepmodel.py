import copy
import random

spaces = [0]*11
pheromones = [0]*11

first_persons = [1,2,3,5,7,10] #初期値
p_move_right = 0.25 #右に移動する確率
p_move_right_pheromon = 0.75 #フェロモンがある場合の右に移動する確率
p_evaporate = 0.5 # 蒸発する確率

def set_person(sp,first):
    for n in first:
        sp[n] = 1
    
    return sp

def next_time(persons,now_pheromone):
    """ 
    次の時間のありの位置を探す
    """
    next_patern = copy.copy(persons)
    next_pheromone = copy.copy(now_pheromone)

    for now_position,val in enumerate(persons):
        if now_position == len(persons) - 1: #一番右側を調べる時
            if persons[0] == 0  and val == 1 and pheromones_dice(now_pheromone[now_position],p_move_right,p_move_right_pheromon): #一番左側が0かつ、移動させる人がいる場合。かつフェロモンのダイスを満たす。
                next_patern[0] = 1
                next_patern[now_position] = 0
        else: #それ以外を調べる
            if persons[now_position + 1] == 0 and val == 1 and pheromones_dice(now_pheromone[now_position],p_move_right,p_move_right_pheromon): #右隣が0かつ、移動させる人がいる場合。かつフェロモンのダイスを満たす。
                next_patern[now_position + 1] = 1
                next_patern[now_position] = 0
        #print(now_position,next_patern)
        #print(now_position,persons)
    next_pheromone = update_pheromones(next_pheromone,next_patern,p_evaporate)

    return (next_patern,next_pheromone)

def pheromones_dice(phe_value,p_move,p_move_phe):
    """
    フェロモンの値と、移動する確率をもとに、移動するかしないかを判断する
    """
    if phe_value == 1:
        if random.random() < p_move_phe: #フェロモンがある場合
            return True
        else:
            return False
    elif phe_value == 0:
        if random.random() < p_move: #フェロモンがない場合
            return True
        else:
            return False
    
def update_pheromones(phe,pers,p_evaporate):
    for order,p in enumerate(pers):
        if p == 0: #粒子がない場合
            if phe[order] == 1: #フェロモンがある場合
                if random.random() < p_evaporate:#蒸発する
                    phe[order] = 0
                else: #蒸発しない
                    phe[order] = 1
            else: #フェロモンがない場合
                phe[order] = 0
        else: # 粒子がある場合
            phe[order] = 1
    
    return phe

    
p = set_person(spaces,first_persons)
pheromones = set_person(pheromones,first_persons)

print(0)
print(p)
for i in range(10):
    print(i + 1)
    per_and_phero = next_time(p,pheromones)
    p = per_and_phero[0]
    pheromones = per_and_phero[1]
    print("あり")
    print(p)
    print("フェロモン")
    print(pheromones)
    print("\n")

