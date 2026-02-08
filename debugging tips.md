# A 5‑step debugging playbook

  When something breaks

  1. **State the bug precisely**
   * “When I do X, I expected Y, but I got Z.”
   * Example: “Calling `run_python_file("./calculator", "tests.py")` returns ‘does not exist’.”

  2. **Narrow the suspect area**
   * Which one or two functions are closest to the bad behavior?
   * Don’t scan the whole project; zoom into where input becomes wrong output.

  3. Make a minimal reproduction
   * Write the smallest snippet that reproduces the bug.
   * Example: in a REPL or small script:
  
  ```py
  run_python_file("./calculator", "tests.py")
  ```
  This strips away the LLM, CLI, arguments, etc.

  4. Instrument the code
   * Add temporary prints / logs to confirm what’s actually happening:
```py
print("DEBUG:", working_directory, file_path, target_path)
print("DEBUG exists?", os.path.isfile(target_path))
```
   * Or use a debugger to step line by line and inspect variables.

  5. Verify the fix with variations
   * After a fix, try:
       A normal case
       A boundary case
       A clearly invalid case
  Example:
       
```py
run_python_file("./calculator", "tests.py")
run_python_file("./calculator", "main.py")
run_python_file("./calculator", "not_real.py")
```

  This gently pushes your solution toward being general, not just “barely passes the test.”
