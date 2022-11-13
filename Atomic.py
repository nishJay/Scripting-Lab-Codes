"""Write Python code to do the following operations:

• Create a dictionary that contains the atomic element symbol and its name.

• Add a unique & duplicate element into this dictionary by interacting with the user.

Observe the output and justify it.

• Display the number of atomic elements in this dictionary

• Ask user to enter an element to search in the dictionary. Display appropriate results.

Rewrite this program so that these operations are inside a function called ‘AtomicDictionary’.

Create another python file called “Atomic.py” and execute this function in it """

def AtomicDictionary() :

    element = {"Na": "Sodium", "AL": "Aluminium"}

    print(element)

    unikey = input("Enter the symbol for a unique element pair\n")

    unisub = input("Enter the element name for {}\n".format(unikey))

    element.update({unikey: unisub})

    unikey = input("Enter the symbol for a duplicate element\n ")

    unisub = input("Enter the element name for {}\n".format(unikey))

    element.update({unikey: unisub})

    print("The number of elements in the dictionary are {}".format(len(element)))

    se = input("Enter the element to search in the dictionary\n")

    if se in element.values():

        print("Element found")

    else:

        print("Element not found")

