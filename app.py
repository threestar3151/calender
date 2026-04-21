import streamlit as st
from streamlit_calendar import calendar

st.set_page_config(page_title="GS25 업무 스케줄", layout="wide")
st.title("🗓️ GS25 4부문 취합 및 마감일 안내")

# \n 을 사용해서 내용을 여러 줄로 나누었습니다.
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
    }
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

# ⭐️ 핵심: 달력 '내부'로 직접 쏴주는 줄바꿈 디자인 코드입니다.
calendar_css = """
.fc-event-main {
    white-space: pre-wrap !important;  /* 줄바꿈 강제 허용 */
    word-wrap: break-word !important;  /* 단어가 길면 자르기 */
    font-size: 0.85em !important;      /* 글씨 크기 조정 */
    line-height: 1.4 !important;       /* 줄 간격 */
    padding: 3px !important;           /* 내부 여백 */
}
.fc-event-title {
    white-space: pre-wrap !important;
}
"""

# 맨 뒤에 custom_css=calendar_css 를 추가해 달력 안쪽으로 밀어넣습니다.
calendar(events=calendar_events, options=calendar_options, custom_css=calendar_css)
