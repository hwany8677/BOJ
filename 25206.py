grade={"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0, "P": 0}
sigma=0
sigma_hakjum=0
for _ in range(20):
    s=input().split()
    hakjum=int(float(s[1])) #10/10 variable naming
    sigma+=hakjum*grade[s[2]]
    sigma_hakjum+=hakjum if s[2]!='P' else 0
gpa=sigma/sigma_hakjum
print("{:.6f}".format(gpa))