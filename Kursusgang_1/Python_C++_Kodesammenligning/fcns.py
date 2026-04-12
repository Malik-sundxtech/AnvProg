def foo():
    print("Hello from foo\n")


print("1")
lol = foo  # does not run, we need to write foo() to run foo function
print("2")
foo()


lol()
