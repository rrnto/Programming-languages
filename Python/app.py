import streamlit as st

# Set the custom CSS for glowing effect and dark theme
st.markdown("""
    <style>
    body {
        background-color: #1b263b;  /* Dark space-like background */
        color: #e0e1dd;  /* Light text color */
        font-family: "Roboto", sans-serif;
    }
    .stButton > button {
        background-color: #778da9;  /* Button color */
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        box-shadow: 0 0 15px #00ffff;  /* Glowing effect */
    }
    .stRadio > label {
        font-size: 18px;
    }
    .stRadio > div {
        background-color: #2e3b4e;
        border-radius: 5px;
        padding: 10px;
    }
    .stRadio > div > label {
        color: #e0e1dd;
        font-size: 18px;
    }
    .stRadio input[type="radio"]:checked ~ label {
        color: #00ffff;  /* Glowing effect on selected answer */
    }
    </style>
""", unsafe_allow_html=True)

# Questions for the quiz (with more questions in each section)
questions_by_section = {
    "Galaxy Clusters": [
        {
            'question': 'Which of the following statements about galaxy clusters is true?',
            'options': ['A: Clusters contain mostly spiral galaxies', 
                        'B: Dark matter constitutes about 80-85% of the mass in clusters', 
                        'C: Clusters are typically less than 1 Mpc in diameter', 
                        'D: Clusters are fully virialized at all times'],
            'answer_index': 1,  # Correct answer index
            'explanation': 'Dark matter constitutes a significant fraction of the mass in galaxy clusters.'
        },
        {
            'question': 'What is the significance of the Sunyaev-Zeldovich effect in studying galaxy clusters?',
            'options': ['A: It measures the temperature of the cluster gas', 
                        'B: It detects the gravitational lensing of clusters', 
                        'C: It provides a mass-weighted measure of hot gas in clusters', 
                        'D: It identifies the number of galaxies in a cluster'],
            'answer_index': 2,
            'explanation': 'The Sunyaev-Zeldovich effect is crucial for understanding the hot gas in galaxy clusters.'
        },
        {
            'question': 'How does the spatial distribution of galaxies in cD clusters differ from that in spiral-rich clusters?',
            'options': ['A: cD clusters have a uniform distribution of galaxies', 
                        'B: Spiral-rich clusters have a smooth and circularly symmetric distribution', 
                        'C: cD clusters show rapid density increase towards the center', 
                        'D: Spiral-rich clusters have a higher concentration of elliptical galaxies'],
            'answer_index': 2,
            'explanation': 'In cD clusters, the galaxy density increases towards the center, making them highly concentrated.'
        }
    ],
    "Density Wave Theory": [
        {
            'question': 'What is the primary classification scheme proposed by Hubble for galaxies?',
            'options': ['A: The spiral classification', 
                        'B: The tuning fork diagram', 
                        'C: The elliptical classification', 
                        'D: The morphological sequence'],
            'answer_index': 1,
            'explanation': 'Hubble proposed the tuning fork diagram to classify galaxies based on morphology.'
        },
        {
            'question': 'Which type of galaxy is characterized by having a rotating disk and a central bulge but lacks spiral arms?',
            'options': ['A: Elliptical galaxies', 
                        'B: Lenticular galaxies', 
                        'C: Irregular galaxies', 
                        'D: Barred spiral galaxies'],
            'answer_index': 1,
            'explanation': 'Lenticular galaxies have a disk and bulge but no spiral arms.'
        },
        {
            'question': 'What distinguishes Population I stars from Population II stars in galaxies?',
            'options': ['A: Population I stars are older and redder', 
                        'B: Population I stars are found in the bulge of galaxies', 
                        'C: Population I stars are young, hot stars associated with spiral arms', 
                        'D: Population I stars are primarily found in elliptical galaxies'],
            'answer_index': 2,
            'explanation': 'Population I stars are young and found in the spiral arms of galaxies.'
        },
        {
            'question': 'What is the significance of the density wave theory in understanding spiral galaxies?',
            'options': ['A: It explains the formation of elliptical galaxies', 
                        'B: It describes how stars in spiral arms are formed from gas clouds', 
                        'C: It accounts for the random motion of stars in the bulge', 
                        'D: It explains the lack of star formation in lenticular galaxies'],
            'answer_index': 1,
            'explanation': 'The density wave theory explains the spiral arm structure of galaxies.'
        },
        {
            'question': 'How do the properties of galaxies correlate with their classification in the Hubble sequence?',
            'options': ['A: All properties correlate perfectly with Hubble type', 
                        'B: Only mass and luminosity correlate well with Hubble type', 
                        'C: Many physical properties, such as star formation activity, correlate with morphology', 
                        'D: There is no correlation between properties and Hubble type'],
            'answer_index': 2,
            'explanation': 'Many properties like star formation activity correlate with the Hubble classification.'
        }
    ],
    "Elliptical and Dwarf Galaxies": [
        {
            'question': 'What is the modern view of elliptical galaxies regarding their composition?',
            'options': ['A: They contain only old stars with no gas or dust', 
                        'B: They are composed of young stars and abundant gas', 
                        'C: They may contain hot X-ray gas, dust, and cold gas', 
                        'D: They are exclusively formed from mergers of dwarf galaxies'],
            'answer_index': 2,
            'explanation': 'Elliptical galaxies may contain hot X-ray gas, dust, and cold gas.'
        },
        {
            'question': 'Which law describes the surface brightness profile of elliptical galaxies?',
            'options': ['A: The Tully-Fisher relation', 
                        'B: The de Vaucouleurs law', 
                        'C: The Hubble law', 
                        'D: The Sersic profile'],
            'answer_index': 1,
            'explanation': 'The de Vaucouleurs law describes the surface brightness profile of elliptical galaxies.'
        },
        {
            'question': 'What is the primary support mechanism for the structure of elliptical galaxies?',
            'options': ['A: Rotation of stars', 
                        'B: Random motions of stars', 
                        'C: Gas pressure', 
                        'D: Magnetic fields'],
            'answer_index': 1,
            'explanation': 'Elliptical galaxies are supported by random motions of stars.'
        },
        {
            'question': 'How does the metallicity of stars in elliptical galaxies typically vary with radius?',
            'options': ['A: It is uniform throughout the galaxy', 
                        'B: It decreases towards the center', 
                        'C: It increases towards the center', 
                        'D: It is higher in the outer regions'],
            'answer_index': 2,
            'explanation': 'Metallicity tends to increase towards the center of elliptical galaxies.'
        },
        {
            'question': 'What distinguishes dwarf elliptical galaxies (dE) from normal elliptical galaxies?',
            'options': ['A: Dwarf ellipticals are larger and more luminous', 
                        'B: Dwarf ellipticals have a higher star formation rate', 
                        'C: Dwarf ellipticals are dark matter dominated and follow different correlations', 
                        'D: Dwarf ellipticals contain only young stars'],
            'answer_index': 2,
            'explanation': 'Dwarf elliptical galaxies are often dark matter dominated and follow different correlations.'
        }
    ],
    "Galaxy Evolution": [
        {
            'question': 'What is the primary mechanism by which galaxies evolve over time?',
            'options': ['A: Stellar explosions', 
                        'B: Hierarchical merging of structures', 
                        'C: Constant star formation', 
                        'D: Isolation from other galaxies'],
            'answer_index': 1,
            'explanation': 'Galaxies evolve primarily through hierarchical merging of structures.'
        },
        {
            'question': 'Which of the following timescales is associated with the lifetime of massive stars?',
            'options': ['A: ~100 Myr', 
                        'B: ~1 Gyr', 
                        'C: ~10 Gyr', 
                        'D: ~10 Myr'],
            'answer_index': 0,
            'explanation': 'Massive stars have lifetimes on the order of ~100 million years.'
        },
        {
            'question': 'What observational evidence supports the evolution of galaxies?',
            'options': ['A: The presence of dark matter', 
                        'B: Stellar populations in the Milky Way', 
                        'C: The uniformity of cosmic microwave background radiation', 
                        'D: The distribution of quasars'],
            'answer_index': 1,
            'explanation': 'Stellar populations in galaxies provide important evidence for their evolution.'
        },
        {
            'question': 'What is the significance of the BUTcher-Oemler effect in galaxy clusters?',
            'options': ['A: It indicates the presence of dark matter', 
                        'B: It shows that blue galaxies are more common at higher redshifts', 
                        'C: It describes the merger rates of galaxies', 
                        'D: It explains the formation of elliptical galaxies'],
            'answer_index': 1,
            'explanation': 'The Butcher-Oemler effect shows that blue galaxies are more common at higher redshifts.'
        },
        {
            'question': 'How do stellar population synthesis models contribute to our understanding of galaxy evolution?',
            'options': ['A: They predict the mass of dark matter halos', 
                        'B: They estimate the number of galaxies in the universe', 
                        'C: They simulate the number of galaxies in the universe', 
                        'D: They measure the distance to galaxies'],
            'answer_index': 0,
            'explanation': 'Stellar population synthesis models help in predicting the mass of dark matter halos.'
        }
    ]
}

# Function to display each question
def show_question(q, section_name, question_index):
    st.subheader(f"Question: {section_name}")
    st.write(q['question'])

    # Display the options
    options = q['options']
    selected_answer = st.radio("Choose an option:", options, key=f"radio_{section_name}_{question_index}")

    # Add a unique key to the button for submitting the answer
    submit_button_key = f"submit_{section_name}_{question_index}"
    if st.button('Submit Answer', key=submit_button_key):
        st.session_state.submitted = True
        st.session_state.selected_answer = selected_answer
        st.session_state.correct_answer = options[q['answer_index']]
        st.session_state.explanation = q['explanation']

    # Show the answer when "Show Answer" button is pressed
    show_answer_button_key = f"show_answer_{section_name}_{question_index}"
    if st.button('Show Answer', key=show_answer_button_key):
        if selected_answer == options[q['answer_index']]:
            st.success(f"✅ Correct! {q['explanation']}")
        else:
            st.error(f"❌ Incorrect! Correct answer: {options[q['answer_index']]}. {q['explanation']}")

# Main app logic
def main():
    st.title("🌌 Galaxy Quiz")
    st.markdown("Explore the depths of the universe and test your knowledge!")

    # Section selector for quiz
    section_name = st.sidebar.selectbox("Select Section", list(questions_by_section.keys()))
    questions = questions_by_section[section_name]

    # Show each question for the selected section
    for idx, question in enumerate(questions):
        show_question(question, section_name, idx)

if __name__ == "__main__":
    main()
