import unittest
import numpy as np


class SingleQubit(unittest.TestCase):

    def test_Ramsey(self):
        '''
        Test simple Ramsey sequence
        '''
        q1 = Qubit('q1', piAmp=1.0, pi2Amp=0.5, pulseLength=30e-9)
        ramsey = [[X90(q1), Id(q1, delay), X90(q1)] for delay in np.linspace(0.0, 1e-6, 11)]
        show(ramsey[2])
        

class MultiQubit(unittest.TestCase):

    def test_Operators(self):
        q1 = Qubit('q1', piAmp=1.0, pi2Amp=0.5, pulseLength=30e-9)
        # goal is to make this just: q1 = Qubit('q1')
        q2 = Qubit('q2', piAmp=1.0, pi2Amp=0.5, pulseLength=30e-9)
        # seq = [X90(q1), X(q1)*Y(q2), CNOT(q1,q2), X(q2)+Xm(q2), Y(q1)*(X(q2)+Xm(q2)), MEAS(q1,q2)]
        seq = [X90(q1), X(q1)*Y(q2), CNOT(q1,q2), Xm(q2), Y(q1)*X(q2)]
        show(seq)
        #compileSeq(seq)


if __name__ == "__main__":
    
    if  __package__ is None:
        import sys, os
        # The following assumes the script is in the top level of the package
        # directory.  We use dirname() to help get the parent directory to add to
        # sys.path, so that we can import the current package.  This is necessary 
        # since when invoked directly, the 'current' package is not automatically
        # imported.
        parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        sys.path.insert(0, parent_dir)
        import PyQLab
        __package__ = "PyQLab"
        del sys, os
    from .QGL import *

    unittest.main()
#    singleTest = unittest.TestSuite()
#    singleTest.addTest(SingleQubit("Ramsey"))
#    unittest.TextTestRunner(verbosity=2).run(singleTest)
