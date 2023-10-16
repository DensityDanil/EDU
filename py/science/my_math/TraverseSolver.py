#https://stackoverflow.com/questions/39359220/is-there-any-way-to-get-the-step-by-step-solution-in-sympy

import sympy as sp
import matplotlib.pyplot as plt
import networkx as nx
import graphviz
import pygraphviz

class TraverseSolver:

    
    def __init__(self, expr):
        self.expr = expr
        
    def _set_graph(self):
        self.G = nx.nx_agraph.from_agraph(pygraphviz.AGraph(sp.dotprint(self.expr))) #self.G = nx.nx_agraph.from_agraph(pygraphviz.AGraph(sp.dotprint(self.expr))) 
        
    def _set_map(self):
        self._map = dict(zip(self.G.nodes, sp.preorder_traversal(self.expr))) 
        
    def _set_baseNode(self):
        self._baseNode = next(iter(self.G.nodes))
        
    def get_levels(self, mode='draw'):
        if mode == 'draw':
            d = nx.single_source_shortest_path_length(self.G, self._baseNode)
            u, idx = np.unique(list(d.values()), return_index=True)
            levels = [[str(m) for m in n] for n in reversed(np.split(np.array(list(d.keys())), idx[1:]))]
            return levels
        elif mode == 'traverse':
            print(self.G)
    
    def set_color(self, node, color):
        self.G.nodes[node]['color'] = color

    def display_graph(self, fig, n, nshape=(2, 3)):      
        ax = fig.add_subplot(*nshape, n)
        pos = graphviz_layout(self.G, prog='dot')
        colors = nx.get_node_attributes(self.G, 'color')    
        nx.draw(self.G, pos = pos, nodelist=[])
        # draw self.G bbox by bbox:
        for i, n in enumerate(self.G.nodes()):
            nx.draw(nx.subgraph(self.G, [n]), pos={n:pos[n]}, labels = {n:f'${sp.latex(self._map[n])}$'}, nodelist=[],
                    bbox=dict(facecolor=colors[n], edgecolor='black', boxstyle='round,pad=0.7'))
            
    def solve(self, display_graph=True, nshape=(2, 3)):
        self._set_graph() #store sp.srepr+code in each node
        self._set_map() #sp.srepr+code -> expression (without evaluation)
        self._set_baseNode() #sp.srepr+code of self.
        solutionSteps = [self._map[self._baseNode]] #first step that contains initial expression
        levels = self.get_levels(mode='draw')
        if display_graph:
            fig = plt.figure(figsize=(20,10))
        #Step forward
        for i in range(len(levels)):
            if display_graph:
                for node in self.G.nodes(): 
                    self.set_color(node, 'lightblue')
            anyChanges = False
            for activeNode in levels[i]:
                beforeEval = self._map[activeNode]
                if display_graph:
                    self.set_color(activeNode, 'yellow')
                if not beforeEval.is_Atom:
                    afterEval = beforeEval.func(*beforeEval.args, evaluate=True) #is beforeEval different with afterEval
                    if beforeEval != afterEval:
                        self._map[activeNode] = afterEval
                        if display_graph:
                            self.set_color(activeNode, 'lime')
                        anyChanges = True
            # Calculate value of baseNode() using changes, no evaluation      
            if anyChanges:
                for j in range(i+1, len(levels)):
                    for editNode in levels[j]:
                        args = [self._map[node] for node in self.G[editNode]] #each ancestor
                        if not self._map[editNode].is_Atom:
                            self._map[editNode] = self._map[editNode].func(*args, evaluate=False)
                solutionSteps.append(self._map[self._baseNode])
            if display_graph:
                self.display_graph(fig, n=len(solutionSteps), nshape=nshape)
        plt.show()
        return solutionSteps

expr = sp.sympify('-1*(2*3-5*7)', evaluate=False)
steps = TraverseSolver(expr).solve(display_graph=True, nshape=(2, 3))

print('INPUT:', sp.srepr(expr))
print('SOLUTION 1:', ' = '. join([str(step) for step in steps]))
print('SOLUTION 2:', ' = '. join([sp.StrPrinter(dict(order='none'))._print(step) for step in steps])) 
