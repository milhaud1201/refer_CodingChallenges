def solution(n, lost, reserve):
    _lost = sorted(set(lost) - set(reserve))
    _reserve = sorted(set(reserve) - set(lost))
    
    for i in _reserve:
        if i - 1  in _lost:
            _lost.remove(i - 1)
        elif i + 1 in _lost:
            _lost.remove(i + 1)

    return n - len(_lost)
