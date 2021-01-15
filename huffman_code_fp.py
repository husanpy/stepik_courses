def huffman_code(strng):
    freq = {x: strng.count(x) for x in set(strng)}
    codes = dict.fromkeys(strng, "")
    if len(set(strng)) > 1:
        for _ in range(len(freq) - 1):
            l, r = sorted(freq.items(), key=lambda x: x[1])[:2]
            rs, rv, ls, lv = *r, *l
            del freq[rs], freq[ls]
            freq.update({rs + ls: rv + lv})
            for code in codes:
                if code in ls: codes[code] += "0"
                if code in rs: codes[code] += "1"
    else:
        codes[strng[0]] = "0"
    codes = {letter: code[::-1] for letter, code in codes.items()}
    return codes


def main():
    s = input()
    code_dic = huffman_code(s)
    line = "".join([code_dic[x] for x in s])
    print(len(code_dic), len(line))
    print(*[f"{l}: {c}" for l, c in code_dic.items()], sep="\n")
    print(line)
    

if __name__ == '__main__':
    main()
