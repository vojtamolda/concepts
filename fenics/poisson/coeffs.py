import numpy as np
import fenics as fe


# Create mesh and define function space
mesh = fe.UnitSquareMesh(16, 16)
V = fe.FunctionSpace(mesh, 'Lagrange', 1)

# Define boundary condition
ub = fe.Expression('1 + x[0]*x[0] + 2*x[1]*x[1]', degree=1)
bc = fe.DirichletBC(V, ub, lambda x, on_bndry: on_bndry)

# Define weak formulation of the PDE (holds for all v)
u = fe.TrialFunction(V)
v = fe.TestFunction(V)
f = fe.Expression('8*x[0] + 10*x[1]', degree=1)
c = fe.Expression('x[0] + x[1]', degree=1)
a = - c * fe.dot(fe.grad(u), fe.grad(v)) * fe.dx
L = f * v * fe.dx

# Compute solution
u = fe.Function(V)
fe.solve(a == L, u, bc)

# Save solution for ParaView and HTML
fe.File('coeffs.pvd') << u
xdom = open('coeffs.html', 'w')
xdom.write(fe.X3DOM.html(u))

# Interpolate analytical solution and compute error at vertices
ue = fe.interpolate(ub, V)
error = np.abs(ue.vector().get_local() - u.vector().get_local()).max()
print('max error = {:.3g}'.format(error))
