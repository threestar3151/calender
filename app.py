import streamlit as st
from streamlit_calendar import calendar

st.set_page_config(page_title="GS25 업무 스케줄", layout="wide")
st.title("🗓️ GS25 취합 및 마감 스케줄")

# 모바일 및 PC 통합 줄바꿈 디자인 (CSS)
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

# 누적된 취합 일정 데이터 (마감일 당일 표기)
calendar_events = [
    # --- 4월 일정 (기존 누적분) ---
    {"title": "📢 [마케팅] 토스 설치\n👤 담당: 최수민\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", "start": "2026-04-30", "color": "#D98880"},
    {"title": "🧼 [지원] 선도위생 제외\n👤 담당: 이충언\n📝 방법: 엑셀\n🎯 주체: 지역팀", "start": "2026-04-27", "color": "#7FB3D5"},
    {"title": "🥤 [MD] OSC 장려금\n👤 담당: 이종혁\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", "start": "2026-04-28", "color": "#7DCEA0"},
    {"title": "🛒 [지원] 장보기 추가\n👤 담당: 양희진\n📝 방법: 시스템\n🎯 주체: OFC개별", "start": "2026-04-27", "color": "#C39BD3"},
    {"title": "🛵 [O4O] 배달/픽업\n👤 담당: 박정은\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-04-27", "color": "#F0B27A"},
    {"title": "🍗 [MD] 치킨25 소모품\n👤 담당: 최원필\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-04-30", "color": "#73C6B6"},
    
    # --- 5월 일정 (신규 및 누적) ---
    {"title": "🏪 [지원] 특화매대 도입\n👤 담당: 권순백\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-05-18", "color": "#F7DC6F"},
    {"title": "🛵 [O4O] 배민/쿠팡 오픈\n👤 담당: 상현수\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-05-11", "color": "#FAD7A0"},
    
    # --- 신규 추가 내용 (이미지 확인분) ---
    {
        "title": "🛵 [O4O] 배달/픽업 8차\n👤 담당: 박정은\n📝 방법: OFC포탈\n🎯 주체: OFC개별", 
        "start": "2026-05-18", 
        "color": "#AED6F1"  # 연한 파스텔 블루
    },
    {
        "title": "📊 [지원] 재고조사 지연점\n👤 담당: 유찬울\n📝 방법: OFC포탈\n🎯 주체: OFC개별", 
        "start": "2026-05-18", 
        "color": "#A9DFBF"  # 연한 파스텔 그린
    },
    {
        "title": "🥤 [MD] OSC 장비 규격\n👤 담당: 이종혁\n📝 방법: OFC포탈\n🎯 주체: OFC개별", 
        "start": "2026-05-18", 
        "color": "#E59866"  # 연한 테라코타
    },
    {
        "title": "🍗 [MD] 치킨25 소급취합\n👤 담당: 최원필\n📝 방법: OFC포탈\n🎯 주체: OFC개별", 
        "start": "2026-05-31", 
        "color": "#F9E79F"  # 연한 레몬 옐로우
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

# 사이드바 업무 상세 가이드 업데이트
st.sidebar.header("📋 이번 주 주요 공문")
st.sidebar.info("**O4O_제2026-016호**\n- 배달/픽업 8차 정기 취합\n- 마감: 5/18(월)\n- 비고: 사업자/영업신고증 사진 필수")
st.sidebar.info("**지원_제2026-024호**\n- 재고조사 180일 지연점 일정 수립\n- 마감: 5/18(월)\n- 비고: 대상점 34점 확인")
st.sidebar.info("**MD_제2026-023호**\n- 음료 엔드형 OSC 장비 규격 취합\n- 마감: 5/18(월)\n- 비고: 228점 규격 정보(6단/5단)")
st.sidebar.info("**MD_제2026-022호**\n- 치킨25 4월 소모품 소급 취합\n- 마감: 5/31(일)\n- 비고: 미진행 점포 대상")
