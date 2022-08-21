from lupa import LuaRuntime


def python_print(x: str):
    print(x)


runtime = LuaRuntime()
g = runtime.globals()
setattr(g, "pprint", python_print)

code = """
local x = "I wasn’t just playing around."
pprint("’")
pprint(string.byte(string.sub(string.sub(x,-23),1,1)))

local sub_working = string.sub(x, -21)
pprint(sub_working)


local subs_problem = string.sub(x, -23)
pprint(subs_problem)
"""

runtime.execute(code)
