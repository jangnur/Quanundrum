import numpy as np

fimport quanundrum.utils as ut
from quanundrum.protocol import Protocol, ProtocolStep
from quanundrum.quantumsystem import QuantumSystem
from quanundrum.agents import observe
from quanundrum.inference_procedures import forward_inference, backward_inference
from projectq.ops import H


def action1(qsys:QuantumSystem):
    H | qsys['s']
    
step1 = ProtocolStep(domain={'Qubit': 's'},
                     descr = 'Prepare Qubit s by applying H ',
                     time  = 0,
                     action = action1)

def action2(qsys:QuantumSystem):
    observe(qsys['Alice_memory'],qsys['s'])
    
step2 = ProtocolStep(domain={'Qubit': 's',
                             'AgentMemory(1)': 'Alice'},
                     descr = 'Alice observes s',
                     time  = 1,
                     action = action2)

def action3(qsys:QuantumSystem):
    observe(qsys['Bob_memory'],qsys['s'])
    
step3 = ProtocolStep(domain={'Qubit': 's',
                             'AgentMemory(1)': 'Bob'},
                     descr = 'Bob observes s',
                     time  = 2,
                     action = action3)


