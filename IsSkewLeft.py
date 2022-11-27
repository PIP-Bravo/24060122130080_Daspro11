from tree import*

def isSkewLeft(P):
    if IsTreeEmpty(P):
        return False
    else:
        if IsUnerLeftPB(P) == True and not IsOneElmtPB(P):
            return isSkewLeft(Left(P))
        if IsOneElmtPB(P):
            return True
        else:
            return False

S = MakePb(1, MakePb(2, MakePb(4, MakePb(6, None, None), None) , None) , None)
P = MakePb(1, MakePb(2, MakePb(4, MakePb(6, MakePb(8, None, None), MakePb(9, None, None) ), None) , None) , None)
print(S)
print(P)
print(isSkewLeft(S))
print(isSkewLeft(P))