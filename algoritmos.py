def havel_hakimi(sucesion):
    if any(x >= len(sucesion) for x in sucesion):
        return False
    sucesion = sorted(sucesion, reverse=True)
    while not any(x < 0 for x in sucesion):
        if not any(sucesion):
            return True
        for i in range(sucesion.pop(0)):
            sucesion[i] -= 1
        sucesion.sort(reverse=True)
    else:
        return False
