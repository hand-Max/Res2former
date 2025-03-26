![alt text](image-1.png)
1.首先获取所训练动作需要的场景/零件高斯模型，同时得到搭建仿真场景所需的.stl格式数学模型，以及与真机机器人结构信息一致的mujoco模型文件
2.然后将高斯画面中零件和场景物体与mujoco场景目标一比一对齐，并搭建所采集场景的仿真场景
3.基于不同动作的仿真数据采集要求，调整仿真动作和数据采集程序
4.根据现场动作和底盘误差范围，设置仿真数据采集的随机变量数值范围，运行和保存所需要的图像/关节/坐标
使用示例
高斯/数学模型对齐：
通过https://playcanvas.com/supersplat/editor/ 网页工具，对齐高斯零件与高斯背景空间位置，如下
![alt text](image-2.png)
动作场景搭建：
根据动作需求现场零件高度/相对位置等量测结果，修改mujoco配置文件xml信息，使与现场一致
参考 下配置文件：
http://192.168.1.237:3000/SimToReal/Topia3DTrain/src/master/mujoco_collect/mocap_sim/mocap_sim/assets/hand_control_v1_new
动作随机参数设置：
基于机器人底盘现实误差范围，机器人动作误差范围，零件位姿误差范围等参数，在程序中设置各误差范围数值大小，使涵盖或大于现场最大误差
参数修改位置参考：
http://192.168.1.237:3000/SimToReal/Topia3DTrain/src/master/mujoco_collect/mocap_sim/mocap_sim
生成动作和数据采集：
采集仿真动作需启动三个终端
```python
1.ros2 run sim_render_ros2 render_node
2.python robot_kinemic/robot_kinemic/robot_control.py
3.python mocap_sim/mocap_sim/htc_mocap_act.py
```
第一个终端启动后保持后台启动，实时渲染高斯场景画面，并由ros2话题发出；后分别启动第二第三个终端开始采集动作数据
参考代码:
http://192.168.1.237:3000/SimToReal/Topia3DTrain/src/master/mujoco_collect


mujoco和高斯模型采集数据的代码执行逻辑：

制作背景和零件的高斯模型，分别赋值modelPath和productPly，调整零件高斯模型的位置factory_obj，使其在指定背景中的夹具上；
确定零件的抓取点和机器人头部相机和腰部的弯曲幅度（仿真设置，分别修改mocap_data和waist_inl，保证机器人在此设置下能抓取到零件和取出零件(手臂不超限制)；
调整仿真中机器人位置chassis_position 和相机焦距camera_head_fovy值，使仿真中相机焦距和真机焦距对齐；
调整仿真中零件的抓取点（tool_T_l，tool_T_r）；
确定机器人的随机偏移量（前后偏移和左右偏移）random.uniform()，保证最大偏移量时，零件在相机画面内（保证yolo模型检测的区域在相机画面内）；
设置循环采集数据次数self.cmax ：
```python
for i in self.cmax：
    pos= random.uniform()#给底盘一个随机误差
    chassis_position+=pos
    left_hand_des=mat2pos_quaternion(np.linalg.inv(waist_T) @ tool_T_l @ np.linalg.inv(end_effector_l))#计算mujoco坐标系下左右手到零件的抓取点的运动距离。
    right_hand_des=mat2pos_quaternion(np.linalg.inv(waist_T) @ tool_T_r @ np.linalg.inv(end_effector_r))
    inage=camera(Gaussian model)                                                 #从高斯模型中获取相机拍摄的图片
    save.(left_hand_des,right_hand_des,image)
return 
```

