import numpy as np
import fenics as fe


# Create mesh and define function space
mesh = fe.UnitSquareMesh(16, 16)
V = fe.FunctionSpace(mesh, 'Lagrange', 1)

# Define boundary condition
ub = fe.Expression('x[0] + 2*x[1] + 1', degree=1)
bc = fe.DirichletBC(V, ub, lambda x, on_bndry: on_bndry)

# Define weak formulation of the PDE (holds for all v)
u = fe.Function(V)  # No fe.TrialFunction for non-linear F == 0 problems
v = fe.TestFunction(V)
f = fe.Expression('10*x[0] + 20*x[1] + 10', degree=1)
q = lambda u: 1 + u**2
F = - q(u) * fe.dot(fe.grad(u), fe.grad(v)) - f * v

# Compute solution
fe.solve(F * fe.dx == 0, u, bc)

# Save solution for ParaView and HTML
fe.File('non_linear.pvd') << u
xdom = open('non_linear.html', 'w')
xdom.write(fe.X3DOM.html(u))

# Interpolate analytical solution and compute error at vertices
ue = fe.interpolate(ub, V)
error = np.abs(ue.vector().get_local() - u.vector().get_local()).max()
print('max error = {:.3g}'.format(error))
