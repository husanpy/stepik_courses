def create_list_of_items(num):
    """returns list of tuples with item_general_cost and item_volume
       sorted with key item_general_cost / item_volume, i.e. unit cost"""
    l = [tuple(map(int, input().split())) for _ in range(num)]
    l.sort(key=lambda x: x[0] / x[1], reverse=True)
    return l


def create_list_of_costs(L):
    """given list of tuples with item's two characters: general cost and volume
       returns list of unit costs"""
    u = [L[i][0] / L[i][1] for i in range(len(L))]
    u.sort(reverse=True)
    return u


def max_possible_bag(num, bag_power):
    """Solution for Knap Sack problem"""
    if num <= 0 or bag_power <= 0:
        return '0.000'
    item_list = create_list_of_items(num)
    cost_list = create_list_of_costs(item_list)
    bag_list = []
    for i in range(len(item_list)):
        if item_list[i][1] <= bag_power:
            bag_list.append(item_list[i][0])
            bag_power -= item_list[i][1]
        else:
            bag_list.append(cost_list[i] * bag_power)
            bag_power -= bag_power
            break
    result = sum(bag_list)
    return f'{result:.3f}'


def main():
    num_item, w_bag = map(int, input().split())
    print(max_possible_bag(num_item, w_bag))


if __name__ == '__main__':
    main()
