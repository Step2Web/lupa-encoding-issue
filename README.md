# Reproducing encoding issue with lup

## How to run code:

```
poetry install
source .venv/bin/activate
python lupa_test_encoding/main.py
```

## Script
The output of the script is:

```
’
153
 just playing around.
Traceback (most recent call last):
  File "/Users/stephan.weinwurm/src/lupa_test_encoding/lupa_test_encoding/main.py", line 25, in <module>
    runtime.execute(code)
  File "lupa/_lupa.pyx", line 308, in lupa._lupa.LuaRuntime.execute
  File "lupa/_lupa.pyx", line 1324, in lupa._lupa.run_lua
  File "lupa/_lupa.pyx", line 1333, in lupa._lupa.call_lua
  File "lupa/_lupa.pyx", line 1358, in lupa._lupa.execute_lua_call
  File "lupa/_lupa.pyx", line 281, in lupa._lupa.LuaRuntime.reraise_on_exception
  File "lupa/_lupa.pyx", line 1496, in lupa._lupa.py_call_with_gil
  File "lupa/_lupa.pyx", line 1459, in lupa._lupa.call_python
  File "lupa/_lupa.pyx", line 1144, in lupa._lupa.py_from_lua
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x99 in position 0: invalid start byte
```

* printing the problematic character directly is not a problem
* the problematic starting characters byte code is `153`
* Using `string.sub` to pass a string starting with `’` to a python function fails

