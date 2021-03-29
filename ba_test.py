from beam_analysis.Beam import Beam
# define beam parameters
E = 207 * 10**9
I = 2 * 10**-8
L = 1.0

# make the beam and add loads
B = Beam(L, E, I)
B.addPointLoad(0, 11)
B.addPointLoad(1, -10)
B.addAppliedMoment(0, 11*1.0)
B.addDistributedLoad(0, 1, -1.0)

# boundary conditions are required for angle and deflection analysis
B.addBoundaryCondition(0.0, "angle", 0.0)
B.addBoundaryCondition(0.0, "deflection", 0.0)

# run the analysis
B.analyze()
