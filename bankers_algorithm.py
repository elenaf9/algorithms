def bankers_algorithm():
    G = []
    B = []
    p_count = int(input("Anzahl Prozesse: "))
    for i in range(p_count):
        s = input("G: ")
        G.append(tuple(list(map(int, s.split()))))
    print("")
    for i in range(p_count):
        s = input("B: ")
        B.append(tuple(list(map(int, s.split()))))
    print("")
    s = input("v: ")
    print("")
    v = tuple(list(map(int, s.split())))
    n = len(v) # Anzahl der Ressourcen
    f = []
    for i in range(n):
        f.append(v[i])
    R = []
    # berechne die freien Ressourcen f
    # berechne die übrigen Ressourcen R die noch benötigt werden für jeden Prozess
    for i in range(p_count): # für jeden Prozess
        r = []
        for j in range (n): # für jede Ressource
            r.append(G[i][j] - B[i][j])
            f[j] = f[j] - B[i][j]
        R.append(tuple(r))
    print("G: gesamten Ressourcen die von dem Prozess benötigt werden, B die aktuell genutzen, R die übrigen die er jetzt noch braucht (G-B) und f die freie Ressourcen\n")
    print("Beginn mit R=", R, "und f=", tuple(f), "\n")
    while(R.count(0) < p_count):
        success = False
        for i in range(p_count):
            if not success and not R[i] == 0:
                all_satisfied = True
                for j in range(n):
                    if (R[i][j] > f[j]):
                        all_satisfied = False
                if all_satisfied:
                    success = True
                    print("P", i+1, ": G=", G[i], "B=", B[i], "R=", R[i], "terminiert da atm f=", tuple(f))
                    R[i] = 0
                    for j in range(n):
                        f[j] = f[j] + B[i][j]
        if not success:
            print("Could not terminate any more Prozesses. R=", R, "f=", tuple(f))
            break
    print("\nFinished, free Ressources:", tuple(f))

bankers_algorithm()
    



