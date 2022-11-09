"""Write a python class to reverse a sentence (initialized via constructor) word
by word. Example: “I am here” should be reversed as “here am I”. Create instances of this
class for each of the three strings input by the user and display the reversed string for each, in
descending order of number of vowels in the string"""


class ulta:
    def __init__(self):
        self.line = ""

    def rev(self):
        li = self.line.split()
        return " ".join(reversed(li))


ob = [ulta(), ulta(), ulta()]

print("Enter 3 strings")

st = ["", "", ""]
co = [0, 0, 0]
dict = {}
for i in range(3):
    ob[i].line = input()
    st[i] = ob[i].rev()
    for j in st[i]:
        if j.lower() in ['a', 'e', 'i', 'o', 'u']:
            co[i] += 1

    dict.update({st[i]: co[i]})
print(st)
print(dict)
print(sorted(dict,key=lambda x:x[1]))
