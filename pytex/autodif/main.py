from variable import Variable


x = Variable([[2, 1]], require_grad=True)
y = Variable([[1], [2]], require_grad=True)
u = x @ y
v = u
v.backward()
q = x.grad
v.zero_grad()
f = q @ q.t()
print(f, q)
f.backward()
print(y.grad)


