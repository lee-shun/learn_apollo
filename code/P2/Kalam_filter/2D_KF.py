from mathlib.Matrix_module import Matrix
import sys
sys.path.append("../../P2")

'''
Implement the KF below
'''

measurements = [1, 2, 3]

x = Matrix([[0.], [0.]])               # initial state (location and velocity)
P = Matrix([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = Matrix([[0.], [0.]])               # external motion
F = Matrix([[1., 1.], [0, 1.]])        # next state function
H = Matrix([[1., 0.]])                 # measurement function
R = Matrix([[1.]])                     # measurement uncertainty
I = Matrix([[1., 0.], [0., 1.]])       # identity matrix


def kalman_filter(x, P):
    for i in range(len(measurements)):
        #update
        Z = Matrix([[measurements[i]]])
        y = Z - (H*x)  # 此处的x是上一步的估计值
        S = H*P*H.transpose()+R
        K = P*H.transpose()*S.inverse()
        x = x+(K*y)

        P = (I-(K*H))*P

        #prediction
        x = (F*x)+u
        P = F*P*F.transpose()

    return x, P


print(kalman_filter(x, P))
