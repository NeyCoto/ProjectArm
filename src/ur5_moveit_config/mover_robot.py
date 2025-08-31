#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from moveit_msgs.msg import DisplayTrajectory
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy
import numpy as np

# configurar NumPy para imprimir sin notación científica y con 2 decimales
np.set_printoptions(suppress=True, precision=2)

class PlannedTrajectoryPrinter(Node):
    def __init__(self):
        super().__init__('planned_trajectory_printer')
        from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy
        traj_qos = QoSProfile(
            depth=10,
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.VOLATILE  # compatible con MoveIt
        )

        self.subscription = self.create_subscription(
            DisplayTrajectory,
            '/display_planned_path',
            self.trajectory_callback,
            traj_qos
        )

        self.trajectory_matrix = []  # lista donde se guardarán los puntos
        self.get_logger().info('Nodo iniciado ✅ Escuchando /display_planned_path')

    def trajectory_callback(self, msg: DisplayTrajectory):
        self.get_logger().info('--- Nueva trayectoria planificada ---')
        for traj in msg.trajectory:
            for point in traj.joint_trajectory.points:
                # Tomamos todas las 6 juntas
                row = list(point.positions[:6])
                self.trajectory_matrix.append(row)

        # Convertimos a matriz n×6
        traj_array = np.array(self.trajectory_matrix)
        traj_array = np.round(np.degrees(traj_array),2)
        self.get_logger().info(f"Matriz de trayectoria (n×6):\n{traj_array}")
        traj_array = np.round(traj_array,0)
        self.get_logger().info(f"Matriz de trayectoria a enteros (n×6):\n{traj_array}")

def main(args=None):
    rclpy.init(args=args)
    node = PlannedTrajectoryPrinter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

