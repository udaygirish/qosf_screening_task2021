# QOSF Quantum Mentorship Program
---
### Submitted Task : Task 4




#### Overall Description of the Problem
Write a code for solving Max-Cut problem using the resources given on Unweighted Graph and then further optimize and generalize so that it can for any different input and also works with Weighted problem where in case the optimization is done by using weights of edges.

#### Code Structure

The code description is as follows:

    1. circuit_create.py
        -> This module contains the basic function to compute cost and to create the circuit and some generalizations 
    
    2. network_cp.py 
        -> This module contains the networkx implementation to create a networkx graph and visualise the Edges and nodes.

    3. main.py
       -> This script is responsible for the initialization, function calls and the optimization of the cost function.


Output folder contains output images showing weighted and non weighted graphs difference and also the images of the graphs itself.

For installing dependencies please use

        pip3/pip install -r requirements.txt

For running different networks modifications can be made in network.json

     Network.json Structure

    1.  "Note" - Just a general description
    2.  "Edges" - For declaring the network edges
    3.  "Weights" - Give the edge weights in the same order as edges are declared
    4.  "num" - no of nodes
    5.  "depth" - Depth of the network equal to length of weights or edges
    6.  "rep" - Number of repetitions 
    7.  "output_path" : to declare output images path
    8.  "max_iter" : number of iteration to run optimization for

### Credits
Most of the code taken and understood some concepts from these blogs:
         
         https://lucaman99.github.io/new_blog/2020/mar16.html
         https://qxf2.com/blog/drawing-weighted-graphs-with-networkx/

         Wiki articles on Max-cut problem.
