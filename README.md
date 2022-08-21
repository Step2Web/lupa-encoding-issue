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
Ex 1: Printing the character directly works
’


Ex 2: Handling and printing a string with the probelmatic character works
I wasn’t


Ex 3: Handling a string and printing a substring without the problematic character works
t just playing around.


Ex 4: Handling a string and printing a substring with the problematic character as first character fails
Traceback (most recent call last):
  File "/Users/stephan.weinwurm/src/lupa_test_encoding/lupa_test_encoding/main.py", line 50, in <module>
    runtime.execute(code + s)
  File "lupa/_lupa.pyx", line 308, in lupa._lupa.LuaRuntime.execute
  File "lupa/_lupa.pyx", line 1324, in lupa._lupa.run_lua
  File "lupa/_lupa.pyx", line 1333, in lupa._lupa.call_lua
  File "lupa/_lupa.pyx", line 1358, in lupa._lupa.execute_lua_call
  File "lupa/_lupa.pyx", line 281, in lupa._lupa.LuaRuntime.reraise_on_exception
  File "lupa/_lupa.pyx", line 1496, in lupa._lupa.py_call_with_gil
  File "lupa/_lupa.pyx", line 1459, in lupa._lupa.call_python
  File "lupa/_lupa.pyx", line 1144, in lupa._lupa.py_from_lua
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x99 in position 0: invalid start byte
'utf-8' codec can't decode byte 0x99 in position 0: invalid start byte


Ex 5: Handling a string and printing a substring with the problematic character not as first character fails
Traceback (most recent call last):
  File "/Users/stephan.weinwurm/src/lupa_test_encoding/lupa_test_encoding/main.py", line 50, in <module>
    runtime.execute(code + s)
  File "lupa/_lupa.pyx", line 308, in lupa._lupa.LuaRuntime.execute
  File "lupa/_lupa.pyx", line 1324, in lupa._lupa.run_lua
  File "lupa/_lupa.pyx", line 1333, in lupa._lupa.call_lua
  File "lupa/_lupa.pyx", line 1358, in lupa._lupa.execute_lua_call
  File "lupa/_lupa.pyx", line 281, in lupa._lupa.LuaRuntime.reraise_on_exception
  File "lupa/_lupa.pyx", line 1496, in lupa._lupa.py_call_with_gil
  File "lupa/_lupa.pyx", line 1459, in lupa._lupa.call_python
  File "lupa/_lupa.pyx", line 1144, in lupa._lupa.py_from_lua
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
```

