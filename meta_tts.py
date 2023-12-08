import torch
import mysql.connector



# # 1) MySQL 연결 설정
# mydb = mysql.connector.connect(
#     host="호스트주소",
#     user="유저이름",
#     password="비밀번호",
#     database="데이터베이스이름"
# )

# # 2) user_id, portfolio_no 에 따라 질문을 3개 가져옴

# # 커서 생성
# mycursor = mydb.cursor()

# # 데이터베이스에서 특정 행 가져오기
# mycursor.execute("SELECT * FROM your_table_name WHERE (user_id = ) and (portfolio_no = )")  

# # 행을 변수에 담기
# questions = mycursor.fetchall()
# # question_no, question_content, question_order, question_use, portfolio_no, user_id, question_type, tts_path
questions = [ #DB 연결 전, 임의 행 데이터
    (1, "입사 후 포부가 무엇인가요?", 1, 1, 1, "user_1", "voice_hg", "NULL"),
    (2, "해당 프로젝트에서 어떤 인공지능 기술이 사용되었나요?", 2, 2, 1, "user_2", "voice_ic", "NULL"),
    (3, "상사가 부당한 업무 지시를 시킨다면 어떻게 할 것인가요?", 3, 3, 1, "user_3", "voice_nr", "NULL")
]


from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2") #합칠 때 속성에 gpu=True 추가

for q in questions:
    # generate speech by cloning a voice using custom settings
    tts.tts_to_file(text= q[1], #질문 _ DB에서 가져온 정보로
                file_path= f"tts_result/{q[5]}_{q[6]}_{q[0]}.wav", #결과값으로 저장될 파일명 _ "사용자id_면접관번호_질문번호.wav"
                speaker_wav= f"{q[6]}.wav", #면접관 음성 _ DB에서 가져온 정보로
                language="ko"
                )
    print(f"tts_result/{q[5]}_{q[6]}_{q[0]}.wav")
    # #생성된 파일 경로 DB에 저장
    # sql = "UPDATE question_table SET tts_path = %s WHERE question_no = %s"
    # val = (f"tts_result/{q[5]}_{q[6]}_{q[0]}.wav", q[0])  # q[0]은 question_no에 해당하는 값

    # mycursor.execute(sql, val)
    # mydb.commit()






