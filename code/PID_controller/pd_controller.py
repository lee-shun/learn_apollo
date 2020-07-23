############## ADD / MODIFY CODE BELOW ####################
# ------------------------------------------------------------------------
#
# run - does a single control run

from Robot import *

print("hello: pd_controller!!!")

robot = Robot()
robot.set(0,1,0)

def run(robot, tau_p, tau_d, n=1000, speed=1.0):
    x_trajectory = []
    y_trajectory = []

    """
    pd_controller
    """
    prev_cte = robot.y
    for i in range(n):
        cte = robot.y
        diff_cte = cte - prev_cte
        prev_cte = cte
        steer = -tau_p * cte - tau_d * diff_cte
        robot.move(steer, speed)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)

    return x_trajectory, y_trajectory


x_trajectory, y_trajectory = run(robot, 0.1,0.3)
n = len(x_trajectory)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
ax1.plot(x_trajectory, y_trajectory, 'g', label='P controller')
ax1.plot(x_trajectory, np.zeros(n), 'r', label='reference')

plt.show()
