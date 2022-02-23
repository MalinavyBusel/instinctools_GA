def backpack(vol: int, price: int, v_p_pairs: list):
    '''Takes the max allowed volume, max allowed price and the list
    of [volume, price] pairs and returns the max possible price and the list of item ids to get this price'''

    # makes list of lists [item_id, volume, price]
    id_v_p = [[pair[0], *pair[1]] for pair in enumerate(v_p_pairs)]

    # all unique volumes sorted and converted to list again in order to use __getitem__
    all_vs = list(set([pair[1] for pair in id_v_p if pair[1] <= vol]))

    # making the matrix of lists [price, [item_ids]]
    dynamic_table = []
    for y in range(len(id_v_p)):
        dynamic_table.append([])
        for x in range(len(all_vs)):
            dynamic_table[y].append(backpack_filler(all_vs[x], id_v_p[:y + 1], x, y, dynamic_table, all_vs, price))

    # returning the best possible variant of filling the backpack
    return dynamic_table[-1][-1]


def backpack_filler(max_vol, items, x, y, dynamic_table, all_vs, price):
    '''returns (price, [ids])'''

    # remains checks if the volume of the newest item in the dyn_table less than the max_volume for this part of table
    remains = max_vol - items[-1][1]
    if remains >= 0:

        # now if y == 0 we add our item, given as an argument, because now there are now other items to compare with
        if y == 0:
            return [items[0][2], [items[0][0]]]

        else:
            # now we compare the upper price of dyn_table with the price of (new item + best price of a remained volume)
            old = dynamic_table[y - 1][x]
            new = [items[-1][2], [items[-1][0]]]
            added_to_free_space = [0, []]

            # here we calculate the remained volume and find its max_price
            for ind in range(len(all_vs)):
                if remains >= all_vs[ind]:
                    added_to_free_space = dynamic_table[y - 1][ind]
                else:
                    break
            new[0] += added_to_free_space[0]
            new[1] += added_to_free_space[1]

            # if any of the compared prices are more than the total allowed price, we won,t add it
            if old[0] > price and new[0] > price:
                return dynamic_table[y - 1][x]
            elif old[0] > price:
                return new
            elif new[0] > price:
                return old

            # else we compare the prices and choose the biggest
            else:
                return old if old[0] > new[0] else new

    else:
        return [0, []] if y == 0 else dynamic_table[y - 1][x]

if __name__ == '__main__':
    print(backpack(4, 5000, [[4, 3000], [3, 2000], [1, 1500]]))
