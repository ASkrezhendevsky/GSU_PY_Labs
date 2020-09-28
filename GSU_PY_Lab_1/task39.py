inputList = ['sad', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl' ]
element = 'ruby'
print(len(inputList) - (inputList[::-1]).index(element) - 1)


