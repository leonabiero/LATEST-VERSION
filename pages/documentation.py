import streamlit as st
from services.draft_storage import save_draft
from services.language import init_language

T = init_language()

st.title(T["doc"])

case_ref = st.text_input(T["case_ref"])
doc_type = st.selectbox(T["doc_type"], ["Nota de caso", "Entrevista", "Seguimiento"])
language = st.selectbox(T["language"], ["Español", "Euskera", "English"])
text = st.text_area(T["text"])

if st.button(T["save"]):
    if text.strip():
        save_draft(case_ref, doc_type, language, text)
        st.session_state.save_status = "success"
    else:
        st.session_state.save_status = "empty"

if "save_status" not in st.session_state:
    st.session_state.save_status = ""

if st.session_state.save_status == "success":
    st.success(T["success"])
elif st.session_state.save_status == "empty":
    st.warning(T["empty"])