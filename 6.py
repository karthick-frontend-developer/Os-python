P=5
R=3
Def calculateNeed(need,maxm,allot):
    For I in range(P):
        For j in range®:
            Need[i][j]=maxm[i][j]-allot[i][j]
Def isSafe(processes,avail,maxm,allot):
    Need=[]
    For I in range(P):
        L=[]
        For j in range®:
            l.append(0)
        need.append(l)
    calculateNeed(need,maxm,allot)
    finish=[0]*P
    safeSeq=[0]*P
    work=[0]*R
    for I in range®:
        work[i]=avail[i]
    count=0
    while(count<P):
        found=False
        for p in range(P):
            if(finish[p]==0):
                for j in range®:
                    if (need[p][j]>work[j]):
                        break
                if(j==R-1):
                    for k in range®:
                        work[k]+=allot[p][k]
                    safeSeq[count]=P
                    count+=1
                    finish[p]=1
                    found=True
            if(found==False):
                print(“System is not in safe state”)
                return False
        print(“System is in Safe state”,”\nSafe sequence is:”,end=””)
        print(*safeSeq)
        return True
if __name__==”__main__”:
    processes=[0,1,2,3,4]
    avail=[3,3,2]
    maxm=[[0,1,0],[2,0,0],[3,0,2],[2,2,2],[4,3,3]]
    allot=[[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
    isSafe(processes,avail,maxm,allot)
