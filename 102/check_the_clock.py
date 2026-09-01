# COTT's own rules, enumerated on the four-position cycle. 0 = one quarter turn.
name={0:"1",1:"0",2:"-1",3:"w"}
mul=lambda a,b:(a+b)%4
neg=lambda a:(a+2)%4
ONE,ZERO,MINUS1,W=0,1,2,3
def power(x,n):
    r=ONE
    for _ in range(n): r=mul(r,x)
    return r
for t,v in [("0*w = 1 (axiom)",mul(ZERO,W)==ONE),("0^2 = -1",power(ZERO,2)==MINUS1),
            ("0^3 = -0",power(ZERO,3)==neg(ZERO)),("0^4 = 1",power(ZERO,4)==ONE),
            ("-(-0) = 0",neg(neg(ZERO))==ZERO),("-(-w) = w",neg(neg(W))==W),
            ("(-0)*(-0) = -1 [line 103]",mul(neg(ZERO),neg(ZERO))==MINUS1)]:
    print(f"{t:<30s} {'PASS' if v else 'FAIL'}")
print(f"\n-0 = {name[neg(ZERO)]}   -w = {name[neg(W)]}   -> carrier CLOSED")
print("\nline 105 says 0^n != (-0)^n for ALL n:")
for n in range(1,9):
    a,b=power(ZERO,n),power(neg(ZERO),n)
    print(f"  n={n}: {name[a]:<3s} vs {name[b]:<3s} {'differ' if a!=b else 'EQUAL -> line 105 FALSE'}")
print(f"\nOPEN RULE #1: 0^3={name[power(ZERO,3)]}  (-0)^3={name[power(neg(ZERO),3)]}  "
      f"-(0^3)={name[neg(power(ZERO,3))]}  =>  (-0)^3 = -0^3 : {power(neg(ZERO),3)==neg(power(ZERO,3))}")
