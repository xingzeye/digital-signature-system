from Crypto.Util.number import *

m = bytes_to_long(b'xxxxxxxxxxzzzzzzzzzyyyyyyyyyy1234321llllloooookkkkkiiii')
p = getPrime(1000)
q = getPrime(1000)
n = p*q
e = getPrime(80)
c = pow(m,e,n)
print("p=",p)
print("q=",q)
print("e=",e)
print("c=",c)
phi = (p-1)*(q-1)
d = pow(e,-1,phi)
m1 = pow(c,d,n)
print("d=",d)
print("m1=",long_to_bytes(m1))

#p= 777721936730107027028074326469
#q= 848546432764847580797074605043
#e= 1081446926311501917443761
#c= 567742319729771343570693911903003147090963256752363503168290
#n = p*q

#print(long_to_bytes(m))