from collections import Counter
def can_patch(bridge,planks):
    hole_lengths = [j - i for i in range(len(bridge))
                if bridge[i] == 0 and (i == 0 or bridge[i-1] == 1)
                for j in range(i+1, len(bridge)+1)
                if (j == len(bridge) or bridge[j] == 1) and all(bridge[k] == 0 for k in range(i, j)) and (j - i) > 1]

    plank_counter = Counter(planks)
    return all(plank_counter[hole] > 0 and not plank_counter.subtract([hole]) for hole in hole_lengths)

print(can_patch([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 2]))
