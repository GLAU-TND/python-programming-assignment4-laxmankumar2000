# This problem was asked by Twitter.
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

ls=eval(input("enter a list"))
a=aval(iput("enter the query string"))
n=[]
for i in ls:
    if i.startswith(a)==True:
      n.append(i)
print(n)