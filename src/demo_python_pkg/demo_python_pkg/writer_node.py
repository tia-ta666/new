import rclpy
from .PersonNode import Person_Node


class WriterNode(Person_Node):
    def __init__(self, name: str, age: int, book: str) -> None:
        super().__init__('writer_node', name, age)
        self.book = book


def main(args=None):
    rclpy.init(args=args)                       # ★ 必须先 init
    writer = WriterNode('李四', 18, '《三国演义》')
    writer.eat('香蕉')
    writer.destroy_node()                       # 只打印就退出，不 spin
    rclpy.shutdown()


if __name__ == '__main__':
    main()