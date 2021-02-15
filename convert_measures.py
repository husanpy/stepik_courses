"""very simple. Useful here is '{.2e}'.format(x)"""

def convert_to_m(string):
    x, prev, _, res = string.split()
    x = float(x)
    ratios = {'mile': 1609, 'yard': 0.9144, 'foot': 0.3048, 'inch': 0.0254, 'km': 1000, 'm': 1, 'cm': 0.01, 'mm': 0.001}
    result = ratios[prev] * x / ratios[res]
    return '{:.2e}'.format(result)


def main():
    print(convert_to_m('1 mile in mile'))


if __name__ == '__main__':
    main()
