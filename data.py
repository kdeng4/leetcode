def decode(message_file):
    with open(message_file) as f:
        lines = f.read().splitlines()

    words = [''] * len(lines)
    for line in lines:
        num, text, *_ = line.split(' ')
        words[int(num) - 1] = text

    ans = ''
    next_idx = 0
    rolling_gap = 2

    while next_idx < len(words):
        ans += words[next_idx] + ' '
        next_idx += rolling_gap
        rolling_gap += 1
    ans = ans[:-1]
    return ans


out = decode('sample/coding_qual_input.txt')
print(out)