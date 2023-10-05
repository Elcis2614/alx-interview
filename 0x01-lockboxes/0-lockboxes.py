def canUnlockAll(boxes):
    gates = [0 for box in boxes]
    gates[0] = 1

    def openLock(addresses):
        if (addresses == []):
            return
        for address in addresses:
            if address >= len(gates):
                return
            elif gates[address] != 1:
                gates[address] = 1
                openLock(boxes[address])
                continue
            else:
                continue
    openLock(boxes[0])
    return (0 not in gates)
