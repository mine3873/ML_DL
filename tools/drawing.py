import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# 데이터 포인트 설정
x = np.array([-1, 0, 1])
y = np.array([1, 0, 0.8])

# 벡터 정의
v1 = np.array([-1, 1])  # 왼쪽 벡터 (-1,1)
v2 = np.array([1, 0.8])  # 오른쪽 벡터 (1,0.8)
x_axis = np.array([1, 0])  # x축 양의 방향 벡터 (1,0)

# 벡터와 x축이 이루는 각도 계산
def angle_with_x_axis(v):
    dot_product = np.dot(v, x_axis)
    norm_v = np.linalg.norm(v)
    norm_x = np.linalg.norm(x_axis)
    theta_rad = np.arccos(dot_product / (norm_v * norm_x))  # 라디안 단위
    theta_deg = np.degrees(theta_rad)  # 도 단위 변환
    return theta_deg

theta1 = angle_with_x_axis(v1)
theta2 = angle_with_x_axis(v2)

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label="Graph Lines")

# xy축 추가
ax.axhline(0, color='black', linewidth=1)  # x축
ax.axvline(0, color='black', linewidth=1)  # y축

# 원호 추가 (계산된 각도 적용)
arc1 = Arc((0, 0), 0.5, 0.5, angle=0, theta1=theta2, theta2=theta1, color='r', lw=2)  # 왼쪽 벡터

ax.add_patch(arc1)


# 각도 텍스트 표시
ax.text(-0.35, 0.2, "θ", fontsize=12, color='r')  # 왼쪽 벡터

# 그래프 스타일 조정
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-0.1, 1.1)
ax.set_aspect('equal')

plt.show()
