from lupa import LuaRuntime


def python_print(x: str):
    print(x)


runtime = LuaRuntime()
g = runtime.globals()
setattr(g, "pprint", python_print)

code = """
local x = "I wasn’t being serious lol. I thought you got that and were also playing into it."
pprint("’")
pprint(string.byte(string.sub(string.sub(x,-75),1,1)))
local subs = string.sub(x, -75)
pprint(subs)
"""

runtime.execute(code)
