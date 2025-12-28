import numpy as np
import matplotlib.pyplot as plt

# 1. 파라미터 설정 (DSP 연구의 기본 변수들)
fs = 44100      # 샘플링 주파수 (1초를 44,100개로 쪼개기)
f = 440         # 신호 주파수 (라음, A4)
duration = 0.01 # 0.01초 동안의 신호만 확인

# 2. 시간축 생성: 0부터 duration까지 1/fs 간격으로 생성
t = np.arange(0, duration, 1/fs)

# 3. 사인파 생성: y = A * sin(2 * pi * f * t)
# 여기서는 진폭(A)을 1로 설정합니다.
y = np.sin(2 * np.pi * f * t)

# 4. 시각화 (Matplotlib 활용)
plt.figure(figsize=(10, 4))
plt.plot(t, y, label=f'{f}Hz Sine Wave')
plt.title("Basic Sine Waveform")
plt.xlabel("Time [sec]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()