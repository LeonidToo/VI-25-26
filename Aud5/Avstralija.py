from constraint import *

problem=Problem()

problem.addVariables(["WA","NT","SA","QU","NSW","VI","T"],["red","green","blue"])
problem.addConstraint(lambda a, b: b != a, ["WA", "NT"])
problem.addConstraint(lambda a, b: b != a, ["WA", "SA"])
problem.addConstraint(lambda a, b: b != a, ["SA", "NT"])
problem.addConstraint(lambda a, b: b != a, ["QU", "NT"])
problem.addConstraint(lambda a, b: b != a, ["SA", "QU"])
problem.addConstraint(lambda a, b: b != a, ["SA", "NSW"])
problem.addConstraint(lambda a, b: b != a, ["SA", "VI"])
problem.addConstraint(lambda a, b: b != a, ["NSW", "QU"])

print(problem.getSolution())



