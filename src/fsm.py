import graphviz

#Parameter check
def param_check(*ty2):  
    def common(fun):
        def deal(*fun_x):
            ty=map(to_check_fun,ty2)
            if ty:
                x_list=[a for a in fun_x]
                x_list_it=iter(x_list)
                result=[]
                for t_check in ty:
                    r=t_check(x_list_it.__next__())
                    result.append(r)
                print('param check result: ',result)
                    
            return fun(*fun_x)
        
        return deal                
    return common

def to_check_fun(t):
    return lambda x:isinstance(x,t)


class StateMachine:
    def __init__(self): 
        self.handlers = {}        # State transfer function dictionary
        self.start_state = None    # Initial state
        self.state=[]
        self.state_action={}       # Explain what this state is doing
        self.clk=0                # clock
        self.light_state_history = []   # State light logic history at each clock
        self.transition_history = []  #Each state transfer record

    #Set the starting state
    @param_check(object,str)
    def set_start(self, state):
        self.start_state = state

    #Add status
    @param_check(object,str,str)
    def add_state(self, name, action):
        self.state_action[name]=action
        self.state.append(name)

    #Set state transition function
    @param_check(object,str,object)
    def add_transition(self,state,function):
        self.handlers[state] = function  #Set state transition for each state
        return function

    @param_check(object,int)
    def run(self, clk_n):
        handler = self.handlers[self.start_state]
        current_state=self.start_state
        all_clk=clk_n
        self.light_state_history.append((self.clk,self.state_action[self.start_state]))
        # Start processing from the Start state
        while clk_n>0:
            self.light_state_history.append((all_clk-clk_n+1,self.state_action[current_state])) #Log the logic of traffic lights
            (clk_new, next_state) = handler(self.clk)     # Transform to a new state after a state transition function
            self.clk=clk_new
            self.transition_history.append((all_clk-clk_n+1,current_state,next_state)) #Log the logic of fsm transition
            handler = self.handlers[next_state]
            current_state=next_state
            clk_n-=1

    @param_check(object)
    def visualize(self,clk1,clk2):
        time=[clk1,clk2,clk1,clk2]
        res = []
        res.append("digraph G {")
        res.append("  rankdir=LR;")
        for v in self.state:
            res.append("  {}[];".format(v))
        for index,v in enumerate(self.state):
            for index2,q in enumerate(self.state):
                if(v==q):
                    res.append('  {} -> {}[label="clk<{}; clk++"];'.format(v, q, time[index]))
                if index2-index==1:
                    res.append('  {} -> {}[label="clk>={}; clk=0"];'.format(v, q, time[index]))
        length=len(self.state)
        res.append('  {} -> {}[label="clk>={}; clk=0"];'.format(self.state[length-1], self.state[0], clk2))
        
        res.append("}")

        return "\n".join(res)

if __name__ == "__main__":
    clk1 = 3
    clk2 = 1
    m = StateMachine()
    m.add_state("s0","Junction A green,Junction B red")
    m.add_state("s1","Junction A yellow,Junction B red")
    m.add_state("s2","Junction A red,Junction B green")
    m.add_state("s3","Junction A red,Junction B yellow")
    m.set_start("s0")
    m.add_transition("s0",lambda clk: (clk+1,"s0") if clk<clk1 else (0,"s1"))
    m.add_transition("s1",lambda clk: (clk+1,"s1") if clk<clk2 else (0,"s2"))
    m.add_transition("s2",lambda clk: (clk+1,"s2") if clk<clk1 else (0,"s3"))
    m.add_transition("s3",lambda clk: (clk+1,"s3") if clk<clk2 else (0,"s0"))

    m.run(18)
    print(m.light_state_history)
    print(m.transition_history)

    dot=m.visualize(clk1,clk2)
    f= open('fsm.dot','w') 
    f.write(dot)
    f.close()

    with open("fsm.dot") as f:
        dot_graph = f.read()
    dot=graphviz.Source(dot_graph)
    dot.view()
