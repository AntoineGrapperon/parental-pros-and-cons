import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Parental Pros & Cons",
    page_icon="👶",
    layout="wide"
)

# Sample Data Structure
DATA = {
    "Feeding": {
        "Breastfeeding vs. Formula": {
            "description": "Deciding how to nourish your newborn in the first year.",
            "options": [
                {
                    "name": "Breastfeeding",
                    "pros": ["Provides essential antibodies", "Promotes bonding", "Cost-effective (free)", "Always at the right temperature"],
                    "cons": ["Physically demanding for the mother", "Harder to share feeding duties", "Can be painful initially", "Dietary restrictions may apply"],
                    "resources": [{"name": "La Leche League International", "url": "https://www.llli.org/"}]
                },
                {
                    "name": "Formula Feeding",
                    "pros": ["Anyone can feed the baby", "Easier to track intake", "More flexibility for the mother", "No dietary restrictions for mom"],
                    "cons": ["Expensive (ongoing cost)", "Requires preparation and sterilization", "Doesn't provide antibodies", "Can cause digestive sensitivity"],
                    "resources": [{"name": "CDC: Choosing a Formula", "url": "https://www.cdc.gov/nutrition/infantandtoddlernutrition/formula-feeding/index.html"}]
                }
            ]
        },
        "Intro to Solids: BLW vs. Purees": {
            "description": "Choosing a method to introduce solid foods around 6 months.",
            "options": [
                {
                    "name": "Baby-Led Weaning (BLW)",
                    "pros": ["Encourages self-regulation", "Easier family meals", "Develops fine motor skills", "Explores textures early"],
                    "cons": ["Can be very messy", "Higher anxiety about choking", "Harder to track exact intake", "Requires careful prep of 'finger foods'"],
                    "resources": [{"name": "Solid Starts", "url": "https://solidstarts.com/"}]
                },
                {
                    "name": "Traditional Purees",
                    "pros": ["Easier to track amount eaten", "Lower initial mess", "Less immediate choking anxiety", "Controlled introduction of flavors"],
                    "cons": ["Requires extra prep/blending", "Slower transition to family table", "Delayed texture exposure", "Babies may resist lumps later"],
                    "resources": [{"name": "Mayo Clinic Solids Guide", "url": "https://www.mayoclinic.org/healthy-lifestyle/infant-and-toddler-health/in-depth/healthy-baby/art-20046200"}]
                }
            ]
        }
    },
    "Sleep": {
        "Crib vs. Bassinet": {
            "description": "Where should the baby sleep during the first few months?",
            "options": [
                {
                    "name": "Bassinet",
                    "pros": ["Portable and smaller", "Fits easily in parents' room", "Easier to reach baby at night", "Cozy for newborns"],
                    "cons": ["Short lifespan (outgrown quickly)", "Lower weight limits", "Extra expense before buying a crib", "Less stable than a crib"],
                    "resources": [{"name": "AAP Safe Sleep Guidelines", "url": "https://www.aap.org/en/patient-care/safe-sleep/"}]
                },
                {
                    "name": "Full-Size Crib",
                    "pros": ["Long-term use (years)", "Sturdy and safe", "Standardized mattress sizes", "Higher weight/height limits"],
                    "cons": ["Large footprint", "Not portable", "Can feel 'too big' for a tiny newborn", "More expensive initially"],
                    "resources": [{"name": "Consumer Reports Crib Guide", "url": "https://www.consumerreports.org/babies-kids/cribs/buying-guide/"}]
                }
            ]
        }
    },
    "Gear": {
        "Cloth vs. Disposable Diapers": {
            "description": "Managing the thousands of diaper changes ahead.",
            "options": [
                {
                    "name": "Cloth Diapers",
                    "pros": ["Environmentally friendly", "Cheaper in the long run", "Fewer chemicals", "Earlier potty training often reported"],
                    "cons": ["Significant laundry load", "High upfront cost", "Less convenient for travel", "Can be bulkier under clothes"],
                    "resources": [{"name": "Real Diaper Association", "url": "https://www.realdiaperassociation.org/"}]
                },
                {
                    "name": "Disposable Diapers",
                    "pros": ["Extremely convenient", "High absorbency (less changing)", "Easy for travel/daycare", "Low upfront cost"],
                    "cons": ["Significant environmental waste", "Expensive over 2-3 years", "Contains chemicals/perfumes", "Higher risk of 'blowouts'"],
                    "resources": [{"name": "Eco-friendly Disposable Reviews", "url": "https://www.babygearlab.com/topics/diapering-potty/best-disposable-diaper"}]
                }
            ]
        }
    }
}

# Sidebar for Navigation
st.sidebar.title("Parental Guide")
category = st.sidebar.selectbox("Choose a Category", list(DATA.keys()))

if category:
    question = st.sidebar.selectbox("Select a Topic", list(DATA[category].keys()))

# Main Content
st.title("👶 Parental Pros & Cons")
st.write("Making informed decisions for your little one.")
st.markdown("---")

if category and question:
    selected_data = DATA[category][question]
    
    st.header(question)
    st.info(selected_data["description"])
    
    # Create columns for the options
    cols = st.columns(len(selected_data["options"]))
    
    for i, option in enumerate(selected_data["options"]):
        with cols[i]:
            st.subheader(f"Option: {option['name']}")
            
            st.write("✅ **Pros**")
            for pro in option["pros"]:
                st.write(f"- {pro}")
                
            st.write("❌ **Cons**")
            for con in option["cons"]:
                st.write(f"- {con}")
            
            st.write("📚 **Resources**")
            for res in option["resources"]:
                st.write(f"[{res['name']}]({res['url']})")

else:
    st.write("Select a topic from the sidebar to begin.")

# Footer
st.markdown("---")
st.caption("Disclaimer: This tool is for informational purposes only. Always consult with your pediatrician for medical advice.")
