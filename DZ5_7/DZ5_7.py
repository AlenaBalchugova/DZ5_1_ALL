import json
with open('firms.txt','r') as text1:
    summ = 0
    plas = 0
    fa = []
    for line in text1:
        firm = {}
        income = 0
        end = line.replace('\n', ' ')
        ls= end.split(' ')
        income = int(ls[2]) - int(ls[3])
        if income > 0:
            plas += 1
            summ +=income
        firm[ls[0]] = income
        print(firm)
        fa.append(firm)
    ai = summ /plas
    fa.append({'average_profit': ai })
    print(fa)
    print('')

    with open('new.json','w') as fn:

        json.dump(fa, fn)
        wanna_look_at = json.dumps(fa)
        print(wanna_look_at)