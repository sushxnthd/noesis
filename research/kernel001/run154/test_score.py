"""No trained checkpoints required for CI smoke tests."""
import numpy as np
from research.kernel001.run154.score import affine,score
from research.kernel001.run154.beam_verify import beam,exact
def test_affine_matches_one_step():
 A=np.array([[1.0,0.2],[0.1,0.9]]);E=np.array([[0.3,-0.2],[-0.1,0.1],[0.0,0.0]])
 h=np.array([[1.0,0.0],[0.0,1.0],[1.0,2.0]])
 J,b=affine(h,A,E,(0,1))
 x=np.maximum(0,np.maximum(0,h@A.T+E[0])@A.T+E[1])
 assert np.allclose(np.einsum("nij,nj->ni",J,h)+b,x,atol=1e-14)
def test_exact_rejects_simple_wrong_model():
 cp={"parameters":{"A":[[1.0]],"E":[[0.0],[0.0],[0.0]],"w":[0.0]}}
 assert exact(cp,[0])["failure"]
 assert beam(cp,3)["depth"]==1
 assert score(cp)["predict_failure"]
