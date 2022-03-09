import pathlib
import csv

from collections import defaultdict


def valuator(currencies: str, data: str, matchings: str):
    curr_path = pathlib.Path(currencies)
    data_path = pathlib.Path(data)
    match_path = pathlib.Path(matchings)
    curr_dict = {}
    data_dict = {}
    match_dict = {}
    aver_and_ign = {}
    with curr_path.open('r') as c, match_path.open('r') as m:
        curr_reader = csv.reader(c)

        line_count = 0
        for curr, ratio in curr_reader:
            if not line_count:
                line_count += 1
                continue
            curr_dict[curr] = float(ratio)
            line_count += 1

        match_reader = csv.reader(m, delimiter=',')

        line_count = 0
        for match_id, total_count in match_reader:
            if not line_count:
                line_count += 1
                continue
            # defaultdict is used for cases, when two products can have
            # the same price as a key
            data_dict[match_id] = defaultdict(list)
            match_dict[match_id] = total_count
            # aver_and_ign is used to calculate aver price
            # and ignored_count(len(aver_and_count[match_id]) - match_dict[match_id])
            aver_and_ign[match_id] = []
            line_count += 1

    with data_path.open('r') as d:
        data_reader = csv.reader(d)

        line_count = 0
        for id_, price, currency, quantity, match_id in data_reader:
            if not line_count:
                line_count += 1
                continue
            total_price = int(price)*curr_dict[currency]*int(quantity)
            data_list = [match_id, total_price, currency]
            data_dict[match_id][total_price].append(data_list)
            aver_and_ign[match_id].append(total_price)
            line_count += 1

    total_data = []
    for match_id in data_dict.keys():
        list_of_pr = sorted([t_price for t_price in data_dict[match_id].keys()], reverse=True)

        end_ind = int(match_dict[match_id])

        key = data_dict[match_id]
        list_of_data = [key[inf] for inf in list_of_pr[:end_ind]]

        ign_count = len(aver_and_ign[match_id]) - int(match_dict[match_id])
        aver_pr = sum(aver_and_ign[match_id])/len(aver_and_ign[match_id])

        for elems in list_of_data:
            for elem in elems:
                elem1 = [elem[0], elem[1], aver_pr, elem[2], ign_count]
                total_data.append(elem1)

    with open('output.csv', 'w', newline='') as o:
        writer = csv.writer(o)
        for line in total_data:
            writer.writerow(line)
    return None


valuator('currencies.csv', 'data.csv', 'matchings.csv')
