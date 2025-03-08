"""
Práctica 1: Diseño de controladores

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Angel Eduardo Juarez Salazar
Número de control: 22210417
Correo institucional: L22210417@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Instalar librerias en consola
#!pip install control
#!pip install slycot

# Librerías para cálculo numérico y generación de gráficas
import numpy as np
import math as m
import matplotlib.pyplot as plt
import control as ctrl

# Datos de la simulación
x0,t0,tend,dt,w,h = 0,0,10,1E-3,6,3
N = round((tend-t0)/dt)+1
t = np.linspace(t0,tend,N)
u1 = np.ones(N) #Escalon unitario
u2 = np.zeros(N);u2[round(1/dt):round(2/dt)] = 1 #Impulso
u3 = (np.linspace(0,tend,N))/tend #Rampa con pendiente 1/10
u4 = np.sin(m.pi/2*t) #Funcion sinusoidal, pi/2 =250 mHz

u = np.stack((u1,u2,u3,u4),axis = 1)
signal = ["Escalon", "Impulso","Rampa","Sin"]

# Componentes del circuito RLC y función de transferencia
R=10E3

L=2.2E-3

C=10E-6
num = [C*L*R,C*R**2+L,R]
den = [3*C*L*R,5*C*R**2+L,2*R]
sys = ctrl.tf(num,den)
print(sys)

# Componentes del controlador
Cr=10E-6
kI=595
kP=750
Re= 1/(kI*Cr); print('Re=',Re)
Rr= (kP*Re) ; print ('Rr=',Rr)
numPID=[Rr*Cr,0]
denPID=[Re*Cr,0]
PID = ctrl.tf(numPID,denPID)
print(PID)

# Sistema de control en lazo cerrado
X= ctrl.series(PID,sys)
sysPID= ctrl.feedback(X,1,sign = -1)
print(sysPID)



# Respuesta del sistema en lazo abierto y en lazo cerrado

fig1 = plt.figure();

plt.plot(t,u1,"-",color = [92/255,179/255,56/255], label = "Ve(t)")
ts,PA = ctrl.forced_response(sys,t,u1,x0)
plt.plot(t,PA,"-",color = [251/255,65/255,65/255], label = "Vs(t)")
_,VPID = ctrl.forced_response(sysPID,t,u1,x0)
plt.plot(t,VPID,":",linewidth=3, color = [251/255,65/255,65/255], label = "VPID(t)")
plt.xlim(-0.25,10);plt.xticks(np.arange(0,11,1.0))
plt.ylim(0,1.2); plt.yticks(np.arange(0,1.2,0.1))
plt.xlabel("t[s]",fontsize=11)
plt.ylabel("V_i(t)",fontsize=11)
plt.legend(bbox_to_anchor=(0.5,-0.3),loc="center",ncol=3,fontsize=8,frameon=False)
plt.show()



fig2 = plt.figure();
plt.plot(t,u2,"-",color = [0/255,107/255,255/255], label = "Ve(t)")
ts,PA = ctrl.forced_response(sys,t,u2,x0)
plt.plot(t,PA,"-",color = [0/255,107/255,255/255], label = "Vs(t)")
_,VPID = ctrl.forced_response(sysPID,t,u2,x0)
plt.plot(t,VPID,":",linewidth=3, color = [251/255,65/255,65/255], label = "VPID(t)")
plt.xlim(-0.25,10);plt.xticks(np.arange(0,11,1.0))
plt.ylim(0,1.2); plt.yticks(np.arange(0,1.2,0.1))
plt.xlabel("t[s]",fontsize=11)
plt.ylabel("V_i(t)",fontsize=11)
plt.legend(bbox_to_anchor=(0.5,-0.3),loc="center",ncol=3,fontsize=8,frameon=False)

plt.show()


fig3 = plt.figure();

plt.plot(t,u3,"-",color = [59/255,30/255,84/255], label = "Ve(t)")
ts,PA = ctrl.forced_response(sys,t,u3,x0)

plt.plot(t,PA,"-",color = [0.3,0.5,0.2], label = "Vs(t)")

_,VPID = ctrl.forced_response(sysPID,t,u3,x0)

plt.plot(t,VPID,":",linewidth=3, color = [251/255,65/255,65/255], label = "VPID(t)")
plt.xlim(-0.25,10);plt.xticks(np.arange(0,11,1.0))
plt.ylim(0,1.2); plt.yticks(np.arange(0,1.2,0.1))
plt.xlabel("t[s]",fontsize=11)
plt.ylabel("V_i(t)",fontsize=11)
plt.legend(bbox_to_anchor=(0.5,-0.3),loc="center",ncol=3,fontsize=8,frameon=False)

plt.show()

fig4 = plt.figure();

plt.plot(t,u4,"-",color = [251/255,65/255,65/255], label = "Va(t)")
ts,PA = ctrl.forced_response(sys,t,u4,x0)

plt.plot(t,PA,"-",color = [0.3,0.5,0.2], label = "Vs(t)")
_,VPID = ctrl.forced_response(sysPID,t,u4,x0)

plt.plot(t,VPID,":",linewidth=3, color = [251/255,65/255,65/255], label = "VPID(t)")
plt.xlim(-0.25,10);plt.xticks(np.arange(0,11,1.0))
plt.ylim(-1,1.2); plt.yticks(np.arange(-1.1,1.2,0.2))
plt.xlabel("t[s]",fontsize=11)
plt.ylabel("V_i(t)",fontsize=11)
plt.legend(bbox_to_anchor=(0.5,-0.3),loc="center",ncol=3,fontsize=8,frameon=False)


plt.show()

