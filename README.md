# 🤖 ProjectArm - Simulación de Robot en ROS 2

Este proyecto contiene la simulación de un brazo antropomórfico en **ROS 2 Humble**, utilizando **URDF, RViz y MoveIt 2**.

---

## 📥 Clonar el repositorio

```bash
git clone https://github.com/NeyCoto/ProjectArm.git
cd ProjectArm
```

---

## ⚙️ Instalación de dependencias

### RViz
```bash
sudo apt update
sudo apt install ros-humble-rviz2
rviz2
```

### MoveIt 2
```bash
sudo apt update
sudo apt install ros-humble-moveit
ros2 launch moveit2_tutorials demo.launch.py
```

---

## 🔨 Compilación del proyecto
```bash
colcon build
source install/setup.bash
```

---

## 🚀 Cargar la simulación en RViz
```bash
ros2 launch ur5Model display.launch.py
```

---

## 🦾 Planificación de movimiento con MoveIt 2
```bash
ros2 launch ur5_moveit_config demo.launch.py
```

---

## 📂 Estructura del proyecto
```
ProjectArm/
├── src/                # Paquetes del robot
├── urdf/               # Modelo URDF del robot
├── launch/             # Archivos de lanzamiento
└── README.md           # Documentación del proyecto
```

---

## 👨‍💻 Autor
- Ney Coto
