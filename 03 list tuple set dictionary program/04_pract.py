s = set()

print(type(s))
print(s)

s.add(10)
s.add(10)
s.add(20)
s.add(30)
s.add(40)
s.add(50)
s.add(60)
print("\nset data:",s)

print("\nLength of string:",len(s))

s.remove(40)
print("\n40 remove from set:",s)

s.pop()
print("\npop data from set:",s)

s2 = {50,20,30,60,70,80,90,100}

differ = s2.difference(s)
print("\nDifferent element in set s2:",differ)

union_s_s2 = s.union(s2)
print("\nUnion of s and s2:",union_s_s2)

intersection_s_s2 = s.intersection(s2)
print("\nIntersecton of s and s2:",intersection_s_s2)

s.clear()
print(s)