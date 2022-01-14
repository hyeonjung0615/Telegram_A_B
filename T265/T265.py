from typing import _get_type_hints_obj_allowed_types
from telegram.ext import Updater
from telegram.ext import CommandHandler
import pyrealsense2 as rs

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


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


def startT265(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text= "INPUT : /T265on or /T265off")
    T265()
    


# def T265_ON(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text= "T265 ON") 

# def T265_OFF(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text= "T265 OFF")


startT265_handler = CommandHandler('startT265', startT265)
# T265on_handler = CommandHandler('T265on', T265_ON)
# T265off_handler = CommandHandler('T265off', T265_OFF)

dispatcher.add_handler(startT265_handler)
# dispatcher.add_handler(T265on_handler)
# dispatcher.add_handler(T265off_handler)

updater.start_polling()
updater.idle()