"""Huffman code realization with heapq"""

import heapq
from collections import Counter, namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code


def huffman_decode(encoded, code):
    coded = ''
    encod_str = str(encoded)
    code_keys = list(code.keys())
    code_vals = list(code.values())
    i = 1
    while i < len(encod_str) + 1:
        ch = encod_str[:i]
        if ch in code_vals:
            position = code_vals.index(ch)
            coded += code_keys[position]
            encod_str = encod_str[i:]
            i = 1
        else:
            i += 1
    return coded


def main():
    s = input()
    code = huffman_encode(s)
    encoded = ''.join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print(f'{ch}: {code[ch]}')
    print(encoded)
    print(code)
    print()
    print(huffman_decode(encoded, code))


def test(n_iter=100):
    import random
    import string

    for i in range(n_iter):
        length = random.randint(0, 32)
        s = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        code = huffman_encode(s)
        encoded = ''.join(code[ch] for ch in s)
        assert huffman_decode(encoded, code) == s


if __name__ == '__main__':
    main()

