from tree import*

def LevelOfX(P,X):
    if  not IsMemberTree(P,X):
        return 0
    else:
        if Akar(P)==X:
            return 0
        else :
            if IsBinerPB(P):
                return 1 + LevelOfX(Left(P),X) + LevelOfX(Right(P),X)
            elif IsUnerLeftPB(P):
                return 1 + LevelOfX(Left(P),X)
            elif IsUnerRightPB(P):
                return 1 + LevelOfX(Right(P),X)
            
P = MakePb(2,MakePb(3,MakePb(1,None,None),MakePb(5,None,None)),MakePb(3,MakePb(2,None,None),MakePb(4,None,None)))
print(P)
print(LevelOfX(P,5))