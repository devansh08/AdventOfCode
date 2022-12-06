signal = open("input").readline()

i = 0
while i < len(signal) - 4:
    chunk = signal[i : i + 4]
    freq = {c: chunk.count(c) for c in chunk}

    if len(freq.keys()) == 4:
        print(i + 4)
        break
    else:
        i += chunk.index([c for c in freq.keys() if freq[c] != 1][0]) + 1
