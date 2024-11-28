---
title: Simulink与COMSOL协同仿真
categories:
  - 软件学习
translate_title: simulink-and-comsol-cosimulation
date: 2019-08-26 17:15:00
tags: [CAE, COMSOL, 仿真, Simulink, 计算, Matlab, PID]
---

#### 需求背景

Matlab/Simulink用于控制系统仿真，COMSOL用于模型有限元仿真，如果有限元模型是控制系统的一部分，则需要将二者联立，实现Simulink和COMSOL的协同仿真。

COMSOL 3.5版本（包括之前的FEMLAB）以前，提供了导出COMSOL模型到Simulink的标准接口，但对于非线性模型来说，直接导出的模型不能直接使用。后续版本，COMSOL取消了直接导出Simulink的功能，与Simulink的连接方式也发生了变更。

思路上，Simulink的S-function支持用户自定义任意子系统，COMSOL模型可以直接保存为Matlab的".m"文件，将其修改作为S-function的一部分直接导入到控制系统中即可。Simulink模型在仿真的过程中调用S函数，通过S函数对COMSOL的边界条件或物理参数进行修改，其后COMSOL执行一个仿真步，获取COMSOL执行该仿真步的结果并传递给Simulink，作为Simulink执行下一步的参数设置依据。

#### Demo：模拟温度控制系统

如下图所示一个简单的温度控制系统，PID控制系统的输出功率，S-Function调用COMSOL对指定功率的模型做传热分析，计算得到温度结果与参比温度（300K）进行比较，温度低则提高控制系统输出功率，温度高则降低控制系统输出功率。多次迭代后，使系统输出温度稳定在参比温度附近。

![Simulink_S_function](/assets/img/blogimgs/cax/comsol_simulink/Simulink_S_function.png)

计算过程中实时监控的温度变化曲线如下。初始温度为293.15K，初始加热功率为0W/m<sup>3</sup>，PID控制器自动调高输出功率，最终COMSOL计算得到的监测点温度逐渐逼近参比温度300K。

![Simulink_Scope](/assets/img/blogimgs/cax/comsol_simulink/Simulink_Scope.png)

监测点（中心点）温度达到参比温度时，COMSOL传热计算结果如下，此时，PID控制器输出的功率为155.5893W/m<sup>3</sup>。

![COMSOL_Capture](/assets/img/blogimgs/cax/comsol_simulink/COMSOL_Capture.png)

对模型设置感兴趣，请联系作者。
