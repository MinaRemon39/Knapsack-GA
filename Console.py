from knapsack_genetic import genetic_algorithm

cases = int(input("Number of cases: "))

for case in range(cases):
    weights=[]
    benfits=[]
    number_of_items = int(input("Number of items: "))
    knapsack_size = int(input("Max weight: "))
    for i in range(number_of_items):
        item = input("Enter weight,benfit: ").split()
        weights.append(int(item[0]))
        benfits.append(int(item[1]))

    chromo,total_benfit = genetic_algorithm(benfits,weights,knapsack_size)
    print("Case ID: ",case+1)
    print("Totsl benfit: ",total_benfit)
    counts = chromo.count(1)
    print(counts)
    for i in range(len(chromo)):
        if(chromo[i]==1):
            print(weights[i],benfits[i])
