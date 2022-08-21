from lupa import LuaRuntime
import traceback


def python_print(x: str):
    print(x)


runtime = LuaRuntime()
g = runtime.globals()
setattr(g, "pprint", python_print)

code = """
local x = "I wasn’t just playing around."
"""

ex1 = """
pprint("Ex 1: Printing the character directly works")
pprint("’")
"""

ex2 = """
pprint("Ex 2: Handling and printing a string with the probelmatic character works")
pprint(string.sub(x,1,10))
"""

ex3 = """
pprint("Ex 3: Handling a string and printing a substring without the problematic character works")
local s1 = string.sub(x , -22)
pprint(s1)
"""

ex4 = """
pprint("Ex 4: Handling a string and printing a substring with the problematic character as first character fails")
local s2 = string.sub(x , -23)
pprint(s2)
"""

ex5 = """
pprint("Ex 5: Handling a string and printing a substring with the problematic character not as first character fails")
local s3 = string.sub(x , -24)
pprint(s3)
"""

samples = [ex1, ex2, ex3, ex4, ex5]

for s in samples:
    try:
        print("\n")
        runtime.execute(code + s)
    except Exception as e:
        traceback.print_exc()
        print(e)
