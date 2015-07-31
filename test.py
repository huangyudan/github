#iter and generator
#the first try
#=================================
i = iter('abcd')
print i.next()
print i.next()
print i.next()

s = {'one':1,'two':2,'three':3}
print s
m = iter(s)
print m.next()
print m.next()
print m.next()