1. 位置和姿态：

2. 要求：
        精度10cm
        鲁棒性

3. 定位方式：
        1. 基于电子信号 :例如GPS
        2. 航机推算     :例如IMU
        3. 环境特征匹配 :Lidar、Camera等

4. 差分GPS：
        位置差分以及距离差分：
                1.伪距差分
                2.载波相位差分:精度较高

5. 激光定位：
        需要有概率地图：实时的激光点云与预先有的地图做匹配

6. 视觉定位：
        深度学习的方式检测出车道线，之后再与高精地图做匹配

7. 惯性导航：
        加速度计以及陀螺仪i
需要注意的一点事：各种传感器的时间戳的对准。


8. 多传感器融合定位：
        各个传感器得到的原始位置以及姿态等信息，进入卡尔曼滤波器

9. 相机坐标系：
        车辆的原点选做IMU的安装点，相机坐标系与相机与IMU
        原点在光心

10. 激光雷达坐标系：




-----------------------------------------------------------------



 ## 百度的定位解决方案：

1. GNSS定位

2. 激光点云定位：
        利用现有点云以及实时擦计的点云在一定范围内做平方差的总和，
        最小的位置作为车辆的位置估计

        LK算法，将航向角首先进行一个优化。