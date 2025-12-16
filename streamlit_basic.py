import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# 1. 환경변수 로드
load_dotenv()

# 2. OpenAI 클라이언트 생성
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 3. UI
st.title("ChatGPT Streamlit App")

user_input = st.text_input("질문을 입력하세요")

# 4. 버튼 클릭 시 GPT 호출
if st.button("질문하기") and user_input:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    st.write(response.choices[0].message.content)
