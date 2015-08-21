#all those who believe in psychokinesis raise my hand
#llthswhblvnpsychknssrsmyhnd
#aoeoeieeioieiaiea


words = raw_input("write some words -> ")
#words = "all those who believe in psychokinesis raise my hand"
vowels = 'aeoiu'

print "".join(x for x in words.replace(" ","") if x not in vowels)
print "".join(x for x in words if x in vowels)