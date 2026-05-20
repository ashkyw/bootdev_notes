# Welcome to Memory Management

Understanding how your _software_ runs on _hardware_ is important for writing fast, performant code. In this course we'll be talking all about one of the main aspects of software performance: **memory management**.

## C Program Structure

In python you do something like this:

```py
python slow_program.py
```

The Python interperter then executes the file top-to-bottom. If you have a `print()` at the top level, then it will print something.

The entire file is _interpreted line by line, but that's not how C works_.

### The simplest C Program:

The simplest C program is essentially:

```C
int main(){
  return 0;
}
```
