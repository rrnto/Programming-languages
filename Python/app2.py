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
  "Quasars, Active Galactic Nuclei, and Supermassive Black Holes": [
    {
      "question": "The end of jet in radio galaxy is usually marked with a:",
      "options": ["A. Hot Spot", "B. Lobe", "C. Core", "D. X"],
      "answer_index": 0,
      "explanation": "The end of the jet in a radio galaxy is often marked by hot spots where the jet collides with the surrounding material, creating bright, energetic regions."
    },
    {
      "question": "What is the ultimate energy source in an Active Galaxy?",
      "options": ["A. Nuclear fusion in stars.", "B. Nuclear fission in stars.", "C. Accretion of material onto a supermassive black hole.", "D. Direct conversion of matter into energy in the hot spots."],
      "answer_index": 2,
      "explanation": "The ultimate energy source in an Active Galaxy comes from accretion of material onto a supermassive black hole, which releases a tremendous amount of energy in the process."
    },
    {
      "question": "What lurks at the center of our galaxy?",
      "options": ["A. A 3 million solar mass black hole.", "B. A giant star cluster", "C. A 30 solar mass black hole", "D. Darth Vader"],
      "answer_index": 0,
      "explanation": "At the center of our galaxy lies a supermassive black hole known as Sagittarius A*, which has a mass of about 4.1 million solar masses."
    },
    {
      "question": "Some extragalactic jets have components that appear to move faster than light (superluminal motion). This happens because:",
      "options": ["A. It is an illusion because the jets are pointed at us and moving close to the speed of light.", "B. Jets actually exceed the speed of light.", "C. Photons travel slower in intergalactic medium.", "D. Relativity breaks down near AGN."],
      "answer_index": 0,
      "explanation": "Superluminal motion is an optical illusion created when the jet is moving at relativistic speeds nearly parallel to the line of sight, making the components appear to exceed the speed of light."
    },
    {
      "question": "What sources dominate the sky at radio wavelengths?",
      "options": ["A. Normal galaxies", "B. Star-forming regions", "C. Active Galaxies", "D. Pulsars"],
      "answer_index": 2,
      "explanation": "Active Galaxies, particularly those with active galactic nuclei, dominate the sky at radio wavelengths, emitting significant radio waves due to the processes occurring around supermassive black holes."
    },
    {
      "question": "What is the most efficient energy source in the Universe?",
      "options": ["A. Nuclear fusion", "B. Chemical reactions", "C. Accretion onto a black hole", "D. Solar radiation"],
      "answer_index": 2,
      "explanation": "Accretion onto a black hole is considered the most efficient energy source in the Universe, as it can convert a large amount of mass into energy according to E=mc²."
    }
  ],

  "Galaxy Evolution": [
    {
      "question": "What do we call a galaxy with an unusually high star formation rate?",
      "options": ["A. A ring galaxy", "B. An elliptical galaxy", "C. A starburst galaxy", "D. A protogalaxy"],
      "answer_index": 2,
      "explanation": "A starburst galaxy is known for its exceptionally high rate of star formation compared to typical galaxies."
    },
    {
      "question": "What is the primary mechanism by which galaxies evolve over time?",
      "options": ["A: Stellar explosions", "B: Hierarchical merging of structures", "C: Constant star formation", "D: Isolation from other galaxies"],
      "answer_index": 1,
      "explanation": "Galaxies evolve primarily through hierarchical merging of structures."
    },
    {
      "question": "Which of the following timescales is associated with the lifetime of massive stars?",
      "options": ["A: ~100 Myr", "B: ~1 Gyr", "C: ~10 Gyr", "D: ~10 Myr"],
      "answer_index": 0,
      "explanation": "Massive stars have lifetimes on the order of ~100 million years."
    },
    {
      "question": "What observational evidence supports the evolution of galaxies?",
      "options": ["A: The presence of dark matter", "B: Stellar populations in the Milky Way", "C: The uniformity of cosmic microwave background radiation", "D: The distribution of quasars"],
      "answer_index": 1,
      "explanation": "Stellar populations in galaxies provide important evidence for their evolution."
    },
    {
      "question": "What is the significance of the BUTcher-Oemler effect in galaxy clusters?",
      "options": ["A: It indicates the presence of dark matter", "B: It shows that blue galaxies are more common at higher redshifts", "C: It describes the merger rates of galaxies", "D: It explains the formation of elliptical galaxies"],
      "answer_index": 1,
      "explanation": "The Butcher-Oemler effect shows that blue galaxies are more common at higher redshifts."
    },
    {
      "question": "How do stellar population synthesis models contribute to our understanding of galaxy evolution?",
      "options": ["A: They predict the mass of dark matter halos", "B: They estimate the number of galaxies in the universe", "C: They simulate the number of galaxies in the universe", "D: They measure the distance to galaxies"],
      "answer_index": 0,
      "explanation": "Stellar population synthesis models help in predicting the mass of dark matter halos."
    }
  ],

  "Elliptical and Dwarf Galaxies": [
    {
      "question": "What type of galaxy contains the most stars?",
      "options": ["A. Elliptical", "B. Dwarf Elliptical", "C. Spiral", "D. Irregular"],
      "answer_index": 0,
      "explanation": "Elliptical galaxies contain the most stars, with some massive ellipticals housing trillions of stars."
    },
    {
      "question": "What type of galaxy is the Large Magellanic Cloud?",
      "options": ["A. Elliptical", "B. Dwarf Elliptical", "C. Spiral", "D. Irregular"],
      "answer_index": 3,
      "explanation": "The Large Magellanic Cloud is classified as an irregular galaxy, characterized by its chaotic shape and large amounts of gas and dust."
    },
    {
      "question": "What sort of environment do you often find cD galaxies in but very rarely find any spiral galaxies in?",
      "options": ["A. In small groups of galaxies", "B. In the field", "C. In the center of very rich clusters", "D. In voids"],
      "answer_index": 2,
      "explanation": "cD galaxies are typically found at the centers of rich galaxy clusters, where spiral galaxies are rare due to environmental effects."
    },
    {
      "question": "What is the modern view of elliptical galaxies regarding their composition?",
      "options": ["A: They contain only old stars with no gas or dust", 
                  "B: They are composed of young stars and abundant gas", 
                  "C: They may contain hot X-ray gas, dust, and cold gas", 
                  "D: They are exclusively formed from mergers of dwarf galaxies"],
      "answer_index": 2,
      "explanation": "Elliptical galaxies may contain hot X-ray gas, dust, and cold gas."
    },
    {
      "question": "Which law describes the surface brightness profile of elliptical galaxies?",
      "options": ["A: The Tully-Fisher relation", 
                  "B: The de Vaucouleurs law", 
                  "C: The Hubble law", 
                  "D: The Sersic profile"],
      "answer_index": 1,
      "explanation": "The de Vaucouleurs law describes the surface brightness profile of elliptical galaxies."
    },
    {
      "question": "What is the primary support mechanism for the structure of elliptical galaxies?",
      "options": ["A: Rotation of stars", 
                  "B: Random motions of stars", 
                  "C: Gas pressure", 
                  "D: Magnetic fields"],
      "answer_index": 1,
      "explanation": "Elliptical galaxies are supported by random motions of stars."
    },
    {
      "question": "How does the metallicity of stars in elliptical galaxies typically vary with radius?",
      "options": ["A: It is uniform throughout the galaxy", 
                  "B: It decreases towards the center", 
                  "C: It increases towards the center", 
                  "D: It is higher in the outer regions"],
      "answer_index": 2,
      "explanation": "Metallicity tends to increase towards the center of elliptical galaxies."
    },
    {
      "question": "What distinguishes dwarf elliptical galaxies (dE) from normal elliptical galaxies?",
      "options": ["A: Dwarf ellipticals are larger and more luminous", 
                  "B: Dwarf ellipticals have a higher star formation rate", 
                  "C: Dwarf ellipticals are dark matter dominated and follow different correlations", 
                  "D: Dwarf ellipticals contain only young stars"],
      "answer_index": 2,
      "explanation": "Dwarf elliptical galaxies are often dark matter dominated and follow different correlations."
    }
  ],

  "Galaxy Morphology, Classification, Hubble Sequence, and Spiral Galaxies": [
    {
      "question": "What type of galaxy do we live in?",
      "options": ["A. Elliptical", "B. Dwarf Elliptical", "C. Spiral", "D. Irregular"],
      "answer_index": 2,
      "explanation": "We live in a barred spiral galaxy, known as the Milky Way, characterized by its spiral arm and central bulge."
    },
    {
      "question": "Our solar system is located:",
      "options": ["A. Near the center of the Milky Way galaxy in the bulge.", "B. 4 kpc from the center of the Milky Way in the halo.", "C. 8 kpc from the center of the Milky Way in the disk.", "D. 20 kpc from the center of the Milky Way in the disk."],
      "answer_index": 2,
      "explanation": "Our solar system is situated about 8 kiloparsecs (kpc), or approximately 27,000 light years, from the center of the Milky Way galaxy. It resides within the galactic disk, specifically on the inner edge of the Orion Arm."
    },
    {
      "question": "How long does it take our solar system to orbit once around the Milky Way?",
      "options": ["A. 1 year", "B. 2 million years", "C. 250 million years", "D. 250 billion years (longer than the age of the universe)"],
      "answer_index": 2,
      "explanation": "It takes our solar system approximately 250 million years to complete one orbit around the Milky Way’s center, a period often referred to as a 'cosmic year.'"
    }
  ],

  "Intergalactic Medium and the Cosmic Web": [
    {
      "question": "What makes up most of the mass (90%) of the Milky Way Galaxy?",
      "options": ["A. Hydrogen gas", "B. Stars", "C. Dead stars (white dwarfs, neutron stars, and black holes)", "D. We don’t know"],
      "answer_index": 3,
      "explanation": "Most of the mass of the Milky Way is thought to be composed of dark matter, which we cannot see or detect directly, hence the uncertainty."
    }
  ],

  "Large Scale Structure - Observations": [
    {
      "question": "Suppose we see a galaxy moving away from us at 300 km/s. How far away is it?",
      "options": ["A. 1 AU", "B. 8 kpc", "C. 4 Mpc", "D. 1 Gpc"],
      "answer_index": 2,
      "explanation": "Using Hubble’s Law, a galaxy moving away at 300 km/s corresponds to approximately 4 Mpc, or about 13 million ly away."
    },
    {
      "question": "What is the significance of the 'Great Wall' structure revealed in redshift surveys?",
      "options": ["A. It is the largest known galaxy.", "B. It is a ~100 Mpc structure that indicates the scale of large cosmic structures.", "C. It is a void in distribution of galaxies.", "D. It represents the edge of the observable universe."],
      "answer_index": 1,
      "explanation": "The 'Great Wall' is a vast conglomeration of galaxies spanning over 500 million light-years (about 150 megaparsecs), discovered through redshift surveys. Its existence demonstrates the immense scale of large-scale cosmic structures in the universe."
    },
    {
      "question": "What is the purpose of redshift surveys in cosmology?",
      "options": ["A. To measure the temperature of cosmic microwave background radiation.", "B. To map the 3-D distribution of galaxies in space.", "C. To determine the age of the universe.", "D. To study the chemical composition of stars."],
      "answer_index": 1,
      "explanation": "Redshift surveys measure the redshifts of galaxies to determine their distances and positions, allowing astronomers to map the three-dimensional structure of the universe. These maps reveal how galaxies are distributed and help in studying the large-scale structure of the cosmos."
    },
    {
      "question": "As photons travel through our expanding Universe over millions (or billions) of years, what happens to them?",
      "options": ["A. Their wavelength decreases", "B. Their wavelength increases", "C. They disappear", "D. They become visible light"],
      "answer_index": 1,
      "explanation": "As the universe expands, photons experience redshift, meaning their wavelength increases and their energy decreases."
    },
    {
      "question": "The cosmological principle states that:",
      "options": ["A. The universe is static and eternal", "B. The universe is isotropic and homogeneous on large scales", "C. The universe is filled with wormholes", "D. The universe is only 6,000 years old"],
      "answer_index": 1,
      "explanation": "Isotropic means the same in all directions and homogeneous means the same everywhere; this applies on large scales, not necessarily on small ones."
    }
  ],

  "Evolution of Clustering": [
    {
      "question": "How does the peculiar velocity field relate to the mass density field in the universe?",
      "options": ["A. It is independent of the mass density field.", "B. It is generated by the mass density field and reflects the underlying mass concentrations.", "C. It only affects small-scale structures.", "D. It is only relevant for dark matter."],
      "answer_index": 1,
      "explanation": "On large scales, the peculiar velocity field is coherent with the underlying mass density field. This means that peculiar velocities (deviations from the uniform cosmic expansion) are generated by mass concentrations and can be used to infer and study the distribution of matter in the universe."
    },
    {
      "question": "Our own Milky Way is part of:",
      "options": ["A. A large cluster with thousands of galaxies", "B. A small group of ~30 galaxies", "C. An isolated region with no other galaxies nearby", "D. A globular cluster"],
      "answer_index": 1,
      "explanation": "The Milky Way is part of the Local Group, which consists of about 30 galaxies, including Andromeda Galaxy and several smaller galaxies."
    }
  ],

  "Biasing": [
    {
      "question": "At what redshift do galaxies become more biased tracers of mass?",
      "options": ["A. At z = 0", "B. At z = 1", "C. At z = 2", "D. At z = 10"],
      "answer_index": 2,
      "explanation": "Halo bias increases with redshift. Massive halos are rarer at high redshift. These rare peaks have a higher clustering bias."
    },
    {
      "question": "What does the bias factor (b) indicate in the context of galaxy clustering?",
      "options": ["A. Galaxies trace dark matter exactly", "B. Galaxies avoid dense regions", "C. Describes how light (galaxies) traces mass (dark matter) in the Universe", "D. Galaxies form only in voids"],
      "answer_index": 2,
      "explanation": "The bias factor describes how galaxies (light) trace the distribution of dark matter in the Universe, which may not always be a direct match."
    }
  ],

  "Galaxy Clusters": [
    {
      "question": "The origin of the intra-cluster gas in clusters of galaxies is:",
      "options": ["A. Primordial gas left over from the Big Bang", "B. Material ejected or stripped out of galaxies long after the formation of the cluster", "C. Gas formed inside the cluster", "D. Gas from the Milky Way"],
      "answer_index": 1,
      "explanation": "The intracluster gas primarily originates from material that has been ejected or stripped from galaxies over time due to gravitational interactions within the cluster."
    },
    {
      "question": "Which of the following statements about galaxy clusters is true?",
      "options": ["A. Dark Matter constitutes about 8-85% of the mass in clusters", "B. All galaxies in clusters are spirals", "C. Galaxy clusters are made entirely of visible matter", "D. Galaxy clusters are unstable and short-lived"],
      "answer_index": 0,
      "explanation": "Dark Matter constitutes a large fraction (~85%) of the total mass in galaxy clusters, though exact values vary between clusters."
    },
    {
      "question": "What is the significance of the Sunyaev-Zel’dovich effect in studying galaxy clusters?",
      "options": ["A. It measures the number of stars in a cluster", "B. It provides a mass-weighted measure of hot gas in clusters", "C. It detects black holes directly", "D. It reveals the presence of planets"],
      "answer_index": 1,
      "explanation": "The Sunyaev-Zel’dovich effect allows astronomers to probe the hot intracluster gas independently of distance, providing a mass-weighted view of galaxy clusters."
    },
    {
      "question": "Which of the following statements about galaxy clusters is true?",
      "options": ["A: Clusters contain mostly spiral galaxies", 
                  "B: Dark matter constitutes about 80-85% of the mass in clusters", 
                  "C: Clusters are typically less than 1 Mpc in diameter", 
                  "D: Clusters are fully virialized at all times"],
      "answer_index": 1,
      "explanation": "Dark matter constitutes a significant fraction of the mass in galaxy clusters."
    },
    {
      "question": "What is the significance of the Sunyaev-Zeldovich effect in studying galaxy clusters?",
      "options": ["A: It measures the temperature of the cluster gas", 
                  "B: It detects the gravitational lensing of clusters", 
                  "C: It provides a mass-weighted measure of hot gas in clusters", 
                  "D: It identifies the number of galaxies in a cluster"],
      "answer_index": 2,
      "explanation": "The Sunyaev-Zeldovich effect is crucial for understanding the hot gas in galaxy clusters."
    },
    {
      "question": "How does the spatial distribution of galaxies in cD clusters differ from that in spiral-rich clusters?",
      "options": ["A: cD clusters have a uniform distribution of galaxies", 
                  "B: Spiral-rich clusters have a smooth and circularly symmetric distribution", 
                  "C: cD clusters show rapid density increase towards the center", 
                  "D: Spiral-rich clusters have a higher concentration of elliptical galaxies"],
      "answer_index": 2,
      "explanation": "In cD clusters, the galaxy density increases towards the center, making them highly concentrated."
    }
  ],

  "Formation of Quasars and the Growth of Supermassive Black Holes": [
    {
      "question": "Most compact jets are one-sided because:",
      "options": ["A. One side is destroyed", "B. The jets are strongly beamed, and one side is pointing closer to us", "C. Light travels slower on one side", "D. Magnetic fields bend the jet"],
      "answer_index": 1,
      "explanation": "Most compact jets appear one-sided due to relativistic beaming, where the side pointing towards us is amplified in brightness because of its high speed."
    }
  ],

  "Density Wave Theory": [
    {
      "question": "What is the primary classification scheme proposed by Hubble for galaxies?",
      "options": ["A: The spiral classification", 
                  "B: The tuning fork diagram", 
                  "C: The elliptical classification", 
                  "D: The morphological sequence"],
      "answer_index": 1,
      "explanation": "Hubble proposed the tuning fork diagram to classify galaxies based on morphology."
    },
    {
      "question": "Which type of galaxy is characterized by having a rotating disk and a central bulge but lacks spiral arms?",
      "options": ["A: Elliptical galaxies", 
                  "B: Lenticular galaxies", 
                  "C: Irregular galaxies", 
                  "D: Barred spiral galaxies"],
      "answer_index": 1,
      "explanation": "Lenticular galaxies have a disk and bulge but no spiral arms."
    },
    {
      "question": "What distinguishes Population I stars from Population II stars in galaxies?",
      "options": ["A: Population I stars are older and redder", 
                  "B: Population I stars are found in the bulge of galaxies", 
                  "C: Population I stars are young, hot stars associated with spiral arms", 
                  "D: Population I stars are primarily found in elliptical galaxies"],
      "answer_index": 2,
      "explanation": "Population I stars are young and found in the spiral arms of galaxies."
    },
    {
      "question": "What is the significance of the density wave theory in understanding spiral galaxies?",
      "options": ["A: It explains the formation of elliptical galaxies", 
                  "B: It describes how stars in spiral arms are formed from gas clouds", 
                  "C: It accounts for the random motion of stars in the bulge", 
                  "D: It explains the lack of star formation in lenticular galaxies"],
      "answer_index": 1,
      "explanation": "The density wave theory explains the spiral arm structure of galaxies."
    },
    {
      "question": "How do the properties of galaxies correlate with their classification in the Hubble sequence?",
      "options": ["A: All properties correlate perfectly with Hubble type", 
                  "B: Only mass and luminosity correlate well with Hubble type", 
                  "C: Many physical properties, such as star formation activity, correlate with morphology", 
                  "D: There is no correlation between properties and Hubble type"],
      "answer_index": 2,
      "explanation": "Many properties like star formation activity correlate with the Hubble classification."
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
