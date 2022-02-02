def exibe_candidatos(deque, pos, ordem):
    if pos < deque.size() and pos >= 0:
        if ordem == 'direta':
            for i in range(deque.size()):
                if i < pos:
                    deque.remove_front()
                else:
                    print(deque.remove_front())
        elif ordem == 'inversa':
            ind = deque.size()
            
            for i in range(deque.size()):
                if ind > pos + 1:
                    deque.remove_rear()
                else:
                    print(deque.remove_rear())
                ind -= 1