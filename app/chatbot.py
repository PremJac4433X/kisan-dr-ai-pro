"""
KisanDr AI: Agricultural Knowledge Engine & Multilingual Chatbot.
Provides contextual agricultural advisory, disease treatment tips,
fertilizer guidance, and weather spray safety in 9 Indian regional languages.
Supports optional Google Gemini API fallback when GEMINI_API_KEY is configured.
"""

import os
import re
from typing import Optional, List, Dict, Any

from app.disease_db import CROP_DISEASES, CROPS_LIST, CROPS_CATALOG

# Common agricultural queries and localized responses
AGRI_KNOWLEDGE = {
    "organic_recipes": {
        "neem_oil": {
            "title": "Neem Oil Spray (नीम का तेल छिड़काव)",
            "recipe": "Mix 5ml pure cold-pressed neem oil + 2ml liquid soap or detergent in 1 liter of warm water. Shake vigorously. Spray every 7-10 days early morning or late evening. Effective against sucking pests, aphids, whiteflies, and early fungal spots.",
            "recipe_hi": "1 लीटर गुनगुने पानी में 5 मिली नीम का तेल और 2 मिली तरल साबुन मिलाएं। अच्छी तरह हिलाएं। सुबह या शाम को छिड़कें। यह माहू, सफेद मक्खी और फफूंद के धब्बों पर अत्यधिक प्रभावी है।"
        },
        "jeevamrut": {
            "title": "Jeevamrut Microbial Tonic (जीवामृत)",
            "recipe": "In 200L water, mix 10kg fresh cow dung, 10L cow urine, 2kg jaggery, 2kg pulse flour (besan), and a handful of fertile farm soil. Ferment in shade for 48 hours stirring clockwise twice daily. Apply 200L per acre via irrigation.",
            "recipe_hi": "200 लीटर पानी में 10 किलो ताजा देशी गाय का गोबर, 10 लीटर गोमूत्र, 2 किलो गुड़, 2 किलो बेसन और मुट्ठी भर उपजाऊ मिट्टी मिलाएं। 48 घंटे छांव में रखें और दिन में दो बार चलाएं। 1 एकड़ में सिंचाई के साथ दें।"
        },
        "buttermilk_fungicide": {
            "title": "Sour Buttermilk Bio-Fungicide (खट्टी छाछ कवकनाशी)",
            "recipe": "Take 5 liters of sour buttermilk (fermented 4-5 days in a copper vessel). Dilute with 40-50 liters of water. Spray on crops suffering from powdery mildew, leaf curl, and downy mildew.",
            "recipe_hi": "तांबे के बर्तन में 4-5 दिन पुरानी 5 लीटर खट्टी छाछ लें। इसे 45-50 लीटर पानी में मिलाकर छान लें। यह चूर्णिल आसिता (पाउडरी मिल्ड्यू) और पत्ती मरोड़ पर रामबाण काम करता है।"
        }
    },
    "fertilizer_guide": {
        "general": {
            "advice": "General balanced fertilization requires N:P:K in recommended ratios (usually 4:2:1 for cereals, 2:1:1 for vegetables). Always apply nitrogen in split doses. Apply phosphatic fertilizers (DAP/SSP) as basal dose near root zone during sowing.",
            "advice_hi": "सामान्य संतुलित पोषण के लिए N:P:K का उचित अनुपात अपनाएं। यूरिया (नाइट्रोजन) को हमेशा 2-3 किस्तों में दें। डीएपी या एसएसपी को बुवाई के समय बीज के नीचे जड़ क्षेत्र में डालें।"
        }
    }
}

SUGGESTED_PROMPTS = {
    "en": [
        "🌱 How to prepare organic neem spray?",
        "🌧️ Can I spray fungicides during rainy weather?",
        "🧪 What is the correct dosage of Mancozeb?",
        "🍅 How to treat leaf curl in tomato and chilli?",
        "🌾 Best fertilizer schedule for wheat & paddy"
    ],
    "hi": [
        "🌱 जैविक नीम का स्प्रे कैसे बनाएं?",
        "🌧️ क्या बारिश के मौसम में दवा छिड़क सकते हैं?",
        "🧪 मैंकोजेब की सही मात्रा (डोज़) क्या है?",
        "🍅 टमाटर और मिर्च में पत्ती मरोड़ रोग का इलाज?",
        "🌾 गेहूं और धान के लिए खाद की सही मात्रा?"
    ],
    "te": [
        "🌱 వేప నూనె స్ప్రే ఎలా తయారు చేయాలి?",
        "🌧️ వర్షపు కాలంలో మందులు పిచికారీ చేయవచ్చా?",
        "🧪 మాంకోజెబ్ మోతాదు ఎంత?",
        "🍅 టమాట, మిరప ఆకు ముడత నివారణ ఎలా?"
    ],
    "ta": [
        "🌱 வேப்ப எண்ணெய் தெளிப்பது எப்படி?",
        "🌧️ மழைக்காலத்தில் பூச்சிக்கொல்லி அடிக்கலாமா?",
        "🧪 மான்கோசெப் சரியான அளவு என்ன?",
        "🍅 தக்காளி இலை சுருட்டல் நோய் சிகிச்சை?"
    ]
}


def _clean_text(text: str) -> str:
    return re.sub(r'[^\w\s]', ' ', text.lower())


def answer_farmer_query(
    message: str,
    lang: str = "hi",
    crop: Optional[str] = None,
    disease_id: Optional[str] = None,
    history: Optional[List[Dict[str, str]]] = None
) -> Dict[str, Any]:
    """
    Answers farmer queries using domain-specific Agricultural Knowledge Base.
    Generates intelligent localized recommendations for treatments, dosages,
    fertilizers, and weather precautions.
    """
    query_clean = _clean_text(message)
    tokens = set(query_clean.split())

    # 1. Check if Gemini API is available for open generative intelligence
    gemini_key = os.environ.get("GEMINI_API_KEY")
    if gemini_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=gemini_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = (
                f"You are KisanDr AI, an empathetic and highly knowledgeable agricultural scientist "
                f"assisting an Indian farmer. Answer clearly, accurately, and practically in {lang} language.\n"
                f"Context: Crop={crop or 'General'}, Diagnosed Disease={disease_id or 'None'}.\n"
                f"Farmer question: {message}\n"
                f"Format your response with helpful bullet points: Disease/Issue Cause, Organic Remedy, Chemical Dose, and Safety Precautions."
            )
            res = model.generate_content(prompt)
            if res and res.text:
                return {
                    "reply": res.text,
                    "source": "AI Agronomist",
                    "suggestions": SUGGESTED_PROMPTS.get(lang, SUGGESTED_PROMPTS["en"]),
                    "satisfied_prompt": "Did this answer resolve your farm query? / क्या यह उत्तर आपके लिए उपयोगी रहा?"
                }
        except Exception:
            pass  # Seamlessly fallback to offline rule-based knowledge engine

    # 2. Offline Agricultural Knowledge Engine
    reply_lines = []
    
    # Specific disease context provided
    matched_disease = None
    if disease_id and disease_id in CROP_DISEASES:
        matched_disease = CROP_DISEASES[disease_id]
    else:
        # Match disease from message
        for d_id, d_info in CROP_DISEASES.items():
            d_name_tokens = set(_clean_text(d_info["disease_name"]).split())
            if d_name_tokens.intersection(tokens) and len(d_name_tokens.intersection(tokens)) >= 2:
                matched_disease = d_info
                break

    # Check for Crop mentions
    detected_crop = crop
    if not detected_crop or detected_crop == "auto":
        for c in CROPS_LIST:
            c_name = c["name"].lower() if isinstance(c, dict) else str(c).lower()
            c_key = c.get("key", "").lower() if isinstance(c, dict) else ""
            if (c_key and c_key in query_clean) or any(part in query_clean for part in c_name.split("/")):
                detected_crop = c["name"] if isinstance(c, dict) else str(c)
                break

    # Topic A: Neem Oil / Organic Sprays
    if any(k in query_clean for k in ["neem", "organic", "jaivik", "जैविक", "नीम", "వేప", "வேப்ப"]):
        if lang == "hi":
            reply_lines.append("🌿 **प्राकृतिक एवं जैविक उपचार (Organic Remedy):**")
            reply_lines.append(AGRI_KNOWLEDGE["organic_recipes"]["neem_oil"]["recipe_hi"])
            reply_lines.append("\n🥛 **फफूंदनाशक खट्टी छाछ नुस्खा:**")
            reply_lines.append(AGRI_KNOWLEDGE["organic_recipes"]["buttermilk_fungicide"]["recipe_hi"])
        else:
            reply_lines.append("🌿 **Natural Organic Treatment:**")
            reply_lines.append(AGRI_KNOWLEDGE["organic_recipes"]["neem_oil"]["recipe"])
            reply_lines.append("\n🥛 **Bio-Fungicide Buttermilk Spray:**")
            reply_lines.append(AGRI_KNOWLEDGE["organic_recipes"]["buttermilk_fungicide"]["recipe"])

    # Topic B: Leaf Curl / Virus / Whitefly
    elif any(k in query_clean for k in ["curl", "murda", "churda", "मरोड़", "मुडత", "சுருட்டல்"]):
        if lang == "hi":
            reply_lines.append("🍃 **पत्ती मरोड़ रोग (Leaf Curl Virus) नियंत्रण:**")
            reply_lines.append("1. **कारण:** यह रोग सफेद मक्खी (Whitefly) या रस चूसक कीटों द्वारा फैलता है।")
            reply_lines.append("2. **जैविक रोकथाम:** पीले चिपचिपे कार्ड (Yellow Sticky Traps) 15-20 प्रति एकड़ लगाएं। 5ml नीम का तेल प्रति लीटर पानी में मिलाकर स्प्रे करें।")
            reply_lines.append("3. **रासायनिक दवा:** इमिडाक्लोप्रिड 17.8% SL (0.5 मिली/लीटर) या एसिटामिप्रिड 20% SP (0.5 ग्राम/लीटर) का छिड़काव करें।")
            reply_lines.append("4. **सलाह:** गंभीर रूप से ग्रसित पौधों को उखाड़कर तुरंत खेत से दूर नष्ट कर दें।")
        else:
            reply_lines.append("🍃 **Leaf Curl Management Advisory:**")
            reply_lines.append("1. **Cause:** Transmitted by vector pests like whiteflies and thrips.")
            reply_lines.append("2. **Organic Control:** Install 15-20 Yellow Sticky Traps per acre. Spray cold-pressed Neem Oil @ 5ml/L.")
            reply_lines.append("3. **Chemical Vector Control:** Imidacloprid 17.8% SL @ 0.5ml/L or Acetamiprid 20% SP @ 0.5g/L.")
            reply_lines.append("4. **Field Sanitation:** Uproot and burn severely infected viral plants to prevent farm transmission.")

    # Topic C: Rain / Spraying Weather
    elif any(k in query_clean for k in ["rain", "barish", "weather", "spray", "बारिश", "मौसम", "वर्षा", "వాన", "மழை"]):
        if lang == "hi":
            reply_lines.append("🌧️ **वर्षा काल में कीटनाशक व फफूंदनाशक छिड़काव दिशानिर्देश:**")
            reply_lines.append("1. **मौसम का ध्यान:** छिड़काव के बाद कम से कम 2-3 घंटे बारिश नहीं होनी चाहिए, तभी दवा पत्ती पर चिपकती है।")
            reply_lines.append("2. **स्टिकर (स्प्रेडर) का उपयोग:** बरसात के मौसम में दवा के साथ सिलिकॉन आधारित स्टीकर (0.5 मिली/लीटर) अवश्य मिलाएं।")
            reply_lines.append("3. **समय:** सुबह 7 से 10 बजे के बीच या शाम 4 से 6 बजे के बीच ही छिड़काव करें जब धूप मध्यम हो।")
        else:
            reply_lines.append("🌧️ **Monsoon & Rain Spraying Guidelines:**")
            reply_lines.append("1. **Rainfast Window:** Ensure at least 2 to 3 rain-free hours after spraying for foliar absorption.")
            reply_lines.append("2. **Add Wetting Agent (Sticker):** Always mix a silicone-based agricultural spreader/sticker (0.5ml/L) to prevent rain wash-off.")
            reply_lines.append("3. **Timing:** Spray during cool morning hours (7-10 AM) or late afternoon (4-6 PM). Never spray during peak mid-day heat.")

    # Topic D: Fertilizer / Khad / NPK
    elif any(k in query_clean for k in ["fertilizer", "khad", "npk", "urea", "dap", "खाद", "यूरिया", "डीएपी"]):
        if lang == "hi":
            reply_lines.append("🌾 **संतुलित उर्वरक एवं पोषण प्रबंधन:**")
            reply_lines.append("1. **बुवाई के समय:** डीएपी (DAP) या सिंगल सुपर फास्फेट (SSP) + पोटाश की पूरी मात्रा खेत की तैयारी के समय दें।")
            reply_lines.append("2. **यूरिया का प्रयोग:** नाइट्रोजन (यूरिया) को कभी भी एक साथ न डालें। इसे 2 से 3 बराबर किस्तों में टॉप-ड्रेसिंग के रूप में दें।")
            reply_lines.append("3. **सूक्ष्म पोषक तत्व:** जिंक सल्फेट (21%) 10 किलो/एकड़ और बोरॉन का पर्णीय छिड़काव फूल आने से पहले करें।")
        else:
            reply_lines.append("🌾 **Balanced Nutrition & Fertilizer Schedule:**")
            reply_lines.append("1. **Basal Application:** Apply full Phosphatic (DAP/SSP) and Potassic fertilizers at final land preparation.")
            reply_lines.append("2. **Split Nitrogen:** Never dump total Urea in one go. Split into 2-3 equal doses matching crop tillering/vegetative peaks.")
            reply_lines.append("3. **Micronutrients:** Zinc deficiency causes yellowing between veins; spray Chelated Zinc (1g/L) during active growth.")

    # Topic E: Matched Disease from DB or diagnosed leaf
    elif matched_disease:
        d_name = matched_disease.get("disease_name")
        p_name = matched_disease.get("pathogen", "Pathogen")
        p_type = matched_disease.get("pathogen_type", "Fungal")
        org_treatments = matched_disease.get("organic_treatment", [])
        chem_treatments = matched_disease.get("chemical_treatment", [])
        prev_practices = matched_disease.get("preventive_practices", [])

        if lang == "hi":
            reply_lines.append(f"🔍 **पहचान: {d_name}** ({matched_disease.get('crop')} फसल)")
            reply_lines.append(f"• **रोगजनक कारक:** {p_name} ({p_type})")
            reply_lines.append("\n🌱 **जैविक उपचार:**")
            for t in org_treatments[:2]:
                reply_lines.append(f"  - {t}")
            reply_lines.append("\n🧪 **रासायनिक उपचार:**")
            for c in chem_treatments[:2]:
                reply_lines.append(f"  - {c}")
            reply_lines.append("\n🛡️ **रोकथाम:**")
            for p in prev_practices[:2]:
                reply_lines.append(f"  - {p}")
        else:
            reply_lines.append(f"🔍 **Clinical Profile: {d_name}** (Crop: {matched_disease.get('crop')})")
            reply_lines.append(f"• **Causative Pathogen:** {p_name} ({p_type})")
            reply_lines.append("\n🌱 **Organic Remedies:**")
            for t in org_treatments[:2]:
                reply_lines.append(f"  - {t}")
            reply_lines.append("\n🧪 **Chemical Treatments:**")
            for c in chem_treatments[:2]:
                reply_lines.append(f"  - {c}")
            reply_lines.append("\n🛡️ **Preventive Measures:**")
            for p in prev_practices[:2]:
                reply_lines.append(f"  - {p}")

    # General Helpful Agronomy Response
    else:
        if lang == "hi":
            reply_lines.append("👨‍🌾 **नमस्ते किसान भाई! मैं आपका कृषि मित्र (KisanDr Assistant) हूँ।**")
            reply_lines.append("आप मुझसे फसल सुरक्षा, रोग निदान, खाद, जैविक कीटनाशक (नीम स्प्रे, जीवामृत) या मौसम आधारित छिड़काव के बारे में पूछ सकते हैं।")
            reply_lines.append("\n**सुझाव:**")
            reply_lines.append("• फसल की पत्ती का फोटो ऊपर अपलोड करें ताकि मैं सटीक बीमारी पहचान सकूं।")
            reply_lines.append("• या नीचे दिए गए किसी भी प्रश्न पर क्लिक करें:")
        else:
            reply_lines.append("👨‍🌾 **Hello Farmer Friend! I am your KisanDr AI Agronomy Assistant.**")
            reply_lines.append("You can ask me anything about crop diseases, organic remedies, pesticide dosages, fertilizer plans, or weather spray alerts.")
            reply_lines.append("\n**Quick Tip:**")
            reply_lines.append("• Upload a leaf photo above for instant visual diagnosis and customized stage-wise recovery advice.")
            reply_lines.append("• Or click any quick suggested question below:")

    final_reply = "\n".join(reply_lines)
    suggestions = SUGGESTED_PROMPTS.get(lang, SUGGESTED_PROMPTS["en"])

    return {
        "reply": final_reply,
        "source": "KisanDr Agronomy Engine",
        "suggestions": suggestions,
        "satisfied_prompt": "क्या आप इस उत्तर से संतुष्ट हैं? / Was this advice helpful?"
    }
