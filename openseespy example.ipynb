#!/usr/bin/env python
# coding: utf-8

# ![Screenshot_1.png](attachment:Screenshot_1.png)

# In[1]:


pip install openseespy


# In[2]:


import openseespy.opensees as op

# =============================================================================
# Units
# =============================================================================

m = 1
N = 1
Pa = 1




# =============================================================================
# Input Variables
# =============================================================================

x1 = 0.
y1 = 0.

x2 = 6*m
y2 = 0.

x3 = 3*m
y3 = 4*m


A1 = 0.0004*m**2


E = 200*10**9*Pa


Py = -10000*N



# =============================================================================
# OpenSees Analysis
# =============================================================================


# remove existing model
op.wipe()

# set modelbuilder
op.model('basic', '-ndm', 2, '-ndf', 3)

# define materials
op.uniaxialMaterial("Elastic", 1, E)

# create nodes
op.node(1, x1, y1)
op.node(2, x2, y2)
op.node(3, x3, y3)



# set boundary condition
op.fix(1, 1, 1, 1)
op.fix(2, 1, 1, 1)
op.fix(3, 0, 0, 1)


# define elements
# op.element('Truss', eleTag, *eleNodes, A, matTag[, '-rho', rho][, '-cMass', cFlag][, '-doRayleigh', rFlag])
op.element("Truss", 1, 1, 3, A1, 1)
op.element("Truss", 2, 2, 3, A1, 1)



# create TimeSeries
op.timeSeries("Linear", 1)

# create a plain load pattern
op.pattern("Plain", 1, 1)

# Create the nodal load - command: load nodeID xForce yForce
op.load(3, 0, Py, 0.)


# Record Results
op.recorder('Node', '-file', "NodeDisp.out", '-time', '-node', 3, '-dof', 1,2,'disp')
op.recorder('Node', '-file', "Reaction.out", '-time', '-node', 1,2, '-dof', 1,2,'reaction')
op.recorder('Element', '-file', "Elements.out",'-time','-ele', 1,2, 'forces')


# create SOE
op.system("BandSPD")
# create DOF number
op.numberer("RCM")
# create constraint handler
op.constraints("Plain")

# create integrator
op.integrator("LoadControl", 1.0)

# create algorithm
op.algorithm("Newton")

# create analysis object
op.analysis("Static")

# perform the analysis
op.initialize() 


ok = op.analyze(1)


op.wipe()


# In[ ]:




