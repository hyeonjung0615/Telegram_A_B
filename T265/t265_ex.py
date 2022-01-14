#!/usr/bin/python
# -*- coding: utf-8 -*-
## License: Apache 2.0. See LICENSE file in root directory.
## Copyright(c) 2019 Intel Corporation. All Rights Reserved.

#####################################################
##           librealsense T265 example             ##
#####################################################

# 먼저 라이브러리를 가져옵니다.
import pyrealsense2 as rs

# 실제 장치와 센서를 캡슐화하는 RealSense 파이프라인 선언
pipe = rs.pipeline()

# 구성 객체를 빌드하고 포즈 데이터를 요청합니다.
cfg = rs.config()
cfg.enable_stream(rs.stream.pose)

# 요청된 구성으로 스트리밍 시작
pipe.start(cfg)

def T265CAM():
    pipe = rs.pipeline()              # 먼저 라이브러리를 가져옵니다.
    cfg = rs.config()                 # 실제 장치와 센서를 캡슐화하는 RealSense 파이프라인 선언
    cfg.enable_stream(rs.stream.pose) # 구성 객체를 빌드하고 포즈 데이터를 요청합니다.
    pipe.start(cfg)                   # 요청된 구성으로 스트리밍 시작

    try:
        for _ in range(50):
            # 카메라에서 다음 프레임 세트를 기다립니다.
            frames = pipe.wait_for_frames()

            # 포즈 프레임 가져오기
            pose = frames.get_pose_frame()
            if pose:
                # 포즈 데이터의 일부를 터미널에 출력
                data = pose.get_pose_data()
                print("Frame #{}".format(pose.frame_number))
                print("Position: {}".format(data.translation))
                print("Velocity: {}".format(data.velocity))
                print("Acceleration: {}\n".format(data.acceleration))

    finally:
            pipe.stop()