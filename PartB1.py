"""Write a python class to reverse a sentence (initialized via constructor) word
by word. Example: “I am here” should be reversed as “here am I”. Create instances of this
class for each of the three strings input by the user and display the reversed string for each, in
descending order of number of vowels in the string"""


class ulta:
    line =""
    def __init__(self, line):
        self.line = " ".join(reversed(line))


ob = []

print("Enter 3 strings")

st = ["", "", ""]
co = [0, 0, 0]
dict = {}
for i in range(3):
    ob.append(ulta(input()))
    st[i]=ob[i].line
    for j in st[i]:
        if j.lower() in ['a', 'e', 'i', 'o', 'u']:
            co[i] += 1

    dict.update({st[i]: co[i]})
print(st)
print(dict)
print(sorted(dict.items(),key=lambda x:x[1],reverse=True))
