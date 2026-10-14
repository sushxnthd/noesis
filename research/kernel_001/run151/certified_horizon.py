"""Conservative IEEE-754 forward-error envelope for exhaustive RNN evaluation."""
import numpy as np

def bounds(A,E,w,states_by_depth):
    u=2.0**-53
    gamma=8*u/(1-8*u)
    normA=float(np.max(np.sum(np.abs(A),axis=1)))*(1+gamma)
    normw=float(np.sum(np.abs(w)))*(1+gamma)
    normE=float(np.max(np.abs(E)))
    state_error=0.0
    result=[]
    for depth,(previous_max,current_max) in enumerate(states_by_depth,1):
        state_error=normA*state_error+100*gamma*(normA*previous_max+normE)
        output_error=normw*state_error+100*gamma*(normw*current_max+depth)
        result.append(output_error)
    return result
