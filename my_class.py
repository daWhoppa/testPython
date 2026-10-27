v1 = 'Harry Potter|J.K. Rowling|400'
v2 = 'Dune|Frank Herbert|'

split_v1 = v1.split('|')
split_v2 = v2.split('|')

print(split_v1)  # Output: ['Harry Potter', 'J.K. Rowling', '400']
print(split_v2)  # Output: ['Dune', 'Frank Herbert', '']

print(split_v2[0])  # Output: 'Dune'
print(split_v2[1])  # Output: 'Frank Herbert'
print(split_v2[2] == 'hgf')  # Output: ''