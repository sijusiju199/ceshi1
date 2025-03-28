import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")


if st.button("点我一下"):
    st.write("你成功点击了按钮！🎉")
if st.button("点我二下"):
    st.write("你成功第二次点击了按钮！🎉")    

def rxl(io,sheet_name=0,header=0,names=None,index_col=None,usecols=None,dtype=None):#读表函数，io='xl/表名.xlsx'
    df=pd.read_excel(io=io,sheet_name=sheet_name,header=header,
                     names=names,index_col=index_col,usecols=usecols,dtype=dtype)
    return df

uploaded_file=st.file_uploader("上传一个CSV文件",type=["csv"])
if uploaded_file:
    df=pd.read_csv(uploaded_file)
    st.write(df)
    
uploaded_file=st.file_uploader("上传一个CSV文件",type=["xlsx"])
if uploaded_file:
    df=pd.read_excel(uploaded_file)
    st.write(df)

col1, col2 = st.columns(2)

col1.write("这是左侧内容")
col2.write("这是右侧内容")

st.set_page_config(page_title="我的多页面应用",page_icon="📚")

st.title("欢迎来到我的 Streamlit 多页面应用！ 🎉")
st.write("请使用左侧导航栏选择页面")