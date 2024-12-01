with open("input.txt", "r") as f:
    # part 1
    list1 = []
    list2 = []
    for line in f.readlines():
        segements = line.split(" ")
        list1.append(int(segements[0]))
        list2.append(int(segements[-1]))
    list1.sort()
    list2.sort()

    total_distance = 0
    for i in zip(list1, list2):
        total_distance += abs(i[0] - i[1])
    
    print(total_distance)

    # part 2
    counted_list2 = {}
    for i in list2:
        if i in counted_list2.keys():
            counted_list2[i] += 1
        else:
            counted_list2[i] = 1
    
    similarity_score = 0
    for n in list1:
        if n in counted_list2.keys():
            similarity_score += n * counted_list2[n]

    print(similarity_score)
