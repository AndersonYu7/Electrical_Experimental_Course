import cv2
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

class HandPoseAnalyzer:
    @staticmethod
    # 根據兩點的座標，計算角度
    def vector_2d_angle(v1, v2):
        v1_x = v1[0]
        v1_y = v1[1]
        v2_x = v2[0]
        v2_y = v2[1]
        try:
            angle_= math.degrees(math.acos((v1_x*v2_x+v1_y*v2_y)/(((v1_x**2+v1_y**2)**0.5)*((v2_x**2+v2_y**2)**0.5))))
        except:
            angle_ = 180
        return angle_

    @staticmethod
    # 根據傳入的 21 個節點座標，得到該手指的角度
    def hand_angle(hand_):
        angle_list = []
        # thumb 大拇指角度
        angle_ = HandPoseAnalyzer.vector_2d_angle(
            ((int(hand_[0][0])- int(hand_[2][0])),(int(hand_[0][1])-int(hand_[2][1]))),
            ((int(hand_[3][0])- int(hand_[4][0])),(int(hand_[3][1])- int(hand_[4][1])))
            )
        angle_list.append(angle_)
        # index 食指角度
        angle_ = HandPoseAnalyzer.vector_2d_angle(
            ((int(hand_[0][0])-int(hand_[6][0])),(int(hand_[0][1])- int(hand_[6][1]))),
            ((int(hand_[7][0])- int(hand_[8][0])),(int(hand_[7][1])- int(hand_[8][1])))
            )
        angle_list.append(angle_)
        # middle 中指角度
        angle_ = HandPoseAnalyzer.vector_2d_angle(
            ((int(hand_[0][0])- int(hand_[10][0])),(int(hand_[0][1])- int(hand_[10][1]))),
            ((int(hand_[11][0])- int(hand_[12][0])),(int(hand_[11][1])- int(hand_[12][1])))
            )
        angle_list.append(angle_)
        # ring 無名指角度
        angle_ = HandPoseAnalyzer.vector_2d_angle(
            ((int(hand_[0][0])- int(hand_[14][0])),(int(hand_[0][1])- int(hand_[14][1]))),
            ((int(hand_[15][0])- int(hand_[16][0])),(int(hand_[15][1])- int(hand_[16][1])))
            )
        angle_list.append(angle_)
        # pink 小拇指角度
        angle_ = HandPoseAnalyzer.vector_2d_angle(
            ((int(hand_[0][0])- int(hand_[18][0])),(int(hand_[0][1])- int(hand_[18][1]))),
            ((int(hand_[19][0])- int(hand_[20][0])),(int(hand_[19][1])- int(hand_[20][1])))
            )
        angle_list.append(angle_)
        return angle_list

    @staticmethod
    # 根據手指角度的串列內容，返回對應的手勢名稱
    def hand_pos(finger_angle):
        f1 = finger_angle[0]   # 大拇指角度
        f2 = finger_angle[1]   # 食指角度
        f3 = finger_angle[2]   # 中指角度
        f4 = finger_angle[3]   # 無名指角度
        f5 = finger_angle[4]   # 小拇指角度

        # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
        if f1<50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
            return 'good'
        elif f1>=50 and f2>=50 and f3<50 and f4>=50 and f5>=50:
            return 'no!!!'
        elif f1<50 and f2<50 and f3>=50 and f4>=50 and f5<50: 
            return 'ROCK!'
        elif f1>=50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
            return '0'
        elif f1>=50 and f2>=50 and f3>=50 and f4>=50 and f5<50:
            return 'pink'
        elif f1>=50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
            return '1'
        elif f1>=50 and f2<50 and f3<50 and f4>=50 and f5>=50:
            return '2'
        elif f1>=50 and f2>=50 and f3<50 and f4<50 and f5<50:
            return 'ok'
        elif f1<50 and f2>=50 and f3<50 and f4<50 and f5<50:
            return 'ok'
        elif f1>=50 and f2<50 and f3<50 and f4<50 and f5>50:
            return '3'
        elif f1>=50 and f2<50 and f3<50 and f4<50 and f5<50:
            return '4'
        elif f1<50 and f2<50 and f3<50 and f4<50 and f5<50:
            return '5'
        elif f1<50 and f2>=50 and f3>=50 and f4>=50 and f5<50:
            return '6'
        elif f1<50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
            return '7'
        elif f1<50 and f2<50 and f3<50 and f4>=50 and f5>=50:
            return '8'
        elif f1<50 and f2<50 and f3<50 and f4<50 and f5>=50:
            return '9'
        else:
            return ''

class HandDirectionAnalyzer:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()

    def analyze_hand_direction(self, hand_landmarks, depth_image):
        directions = []

        # 手指關節的索引
        finger_joint_indices = [
            (0, 1),  # 大拇指: 手腕到第一個關節
            (1, 2),  # 大拇指: 第一個關節到第二個關節
            (2, 3),  # 大拇指: 第二個關節到第三個關節
            (3, 4),  # 大拇指: 第三個關節到指尖
            (0, 5),  # 食指: 手腕到第一個關節
            (5, 6),  # 食指: 第一個關節到第二個關節
            (6, 7),  # 食指: 第二個關節到第三個關節
            (7, 8),  # 食指: 第三個關節到指尖
            (0, 9),  # 中指: 手腕到第一個關節
            (9, 10), # 中指: 第一個關節到第二個關節
            (10, 11),# 中指: 第二個關節到第三個關節
            (11, 12),# 中指: 第三個關節到指尖
            (0, 13), # 無名指: 手腕到第一個關節
            (13, 14),# 無名指: 第一個關節到第二個關節
            (14, 15),# 無名指: 第二個關節到第三個關節
            (15, 16),# 無名指: 第三個關節到指尖
            (0, 17),  # 小拇指: 手腕到第一個關節
            (17, 18),# 小拇指: 第一個關節到第二個關節
            (18, 19),# 小拇指: 第二個關節到第三個關節
            (19, 20) # 小拇指: 第三個關節到指尖
        ]

        for joint_pair in finger_joint_indices:
            joint_start, joint_end = joint_pair
            start_point = (
                int(hand_landmarks.landmark[joint_start].x * depth_image.shape[1]),
                int(hand_landmarks.landmark[joint_start].y * depth_image.shape[0])
            )
            end_point = (
                int(hand_landmarks.landmark[joint_end].x * depth_image.shape[1]),
                int(hand_landmarks.landmark[joint_end].y * depth_image.shape[0])
            )

            # 計算方向向量
            direction_vector = (end_point[0] - start_point[0], end_point[1] - start_point[1])
            directions.append(direction_vector)

        return directions