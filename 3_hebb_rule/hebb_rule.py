class hebb:
    def __init__(self):
        pass

    def learn(self, inputs,  targets):
        w = [0,0,0]
        #inputs[0]#inputs[0:4]#[x[0] for x in inputs]
        #print(len(inputs))
        for i in range(0, len(inputs)):
            for j in range(0, len(inputs[i]) -1):
                w[j] = w[j] + inputs[i][j] * targets[i]
            w[2] = w[2] + targets[i]
            print(w)
        return w

if __name__ == '__main__':
    h = hebb
    inputs = [[1,1,1], [1,-1,1], [-1,1,1], [-1,-1,1]]
    targets = [1,-1,-1,-1]

    print("Weigths: ", h.learn(0,inputs,targets))
