
from skfuzzy import control as ctrl 
import numpy as np
import skfuzzy as fuzz


var_x= ctrl.Antecedent(np.arange(6,19,1), "X")
var_y= ctrl.Antecedent(np.arange(3,12,1), "Y")

var_z= ctrl.Consequent(np.arange(-0.1,0.11,0.01), "z")

var_x['Dx']=fuzz.trimf(var_x.universe,[6,6,12])
var_x['Nx']=fuzz.trimf(var_x.universe,[6,12,18])
var_x['Yx']=fuzz.trimf(var_x.universe,[12,18,18])

var_x.view()

var_y['Dy']=fuzz.trimf(var_y.universe,[3,3,7])
var_y['Ny']=fuzz.trimf(var_y.universe,[3,7,11])
var_y['Yy']=fuzz.trimf(var_y.universe,[7,11,11])

var_y.view()


var_z['AZ1']=fuzz.trimf(var_z.universe,[-0.1,-0.05,0.0])
var_z['AZ2']=fuzz.trimf(var_z.universe,[-0.1,-0.1,-0.05])
var_z['DY']=fuzz.trimf(var_z.universe,[-0.05,0.0,0.05])
var_z['AR1']=fuzz.trimf(var_z.universe,[0.0,0.05,0.1])
var_z['AR2']=fuzz.trimf(var_z.universe,[0.05,0.1,0.1])


var_z.view()


rule1=ctrl.Rule(var_x['Yx'] & var_y['Dy'],var_z['AR1'])
rule2=ctrl.Rule(var_x['Yx'] & var_y['Ny'],var_z['AR1'])
rule3=ctrl.Rule(var_x['Yx'] & var_y['Yy'],var_z['AR2'])
rule4=ctrl.Rule(var_x['Nx'] & var_y['Dy'],var_z['AZ1'])
rule5=ctrl.Rule(var_x['Nx'] & var_y['Ny'],var_z['DY'])
rule6=ctrl.Rule(var_x['Nx'] & var_y['Yy'],var_z['AR1'])
rule7=ctrl.Rule(var_x['Dx'] & var_y['Dy'],var_z['AZ2'])
rule8=ctrl.Rule(var_x['Dx'] & var_y['Ny'],var_z['AZ1'])
rule9=ctrl.Rule(var_x['Dx'] & var_y['Yy'],var_z['AZ1'])


rule_control= ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9])
sim=ctrl.ControlSystemSimulation(rule_control)

sim.input['X']=15
sim.input['Y']=10

sim.compute()
sonuc=sim.output['z']
print("",sonuc)
var_z.view(sim=sim)
