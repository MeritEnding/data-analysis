import cv2
import numpy as np

# 가상의 온도 데이터를 생성하는 함수
def generate_fake_temperature_data(shape):
    return np.random.uniform(low=36.0, high=38.5, size=shape)

# 이상치를 감지하는 함수
def detect_outliers(temperature_data, threshold):
    outliers = temperature_data > threshold
    return outliers

# 이상치 판단 기준 온도 설정 (예: 37.5도)
threshold_temperature = 37.5

# 온도 데이터를 생성 (가상의 데이터를 사용하므로 실제 카메라 연결은 고려하지 않음)
temperature_data = generate_fake_temperature_data((480, 640))

# 이상치 감지
outliers = detect_outliers(temperature_data, threshold_temperature)

# 이상치가 감지되면 경고 메시지 출력
if np.any(outliers):
    print("이상치가 감지되었습니다. 문제가 있을 수 있습니다.")
else:
    print("정상 온도입니다.")

# 온도 데이터 시각화 (예시)
cv2.imshow('Temperature Data', temperature_data)
cv2.waitKey(0)
cv2.destroyAllWindows()
