# Lesson 10: Writing ROS 2 nodes

**Goal:** write your own nodes in Python: **subscribers** that listen, **publishers** that talk,
**timers** that do something every so often, and a node that does all three. Then open up
`arm.py` again: now the ROS parts make sense.

You already know every Python idea you need, from Lessons 5 and 6. A node is a **class** that
**inherits** from `Node`, and ROS calls your **callbacks** whenever a message arrives or a
timer goes off. `rclpy` is ROS 2's Python library.

**Simulation:** `ros2 launch workshop_arm workshop.launch.py stage:=1`

Run each exercise from a second terminal in this folder (`python ex1_joint_listener.py`), and
stop it with `Ctrl+C`. Nodes run until you stop them: that's normal.

## The shape of every node

```python
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState          # 1. the message type you need


class JointListener(Node):                      # 2. your node is a Node...

    def __init__(self):
        super().__init__('joint_listener')      # 3. ...with a name (see: ros2 node list)
        self.create_subscription(JointState, '/follower/joint_states', self.on_joints, 10)

    def on_joints(self, msg):                   # 4. ROS calls this for every message
        print(msg.position)


def main():
    rclpy.init()                                # 5. start ROS
    rclpy.spin(JointListener())                 # 6. wait for messages, call callbacks, forever
```

How do you know the message type? `ros2 topic info /follower/joint_states` tells you
(`sensor_msgs/msg/JointState`), and `ros2 interface show sensor_msgs/msg/JointState` shows what's
inside it. In Python, `sensor_msgs/msg/JointState` becomes `from sensor_msgs.msg import JointState`.

## Exercises (together)

1. **[`ex1_joint_listener.py`](ex1_joint_listener.py): a subscriber.**
   Listen to `/follower/joint_states` and print each joint angle in degrees.
2. **[`ex2_talker.py`](ex2_talker.py) and [`ex2_listener.py`](ex2_listener.py): a publisher and
   a timer.** A talker that sends a message twice a second, and a listener you finish. Run them
   in two terminals, then try two of each. *(No simulation needed.)*
3. **[`ex3_motion_detector.py`](ex3_motion_detector.py): listen *and* talk.**
   Turn 100 joint-angle messages a second into one simple message: is the arm `moving` or
   `still`? Watch it with `ros2 topic echo /arm_status`.
4. **Back to `arm.py`.** Open
   [`src/workshop_arm/workshop_arm/arm.py`](../../src/workshop_arm/workshop_arm/arm.py) and find:
   - `self.node = Node('workshop_arm')`. `Arm` *has* a node instead of *being* one. Why might
     that be friendlier for beginners than `class Arm(Node)`?
   - The two `ActionClient`s. What are they talking to? (Compare with `ros2 action list`.)
   - The two `create_client` lines. Those are **service** clients. What do the services do?
   - `where_am_i`. It uses the same TF lookup as this lesson's challenge.

## Services and actions, briefly

Topics are one-way: you publish and hope someone's listening. Sometimes you need an answer:

| | Use it when | Example in `arm.py` |
|---|---|---|
| **Topic** | a stream of data, many listeners | `/follower/joint_states` |
| **Service** | a quick question and one answer | "what's on the table?" (`/get_planning_scene`) |
| **Action** | a long job, with progress, that can be cancelled | "move the arm here" (`/move_action`) |

`Arm` hides these behind one-line methods. Writing your own service and action clients is a
good stretch goal after the course.

## Challenge (on your own)

**[`challenge_safety_monitor.py`](challenge_safety_monitor.py): a safety monitor node.**
Watch where the gripper is (using TF, set up for you) and warn whenever it goes below 3 cm
above the table. Publish the warnings on `/safety_warnings` so other nodes could react.

You'll turn this node into a proper ROS package, with its own launch file, in Lesson 11.

## Things to remember

| Idea | Example |
|---|---|
| A node is a class built on `Node` | `class Talker(Node):` |
| Give the node a name | `super().__init__('talker')` |
| Listen to a topic | `self.create_subscription(Type, '/topic', self.callback, 10)` |
| Talk on a topic | `self.pub = self.create_publisher(Type, '/topic', 10)`, then `self.pub.publish(msg)` |
| Do something every N seconds | `self.create_timer(0.5, self.on_timer)` |
| Make a message | `msg = String()`, `msg.data = 'hi'`, or `String(data='hi')` |
| Run the node | `rclpy.init()`, then `rclpy.spin(node)` |
| Find a topic's type | `ros2 topic info /topic` |
| See what's in a type | `ros2 interface show std_msgs/msg/String` |

**Next:** [Lesson 11: Packages and launch files](../11_packages_and_launch/)
