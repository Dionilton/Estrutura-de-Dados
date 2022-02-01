def exibe_candidatos(deque, pos, ordem):
    deque = Deque()
    if ordem == 'direta':
        while pos < deque.size():
            print(deque.items[pos])
            pos += 1
    else:
        while pos >= 0:
            print(deque.items[pos])
            pos -= 1