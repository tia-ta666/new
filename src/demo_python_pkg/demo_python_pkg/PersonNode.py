import rclpy
from rclpy.node import Node


class Person_Node(Node):
    def __init__(self, node_name: str, name: str, age: int) -> None:
        super().__init__(node_name)      # ★ 关键：先调用父类 Node 构造
        self.name = name
        self.age = age
        self.get_logger().info(f"Person_Node 初始化完成：{self.name}, {self.age}岁")

    def eat(self, food: str) -> None:
        self.get_logger().info(f"我叫{self.name}，今年{self.age}岁，正在吃{food}")


def main(args=None):
    rclpy.init(args=args)
    node = Person_Node('person_node', '张三', 20)
    node.eat('苹果')
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
