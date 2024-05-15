#モジュール
import streamlit as st
from components import header, top, service, team, portfolio, footer

#ページ設定
st.set_page_config(
    page_title="RK Technology", 
    page_icon="./img/logo.jpeg", 
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={
         'Get Help': 'https://www.google.com',
         'Report a bug': "https://www.google.com",
         'About': """
         ##RK Technology
         あああああああああああああああああああああ
         """
     })

#ヘッダー
language = header()

# 1ページ目: キャッチフレーズと画像
top(language)

# 2ページ目: 提供サービス
service(language)

# 3ページ目: チームメンバー
team(language)

# 4ページ目: ポートフォリオ
portfolio(language)

# 5ページ目: コンタクト
footer(language)

#footer
st.write("© 2024 RK Technology")
urlIllust = "https://storyset.com/"
st.caption("[Illustration by Storyset](%s)" % urlIllust)