
Bash and ZSH are shells. Also powerful programming languages.
Shells are primarily for running other programs and small scripts.

Terminal: The program that accepts text-based input and renders text on screen
Shell or REPL (Read, Evaluate, Print, Loop): The program behind the scenes of a terminal that runs commands
R - Read typed commands
E - Evaluate the commands, usually by running other programs
P - Print output of commands
L - Loop prompt for next command

Functions:
  echo "Text" = return text
  whoami = user name
  expr # + # = Addition
  history = returns history of commands input into the shell
    history + # = returns # history of commands input
  clear = Clears terminal text

Variable creation:
  variable=<value> (no spaces)

Syntax:
  $ at the start of a line denotes shell prompt and should not be typed
  $ needs to be in front of a variable for calls
    $ echo $name would print
  String interpolation is built in.
    name="World"
    $ echo Hello $name
    Hello World

  Example:
  From the terminal window:
    bankname="WorldBanc"
    founded="1969"
    ceo="Jeff Gates"
    echo $bankname was founded in $founded by $ceo
      WorldBanc was foudned in 1969 by Jeff Gates

  Shortcuts:
    UP or DOWN arrows - Cycle through recent commands
    ctrl+L - Clear terminal text

File structures:
Paths:
  Relative path: takes current directory into account
    fords/mustang.txt
      - Easier to read and write, easier to reason
      - Good so long as you're in the correct directory
  Absolute path: starts at the root of the file system
    /vehicles/cars/ford/mustang.txt
      - More verbose
      - Useful when unsure of directory

  Directory Commands:
  - pwd = print current working directory
  - ls = list items in current directory
  - ls <value> = list items in target directory
  - cd <value> = change directory
  - cd .. = go back a directory
      .. means parent directory
  File commands:
  - cat <file> = concatenate bytes to view files in terminal
  - head -# (# defaults to 10)= print first # of lines of a file
  - tail -# (# defaults to 10)= print last # lines of a file
  - less / more - read files, use less most often
      - less: enter scrolls lines q exits
      - less -N: enumerates lines spacebar scrolls to next page, b goes back
  - touch: updates the access and modification timestamps of a file
           if a file does not exist one will be created, can make multiple at once
  - mkdir <value>: make directory
  - mv <old value> <new value>: move file or directory to new location: rename                                     file or folder
  - rm <value>: delete file or folder
  - rm -r <value>: deletes a directory and all of its contents using recursion
  - cp <value> <location>: copy file or directory
  - cp -R <value> <location>: copy a directory and all contents using recursion
  - ~ home directory alias cd ~ takes you to /users/name
  - grep: search for something in a file, similar to ctrl+f
        grep "hello" words.txt
      Can grep multiple files
        grep "hello" hello.txt hello2.txt
  - grep -r "hello" <location>: search entire directory including all subs and                                     files in directory.
  - Use grep -r "value" . for current directory. "." means current directory
  - find <directory> -name <value>: search a directory for a file name
    - can search by pattern: find <directory> -name "*.txt" * is wildcard
    - find <directory> -name "*chad*" would look for all filenames containing chad

Permissions:
  
