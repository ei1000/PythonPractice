attack = [1,2,3,4,5,7]
defend = [1,2,3,4,5]
resultat = []


# greater_list = len(liste1) - len(liste2)
# print(greater_list)
# if greater_list > 0:
#     range_list = len(liste1)
#     for x in range(greater_list):
#         liste2.append(0)
#     print(len(liste2))
# else:
#     range_list = len(liste2)
#     for x in range(0,abs(greater_list)):
#         liste1.append(0)
#     print(len(liste1))



# print(range_list)

# for x in range(0,range_list):
#     resultat.append(liste1[x]-liste2[x])



def is_defended(attackers, defenders):
    survivors = 0
    greater_list = len(defenders) - len(attackers)
    print(greater_list)
    if greater_list > 0:
        range_list = len(defenders)
        for x in range(greater_list):
            attackers.append(0)
        print(len(attackers))
    else:
        range_list = len(attackers)
        for x in range(0,abs(greater_list)):
            defenders.append(0)
        print(len(defenders))
    
    for x in range(0,range_list):
        battle = defenders[x]-attackers[x]
        print(battle)
        if battle == 0:
            pass
        elif battle > 0:
            survivors += 1
        elif battle < 0:
            survivors -=1
        print(f'battle: {x}')
    
    print(survivors)
    
    if survivors > 0:
        return True
    elif survivors < 0:
        return False
    else:
        if survivors == 0 and sum(attackers) == sum(defenders):
            return True
        elif survivors == 0 and sum(attackers) > sum(defenders):
            return False
        elif survivors == 0 and sum(attackers) < sum(defenders):
            return True
    

print(is_defended([49, 30, 8, 17, 31, 32],[49, 15, 37, 16, 23, 7, 4, 45]))

test1 = [1,2,3,4,5,6]
print(max(2))