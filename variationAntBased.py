from SIMULATIONS import *

N = 100
ListaStdY = np.zeros((N,1))
ListaStdP = np.zeros((N,1))
c1 = 1.5
c2 = 0.5
interaction = 'Ising'
numAgentes = int(np.sum(np.genfromtxt('America.csv', delimiter=',')) + 1)
topologia = 'AmericaC'
LambdaImitationRate = 0.6
BetaSelfConversion =0.15
EtaOutConversion = 0.6
Temp = 150

for i in range(0,N):
    sim = Simulation(interaction, numAgentes, topologia, c1, c2)
    sim.Grid.ImitationRate = LambdaImitationRate
    sim.Grid.SelfConversion = BetaSelfConversion
    sim.Grid.OutConversion = EtaOutConversion
    sim.Gamma = Temp
    sim.ConstantSigma1 = 0.5/100
    sim.ConstantSigma2 = 0.5/100
    sim.ConstantSigma3 = 0.5/100
    sim.MakeSimulation()
    sim.SomeStatisticalTests()
    ListaStdP[i]=sim.StdP
    ListaStdY[i]=sim.StdY

fig1 = plt.figure(1)
MakeAnHistogram(ListaStdY,'Standard deviation of the ouput gap',15)
fig2 = plt.figure(2)
MakeAnHistogram(ListaStdP,'Standard deviation of the inflation',15)

sim = Simulation(interaction, numAgentes, topologia, c1, c2)
sim.Grid.ImitationRate = LambdaImitationRate
sim.Grid.SelfConversion = BetaSelfConversion
sim.Grid.OutConversion = EtaOutConversion
sim.Gamma = Temp
sim.ConstantSigma1 = 0.5/100
sim.ConstantSigma2 = 0.5/100
sim.ConstantSigma3 = 0.5/100
sim.MakeSimulation()
sim.AllStatisticalTests()
sim.TimeSeriesGraph(3)
sim.FrequencyGraphOfTimeSeries(7, 20)