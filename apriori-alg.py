def count(lists, items):
    c = 0
    for l in lists:
        if set(items).issubset(l):
            c += 1
    return c

def create_new_set(Li, i):
    Ci = []
    for l in Li:
        for m in Li:
            new = l + m
            new = list(dict.fromkeys(new))
            if (len(new) == i + 1):
                already_in = False
                for o in Ci:
                    if (set(new).issubset(o)):
                        already_in = True
                if not already_in:
                    Ci.append(new)
    return Ci

def create_association_rules(Lis):
    rules = []
    for l in Lis:
        for item in l:
            others = l.copy()
            others.remove(item)
            rules.append(item + "-" + ''.join(others))
            rules.append(''.join(others) + "-" + item)
    rules = list(dict.fromkeys(rules))
    return rules

def calc():
    min_supp = float(input("minimum support = "))
    min_conf = float(input("minimum confidence = "))
    n = int(input("Number of sets = "))
    sets = []
    Ci = []
    for i in range(0, n):
        input_string = input("Enter values for new set: ")
        new_value_list = list(input_string)
        sets.append(new_value_list)
        for x in new_value_list:
            if not [x] in Ci:
                Ci.append([x])
    L = []
    support_values = {}
    i = 0
    while len(Ci) > 0:
        Li = []
        print("C", i, ": ")
        for items in Ci:
            supp = count(sets, items) / n
            print("sup(", items, ") =", supp)
            items_duplicate = items + items
            for j in range(0, len(items)):
                combi = items_duplicate[j: (len(items) + j)]
                support_values[''.join(combi)] = supp
                support_values[''.join(combi[::-1])] = supp
            if supp >= min_supp:
                Li.append(items)
        print("L", i, ": ", Li)
        if i > 0:
            L = L + Li
        i += 1
        Ci = create_new_set(Li, i)
    association_rules = create_association_rules(L)
    for rule in association_rules:
        x = rule.split("-")[0]
        y = rule.split("-")[1]
        xy = x+y
        suppX = support_values[x]
        suppXY = support_values[xy]
        conf = suppXY / suppX
        statement = ""
        if conf > min_conf:
            statement = ">= minConf -> wer "+ x + " kauft, kauft " + y
        print("conf(", x, "->", y, ") =", conf, statement )

    
calc()
