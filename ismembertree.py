from tree import*

def IsMemberTree(P,X):
    if IsTreeEmpty(P):
        return False
    else:
        if Akar(P)==X:
            return True
        else:
            return IsMemberTree(Left(P),X) or IsMemberTree(Right(P), X)

S= MakePb(2, None, MakePb(3, None, MakePb(4, None, MakePb(5, None, None))))
P= MakePb(1, MakePb(2, MakePb(4, MakePb(6, None, None), None) , None) , None)
print(S)
print(P)
print(IsMemberTree(S,5))
print(IsMemberTree(P,7))