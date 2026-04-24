import streamlit as st
from streamlit_calendar import calendar

st.set_page_config(page_title="GS25 업무 스케줄", layout="wide")
st.title("🗓️ GS25 취합 및 마감 스케줄")

# 모바일 및 PC 통합 줄바꿈 디자인
calendar_css = """
.fc-event-main {
    white-space: pre-wrap !important;
    word-wrap: break-word !important;
    line-height: 1.3 !important;
    padding: 2px !important;
}
@media (max-width: 768px) {
    .fc-event-title { font-size: 0.75em !important; }
}
"""

# 누적된 취합 일정 데이터
calendar_events = [
    # 4월 4주차 일정
    {"title": "📢 [마케팅] 토스 설치\n👤 담당: 최수민\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", "start": "2026-04-30", "color": "#D98880"},
    {"title": "🧼 [지원] 선도위생 제외\n👤 담당: 이충언\n📝 방법: 엑셀\n🎯 주체: 지역팀", "start": "2026-04-27", "color": "#7FB3D5"},
    {"title": "🥤 [MD] OSC 장려금\n👤 담당: 이종혁\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", "start": "2026-04-28", "color": "#7DCEA0"},
    {"title": "🛒 [지원] 장보기 추가\n👤 담당: 양희진\n📝 방법: 시스템\n🎯 주체: OFC개별", "start": "2026-04-27", "color": "#C39BD3"},
    {"title": "🛵 [O4O] 배달/픽업\n👤 담당: 박정은\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-04-27", "color": "#F0B27A"},
    {"title": "🍗 [MD] 치킨25 소모품\n👤 담당: 최원필\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-04-30", "color": "#73C6B6"},
    
    # 4월 5주차 신규 추가 일정
    {
        "title": "🏪 [지원] 특화매대 도입 취합\n👤 담당: 권순백\n📝 방법: OFC포탈\n🎯 주체: OFC개별", 
        "start": "2026-05-18", 
        "color": "#F7DC6F"
    },
    {
        "title": "🛵 [O4O] 배민/쿠팡 오픈 취합\n👤 담당: 상현수\n📝 방법: OFC포탈\n🎯 주체: OFC개별", 
        "start": "2026-05-11", 
        "color": "#FAD7A0"
    }
]

calendar_options = {
    "headerToolbar": {
        "left": "prev,next today",
        "center": "title",
        "right": "dayGridMonth,listMonth"
    },
    "initialView": "dayGridMonth",
    "locale": "ko",
    "height": "auto",
}

calendar(events=calendar_events, options=calendar_options, custom_css=calendar_css)

st.sidebar.header("📋 4월 5주차 신규 공문 가이드")
st.sidebar.info("**지원_제2026-023호**\n- 특화매대(K스테이션, 뷰티, 헬스) 도입 희망점\n- 마감: 5/18(월)\n- 비고: 시설요청서 캡처본 필수 첨부")
st.sidebar.info("**O4O_제2026-015호**\n- 배달의민족, 쿠팡이츠 오픈 희망점\n- 마감: 5/11(월)\n- 비고: 사업자등록증/영업신고증 사진 필수")
