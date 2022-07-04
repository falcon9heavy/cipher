"""
Substitution matrix utility development

"""
import string

nums = list(range(1,28))
print(nums)
alpha = list(string.ascii_lowercase)
print(alpha)

m={}
for i,j in zip(nums,alpha):
    m[i]=j
print (m)


#for i, j in zip(nums, string.ascii_lowercase):
#    sub_matrix[i] = j
#sub_matrix[' '] = ' '  # there was no element in key for spaces
#return ''.join(sub_matrix[i] for i in message)