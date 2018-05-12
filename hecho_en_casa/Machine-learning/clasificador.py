from Perceptron import Perceptron

samples = [
    [1, 4],
    [5, 7],
    [1, 3],
    [6, 9],
    [1, 2],
    [2, 1],
    [8, 4],
    [9, 4],
    [6, 8],
    [2, 4],
    [13, 29],
    [14, 9],
    [4, 2],
]

exito = [-1, 1,-1,1,-1,-1,1,1,1,-1,1,1,-1]

network = Perceptron( sample=samples, exit=exito, learn_rate=0.01, epoch_number=1000, bias=-1 )

network.trannig()

while True:
    sample = []
    for i in range( 2 ):
        sample.insert( i, float( input( 'valor: ' ) ) )
    network.sort(sample)