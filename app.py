import streamlit as st
from streamlit_calendar import calendar

st.set_page_config(page_title="GS25 업무 스케줄", layout="wide")

# [마법의 주문] 달력 안의 글씨가 잘리지 않고 여러 줄로 나오게 하는 설정입니다.
st.markdown("""
<style>
.fc-event-title {
    white-space: pre-wrap !important;  /* 줄바꿈을 허용하는 핵심 코드 */
    word-wrap: break-word !important;
    font-size: 0.85em !important;      /* 글씨가 너무 크면 넘치니 살짝 줄임 */
    line-height: 1.4 !important;       /* 줄 간격 최적화 */
}
.fc-event-main {
    padding: 3px !important;           /* 테두리 여백을 줘서 답답하지 않게 함 */
}
</style>
""", unsafe_allow_html=True)

st.title("🗓️ GS25 4부문 취합 및 마감일 안내")

# \n 을 사용해서 [내용], [담당자], [방법/주체]를 여러 줄로 나누었습니다.
calendar_events = [
    {
        "title": "📢 [마케팅] 토스 설치\n👤 담당: 최수민\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", 
        "start": "2026-04-30", 
        "color": "#D98880"
    },
    {
        "title": "🧼 [지원] 선도위생 제외\n👤 담당: 이충언\n📝 방법: 엑셀\n🎯 주체: 지역팀", 
        "start": "2026-04-27", 
        "color": "#7FB3D5"
    },
    {
        "title": "🥤 [MD] OSC 장려금\n👤 담당: 이종혁\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", 
        "start": "2026-04-28", 
        "color": "#7DCEA0"
    },
    {
        "title": "🛒 [지원] 장보기 추가\n👤 담당: 양희진\n📝 방법: 시스템\n🎯 주체: OFC개별", 
        "start": "2026-04-27", 
        "color": "#C39BD3"
    },
    {
        "title": "🛵 [O4O] 배달/픽업\n👤 담당: 박정은\n📝 방법: OFC포탈\n🎯 주체: OFC개별", 
        "start": "2026-04-27", 
        "color": "#F0B27A"
    },
    {
        "title": "🍗 [MD] 치킨25 소모품\n👤 담당: 최원필\n📝 방법: OFC포탈\n🎯 주체: OFC개별", 
        "start": "2026-04-30", 
        "color": "#73C6B6"
    },
]

calendar_options = {
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "dayGridMonth"
    },
    "initialView": "dayGridMonth",
    "locale": "ko",
}

calendar(events=calendar_events, options=calendar_options)
