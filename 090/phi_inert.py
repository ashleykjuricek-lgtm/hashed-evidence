PHI=(1+5**0.5)/2
def pris(d):
    out=[]
    for v in d:
        baseline=min(v,0.45)
        carry=(v-baseline) if v>baseline else 0
        residual=(v-baseline-carry)/PHI
        out.append(baseline+residual+carry*1.02)
    return out
def std(d):
    m=sum(d)/len(d); return [v-0.35*(v-m) for v in d]
def integ(d):
    m=sum(d)/len(d); return max(0,min(100,round(sum((x-m)**2 for x in d)/len(d)*2000)))
worst=max(abs((v/100000.0*1.2 - min(v/100000.0*1.2,0.45)
    - ((v/100000.0*1.2-min(v/100000.0*1.2,0.45)) if v/100000.0*1.2>min(v/100000.0*1.2,0.45) else 0))/PHI)
    for v in range(200001))
print(f"max |residual| over 200,000 samples in [0,1.2] = {worst:.3e}   -> PHI is INERT")
seed=[0.85,0.37]*5; a=seed[:]; b=seed[:]
print("layer | std | traction | traction peak")
for L in range(9):
    print(f"  {L:2d}  | {integ(a):3d} |   {integ(b):3d}    |  {max(b):.4f}")
    a=std(a); b=pris(b)
