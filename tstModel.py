from model.model import Model

mymodel = Model()
mymodel.BuildGraph(2015,'France')
numVertici = mymodel.getNumNodes()
print(f"Numero vertici: {numVertici}")
nodes = mymodel.getNodes()
for n in nodes:
    print(n)
