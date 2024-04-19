import streamlit as st
import time

st.title('Streamlit超入門')

st.write('プログレスバーの表示')


'Start!'

latast_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latast_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)



expander1 = st.expander('問い合わせ内容1')
expander1.write('問い合わせ内容1の解答')
expander2 = st.expander('問い合わせ内容2')
expander2.write('問い合わせ内容2の解答')
expander3 = st.expander('問い合わせ内容3')
expander3.write('問い合わせ内容3の解答')


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')





