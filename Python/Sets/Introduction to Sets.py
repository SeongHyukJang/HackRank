def average(array):
    # your code goes here
    total = 0
    PlantsHeight = set(array)
    for i in PlantsHeight:
        total += i
    return total / len(PlantsHeight)

