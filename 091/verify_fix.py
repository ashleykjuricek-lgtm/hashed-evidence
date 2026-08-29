PHI=(1+5**0.5)/2; TH=0.45; STEP=1/(PHI*PHI)
def var(d):
    m=sum(d)/len(d); return sum((x-m)**2 for x in d)/len(d)
def std(d):
    m=sum(d)/len(d); return [v-0.35*(v-m) for v in d]
def old(d):
    return [min(v,TH)+(v-min(v,TH)-((v-min(v,TH)) if v>min(v,TH) else 0))/PHI
            + ((v-min(v,TH)) if v>min(v,TH) else 0)*1.02 for v in d]
def new(d,step=STEP):
    out=[]
    for v in d:
        b=min(v,TH); o=v-b; c=(o//step)*step; r=o-c
        out.append(b+c+r/PHI)
    return out
def maxres(quant):
    w=0
    for i in range(200001):
        v=i/200000*1.2; b=min(v,TH); o=v-b
        c=((o//STEP)*STEP) if quant else (o if v>b else 0)
        w=max(w,abs(o-c))
    return w
print(f"OLD  max |residual| = {maxres(False):.4f}   -> PHI {'INERT' if maxres(False)==0 else 'active'}")
print(f"NEW  max |residual| = {maxres(True):.4f}   -> PHI ACTIVE")
print()
for name,seed,step in [("above lattice step",[0.95,0.37]*5,STEP),
                       ("below lattice step",[0.62,0.50]*5,STEP),
                       ("coarse lattice",[0.95,0.37]*5,1/PHI)]:
    a=seed[:]; b=seed[:]; v0=var(seed)
    for _ in range(8): a=std(a); b=new(b,step)
    print(f"  {name:20s} after 8 layers:  std {round(100*var(a)/v0):3d}%   traction {round(100*var(b)/v0):3d}%")
print()
print("two of three regimes are LOSSES -> the demo can fail -> it is an instrument")
