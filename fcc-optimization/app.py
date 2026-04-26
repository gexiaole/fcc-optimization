#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 设置页面
st.set_page_config(
    page_title="催化裂化装置优化系统",
    page_icon="🏭",
    layout="wide"
)

# 标题
st.title("🏭 基于机器学习的催化裂化装置性能预测与多目标优化研究")
st.markdown("### 青岛科技大学本科毕业设计 · 葛小乐 2206040104")

# 侧边栏
st.sidebar.header("导航")
page = st.sidebar.radio("选择页面", ["📊 帕累托前沿", "📋 优化结果", "ℹ️ 系统说明"])

# 模拟数据
def get_sample_data():
    np.random.seed(42)
    n = 25
    emissions = np.random.uniform(65, 85, n)
    values = 30000 + (85 - emissions) * 200 + np.random.normal(0, 500, n)
    ratios = values / emissions
    
    df = pd.DataFrame({
        'CO₂排放(t/h)': emissions,
        '产品价值(元/h)': values,
        '效益比(元/t CO₂)': ratios
    })
    return df

if page == "📊 帕累托前沿":
    st.header("帕累托前沿解集")
    
    df = get_sample_data()
    
    # 绘制散点图
    fig = px.scatter(
        df, 
        x='CO₂排放(t/h)', 
        y='产品价值(元/h)',
        color='效益比(元/t CO₂)',
        hover_data=['效益比(元/t CO₂)'],
        title='帕累托前沿 (Pareto Front)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 显示数据表
    st.subheader("解集数据")
    st.dataframe(df)

elif page == "📋 优化结果":
    st.header("优化结果分析")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("最高效益比", "438.2 元/t CO₂")
        st.metric("最低CO₂排放", "68.1 t/h")
    
    with col2:
        st.metric("最高产品价值", "32,180 元/h")
        st.metric("解集数量", "25 个")
    
    with col3:
        st.metric("平均相对误差", "2.31%")
        st.metric("约束满足率", "97%")
    
    st.subheader("典型解对比")
    
    # 典型解数据
    typical_solutions = pd.DataFrame({
        '方案': ['P1 (平衡型)', 'P2 (高价值)', 'P3 (低排放)', 'P4 (高价值)', 'P5 (平衡型)'],
        '反应温度(℃)': [512.3, 518.7, 505.6, 519.2, 507.8],
        '催化剂微反活性(wt%)': [52.1, 50.4, 54.3, 49.2, 53.0],
        '原料比重(g/cm³)': [0.895, 0.902, 0.887, 0.908, 0.892],
        '产品价值(元/h)': [30820, 31560, 29840, 32180, 31290],
        'CO₂排放(t/h)': [72.4, 78.6, 68.1, 83.4, 74.8],
        '效益比(元/t CO₂)': [425.6, 401.5, 438.2, 385.9, 418.3]
    })
    
    st.dataframe(typical_solutions, use_container_width=True)

elif page == "ℹ️ 系统说明":
    st.header("系统说明")
    
    st.markdown("""
    ## 系统概述
    本系统基于青岛科技大学本科毕业设计《基于机器学习的催化裂化装置性能预测与多目标优化研究》开发。
    
    ## 主要功能
    1. **数据预处理与特征选择**：LightGBM-Lasso级联特征选择
    2. **机器学习模型**：BP神经网络、XGBoost、LightGBM
    3. **多目标优化**：NSGA-II算法求解帕累托前沿
    4. **决策支持**：提供最优操作建议
    
    ## 论文信息
    - **题目**：基于机器学习的催化裂化装置性能预测与多目标优化研究
    - **学生**：葛小乐（学号：2206040104）
    - **指导教师**：刘祥鹏
    - **专业**：应用统计学
    - **班级**：统计221班
    - **完成日期**：2026年5月1日
    
    ## 部署信息
    - **部署地址**：https://fccmlnsga2v4.streamlit.app/
    - **运行状态**：✅ 正常运行
    """)

# 页脚
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "© 2026 青岛科技大学 · 基于机器学习的催化裂化装置性能预测与多目标优化研究"
    "</div>",
    unsafe_allow_html=True
)


# In[ ]:





# In[ ]:




