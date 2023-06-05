s = set()
s.add(1)
s.add(2)
print(s)

# clear -> removes all elements from the set
s.clear()
print(s)

# copy -> returns a copy of the set. Note it is a copy, so changes to the original don't effect the copy.
s = {1, 2, 3}
sc = s.copy()
print(sc)
s.add(4)
print(sc)

# difference -> returns the difference of two or more sets.
print(s.difference(sc))

# difference_update -> returns set1 after removing elements found in set2
s1 = {1, 2, 3}
s2 = {1, 4, 5}
s1.difference_update(s2)
print(s1)

# discard -> Removes an element from a set if it is a member. If the element is not a member, do nothing.
print(s)
s.discard(2)
print(s)

# intersection and intersection_update
# Returns the intersection of two or more sets as a new set.(i.e. elements that are common to all of the sets.)
s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1.intersection(s2))
print(s1)

print(s1.intersection_update(s2))
print(s1)

# isdisjoint
# This method will return True if two sets have a null intersection.
s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

# issubset -> This method reports whether another set contains this set.
print(s1)
print(s2)
print(s1.issubset(s2))

# issuperset -> This method will report whether this set contains another set.
print(s2.issuperset(s1))
print(s1.issuperset(s2))

# symmetric_difference and symmetric_update
# Return the symmetric difference of two sets as a new set.(i.e. all elements that are in exactly one of the sets.)
print(s1.symmetric_difference(s2))

# union -> Returns the union of two sets (i.e. all elements that are in either set.)
print(s1.union(s2))

# update -> Update a set with the union of itself and others.
s1.update(s2)
print(s1)