signal = open("input").readline()

i = 0
while i < len(signal) - 14:
    chunk = signal[i : i + 14]
    freq = {c: chunk.count(c) for c in chunk}

    if len(freq.keys()) == 14:
        print(i + 14)
        break
    else:
        i += chunk.index([c for c in freq.keys() if freq[c] != 1][0]) + 1
