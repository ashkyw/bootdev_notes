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

Local Variable creation:
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
  - ls -l = shows permissions
  - ls -a = show hidden files
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
  - rm -rf <value>: f stands for force. If ran with sudo can do serious damage
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
  - grep -r "value" <location> --exclude-dir="value"
      Sets the exclude-dir flag to the value and ignores that directory
    
Permissions:
Represented as a ten-character string:
  drwxrwxrwx
  Break down: 
    First character is always a "d" or "-". 
      "d" = directory, "-" = file
    Next three characters are Owner permissions 
       r = read 
       w = write 
       x = execute
       - = none
      rwx = read, write and execute
      r-x = read, execute
      r-- = read only
  Second set of three characters are Group permissions
  Third set is everyone else

  Commands:
    - chmod: change mode (permissions) of a file or directory
        chmod -R: recursively change all files in directory
        chmod -R u=rwx: change owner permissions to rwx
        chmod -R u=rwx,g=: change group permissions to none
        chmod -R u=rwx,g=,o=: change others permissions to none
        chmod -R u-rwx,g=,o= DIRECTORY: what directory to change permissions of
    - chmod -x <file>: removes executable flag for owner
    - chmod u+x <file>: adds executable flag for owner
    - chown: change owner requires root
    
.sh file extension calls shell scripts. These are text files that contain shell commands. To call them use:
  mydir/program.sh
  If calling in current directory use:
  ./program.sh
Prefix folders are required so the shell knows we are trying to run a program, not an embedded command

Programs:
  Commands:
  - which <value>: tells you location of an installed command line program
  - #!: shebang. Used at the top of a script to tell your shell what program to use to execute the file.
    #!/usr/bin/python3

Programs are just sets of instructions that a computer can execute. An executable is just a file that contains a program.
Two types of programs:
  Compiled programs (Go, C, Rust): Program converted from human-readable code into machine code. To run a compiled program you would simply ./texteditor
  Interpreted Programs (Python, Ruby, Javascript): A program executed by another program that interprets the   human readable code at runtime to machine code for JIT execution. To run an interperted program you need to call which interpreter to use. So you would python texteditor.py

Shells:
  - sh: Bourne shell. Original Unix shell. Very basic, missing QoL features
  - bash: Bourne Again shell. Most popular on Linux, builds off sh, QoL features
  - zsh: Z shell. Most popular on macOS. Builds off sh. QoL features

All variations can run .sh scripts

Bash and Zsh have config files that run every time you start a new shell session. Located in home directory and hidden by default

Environmental Variables:
  Available to all programs ran in the shell
  - env: view environmental variables currently set
  - export NAME="value": sets a variable in the shell
    Once an environmetal variable is set, other scripts can access and use it

PATH:
  A variable containing the list of directories that the shell will look into when running a command.
  Without this variable we would have to directly tell the shell where we want to look, from the intial home directory, every time. i.e. use /bin/ls instead of just ls

When installing a new program via CLI a message will printed with the install path for the program you installed. PAY ATTENTION TO THIS. If you try to run a program and it doesn't run, it's location may not be set within PATH. This line will tell us where it's located so we can find the damn thing.
To add locations to path use the following:
export PATH="$PATH:/<value>/<value>/<etc.>" this will append the directory to your PATH. Note: $PATH calls whatever is already in the PATH variable. Then we append our new directory to the variable by using the :/<value>/<etc>
Make sure to use pwd to get the whole path of the directory, then use that to add to PATH. This will only change your PATH for the current shell session.
To make this permanent, add the export command to your shell config file. .bashrc / .zshrc

I/O:
Commands:
  - man: displays manual for programs with them
      man ls

Flags:
  - the arguements passed to a command using -
      ls -l
  - can be combined with multiple flags
      ls -al
  - single character flags are typically one -
  - multi character flags are typically two --

  curl: CLI tool that lets you make network requests from CLI
  $?: returns exit code of last program ran
    ls ~
    echo $?
    # 0

Standard Output (stdout):
  Stream of data that prints to your terminal
  i.e. print() in python, echo "" for sh

Standard Error (stderr):
  Datastream like standard output, but intended to be used for error messages.      Can be redirected.

Redirecting Streams:
  >: redirects stdout
    echo "Hello world" > hello.txt
  2>: redirects stderr
    cat doesnotexist.txt 2> error.txt

Standard Input (stdin):
  Default place where programs read their input. Simply a stream of data that programs can read from as they run.
    i.e. input() in python, read VARIABLE (must be in caps) in sh

/tmp:
  Directory that exists by default on Unix-like systems in root directory. Files here are deleted by the system routinely. Great to store temp files.

Piping:
  Act of taking output from one program as input for another program. This allows for powerful automation.
  Use | to pipe. Following example takes stdout from one program and pipes it to the stdin for another
    echo "Have you heard the tragedy of Darth Plagueis the Wise?" | wc -w

Interrupt:
  If programs freeze or take too long to execute, use ctrl + c to send a 'SIGINT' signal to the program and tells it to stop

Kill:
  If a program doesn't respond to SIGINT open another shell session and use kill.
  - kill <pid>: pid stands for process id
  - ps aux: shows all processes running including their process ids
      process id will be the first number
    ashkyw 2389  0.0  0.0   6936  3308 pts/1    S+   20:02   0:00 bash private/       bin/malicious.sh force

Unix Philosophy:
  1. Write programs that do one thing and do it well
  2. Write programs to work together
  3. Write programs to handle text streams because that is a universal interface

  1. ls, grep, less exist because they do one thing and do it well. No fluff.
  2. Since specialized programs exist, it's easy to write programs that work together. grep can search for text in a file then pipe it into less to display the results
    - grep "hello" some_file.txt | less
  3. Programs work together easily when they all use the same interface: text streams. 

Top:
  Allows you to see which programs are using the most resources on a computer.
  top: displays resource management
  
Package Managers:
  Software tool designed to help install other software. Their primary functions include downloading software from official sources, installing, updating, remove software, and managing relevant dependencies.
  
