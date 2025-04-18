
s1= 'a-b-c-d'
print(s1.replace('-',','))
print(s1.replace('-',',',2))

s3= 'abc'
s4= 'xyz'
print(s4.join(s3))


s='python is very easy'
s.startswith('python')
print(s.startswith('python'))
print(s.startswith('is'))
print(s.startswith('is',7))
print(s.endswith('easy'))
print(s.endswith('is',0,9))
print(s.removeprefix('py'))
print(s.removesuffix('sy'))
print(s.partition('s'))