def exibe_candidatos(deque, pos, ordem):
    if ordem == 'direta':
        for i in range(deque.size()):
            if i < pos:
                deque.remove_front()
            else:
                print(deque.remove_front())
    elif ordem == 'inversa':
        ind = deque.size()
        
        for i in range(deque.size()):
            if ind > pos:
                deque.remove_rear()
            else:
                print(deque.remove_rear())
            ind -= 1