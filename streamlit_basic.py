# import streamlit as st
# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# # 1. 환경변수 로드
# load_dotenv()

# # 2. OpenAI 클라이언트 생성
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # 3. UI
# st.title("ChatGPT Streamlit App")


# user_input = st.text_input("질문을 입력하세요")

# # 4. 버튼 클릭 시 GPT 호출
# if st.button("질문하기") and user_input:
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "user", "content": user_input}
#         ]
#     )
#     st.write(response.choices[0].message.content)

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# -----------------------------
# 1. 환경 변수 로드
# -----------------------------
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------------
# 2. 페이지 기본 설정
# -----------------------------
st.set_page_config(
    page_title="Virtual Assistant",
    page_icon="👺👺👺",
    layout="centered"
)

# -----------------------------
# 3. 헤더 UI
# -----------------------------
st.markdown(
    """
    <div style="text-align:center; padding:20px 0;">
        <h2>Virtual Assistant</h2>
        <p style="color:gray;">도상원의 챗팅방 입니다./p>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# 4. 세션 상태 (대화 기록)
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요. 무엇을 도와드릴까요?"
        }
    ]

# -----------------------------
# 5. 기존 대화 출력 (채팅 UI)
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# 6. 사용자 입력창 (하단 고정)
# -----------------------------
user_input = st.chat_input("메시지를 입력하세요")

# -----------------------------
# 7. GPT 호출
# -----------------------------
if user_input:
    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # GPT 응답
    with st.chat_message("assistant"):
        with st.spinner("생각중..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages
            )
            assistant_message = response.choices[0].message.content
            st.markdown(assistant_message)

    # 응답 저장
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_message}
    )

