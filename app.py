import streamlit as st
from streamlit_calendar import calendar

# 1. 모바일에서 좌우 여백을 최소화하도록 설정
st.set_page_config(page_title="GS25 업무 스케줄", layout="wide")

st.title("🗓️ GS25 4부문 취합 및 마감 스케줄")

# 2. 모바일/PC 통합 디자인 마법 (반응형 CSS)
calendar_css = """
/* 기본 줄바꿈 설정 */
.fc-event-main {
    white-space: pre-wrap !important;
    word-wrap: break-word !important;
    line-height: 1.3 !important;
    padding: 2px !important;
}

/* 모바일 화면(폭 768px 이하)일 때 폰트 크기 및 높이 조절 */
@media (max-width: 768px) {
    .fc-header-toolbar {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }
    .fc-toolbar-title {
        font-size: 1.1em !important;
    }
    .fc-event-title {
        font-size: 0.7em !important;  /* 모바일에서 폰트 조금 더 작게 */
    }
    .fc-daygrid-day-number {
        font-size: 0.8em !important;
    }
}
"""

# 3. 누적 데이터 리스트 (기존 내용 유지)
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

# 4. 달력 설정 (모바일용 '리스트 뷰' 버튼 추가)
calendar_options = {
    "headerToolbar": {
        "left": "prev,next today",
        "center": "title",
        "right": "dayGridMonth,listMonth"  # 'listMonth' 버튼이 모바일에서 꿀기능입니다!
    },
    "initialView": "dayGridMonth",
    "locale": "ko",
    "height": "auto",                  # 화면 높이에 맞춰 자동 조절
    "handleWindowResize": True,         # 화면 크기 변경 시 자동 대응
}

# 최종 달력 실행
calendar(
    events=calendar_events, 
    options=calendar_options, 
    custom_css=calendar_css
)

st.info("💡 모바일에서 화면이 좁다면 우측 상단의 'list' 버튼을 눌러보세요! 리스트 형태로 깔끔하게 보입니다.")
