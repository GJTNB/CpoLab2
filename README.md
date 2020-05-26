## Basic model of computational 
&emsp;&emsp;**list of group members：** Longfei Jiang、 Juntao Gao<br>
&emsp;&emsp;**laboratory work number：** 2<br>
&emsp;&emsp;**variant description：** eDSL for finite state machine (Moore).
### Objectives ###
&emsp;&emsp;&emsp;&emsp;Design an embedded domain-specific language or a simple text parser.<br>
&emsp;&emsp;&emsp;&emsp;Design architecture of a simple interpreter.<br>
&emsp;&emsp;&emsp;&emsp;Develop a simple interpreter for a specific model of computation.<br>
&emsp;&emsp;&emsp;&emsp;Develop unit tests.<br>
&emsp;&emsp;&emsp;&emsp;Develop input data control in the aspect-oriented style.<br>


### Discription ###
&emsp;&emsp;&emsp;&emsp;fsm.py  <br>
&emsp;&emsp;&emsp;&emsp;Suppose the traffic lights at the intersection have red, yellow and green lights in direction a and direction B respectively.There are four states  <br>
&emsp;&emsp;&emsp;&emsp;'S0': direction A's light is green and  direction B's light is red <br>
&emsp;&emsp;&emsp;&emsp;'S1': direction A's light is yellow and  direction B's light is red <br>
&emsp;&emsp;&emsp;&emsp;'S2': direction A's light is red and  direction B's light is green <br>
&emsp;&emsp;&emsp;&emsp;'S3': direction A's light is red and  direction B's light is yellow <br>
&emsp;&emsp;&emsp;&emsp;The state will change as the clk increases. <br>
&emsp;&emsp;&emsp;&emsp;The lights' duration can be defined by users.<br>

&emsp;&emsp;&emsp;&emsp;testfsm.py  <br>
&emsp;&emsp;&emsp;&emsp;In testfsm.py we test the methods of class StateMachine <br>

&emsp;&emsp;&emsp;&emsp;fsm.dot, Source.gv,Source.gv.pdf <br>
&emsp;&emsp;&emsp;&emsp;These three files include the digraph <br>
