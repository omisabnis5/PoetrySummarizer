import streamlit as st
from openai import OpenAI
import os


# Add OpenAI API key to enironment variable
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def summarize_poem(poem):
    prompt = f"You are an expert in literature. I want you to summarize the following poem/verse written in ancient English or Shakespeare English into simplified English that can be understood by a layman. Summarize the following poem:\n\n{poem}\n\nSummary:"

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )


    summary = completion.choices[0].message
    return summary

def main():
    hide_default_st_css = "<style>.st-emotion-cache-zq5wmm, .viewerBadge_container__r5tak { display:none!important }"
    st.markdown(hide_default_st_css, unsafe_allow_html=True)
    st.title("Poem Summarizer")

    # User input: Poem text
    poem_text = st.text_area("Enter a Poem/Verse:")

    # Generate button
    if st.button("Generate Summary"):
        if poem_text:
            # Summarize the poem
            poem_summary = summarize_poem(poem_text)

            # Display the summary
            st.subheader("Simplified Poem/Verse Summary:")
            st.write(poem_summary.content)
        else:
            st.warning("Please enter a poem before generating a summary.")

if __name__ == "__main__":
    main()