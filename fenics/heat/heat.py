import numpy as np
import fenics as fe


# Create mesh and define function space
mesh = fe.UnitSquareMesh(16, 16)
V = fe.FunctionSpace(mesh, 'Lagrange', 1)

# Define boundary condition
Tb = fe.Expression('1 + x[0]*x[0] + 2*x[1]*x[1] + t', degree=1, t=0)
bc = fe.DirichletBC(V, Tb, lambda x, on_bndry: on_bndry)

# Set temperature at the previous time-step to initial value
Tb.t = 0
Tt = fe.interpolate(Tb, V)

# Define weak formulation of the PDE (holds for all v)
T = fe.TrialFunction(V)
v = fe.TestFunction(V)
f = fe.Constant(-5)

dt = 0.1
F = - (T - Tt) / dt * v - fe.dot(fe.grad(T), fe.grad(v)) + f * v
a, L = fe.lhs(F * fe.dx), fe.rhs(F * fe.dx)

# Solution time-stepping
T = fe.Function(V)
file = fe.File('heat.pvd')

while Tb.t <= 1.0:
    # Save solution for ParaView and HTML
    file << Tt
    xdom = open('heat1.html', 'w')
    xdom.write(fe.X3DOM.html(Tt))

    # Solve linear system
    Tb.t += dt
    fe.solve(a == L, T, bc)

    # Interpolate analytical solution and compute error at vertices
    Te = fe.interpolate(Tb, V)
    error = np.abs(Te.vector().get_local() - T.vector().get_local()).max()
    print('time = {:.2f}: error = {:.3g}'.format(Tb.t, error))

    # Assign current solution to previous temperature and plot
    Tt.assign(T)
