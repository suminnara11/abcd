import streamlit as st

# 앱의 제목 설정
st.title('나의 첫 번째 스트림릿 앱')

# 일반 텍스트 출력
st.write('안녕하세요, 스트림릿 월드! 이 코드는 아주 쉽습니다.')

# 버튼 추가하기
if st.button('여기 눌러보세요'):
    st.write('버튼이 눌렸습니다!')
else:
    st.write('버튼을 눌러주세요.')
