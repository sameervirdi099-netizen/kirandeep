import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from mpl_toolkits.mplot3d import Axes3D
import requests
import base64

    
st.set_page_config(
    page_title="Social Media Usage",
    layout="wide"
)


def load_data(uploaded_file=None):
    if uploaded_file is None:
        try:
            return pd.read_csv("t.csv")
        except Exception:
            return None
    if uploaded_file.name.endswith(".csv"):
        return pd.read_csv(uploaded_file)
    if uploaded_file.name.endswith((".xls", ".xlsx")):
        return pd.read_excel(uploaded_file)
    return None

def style_fig(fig, title="", height=450):
    fig.update_layout(
        title=title,
        height=height,
        template="plotly_white",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    return fig

if "df" not in st.session_state:
    st.session_state.df = None
sample_df = load_data(None)
df = st.session_state.df if st.session_state.df is not None else sample_df
if df is None:
    st.error("No data available. Please upload a CSV or Excel dataset.")
    st.stop()
    
def get_base64(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(image_file):
    encoded = get_base64(image_file)

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )
    set_background("photo.png")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
st.markdown("""
<style>
.stApp{
    color:white;
}
.hero{
    background:linear-gradient(90deg,#3C096C,#7B2CBF,#9D4EDD);
    color:white;
    border-radius:20px;
    padding:40px;
}

.metric-card{
    background:#240046;
    border:1px solid #9D4EDD;
    border-radius:18px;
    padding:20px;
}
/* Hero Banner */
.hero{
    background: linear-gradient(135deg,#2563EB,#7C3AED);
    padding:40px;
    border-radius:20px;
    text-align:center;
    color:white;
    margin-bottom:25px;
    box-shadow:0px 10px 25px rgba(0,0,0,.35);
}

.hero h1{
    font-size:45px;
    margin-bottom:10px;
}

.hero p{
    font-size:20px;
    color:white;
}

/* KPI Cards */
.metric-card{
    background:rgba(255,255,255,.08);
    backdrop-filter:blur(15px);
    border:1px solid rgba(255,255,255,.2);
    border-radius:20px;
    padding:25px;
    text-align:center;
    transition:.3s;
    box-shadow:0 8px 20px rgba(0,0,0,.25);
}

.sidebar-title {
            text-align: center;
            font-size: 1.8rem;
            font-weight: 800;
            color: #F5F5F5;
            padding-top: 20px;
            padding-bottom: 10px;
            text-shadow: 1px 1px 4px rgba(0,0,0,0.6);
        }
        
        .sidebar-divider {
            border: none;
            border-top: 1px solid #3a3a3a;
            margin: 0px 10px 15px 10px;
        }
.metric-card:hover{
    transform:translateY(-8px);
    box-shadow:0 15px 30px rgba(37,99,235,.5);
}

.metric-title{
    color:#CBD5E1;
    font-size:18px;
}

.metric-value{
    color:white;
    font-size:34px;
    font-weight:bold;
}

/* Section Titles */

.section{
    color:white;
    font-size:32px;
    font-weight:700;
    margin-top:20px;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    
}

</style>
""",unsafe_allow_html=True)


with st.sidebar:
    st.markdown('<div class="sidebar-title">Teen Mental Health Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)
    
    opt = option_menu(
    "",
    options=["🏠Home","Dataset","📊Visualization","💡Insights","📌About"],
    icons=["house","file-text","activity","lightbulb","person"],
    default_index=0,
    styles={
            "container": {"padding": "0!important", "background-color": "#0b0a0a"},
            "icon": {"color": "#DFEDF3", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "4px 0px",
                "color": "#f5f5f5",
                "padding": "12px",
                "border-radius": "8px",
                "--hover-color": "#F5E1E1",
            },
       
        "nav-link-selected": {"background-color": "#060845", "color": "#ede5e5", "font-weight": "700"},
    
       }
    )       
    
if opt=="🏠Home":



    col1, col2 = st.columns([3, 1])

    with col1:
     st.markdown("""
    
    <h1 style="color:white; font-size:45px;">
        Teen Mental Health &<br>
        Social Media Usage Dashboard
        
    </h1>
    """, unsafe_allow_html=True)

    with col2:
     st.image("image 3.jpeg")
     st.markdown("""
        
        """, unsafe_allow_html=True)
   
    st.markdown(""" 
<p style="font-size:24px; line-height:1.8; color:white;">
Teen Mental Health & Social Media Usage Dashboard This interactive dashboard explores how social media habits may influence the mental health and daily lifestyle of teenagers.With the help of data visualization and statistical analysis, this project provides meaningful insights into screen time, sleep patterns, physical activity, and other factors related to teen well-being.

<br><br>
</p>
""", unsafe_allow_html=True)

    st.markdown("""
    
    <h1 style="color:white; font-size:45px;">
    🎯 Project Objectives
    
    </h1>
    """, unsafe_allow_html=True)
   

    col1,col2,col3,col4=st.columns(4)
    col1,col2,col3,col4=st.columns(4)
    c1,c2,c3=st.columns(3)

    with col1:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">💡Analyze teenagers social media usage patterns</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)

    with col2:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📋Compare usage across different social media platforms</div>
        <div class={len(df)}</div>
    
    
     </div>
    """, unsafe_allow_html=True)
     
    with col3:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📵Present findings through interactive charts and visualizations</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
    with col4:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🧠Analyzing the Impact of Social Media Usage on Teen Mental  Health </div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
     st.divider()
    # st.image("image 1.jpeg",use_column_width=True)
    st.markdown("""
    <h1 style="color:white; font-size:45px;">
    📊 Dashboard Overview
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    col1,col2,col3,col4=st.columns(4)
    col1,col2,col3,col4=st.columns(4)
    c1,c2,c3=st.columns(3)
    
    with col1:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📈interactive data filtering </div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
  
    with col2:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🧬Correlation heatmaps & graphs</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
    with col3:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">💡Key insights and conclusions</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
    with col4:
     st.markdown(f"""
     
    <div class="metric-card">
        <div class="metric-title">🧭Easy-to-use navigation and interface</div>
    <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
   
    st.write("""
    🌍 Why This Project Matters""")
    st.markdown(""" 
<p style="font-size:24px; line-height:1.8; color:white;">
Social media plays a significant role in the lives of teenagers. While it offers opportunities for communication, learning, and entertainment, excessive usage can affect sleep, physical activity, stress levels, and overall mental well-being. This dashboard helps users better understand these patterns through data-driven insights.
<br><br>
</p>
""", unsafe_allow_html=True)

    st.markdown("""
    
    <h1 style="color:white; font-size:45px;">
     🤳 Applications Used in this project
    </h1>
    """, unsafe_allow_html=True)

    col1,col2,col3,col4=st.columns(4)
    col1,col2,col3,col4=st.columns(4)
    c1,c2,c3=st.columns(3)
    
    with col1:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Python</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
     
    with col2:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Streamlit</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
    with col3:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Pandas</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
    with col4:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Seaborn</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
### 💡 Explore the Dashboard""")
    st.markdown("""
<p style="font-size:24px; line-height:1.8; color:white;">
Use the navigation menu on the left to explore the dataset, visualize trends, discover insights, and learn more about the relationship between social media usage and teen mental health.
"Understanding data today helps build healthier digital habits for tomorrow."    
<br><br>
</p>
""", unsafe_allow_html=True)
    st.markdown("---")

    col1,col2,col3,col4=st.columns(4)
    col1,col2,col3,col4=st.columns(4)

    with col1:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">👥 Total Teenagers</div>
        <div class="metric-value">{len(df)}</div>
    </div>
    """, unsafe_allow_html=True)

    with col2:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📱 Avg Usage</div>
        <div class="metric-value">{df['daily_social_media_hours'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)

    with col3:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">😴 Sleep</div>
        <div class="metric-value">{df['sleep_hours'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)

    with col4:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🏃 Activity</div>
        <div class="metric-value">{df['physical_activity'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)

    url = "https://assets9.lottiefiles.com/packages/lf20_qp1q7mct.json"

    animation = requests.get(url).json()

    st_lottie(animation, height=350)
    set_background("photo.png")

elif opt== "Dataset":
    
    
 
    st.markdown('<div class="page-subtitle"></div>', unsafe_allow_html=True)

    
    active_df = st.session_state.df if st.session_state.df is not None else load_data(None)

    if active_df is None:
        st.info("No dataset available yet — upload a CSV or Excel file above to get started.")
    else:
        if st.session_state.df is None:
            st.info("Showing the bundled sample dataset (`t.csv`). "
                    "Upload your own file above to replace it.")

        df = active_df
        n_rows_total = len(df)
        n_cols_total = df.shape[1]
        n_duplicates = int(df.duplicated().sum())
        n_missing = int(df.isna().sum().sum())

        st.markdown('<div class="section-heading-sm">📋 Dataset Summary</div>', unsafe_allow_html=True)
        k1, k2, k3, k4 = st.columns(4)
        with k1:
            st.markdown(f'<div class="kpi-card"><div class="kpi-value">{n_rows_total:,}</div>'
                        f'<div class="kpi-label">Rows</div></div>', unsafe_allow_html=True)
        with k2:
            st.markdown(f'<div class="kpi-card"><div class="kpi-value">{n_cols_total}</div>'
                        f'<div class="kpi-label">Columns</div></div>', unsafe_allow_html=True)
        with k3:
            st.markdown(f'<div class="kpi-card"><div class="kpi-value">{n_duplicates:,}</div>'
                        f'<div class="kpi-label">Duplicate Rows</div></div>', unsafe_allow_html=True)
        with k4:
            st.markdown(f'<div class="kpi-card"><div class="kpi-value">{n_missing:,}</div>'
                        f'<div class="kpi-label">Missing Values</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-heading-sm">📄 Dataset</div>', unsafe_allow_html=True)

        slider_max = max(n_rows_total, 1)
        default_rows = min(20, slider_max)
        n_rows = st.slider("Rows to preview", min_value=1, max_value=slider_max, value=default_rows)

        tab1, tab2 = st.tabs(["🔍 Preview", "🧬 Column Info"])

        with tab1:
        

        
            col_info = pd.DataFrame({
                "Column": df.columns,
                "Data Type": df.dtypes.astype(str).values,
                "Non-Null Count": df.notna().sum().values,
                "Null Count": df.isna().sum().values,
                "Unique Values": [df[c].nunique() for c in df.columns],
            })
            st.dataframe(col_info, width="stretch", hide_index=True)

        with tab2:
            default_col = "Platform" if "Platform" in df.columns else df.columns[0]
            vc_col = st.selectbox("Choose a column", options=df.columns.tolist(),
                                   index=df.columns.tolist().index(default_col))
            vc = df[vc_col].value_counts().reset_index()
            vc.columns = [vc_col, "Count"]
            st.dataframe(vc, width="stretch", hide_index=True)
            

            if df[vc_col].nunique() <= 40:
                vc_chart = vc.head(20).sort_values("Count")
                fig_vc = go.Figure(go.Bar(x=vc_chart["Count"], y=vc_chart[vc_col].astype(str), orientation="h"))
                fig_vc.update_xaxes(title_text="Count")
                fig_vc.update_yaxes(title_text="")
                st.plotly_chart(style_fig(fig_vc, f"Value Counts — {vc_col}", height=min(500, 100 + 28 * len(vc_chart))), width="stretch")
            else:
                st.caption(f"'{vc_col}' has {df[vc_col].nunique():,} unique values — too many to chart, showing the table above instead.")
    set_background("photo.png")         
elif opt=="📊Visualization":
    
    st.markdown("""
    
    <h1 style="color:white; font-size:45px;">
        Teen Mental Health &<br>
        Social Media Usage
        
        
    </h1>
    """, unsafe_allow_html=True)
    col1,col2,col3,col4=st.columns(4)
    col1,col2,col3,col4=st.columns(4)

    with col1:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">👥 Total Teenagers</div>
        <div class="metric-value">{len(df)}</div>
    </div>
    """, unsafe_allow_html=True)

    with col2:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📱 Avg Usage</div>
        <div class="metric-value">{df['daily_social_media_hours'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)

    with col3:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">😴 Sleep</div>
        <div class="metric-value">{df['sleep_hours'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)

    with col4:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🏃 Activity</div>
        <div class="metric-value">{df['physical_activity'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)
     
     st.divider()
     
     
    # col1.metric("👥 Total Teenagers",len(df))
    # col2.metric("📱 Avg Social Media Hours",round(df["daily_social_media_hours"].mean(),2))
    # col3.metric("😴 Avg Sleep Hours",round(df["sleep_hours"].mean(),2))
    # col4.metric("🏃 Avg Physical Activity",round(df["physical_activity"].mean(),2))
    t1,t2,t3,t4,t5=st.tabs(["📊Histogram","📈Line chart","💡Bar Chart","🧩Pie Chart","📌Graphs"])
    st.markdown("---")
    
    with t1:
        st.subheader("📊 Age Distribution")

        fig = px.histogram(
          df,
         x="age",
         nbins=15,
         color_discrete_sequence=px.colors.qualitative.Set1
         )

        st.plotly_chart(fig, use_container_width=True)

        st.divider()

        st.subheader("😴 Sleep Hours Distribution")

        fig = px.histogram(
           df,
        x="sleep_hours",
        nbins=12,
        color_discrete_sequence=["#636EFA"]
        )
        fig.update_layout(height=500,width=800,bargroupgap=0.15)

        st.plotly_chart(fig, use_container_width=True)
        
    with t2:
       st.subheader("📉 Average Stress by Age")

       avg = df.groupby("age")["stress_level"].mean().reset_index()

       fig = px.line(
        avg,
         x="age",
         y="stress_level",
         markers=True,
         color_discrete_sequence=["#00CC96"]
        )

       st.plotly_chart(fig, use_container_width=True)

       st.divider()

       st.subheader("📈 Average Sleep Hours by Age")

       avg_sleep = df.groupby("age")["sleep_hours"].mean().reset_index()

       fig = px.line(
        avg_sleep,
        x="age",
        y="sleep_hours",
        markers=True,
        color_discrete_sequence=["#EF553B"]
        )

       st.plotly_chart(fig, use_container_width=True)
    
    
    with t3:
    #   st.subheader("Gender Distribution
        st.subheader("📈 Gender Distribution")

        gender = df["gender"].value_counts().reset_index()
        gender.columns = ["gender","count"]

        fig = px.bar(
               gender,
             x="gender",
             y="count",
             color="gender",
             color_discrete_sequence=px.colors.qualitative.Set2
             )

        fig.update_layout(bargroupgap=0.50)

        st.plotly_chart(fig, use_container_width=True)
      
        st.divider()

        st.subheader("Charts")
        st.subheader("Stress Level Distribution ")
        fig,ax=plt.subplots()
        color_discrete_sequence=px.colors.qualitative.T10

        df["stress_level"].value_counts().plot(kind="bar",ax=ax)
        
        ax.set_xlabel("stress level")
        ax.set_ylabel("count")
        st.pyplot(fig)
    
    with t4:
      st.subheader("🥧 Gender Distribution")

      fig = px.pie(
         df,
          names="gender",
         color_discrete_sequence=px.colors.qualitative.Pastel
         )

      st.plotly_chart(fig, use_container_width=True)

      st.divider()

      st.subheader("🥧 Stress Level Distribution")

      fig = px.pie(
       df,
       names="stress_level",
       hole=0.4,
       color_discrete_sequence=px.colors.qualitative.Bold
       )

      st.plotly_chart(fig, use_container_width=True)
      
    with t5:
       st.subheader("🔥 Correlation Heatmap")

       corr = df.corr(numeric_only=True)

       fig = px.imshow(
          corr,
         text_auto=True,
         color_continuous_scale="RdBu_r"
        )     

       st.plotly_chart(fig, use_container_width=True)
       
       st.divider()
       
       st.subheader("🌞 Sunburst Chart")

       fig = px.sunburst(
         df,
          path=["gender","stress_level"],
         color="stress_level",
         color_continuous_scale="Turbo"
         )
        
       fig.update_layout(title="🌞 Gender-wise Stress Level Distribution",
         title_x=0.5
         )
       st.plotly_chart(fig, use_container_width=True)
       
       st.divider()

       st.subheader("🌳 Treemap of Gender and Stress Level")

       fig = px.treemap(
        df,
        path=["gender", "stress_level"],
        color="stress_level",
        color_continuous_scale="Viridis"
        )

       st.plotly_chart(fig, use_container_width=True)

       st.divider()

       st.subheader("🎻 Stress Level Distribution by Gender")

       fig = px.violin(
        df,
       x="gender",
       y="stress_level",
       color="gender",
       box=True,
       points="all"
       )

       st.plotly_chart(fig, use_container_width=True)

       st.divider()

       st.subheader("🔵 Age vs Stress Level")

       fig = px.scatter(
        df,
       x="age",
       y="stress_level",
       color="gender",
       size="stress_level",
       hover_data=["gender"]
       )

       st.plotly_chart(fig, use_container_width=True)

       st.divider()

       avg = df.groupby("age")["stress_level"].mean().reset_index()

       fig = px.area(
        avg,
       x="age",
       y="stress_level",
       color_discrete_sequence=["#00CC96"]
       )
       fig.update_layout(
        title="📈 Average Stress Level by Age",
        title_x=0.5
        )

       st.plotly_chart(fig, use_container_width=True)
    set_background("photo.png")
       
elif opt=="💡Insights":
    
  
    st.markdown("""
    <h2 style="font-size:40px;color:#7DF9FF;">
    📌 Major Findings from the Dataset
    </h2>
    """,unsafe_allow_html=True)

    st.success(f"""

### 📱 Social Media Usage

• The dataset contains information from **{len(df)} teenagers**.

• Teenagers spend an average of **{df['daily_social_media_hours'].mean():.2f} hours per day** on social media.

• Excessive daily usage indicates that social networking platforms have become an important part of teenagers' daily routine.

---

### 😴 Sleep Behaviour

• Average sleep duration is **{df['sleep_hours'].mean():.2f} hours per day**.

• Teenagers with longer screen time generally tend to sleep fewer hours.

• Healthy sleep is important for emotional stability, concentration, and academic performance.

---

### 🏃 Physical Activity

• Average physical activity is **{df['physical_activity'].mean():.2f} hours daily**.

• Teenagers who maintain regular physical activity generally demonstrate healthier lifestyle patterns.

• Physical exercise can help reduce stress and improve mental well-being.

""")
    col1,col2,col3,col4=st.columns(4)
    col1,col2,col3,col4=st.columns(4)

    with col1:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">👥 Total Teenagers</div>
        <div class="metric-value">{len(df)}</div>
    </div>
    """, unsafe_allow_html=True)

    with col2:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📱 Avg Usage</div>
        <div class="metric-value">{df['daily_social_media_hours'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)

    with col3:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">😴 Sleep</div>
        <div class="metric-value">{df['sleep_hours'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)

    with col4:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🏃 Activity</div>
        <div class="metric-value">{df['physical_activity'].mean():.1f} hrs</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h2 style="font-size:40px;color:#7DF9FF;">
    🧠 Mental Health Analysis
    </h2>
    """,unsafe_allow_html=True)

    st.info(f"""

### Average Stress Level
**{df['stress_level'].mean():.2f}/10**

Higher stress scores suggest that many teenagers experience emotional pressure related to academic life, social interactions, and digital engagement.

---

### Average Anxiety Level
**{df['anxiety_level'].mean():.2f}/10**

Anxiety levels indicate how frequently teenagers experience worry or nervousness in their daily lives.

---

### Average Addiction Level
**{df['addiction_level'].mean():.2f}/10**

The addiction score highlights the tendency of excessive social media dependence among teenagers.

""")

    st.markdown("""
    <h2 style="font-size:40px;color:#7DF9FF;">
    📊 Important Observations
    </h2>
    """,unsafe_allow_html=True)

    st.markdown("""

### 📱 1. Social Media Usage
- Most teenagers actively use social media every day.
- Higher screen time is one of the most common lifestyle characteristics observed.
- Digital platforms have become a major source of communication and entertainment.

---

### 😴 2. Sleep Pattern
- Increased social media usage is often associated with reduced sleep duration.
- Maintaining 8–10 hours of sleep is important for healthy growth.

---

### 🧠 3. Stress & Anxiety
- Teenagers with higher screen time generally report higher stress and anxiety scores.
- Mental well-being appears closely related to lifestyle habits.

---

### 🏃 4. Physical Activity
- Physical exercise varies considerably across teenagers.
- More active teenagers generally demonstrate healthier daily routines.

---

### 📚 5. Academic Performance
- Balanced digital habits and sufficient sleep contribute positively to academic performance.

---

### 🔍 6. Correlation Analysis
- Social media usage shows positive relationships with stress and anxiety.
- Sleep hours show negative relationships with depression and stress.
- Correlation represents association, **not proof of causation**.

""")

    st.markdown("""
    <h2 style="font-size:40px;color:#7DF9FF;">
    🎯 Recommendations
    </h2>
    """,unsafe_allow_html=True)

    st.success("""

✅ Limit unnecessary daily screen time.

✅ Maintain 8–10 hours of quality sleep.

✅ Exercise regularly.

✅ Take digital breaks.

✅ Encourage healthy online habits.

✅ Spend more time in outdoor and social activities.

✅ Parents and teachers should monitor excessive smartphone usage.

""")

    st.markdown("""
    <h2 style="font-size:40px;color:#7DF9FF;">
    📌 Final Conclusion
    </h2>
    """,unsafe_allow_html=True)

    st.info("""

This dashboard provides a comprehensive analysis of how teenagers' social media usage relates to different aspects of mental health and lifestyle.

The visualizations reveal meaningful patterns between screen time, sleep duration, stress, anxiety, addiction, physical activity, and academic performance.

Although the dataset does not establish direct cause-and-effect relationships, it clearly highlights behavioural trends that can help students, educators, parents, healthcare professionals, and researchers better understand the influence of digital habits on adolescent well-being.

The findings emphasize the importance of maintaining a healthy balance between technology usage, physical activity, proper sleep, and overall mental health.

""")


    url="https://assets2.lottiefiles.com/packages/lf20_jtbfg2nb.json"

    animation=requests.get(url).json()

    st_lottie(animation,height=250)
    set_background("photo.png")   
elif opt=="📌About":

    st.markdown("""
    <h1 style="text-align:center;
               color:#00E5FF;
               font-size:52px;
               font-weight:bold;">
    📌 About This Project
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""

<div style="font-size:24px; line-height:1.9;">

The <b>Teen Mental Health & Social Media Usage Dashboard</b> is an interactive
data visualization project developed to analyze how teenagers' social media
usage relates to their mental health, lifestyle, and daily activities.

The dashboard transforms raw survey data into meaningful visual insights,
allowing users to explore behavioural patterns using interactive charts,
graphs, statistical summaries, and performance indicators.

The project helps users understand how screen time, sleep duration,
physical activity, anxiety, stress, addiction, and academic performance
are interconnected.

</div>

""",unsafe_allow_html=True)

    st.divider()

    st.markdown("""
<h2 style="font-size:40px;color:#7DF9FF;">
🎯 Project Objectives
</h2>
""",unsafe_allow_html=True)

    st.markdown("""

<div style="font-size:24px; line-height:2;">

✔ Analyze teenagers' social media usage patterns.

✔ Study mental health indicators such as stress, anxiety, and addiction.

✔ Explore relationships between screen time and sleep quality.

✔ Compare behavioural patterns across genders.

✔ Visualize the dataset using interactive charts.

✔ Generate meaningful insights through statistical analysis.

✔ Promote awareness of healthy digital habits.

</div>

""",unsafe_allow_html=True)

    st.divider()

    st.markdown("""
<h2 style="font-size:40px;color:#7DF9FF;">
📂 Dataset Information
</h2>
""",unsafe_allow_html=True)

    st.markdown("""

<div style="font-size:24px; line-height:2;">

The dataset contains information related to:

• Age

• Gender

• Daily Social Media Hours

• Platform Usage

• Sleep Hours

• Screen Time Before Sleep

• Academic Performance

• Physical Activity

• Social Interaction

• Stress Level

• Anxiety Level

• Addiction Level

• Depression Label

</div>

""",unsafe_allow_html=True)

    st.divider()

    st.markdown("""
<h2 style="font-size:40px;color:#7DF9FF;">
⚙ Technologies Used
</h2>
""",unsafe_allow_html=True)
    col1,col2,col3,col4=st.columns(4)
    col1,col2,col3,col4=st.columns(4)
    c1,c2,c3=st.columns(3)
    
    with col1:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Python</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
     
    with col2:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Streamlit</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
    with col3:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Pandas</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
     
    with col4:
     st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Seaborn</div>
        <div class={len(df)}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""

<div style="font-size:24px; line-height:2;">

🐍 Python

📊 Pandas

📈 Plotly

📉 Matplotlib

🎨 Seaborn

🚀 Streamlit

💻 VS Code

</div>

""",unsafe_allow_html=True)

    st.divider()

    st.markdown("""
<h2 style="font-size:40px;color:#7DF9FF;">
✨ Dashboard Features
</h2>
""",unsafe_allow_html=True)

    st.markdown("""

<div style="font-size:24px; line-height:2;">

✔ Professional User Interface

✔ Interactive Plotly Charts

✔ Dynamic KPI Cards

✔ Correlation Heatmap

✔ Dataset Explorer

✔ Multiple Data Visualizations

✔ Statistical Summaries

✔ Interactive Insights

✔ User-Friendly Navigation

✔ Responsive Layout

</div>

""",unsafe_allow_html=True)

    st.divider()

    st.markdown("""
<h2 style="font-size:40px;color:#7DF9FF;">
🎯 Target Audience
</h2>
""",unsafe_allow_html=True)

    st.markdown("""

<div style="font-size:24px; line-height:2;">

• Students

• Teachers

• Parents

• Researchers

• Healthcare Professionals

• Educational Institutions

• Policy Makers

</div>

""",unsafe_allow_html=True)

    st.divider()

    st.markdown("""
<h2 style="font-size:40px;color:#7DF9FF;">
👨‍💻 Developed By
</h2>
""",unsafe_allow_html=True)

    st.markdown("""

<div style="font-size:28px; line-height:2;">

<b>Amit Lagah</b>

Data Science Student

Python Developer

Streamlit Dashboard Developer

Data Visualization Enthusiast

</div>

""",unsafe_allow_html=True)

    st.success("""

### 🌍 Final Note

Understanding teenagers' digital behaviour is essential for promoting healthier online habits and improving mental well-being.

This dashboard transforms complex data into meaningful visual stories that support informed decision-making and encourage responsible social media usage.

""")
    set_background("photo.png")