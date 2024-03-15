"""This modules contains data about home page"""

from pathlib import Path
import streamlit as st
import sys
sys.path.append(str(Path(__file__).parent))

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.subheader("Autism Level Predictor")

    # Add image to the home page
    st.image("Autism/images/home.png")

    st.markdown('''Autism spectrum disorder (ASD) is a complex neurodevelopmental condition, and various factors can influence its development and manifestation. Here are 21 factors that can play a role:

1. **Genetics:** Family history and genetic factors contribute significantly to ASD. Certain genetic mutations or variations increase the likelihood of ASD.

2. **Prenatal Factors:** Conditions during pregnancy, such as maternal infections, exposure to certain medications, toxins, or maternal health issues, can affect fetal brain development.

3. **Environmental Factors:** Exposure to environmental toxins, such as air pollutants, heavy metals, pesticides, and other chemicals, may increase the risk of ASD.

4. **Advanced Parental Age:** Both maternal and paternal age, especially when older, have been associated with a higher risk of having a child with ASD.

5. **Birth Complications:** Complications during birth, such as oxygen deprivation, low birth weight, or premature birth, may be linked to an increased risk of ASD.

6. **Immune System Dysfunction:** Disruptions or irregularities in the immune system during critical developmental periods might be a contributing factor.

7. **Neurological Factors:** Differences in brain structure and connectivity, such as abnormal growth patterns or connectivity in certain brain regions, have been observed in individuals with ASD.

8. **Gastrointestinal Issues:** Many individuals with ASD also experience gastrointestinal problems, leading to investigations into the gut-brain connection.

9. **Sensory Processing Differences:** Heightened or reduced sensitivity to sensory stimuli is common in ASD, impacting how individuals perceive and interact with their environment.

10. **Epigenetic Factors:** Environmental influences that can modify gene expression without changing the underlying DNA sequence might contribute to ASD.

11. **Nutritional Factors:** Some research suggests that dietary factors, including nutritional deficiencies or specific dietary components, might influence ASD symptoms.

12. **Hormonal Factors:** Imbalances or differences in hormonal levels during critical developmental stages could potentially impact ASD.

13. **Neurotransmitter Function:** Variations in neurotransmitter levels or functioning, such as serotonin, dopamine, and others, might be associated with ASD.

14. **Social and Environmental Interaction:** Early social experiences and the social environment can significantly impact the development of social skills in individuals with ASD.

15. **Stress During Pregnancy:** High levels of stress or exposure to stressful situations during pregnancy might influence fetal development.

16. **Parental Health:** The physical and mental health status of parents before and during pregnancy can have an impact on the risk of ASD.

17. **Autoimmune Disorders:** Some studies suggest a potential link between autoimmune disorders in mothers and an increased risk of ASD in their children.

18. **Inflammation:** Elevated levels of inflammation markers have been observed in some individuals with ASD, leading to investigations into the role of inflammation.

19. **Sleep Disorders:** Sleep disturbances are common in individuals with ASD, and the relationship between sleep patterns and ASD is an area of ongoing research.

20. **Metabolic Factors:** Variations in metabolic processes or metabolic disorders might contribute to ASD symptoms in some individuals.

21. **Unknown Factors:** Despite extensive research, there are still aspects of ASD that remain unclear, and there might be additional factors that influence its development.

Understanding ASD involves considering these various factors and their potential interactions, but it's important to note that each individual's experience with ASD is unique, and not all factors may apply to everyone.''')

