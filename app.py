import streamlit as st
from streamlit_calendar import calendar

st.set_page_config(page_title="GS25 업무 스케줄", layout="wide")
st.title("🗓️ GS25 부문 취합 및 마감 스케줄")

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

calendar_events = [
    # --- 과거 데이터 누적분 (4월 ~ 5월 3주차 초반) ---
    {"title": "📢 [마케팅] 토스 설치\n👤 담당: 최수민\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", "start": "2026-04-30", "color": "#D98880"},
    {"title": "🧼 [지원] 선도위생 제외\n👤 담당: 이충언\n📝 방법: 엑셀\n🎯 주체: 지역팀", "start": "2026-04-27", "color": "#7FB3D5"},
    {"title": "🥤 [MD] OSC 장려금\n👤 담당: 이종혁\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", "start": "2026-04-28", "color": "#7DCEA0"},
    {"title": "🏪 [지원] 특화매대 도입\n👤 담당: 권순백\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-05-18", "color": "#F7DC6F"},
    {"title": "🛵 [O4O] 배민/쿠팡 오픈\n👤 담당: 상현수\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-05-11", "color": "#FAD7A0"},
    {"title": "🛵 [O4O] 배달/픽업 8차\n👤 담당: 박정은\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-05-18", "color": "#AED6F1"},
    {"title": "📊 [지원] 재고조사 지연점\n👤 담당: 유찬울\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-05-18", "color": "#A9DFBF"},
    {"title": "🥤 [MD] OSC 장비 규격\n👤 담당: 이종혁\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-05-18", "color": "#E59866"},
    {"title": "🍗 [MD] 치킨25 소급취합\n👤 담당: 최원필\n📝 방법: 점포경영시스템\n🎯 주체: OFC개별", "start": "2026-05-31", "color": "#F9E79F"},
    {"title": "📸 [MD] 음료 엔드OSC 진열사진\n👤 담당: 이종혁\n📝 방법: 시스템\n🎯 주체: OFC개별", "start": "2026-05-22", "color": "#F1948A"},
    {"title": "🍧 [MD] 6월 스무디 요청점\n👤 담당: 이규혁\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", "start": "2026-05-25", "color": "#D7BDE2"},
    {"title": "🧼 [지원] 6월 선도위생 제외점\n👤 담당: 이충언\n📝 방법: 엑셀\n🎯 주체: 지역팀", "start": "2026-05-25", "color": "#85C1E9"},
    {"title": "🦟 [MD] 방충용품 집기 입고\n👤 담당: 박거동\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", "start": "2026-05-25", "color": "#A3E4D7"},
    {"title": "🛒 [지원] 6월 장보기 추가\n👤 담당: 양희진\n📝 방법: 시스템\n🎯 주체: OFC개별", "start": "2026-05-25", "color": "#F8C471"},
    {"title": "🍦 [MD] 6월 아크 매출활성화\n👤 담당: 이주용\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-05-25", "color": "#BB8FCE"},
    {"title": "❄️ [MD] 디핀다트 냉동고\n👤 담당: 이주용\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-05-25", "color": "#73C6B6"},
    {"title": "🔍 [지원] 마스터 전수점검 오류\n👤 담당: 김민정\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", "start": "2026-06-05", "color": "#E59866"},
    {"title": "📺 [기타] 리테일미디어 설치\n👤 담당: 윤광복/오봉식\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", "start": "2026-06-08", "color": "#C39BD3"},
    {"title": "📱 [마케팅] 지역화폐 MPM\n👤 담당: 양소연\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", "start": "2026-06-08", "color": "#F1948A"},
    {"title": "🍗 [MD] 치킨25 추가도입\n👤 담당: 최원필\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", "start": "2026-06-01", "color": "#7DCEA0"},
    {"title": "🍕 [MD] 고피자 추가도입\n👤 담당: 배승섭\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", "start": "2026-06-01", "color": "#F8C471"},
    {"title": "🍕 [MD] 고피자 진열장 테스트\n👤 담당: 배승섭\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", "start": "2026-06-01", "color": "#85C1E9"},
    {"title": "💳 [MD] 구글 G-Pin 집기\n👤 담당: 송정환\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-06-08", "color": "#F7DC6F"},
    {"title": "🛵 [O4O] 배달/픽업 9차\n👤 담당: 박정은\n📝 방법: OFC포탈\n🎯 주체: OFC개별", "start": "2026-06-02", "color": "#FAD7A0"},
    {"title": "🏖️ [지원] 해안가 성수기 지원\n👤 담당: 임명섭\n📝 방법: 엑셀/PPT\n🎯 주체: 부문지원팀", "start": "2026-06-08", "color": "#A3E4D7"},

    # --- 신규 추가 데이터 (6월 1주차 안내분 - 총 3건) ---
    {
        "title": "📸 [MD] 6월 엔드OSC 진열사진\n👤 담당: 이종혁\n📝 방법: 시스템\n🎯 주체: OFC개별", 
        "start": "2026-06-15", "color": "#76D7C4"  # 파스텔 틸그린
    },
    {
        "title": "🍺 [마케팅] 데이지라거 포스터\n👤 담당: 최송화\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", 
        "start": "2026-06-08", "color": "#F5B041"  # 파스텔 머스터드
    },
    {
        "title": "📦 [MD] 데이지라거 공박스\n👤 담당: 안재성\n📝 방법: 엑셀\n🎯 주체: 부문지원팀", 
        "start": "2026-06-08", "color": "#85C1E9"  # 파스텔 스카이블루
    }
]

calendar_options = {
    "headerToolbar": {"left": "prev,next today", "center": "title", "right": "dayGridMonth,listMonth"},
    "initialView": "dayGridMonth", "locale": "ko", "height": "auto",
}

calendar(events=calendar_events, options=calendar_options, custom_css=calendar_css)
