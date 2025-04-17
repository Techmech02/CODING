import textwrap as tw
t="""Welcome! Are you completely new to programming? If not then we presume you will be looking for 
information about why and how to get started with Python. Fortunately an experienced programmer in 
any programming language (whatever it may be) can pick up Python very quickly. It s also easy for 
beginners to use and learn, so jump in!"""
x=tw.wrap(t,50)
print(x)
for i in range(len(x)):
    print(x[i])