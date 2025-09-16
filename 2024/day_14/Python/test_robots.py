from robots import Robot


def test_robot_position_after():
    robot = Robot(2, 5, 3, 8)
    assert robot.position_after(1) == Robot(5, 13, 3, 8)
