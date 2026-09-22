import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------------------------------
# 기본 설정
# ----------------------------------------------------------------------------
st.set_page_config(page_title="영화 데이터 그래프 도감 2 - 분포와 관계", layout="wide")
st.title("영화 데이터 그래프 도감 2 - 분포와 관계")

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)

    # 열 이름을 코드에서 다루기 쉬운 이름으로 정리
    df = df.rename(
        columns={
            "movieCd": "movie_code",
            "movieNm": "movie_name",
            "openDt": "open_date",
            "genre": "genre",
            "nation": "nation",
            "first_scrn": "first_screens",
            "first_show": "first_showings",
            "first_week_audi": "first_week_audience",
            "total_audi": "total_audience",
            "days_in_top10": "days_in_top10",
        }
    )

    # 여덟 자리 숫자 날짜(YYYYMMDD) -> datetime
    df["open_date"] = pd.to_datetime(df["open_date"].astype(str), format="%Y%m%d")

    # 장르가 세로막대 기호(|)로 여러 개 적힌 경우 첫 번째 장르만 사용
    df["genre"] = df["genre"].astype(str).str.split("|").str[0].str.strip()

    return df


df = load_data()

st.divider()

# ----------------------------------------------------------------------------
# 구역 1. 장르별 영화 편수 분포
# ----------------------------------------------------------------------------
st.header("1. 장르별 영화 편수")

genre_counts = df["genre"].value_counts().reset_index()
genre_counts.columns = ["genre", "count"]

fig1 = px.pie(
    genre_counts,
    names="genre",
    values="count",
    hole=0.5,
    title="장르별 영화 편수",
)
fig1.update_traces(
    hovertemplate="장르: %{label}<br>편수: %{value}편<br>비율: %{percent}<extra></extra>"
)

st.plotly_chart(fig1, use_container_width=True)

st.info("📌 이 그래프로 알 수 있는 것: (여기에 해석 문구를 입력하세요)")

st.divider()

# ----------------------------------------------------------------------------
# 구역 2. (다음 그래프를 위한 자리)
# ----------------------------------------------------------------------------
st.header("2. (다음 그래프)")
st.caption("여기에 다음 그래프를 추가할 예정입니다.")

st.divider()

# ----------------------------------------------------------------------------
# 구역 3. (다음 그래프를 위한 자리)
# ----------------------------------------------------------------------------
st.header("3. (다음 그래프)")
st.caption("여기에 다음 그래프를 추가할 예정입니다.")
