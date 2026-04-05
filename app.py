import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Parental Pros & Cons",
    page_icon="👶",
    layout="wide"
)

# Translations for UI components
TRANSLATIONS = {
    "English": {
        "title": "👶 Parental Pros & Cons",
        "subtitle": "Making informed decisions for your little one.",
        "sidebar_title": "Settings",
        "choose_cat": "Categories",
        "select_topic": "Select a Topic",
        "option_label": "Option",
        "pros": "✅ Pros",
        "cons": "❌ Cons",
        "resources": "📚 Resources",
        "disclaimer": "Disclaimer: This tool is for informational purposes only. Always consult with your pediatrician for medical advice.",
        "select_start": "Select a topic to begin."
    },
    "Français": {
        "title": "👶 Parents : Pour & Contre",
        "subtitle": "Prenez des décisions éclairées pour votre enfant.",
        "sidebar_title": "Paramètres",
        "choose_cat": "Catégories",
        "select_topic": "Sélectionner un sujet",
        "option_label": "Option",
        "pros": "✅ Avantages",
        "cons": "❌ Inconvénients",
        "resources": "📚 Ressources",
        "disclaimer": "Avertissement : Cet outil est purement informatif. Consultez toujours votre pédiatre pour des conseils médicaux.",
        "select_start": "Sélectionnez un sujet pour commencer."
    },
    "Español": {
        "title": "👶 Padres: Pros y Contras",
        "subtitle": "Tome decisiones informadas para su pequeño.",
        "sidebar_title": "Ajustes",
        "choose_cat": "Categorías",
        "select_topic": "Seleccione un tema",
        "option_label": "Opción",
        "pros": "✅ Pros",
        "cons": "❌ Contras",
        "resources": "📚 Recursos",
        "disclaimer": "Descargo de responsabilidad: Esta herramienta es solo para fines informativos. Consulte siempre con su pediatra para obtener asesoramiento médico.",
        "select_start": "Seleccione un tema para comenzar."
    },
    "中文": {
        "title": "👶 育儿优缺点",
        "subtitle": "为您的宝宝做出明智的决定。",
        "sidebar_title": "设置",
        "choose_cat": "类别",
        "select_topic": "选择一个话题",
        "option_label": "选项",
        "pros": "✅ 优点",
        "cons": "❌ 缺点",
        "resources": "📚 资源",
        "disclaimer": "免责声明：本工具仅供参考。有关医疗建议，请务必咨询您的儿科医生。",
        "select_start": "请选择一个话题开始。"
    }
}

# Multilingual Data
DATA = {
    "Feeding": {
        "en": "Feeding", "fr": "Alimentation", "es": "Alimentación", "zh": "喂养",
        "topics": {
            "Breastfeeding vs. Formula": {
                "en": "Breastfeeding vs. Formula", "fr": "Allaitement vs Biberon", "es": "Lactancia vs. Fórmula", "zh": "母乳喂养 vs. 配方奶",
                "desc": {
                    "en": "Deciding how to nourish your newborn in the first year.",
                    "fr": "Décider comment nourrir votre nouveau-né la première année.",
                    "es": "Decidir cómo alimentar a su recién nacido en el primer año.",
                    "zh": "决定第一年如何抚养您的新生儿。"
                },
                "options": [
                    {
                        "name": {"en": "Breastfeeding", "fr": "Allaitement", "es": "Lactancia", "zh": "母乳喂养"},
                        "pros": {
                            "en": ["Provides antibodies", "Bonding", "Cost-effective", "Right temperature"],
                            "fr": ["Fournit des anticorps", "Favorise le lien", "Gratuit", "Toujours à la bonne température"],
                            "es": ["Proporciona anticuerpos", "Vínculo afectivo", "Rentable", "Temperatura adecuada"],
                            "zh": ["提供抗体", "增强母婴联系", "节省成本", "温度适宜"]
                        },
                        "cons": {
                            "en": ["Physically demanding", "Harder to share duties", "Can be painful"],
                            "fr": ["Physiquement exigeant", "Difficile de partager les tâches", "Peut être douloureux"],
                            "es": ["Físicamente exigente", "Más difícil compartir tareas", "Puede ser doloroso"],
                            "zh": ["身体负担重", "难以分担喂养职责", "最初可能会感到疼痛"]
                        }
                    },
                    {
                        "name": {"en": "Formula", "fr": "Lait infantile", "es": "Fórmula", "zh": "配方奶"},
                        "pros": {
                            "en": ["Anyone can feed", "Easier to track intake", "Flexibility for mother"],
                            "fr": ["Tout le monde peut nourrir", "Suivi facile de la quantité", "Flexibilité pour la mère"],
                            "es": ["Cualquiera puede alimentar", "Más fácil de rastrear la ingesta", "Flexibilidad para la madre"],
                            "zh": ["任何人都可以喂养", "更容易跟踪摄入量", "母亲更灵活"]
                        },
                        "cons": {
                            "en": ["Expensive", "Requires preparation", "Doesn't provide antibodies"],
                            "fr": ["Coûteux", "Nécessite une préparation", "Pas d'anticorps"],
                            "es": ["Costoso", "Requiere preparación", "No proporciona anticuerpos"],
                            "zh": ["价格昂贵", "需要准备工作", "不提供抗体"]
                        }
                    }
                ]
            }
        }
    },
    "Sleep": {
        "en": "Sleep", "fr": "Sommeil", "es": "Sueño", "zh": "睡眠",
        "topics": {
            "Crib vs. Bassinet": {
                "en": "Crib vs. Bassinet", "fr": "Berceau vs Lit à barreaux", "es": "Cuna vs. Moisés", "zh": "婴儿床 vs. 摇篮",
                "desc": {
                    "en": "Where should the baby sleep initially?",
                    "fr": "Où le bébé doit-il dormir au début ?",
                    "es": "¿Dónde debe dormir el bebé inicialmente?",
                    "zh": "婴儿最初应该睡在哪里？"
                },
                "options": [
                    {
                        "name": {"en": "Bassinet", "fr": "Berceau", "es": "Moisés", "zh": "摇篮"},
                        "pros": {
                            "en": ["Portable", "Fits in parent's room", "Cozy"],
                            "fr": ["Portable", "Tient dans la chambre parentale", "Confortable"],
                            "es": ["Portátil", "Cabe en la habitación de los padres", "Acogedor"],
                            "zh": ["便携", "适合放在父母房内", "舒适"]
                        },
                        "cons": {
                            "en": ["Short lifespan", "Weight limits", "Extra expense"],
                            "fr": ["Courte durée d'utilisation", "Limites de poids", "Dépense supplémentaire"],
                            "es": ["Vida útil corta", "Límites de peso", "Gasto extra"],
                            "zh": ["使用周期短", "有重量限制", "额外支出"]
                        }
                    },
                    {
                        "name": {"en": "Full-Size Crib", "fr": "Lit à barreaux", "es": "Cuna grande", "zh": "大尺寸婴儿床"},
                        "pros": {
                            "en": ["Long-term use", "Sturdy", "Standard size"],
                            "fr": ["Utilisation à long terme", "Robuste", "Taille standard"],
                            "es": ["Uso a largo plazo", "Robusta", "Tamaño estándar"],
                            "zh": ["长期使用", "稳固", "标准尺寸"]
                        },
                        "cons": {
                            "en": ["Large footprint", "Not portable", "Initial cost"],
                            "fr": ["Encombrant", "Non portable", "Coût initial"],
                            "es": ["Gran espacio", "No es portátil", "Costo inicial"],
                            "zh": ["占地面积大", "不便移动", "初始成本高"]
                        }
                    }
                ]
            }
        }
    }
}

# Language Selection in Sidebar
st.sidebar.title("🌐 Language")
lang_choice = st.sidebar.selectbox("Select Language / Choisir la langue", list(TRANSLATIONS.keys()))
lang_code = {"English": "en", "Français": "fr", "Español": "es", "中文": "zh"}[lang_choice]

t = TRANSLATIONS[lang_choice]

# Main Content Header
st.title(t["title"])
st.write(t["subtitle"])
st.markdown("---")

# Categories as Tabs
cat_keys = list(DATA.keys())
translated_cats = [DATA[k][lang_code] for k in cat_keys]
tabs = st.tabs(translated_cats)

for i, tab in enumerate(tabs):
    cat_key = cat_keys[i]
    with tab:
        # Topic selection within each tab
        topics_dict = DATA[cat_key]["topics"]
        topic_names = [topics_dict[k][lang_code] for k in topics_dict]
        
        selected_topic_name = st.selectbox(
            t["select_topic"], 
            topic_names, 
            key=f"topic_select_{cat_key}"
        )
        
        # Find the topic key based on the translated name
        topic_key = None
        for k, v in topics_dict.items():
            if v[lang_code] == selected_topic_name:
                topic_key = k
                break
        
        if topic_key:
            selected_data = topics_dict[topic_key]
            st.markdown("### " + selected_topic_name)
            st.info(selected_data["desc"][lang_code])
            
            # Create columns for the options
            cols = st.columns(len(selected_data["options"]))
            
            for j, option in enumerate(selected_data["options"]):
                with cols[j]:
                    st.subheader(f"{t['option_label']}: {option['name'][lang_code]}")
                    
                    st.write(f"**{t['pros']}**")
                    for pro in option["pros"][lang_code]:
                        st.write(f"- {pro}")
                        
                    st.write(f"**{t['cons']}**")
                    for con in option["cons"][lang_code]:
                        st.write(f"- {con}")

# Footer
st.markdown("---")
st.caption(t["disclaimer"])
