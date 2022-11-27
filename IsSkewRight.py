from tree import*

def isSkewRight(P):
    if IsTreeEmpty(P):
        return False
    else:
        if IsUnerRightPB(P) == True and not IsOneElmtPB(P):
            return isSkewRight(Right(P))
        if IsOneElmtPB(P):
            return True
        else:
            return False

S = MakePb(2, None, MakePb(3, None, MakePb(4, None, MakePb(5, None, None))))
P = MakePb(2, None, MakePb(3, None, MakePb(4, None, MakePb(5, MakePb(4, None, None), MakePb(6, None, None)))))
print(S)
print(P)
print(isSkewRight(S))
print(isSkewRight(P))