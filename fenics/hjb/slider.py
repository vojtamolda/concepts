import fenics as fe
from utils import abs


# Create mesh and define function space
mesh = fe.RectangleMesh(fe.Point(-5.0, -5.0), fe.Point(+5.0, +5.0), 64, 64)
W = fe.FunctionSpace(mesh, 'DG', 1)

# Define weak formulation of the PDE (holds for all v)
V = fe.Function(W)
V.rename('V', 'label')
v = fe.TestFunction(W)
f = fe.Expression(['u', 'x[0]'], degree=1, u=1.0)
L = fe.Expression('- 0.5 * (x[0]*x[0] + x[1]*x[1] + u*u)', degree=1, u=1.0)

# Define Neumann boundary condition
gradVn = fe.Expression('0.0', degree=1)

# Variable for value function at the previous time-step
Vt = fe.interpolate(fe.Constant(0.0), W)
Vt.rename('V', 'label')

# HJB PDE to be integrated backward in time
dt = 0.05
F = ((Vt - V) / dt - abs(V.dx(0)) + V.dx(1) * f[1] + L) * v * fe.dx - gradVn * v * fe.ds

# Solution storage for ParaView
time = 1.0
file = fe.File('slider.pvd')
file << (Vt, time)

# Solution time-stepping
while time >= 0.0:
    # Solve linear system and step backward in time
    fe.solve(F == 0, V)
    time -= dt

    # Save solution for ParaView
    file << (V, time)

    # Assign current solution to the previous time-step one
    Vt.assign(V)

xdom = open('slider.html', 'w')
xdom.write(fe.X3DOM.html(V))
