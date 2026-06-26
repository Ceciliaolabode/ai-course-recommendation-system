import streamlit as st
import pickle
import pandas as pd

# Load saved files
similarity = pickle.load(open("recommender/similarity.pkl", "rb"))

course_list = pickle.load(
    open("recommender/course_list.pkl", "rb")
)

courses = pd.DataFrame(course_list)



def recommend(course):

    course_index = courses[
        courses['course_name'] == course
    ].index[0]

    distance = similarity[course_index]

    course_list = sorted(
        list(enumerate(distance)),
        reverse=True,
        key=lambda x: x[1]
    )[1:7]

    recommendations = []

    for i in course_list:

        recommendations.append({
            "name": courses.iloc[i[0]].course_name,
            "url": courses.iloc[i[0]].course_url
        })

    return recommendations


st.title("🎓 Course Recommendation System")

selected_course = st.selectbox(
    "Choose a course",
    courses["course_name"]
)

if st.button("Recommend"):

    recommendations = recommend(selected_course)

    st.subheader("Recommended Courses")

    for course in recommendations:

        st.markdown(
            f"### [{course['name']}]({course['url']})"
        )

        