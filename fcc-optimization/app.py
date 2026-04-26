#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd

# 设置页面
st.set_page_config(
    page_title="催化裂化装置优化研究",
    page_icon="🏭",
    layout="wide"
)

# 标题
st.title("🏭 基于机器学习的催化裂化装置性能预测与多目标优化研究")
st.markdown("### 青岛科技大学本科毕业设计 · 葛小乐 2206040104")

# 侧边栏导航
with st.sidebar:
    st.header("导航")
    page = st.radio("选择页面", [
        "📊 研究成果展示",
        "📋 帕累托前沿解集",
        "📈 优化结果分析",
        "ℹ️ 论文信息"
    ])

# 研究成果展示
if page == "📊 研究成果展示":
    st.header("主要研究成果")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("数据样本量", "42,784 条")
        st.metric("模型 R² 值", "> 0.99")
    
    with col2:
        st.metric("特征筛选", "19 → 7 个")
        st.metric("预测误差", "< 0.11%")
    
    with col3:
        st.metric("效益提升", "9.2%")
        st.metric("CO₂ 减排", "14.5%")
    
    st.markdown("---")
    
    st.subheader("核心创新点")
    st.markdown("""
    1. **LightGBM-Lasso 级联特征选择**：从 19 个操作参数中筛选出 7 个关键参数
    2. **多模型融合策略**：BP 神经网络为主，XGBoost 修正关键指标
    3. **NSGA-II 多目标优化**：同时优化经济效益和碳排放
    4. **可视化决策系统**：为操作人员提供直观的决策支持
    """)

# 帕累托前沿解集
elif page == "📋 帕累托前沿解集":
    st.header("帕累托前沿解集")
    
    # 典型解数据（来自你的论文）
    solutions = pd.DataFrame({
        '方案': ['P1 (平衡型)', 'P2 (高价值)', 'P3 (低排放)', 'P4 (高价值)', 'P5 (平衡型)'],
        '反应温度(℃)': [512.3, 518.7, 505.6, 519.2, 507.8],
        '催化剂微反活性(wt%)': [52.1, 50.4, 54.3, 49.2, 53.0],
        '原料比重(g/cm³)': [0.895, 0.902, 0.887, 0.908, 0.892],
        '产品价值(元/h)': [30820, 31560, 29840, 32180, 31290],
        'CO₂排放(t/h)': [72.4, 78.6, 68.1, 83.4, 74.8],
        '效益比(元/t CO₂)': [425.6, 401.5, 438.2, 385.9, 418.3]
    })
    
    st.subheader("典型帕累托最优解")
    st.dataframe(solutions, use_container_width=True)
    
    st.subheader("帕累托前沿示意图")
    
    # 使用 Streamlit 原生折线图
    chart_data = pd.DataFrame({
        'CO₂排放(t/h)': [68.1, 72.4, 74.8, 78.6, 83.4],
        '产品价值(元/h)': [29840, 30820, 31290, 31560, 32180]
    })
    
    st.line_chart(chart_data, x='CO₂排放(t/h)', y='产品价值(元/h)')
    
    st.info("""
    **解读：**
    - **P3 方案**：低碳排放型，适合碳配额紧张时期
    - **P4 方案**：高经济效益型，适合追求利润最大化时期
    - **P1/P5 方案**：平衡型，兼顾经济与环保
    """)

# 优化结果分析
elif page == "📈 优化结果分析":
    st.header("优化结果分析")
    
    tab1, tab2, tab3 = st.tabs(["🎯 决策建议", "📊 约束满足情况", "🔍 验证结果"])
    
    with tab1:
        st.subheader("生产决策建议")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**高经济效益型（P4）**")
            st.success("""
            - 反应温度：519.2℃
            - 催化剂活性：49.2 wt%
            - 原料比重：0.908 g/cm³
            - 产品价值：32,180 元/h
            - CO₂ 排放：83.4 t/h
            """)
        
        with col2:
            st.markdown("**低碳排放型（P3）**")
            st.success("""
            - 反应温度：505.6℃
            - 催化剂活性：54.3 wt%
            - 原料比重：0.887 g/cm³
            - 产品价值：29,840 元/h
            - CO₂ 排放：68.1 t/h
            """)
    
    with tab2:
        st.subheader("约束条件满足情况")
        
        constraints = pd.DataFrame({
            '约束指标': ['汽油 RON', '汽油干点', '液化气 C5 体积比', '汽油烯烃含量', '操作参数范围'],
            '要求': ['≥ 92', '≤ 215℃', '≤ 2.5 vol%', '≤ 25 vol%', '在设定范围内'],
            '满足情况': ['✅ 满足', '✅ 满足', '✅ 满足', '⚠️ 7% 超限', '✅ 满足'],
            '备注': ['最小值 92.5', '最大值 214.5℃', '最大值 2.06 vol%', '最大超限 0.3%', '全部在范围内']
        })
        
        st.dataframe(constraints, use_container_width=True)
    
    with tab3:
        st.subheader("模型验证结果")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("效益比平均误差", "2.31%")
            st.metric("最高误差组", "3.0~4.2%")
        
        with col2:
            st.metric("约束满足率", "97%")
            st.metric("汽油烯烃超限率", "7%")
            
        with col3:
            st.metric("验证样本数", "100 个")
            st.metric("数据来源", "仿真软件")

# 论文信息
elif page == "ℹ️ 论文信息":
    st.header("论文详细信息")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 基本信息
        - **题目**：基于机器学习的催化裂化装置性能预测与多目标优化研究
        - **学生**：葛小乐
        - **学号**：2206040104
        - **专业**：应用统计学
        - **班级**：统计 221 班
        - **指导教师**：刘祥鹏
        - **完成日期**：2026 年 5 月 1 日
        """)
    
    with col2:
        st.markdown("""
        ### 技术路线


# In[ ]:





# In[ ]:




