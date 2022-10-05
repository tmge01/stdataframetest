#dataframe表示テスト(確認用)
import streamlit as st
import pandas as pd
df = pd.DataFrame({'国語テスト': [55, 96, 76, 82,67],
    '算数テスト': [44, 77, 54, 67, 100],
    '英語テスト': [67, 54, 76, 91, 68]})
st.subheader('テスト結果')
st.dataframe(df)