# 导入所需第三方库：streamlit用于搭建页面，pandas处理表格数据，datetime处理时间
import streamlit as st
import pandas as pd
from datetime import datetime

# 页面基础配置：设置标题、布局为宽屏、侧边栏默认折叠
st.set_page_config(
    page_title="学生数字档案",  # 浏览器标签页标题
    layout="wide",  # 宽布局（适配多列展示）
    initial_sidebar_state="collapsed"  # 初始隐藏侧边栏
)

# 自定义CSS样式：适配深色主题，优化组件视觉效果
st.markdown("""
    <style>
    .main {
        background-color: #1E1E1E;  /* 页面背景色：深灰色 */
        color: #FFFFFF;  /* 全局文字色：白色 */
    }
    .stProgress > div > div > div > div {
        background-color: #2196F3;  /* 进度条颜色：蓝色 */
    }
    .success {
        color: #4CAF50;  /* 成功状态文字色：绿色 */
    }
    .warning {
        color: #FFC107;  /* 警告状态文字色：黄色 */
    }
    .danger {
        color: #F44336;  /* 危险状态文字色：红色 */
    }
    .code-block {
        background-color: #FFFFFF;  /* 代码块背景色：白色 */
        color: #000000;  /* 代码文字色：黑色 */
        padding: 15px;  /* 内边距：15px（避免文字贴边） */
        border-radius: 5px;  /* 圆角：5px（优化视觉） */
        font-family: monospace;  /* 字体：等宽字体（适合代码展示） */
        border: 1px solid #EEEEEE;  /* 边框：浅灰色细边框（区分边界） */
        font-size: 14px;  /* 字体大小：14px（保证可读性） */
    }
    </style>
""", unsafe_allow_html=True)  # 允许渲染HTML/CSS（streamlit默认禁用，需显式开启）


# ========== 1. 标题区域 ==========
st.title("学生 小陆 - 数字档案")  # 页面主标题
st.markdown("---")  # 分割线（视觉分隔不同模块）


# ========== 2. 基础信息模块 ==========
with st.container():  # 创建容器（用于分组组件，方便样式管理）
    st.subheader("📋 基础信息")  # 模块子标题（加图标增强视觉）
    col1, col2, col3 = st.columns(3)  # 分成3列布局（并列展示信息）
    with col1:  # 第一列：展示学生ID和性别
        st.write("学生ID: NO2023-001")  # 输出学生唯一标识
        st.write("性别: 男")  # 输出学生性别
    with col2:  # 第二列：展示注册时间和精神状态
        st.write("注册时间: 2023-09-01")  # 输出注册日期
        st.write("精神状态: ✅ 正常")  # 输出状态（带图标直观展示）
    with col3:  # 第三列：展示当前等级
        st.write("当前等级: 安全 (基础)")  # 输出学生当前权限/等级
st.markdown("---")  # 分割线


# ========== 3. 技能矩阵模块 ==========
with st.container():  # 创建容器分组
    st.subheader("💻 技能矩阵")  # 模块子标题
    # 定义技能数据：包含技能名称、掌握度、变化趋势
    skill_data = {
        "技能": ["C++", "Python", "Java"],  # 技能名称列表
        "掌握度": ["95%", "87%", "68%"],  # 各技能掌握百分比
        "变化": ["↑5%", "↓2%", "↓10%"]  # 相比上次的变化（上升/下降）
    }
    skill_df = pd.DataFrame(skill_data)  # 转换为DataFrame（方便后续处理）
    
    # 用3列布局分别展示每个技能的详情
    cols = st.columns(3)  # 创建3列
    for i, col in enumerate(cols):  # 循环遍历每一列（i为索引，col为列对象）
        with col:  # 在当前列中添加内容
            st.write(f"**{skill_df['技能'][i]}**")  # 输出技能名称（加粗突出）
            # 进度条：将百分比字符串转为浮点数（如"95%"→0.95）
            st.progress(float(skill_df['掌握度'][i].replace('%', ''))/100)
            st.write(f"变化: {skill_df['变化'][i]}")  # 输出变化趋势
st.markdown("---")  # 分割线


# ========== 4. Streamlit课程进度 ==========
with st.container():  # 创建容器分组
    st.subheader("📚 Streamlit课程进度")  # 模块子标题
    st.progress(0.20)  # 进度条：20%进度（参数范围0-1）
st.markdown("---")  # 分割线


# ========== 5. 任务日志模块 ==========
with st.container():  # 创建容器分组
    st.subheader("📝 任务日志")  # 模块子标题
    # 定义任务日志数据：日期、任务名称、状态、难度
    task_data = {
        "日期": ["2025-10-01", "2025-11-01", "2025-12-01"],  # 任务创建/截止日期
        "任务": ["学生成绩系统", "课程管理系统", "教师信息录入"],  # 任务名称
        "状态": ["✅ 完成", "● 进行中", "❌ 未完成"],  # 任务状态（带图标）
        "难度": ["★★☆☆☆", "★★★☆☆", "★★★★☆"]  # 任务难度（星级表示）
    }
    task_df = pd.DataFrame(task_data)  # 转换为DataFrame（用于表格展示）
    # 展示表格：隐藏索引列，自定义列宽和说明
    st.dataframe(
        task_df,  # 要展示的DataFrame数据
        hide_index=True,  # 隐藏默认的索引列（更简洁）
        column_config={  # 自定义列配置
            "状态": st.column_config.TextColumn(
                width="small",  # 列宽：小（节省空间）
                help="任务当前状态"  # 鼠标悬浮提示
            ),
            "难度": st.column_config.TextColumn(
                width="small"  # 难度列设为小宽度
            )
        }
    )
st.markdown("---")  # 分割线


# ========== 6. 最新代码成果模块 ==========
with st.container():  # 创建容器分组
    st.subheader("💻 最新代码成果")  # 模块子标题
    # 定义要展示的代码内容（使用三引号保留格式）
    code_content = '''
def main():
    # 创建画布：宽11英寸，高1英寸（适配"ACCESS GRANTED"文字展示）
    plt.figure(figsize=(11,1))
    # 隐藏坐标轴（只展示文字，不显示图表边框/刻度）
    plt.axis('off')
    # 在画布中央添加文字："ACCESS GRANTED"（授权通过）
    plt.text(0.5, 0.5, 'ACCESS GRANTED', 
             fontsize=20,  # 字体大小20号
             ha='center',  # 水平居中
             va='center')  # 垂直居中
    # 保存图片到本地，文件名为result.png
    plt.savefig('result.png')
    # 在streamlit侧边栏展示保存的图片
    st.sidebar.image('result.png')
    '''
    # 用自定义的code-block样式渲染代码（白色背景+黑色文字）
    st.markdown(f"<div class='code-block'>{code_content}</div>", unsafe_allow_html=True)
st.markdown("---")  # 分割线


# ========== 7. 系统消息模块 ==========
with st.container():  # 创建容器分组
    st.subheader("📢 系统消息")  # 模块子标题
    st.write("✅ 下一个任务目标已解锁。")  # 系统通知：任务解锁
    st.write("📌 任务: 课程管理系统")  # 指定新任务名称
    # 输出任务时间：固定为2023-12-12 12:43:48（datetime构造时间对象）
    st.write(f"🕒 时间: {datetime(2023, 12, 12, 12, 43, 48)}")
    st.write("系统状态: 在线 | 授权等级: 已认证")  # 系统当前状态和授权信息
