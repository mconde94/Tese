from SIMULATIONS import *

c1 = 1.5
c2 = 1.5
interaction = 'Ising'
numAgentes = int(np.sum(np.genfromtxt('America.csv', delimiter=',')) + 1)
topologia = 'AmericaC'
sim = Simulation(interaction, numAgentes, topologia, c1, c2)
sim.Grid.ImitationRate = 0.3
sim.Grid.SelfConversion = 0.1
sim.Grid.OutConversion = 5
sim.Gamma = 100
sim.ConstantSigma1 = 0.5/100
sim.ConstantSigma2 = 0.5/100
sim.ConstantSigma3 = 0.5/100
sim.MakeSimulation()
sim.AllStatisticalTests()
sim.TimeSeriesGraph(0)
sim.FrequencyGraphOfTimeSeries(4, 20)
