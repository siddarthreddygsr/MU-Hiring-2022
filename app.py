import streamlit as st 
import pandas as pd
import numpy as np


st.set_page_config(page_title = 'Dashboard', 
    layout='wide',
    page_icon='💹')

### top row 
st.markdown('## Problem Statement')
st.markdown('>> It is evident through the given data that it is key to organise events managed by various clubs in a Univeristy in order for smooth functioning of the same.')
st.markdown('## Solution')
st.markdown('>> An interactive dashboard for the same would help students, organisers and the University management manage finances, plan and execute these events at ease. ')
st.markdown("## Target Market")

first_kpi, second_kpi, third_kpi = st.columns(3)


with first_kpi:
    st.markdown("**Market Size**")
    number1=522
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

# with second_kpi:
#     st.markdown("**Psychographics**")
#     st.caption = ("parents, students, school management")
#     st.markdown(f"<h1 style='text-align: center; color: red;'>{st}</h1>", unsafe_allow_html=True)

# with third_kpi:
#     st.markdown("**Demographics**")
#     number3 = 333 
#     st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True)


### second row 

st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## Market Segmentation")

first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.columns(6)


with first_kpi:
    st.markdown("** School Management **")
    # number1 = 11
    # st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with second_kpi:
    st.markdown("**Students**")
    number2 = 501
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number2}</h1>", unsafe_allow_html=True)

with third_kpi:
    st.markdown("**Parents**")
    number3 = 1024
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True)

with fourth_kpi:
    st.markdown("**Organizers**")
    number1 = 21
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

# with fifth_kpi:
#     st.markdown("**Second KPI**")
#     number2 = 222 
#     st.markdown(f"<h1 style='text-align: center; color: red;'>{number2}</h1>", unsafe_allow_html=True)

# with sixth_kpi:
#     st.markdown("**Third KPI**")
#     number3 = 333 
#     st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True)

st.markdown("<hr/>", unsafe_allow_html=True)

st.markdown("## Strengths")
st.markdown(">> Extensive analysis of each clubs participation and activity")
st.markdown(">> Value Proposition for the target market through offering a comprehensive dashboard for the users to analyse each clubs performance to determine their budget requirements")
st.markdown(">> Easier access for students to be aware of club activities")
st.markdown(">> Hustle free coordination for organisers")

st.markdown("## Trends to Observe")

first_chart, second_chart = st.columns(2)
st.image('index.png')
# third_chart = st.columns(1)

with first_chart:
    st.image('clubevent.png')
    # chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    # st.line_chart(chart_data)

st.markdown(">> Students have attended event 1 and event 2 of clubs more than event 3 ")
st.markdown(">> Total fest events: 27 ")
st.markdown(">> Total club events : 9")
st.markdown(">> Students attended more fest events than club events from the comparision of these graphs.")


with second_chart:
    st.image('graph.png')
    # chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['Club1', 'Club2', 'Club3'])
    # st.line_chart(chart_data)

    
# st.markdown("## Chart Section: 2")

# first_chart, second_chart = st.columns(2)


# with first_chart:
#     chart_data = pd.DataFrame(np.random.randn(100, 3),columns=['a', 'b', 'c'])
#     st.line_chart(chart_data)

# with second_chart:
#     chart_data = pd.DataFrame(np.random.randn(2000, 3),columns=['a', 'b', 'c'])
#     st.line_chart(chart_data)