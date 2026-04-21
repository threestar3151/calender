import streamlit as st
from streamlit_calendar import calendar

st.set_page_config(page_title="GS25 업무 스케줄", layout="wide")

st.title("🗓️ GS25 4부문 취합 및 마감 스케줄")

# 올려주신 이미지 내용을 바탕으로 [담당자 / 취합방법 / 빨간박스 회신주체]를 반영했습니다.
# 마감일이 당일까지 꽉 차게 보이도록 종료일(end)을 +1일 하여 세팅했습니다.
# 눈의 피로를 덜어주는 차분한(Muted) 파스텔톤 색상으로 구분했습니다.
# 시작일(start)을 '마감일'로 설정하고, 종료일(end)은 삭제하여 당일에만 깔끔하게 표시됩니다.
calendar_events = [
    {"title": "📢 [마케팅] 토스 설치 (최수민 / 엑셀 / 부문지원팀)", "start": "2026-04-30", "color": "#D98880"},
    {"title": "🧼 [지원] 선도위생 제외 (이충언 / 엑셀 / 지역팀)", "start": "2026-04-27", "color": "#7FB3D5"},
    {"title": "🥤 [MD] OSC 장려금 (이종혁 / 엑셀 / 부문지원팀)", "start": "2026-04-28", "color": "#7DCEA0"},
    {"title": "🛒 [지원] 장보기 추가 (양희진 / 시스템 / OFC개별)", "start": "2026-04-27", "color": "#C39BD3"},
    {"title": "🛵 [O4O] 배달/픽업 (박정은 / OFC포탈 / OFC개별)", "start": "2026-04-27", "color": "#F0B27A"},
    {"title": "🍗 [MD] 치킨25 소모품 (최원필 / OFC포탈 / OFC개별)", "start": "2026-04-30", "color": "#73C6B6"},
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

# 사이드바에도 이미지의 디테일한 내용을 업데이트했습니다.
st.sidebar.header("📋 세부 업무 가이드")
st.sidebar.write("**1. 토스 페이스페이 설치** (마케팅_제2026-004호)")
st.sidebar.caption("- 담당자: 최수민 매니저 \n- 기한: 4/30(목) \n- 방법: 엑셀 취합 \n- 주체: 부문지원팀 (빨간박스 기준)")

st.sidebar.write("**2. 05월 선도위생 평가제외점** (지원_제2026-021호)")
st.sidebar.caption("- 담당자: 이충언 매니저 \n- 기한: 4/27(월) \n- 방법: 엑셀 취합 \n- 주체: 지역팀 (빨간박스 기준)")

st.sidebar.write("**3. 음료 전용 엔드형 OSC 장려금** (MD_제2026-020호)")
st.sidebar.caption("- 담당자: 이종혁 매니저 \n- 기한: 4/28(화) \n- 방법: 엑셀 취합 \n- 주체: 부문지원팀 (빨간박스 기준)")

st.sidebar.write("**4. 5월 장보기 대상점 추가** (지원 022호)")
st.sidebar.caption("- 담당자: 양희진 매니저 \n- 기한: 4/27(월) \n- 방법: 점포경영시스템 취합 \n- 주체: OFC개별")

st.sidebar.write("**5. 배달/픽업 정기 취합** (O4O 014호)")
st.sidebar.caption("- 담당자: 박정은 매니저 \n- 기한: 4/27(월) \n- 방법: OFC포탈 \n- 주체: OFC개별")

st.sidebar.write("**6. 치킨25 3월 소모품 소급** (MD 018호)")
st.sidebar.caption("- 담당자: 최원필 매니저 \n- 기한: 4/30(목) \n- 방법: OFC포탈 \n- 주체: OFC개별")
