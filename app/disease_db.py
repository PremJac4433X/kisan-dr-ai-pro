"""
Agricultural Knowledge Base: Crop Disease Database
Contains comprehensive clinical pathology, organic remedies, chemical treatments,
and preventive management for 30+ major crops, fruits, vegetables, cereals, and cash crops.
"""

from typing import Dict, Any, List

CROP_DISEASES: Dict[str, Dict[str, Any]] = {
    # =========================================================================
    # 1. VEGETABLES
    # =========================================================================

    # ------------------ TOMATO ------------------
    "tomato_early_blight": {
        "id": "tomato_early_blight",
        "crop": "Tomato",
        "category": "Vegetables",
        "crop_scientific": "Solanum lycopersicum",
        "disease_name": "Early Blight",
        "pathogen": "Alternaria solani (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Moderate",
        "early_stage_indicators": [
            "Concentric rings ('target board' appearance) on older lower leaves",
            "Yellow halo encircling dark brown to black circular lesions",
            "Lower foliage turns yellow and drops prematurely"
        ],
        "spread_favorable_conditions": "Warm temperatures (24-29°C) combined with high humidity, heavy morning dew, or frequent rain.",
        "organic_remedy": [
            "Spray Neem Seed Kernel Extract (NSKE 5%) or cold-pressed Neem Oil @ 5 ml/liter water with mild soap as emulsifier every 7-10 days.",
            "Apply Trichoderma viride or Trichoderma harzianum bio-fungicide @ 5-10 g/liter of water to foliage and root zone.",
            "Foliar spray with fermented sour buttermilk (1 liter buttermilk in 9 liters water) every 10 days to inhibit fungal germination.",
            "Prune off the lowest 12 inches of foliage to stop soil splashing onto leaves."
        ],
        "chemical_remedy": [
            "First Line: Mancozeb 75% WP @ 2.0 to 2.5 g per liter of water at first symptom appearance.",
            "Alternative / Advanced: Chlorothalonil 75% WP @ 2.0 g/liter or Copper Oxychloride 50% WP @ 3.0 g/liter.",
            "Systemic action (Severe case): Azoxystrobin 23% SC @ 1.0 ml/liter or Difenoconazole 25% EC @ 0.5-1.0 ml/liter.",
            "Safety Interval: Observe a 7-day waiting period between chemical spray and harvest."
        ],
        "preventive_practices": [
            "Implement a 3-year crop rotation avoiding Solanaceous family (Potato, Eggplant, Pepper).",
            "Use drip irrigation rather than overhead sprinklers to keep leaf canopy dry.",
            "Mulch with clean straw or plastic mulch to create a barrier between soil-borne spores and lower leaves.",
            "Stake and space tomato plants at least 45-60 cm apart for adequate air circulation."
        ]
    },
    "tomato_late_blight": {
        "id": "tomato_late_blight",
        "crop": "Tomato",
        "category": "Vegetables",
        "crop_scientific": "Solanum lycopersicum",
        "disease_name": "Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "pathogen_type": "Oomycete / Water Mold",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Water-soaked, pale greenish-grey irregular lesions rapidly expanding on leaf margins",
            "White velvety fungal growth on the underside of infected leaves in humid morning weather",
            "Dark brown blotches on stems with greasy appearance"
        ],
        "spread_favorable_conditions": "Cool (15-20°C) and persistent humid/foggy or rainy conditions (relative humidity > 90%).",
        "organic_remedy": [
            "Spray Bordeaux mixture (1%) or Copper Hydroxide (2.5 g/L) immediately upon symptom detection.",
            "Apply bio-agent Pseudomonas fluorescens @ 10 g/liter water weekly.",
            "Immediately remove and burn/bury severely infected plants to halt field-wide airborne spore epidemics."
        ],
        "chemical_remedy": [
            "Prophylactic / Early stage: Metalaxyl 8% + Mancozeb 64% WP (Ridomil Gold) @ 2.5 g/liter of water.",
            "Active Infection: Dimethomorph 50% WP @ 1.0 g/liter + Mancozeb @ 2.0 g/liter.",
            "Cymoxanil 8% + Mancozeb 64% WP @ 2.0 g/liter with fine mist spray targeting both leaf sides.",
            "Repeat at 7 to 10 day intervals if rainy weather persists."
        ],
        "preventive_practices": [
            "Plant certified disease-free seedlings and resistant cultivars.",
            "Avoid planting adjacent to potato fields.",
            "Strictly avoid sprinkler/overhead irrigation during cool cloudy mornings."
        ]
    },
    "tomato_bacterial_spot": {
        "id": "tomato_bacterial_spot",
        "crop": "Tomato",
        "category": "Vegetables",
        "crop_scientific": "Solanum lycopersicum",
        "disease_name": "Bacterial Spot",
        "pathogen": "Xanthomonas perforans / campestris (Bacteria)",
        "pathogen_type": "Bacterial",
        "severity_level": "Moderate",
        "early_stage_indicators": [
            "Small (less than 3 mm), dark, greasy circular lesions on leaves",
            "Spots look translucent when held against sunlight",
            "Leaf margins develop scorched or ragged edges"
        ],
        "spread_favorable_conditions": "Warm temperatures (25-30°C) accompanied by wind-driven rain or overhead irrigation.",
        "organic_remedy": [
            "Apply liquid copper formulations or Copper soap weekly.",
            "Foliar spray with Bacillus subtilis @ 5 ml/liter.",
            "Avoid handling, pruning, or weeding when the plants are wet."
        ],
        "chemical_remedy": [
            "Spray Copper Oxychloride 50% WP @ 2.5 g/liter tank-mixed with Streptocycline @ 0.1 g/liter (1 g in 10 L).",
            "Kasugamycin 3% SL @ 2.0 ml/liter for systemic bacterial suppression."
        ],
        "preventive_practices": [
            "Hot water seed treatment at 50°C for 25 minutes prior to sowing.",
            "Practice 2-year crop rotation.",
            "Sanitize pruning shears with 10% sodium hypochlorite between rows."
        ]
    },
    "tomato_yellow_leaf_curl": {
        "id": "tomato_yellow_leaf_curl",
        "crop": "Tomato",
        "category": "Vegetables",
        "crop_scientific": "Solanum lycopersicum",
        "disease_name": "Yellow Leaf Curl Virus (TYLCV)",
        "pathogen": "Begomovirus transmitted by Whiteflies (Bemisia tabaci)",
        "pathogen_type": "Viral (Vector-borne)",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Severe upward cupping and curling of leaf margins into boat shape",
            "Interveinal chlorosis (yellowing) with stunted bushy plant growth",
            "Flowers drop prematurely without setting fruit"
        ],
        "spread_favorable_conditions": "Hot, dry conditions promoting explosive Whitefly vector populations.",
        "organic_remedy": [
            "Install Yellow Sticky Traps @ 15-20 traps per acre at crop canopy height.",
            "Spray Neem oil 10,000 PPM @ 2.0 ml/liter or Verticillium lecanii bio-insecticide @ 5 g/liter.",
            "Erect 40-mesh nylon net barrier nurseries to raise virus-free transplants."
        ],
        "chemical_remedy": [
            "Control Whitefly vector: Thiamethoxam 25% WG @ 0.3 g/liter or Imidacloprid 17.8% SL @ 0.5 ml/liter.",
            "Vector rotation: Diafenthiuron 50% WP @ 1.0 g/liter or Spiromesifen 22.9% SC @ 1.0 ml/liter."
        ],
        "preventive_practices": [
            "Rogue out and destroy infected viral plants immediately.",
            "Cultivate TYLCV-tolerant hybrid varieties.",
            "Maintain border rows of maize or sorghum as insect windbreaks."
        ]
    },
    "tomato_healthy": {
        "id": "tomato_healthy",
        "crop": "Tomato",
        "category": "Vegetables",
        "crop_scientific": "Solanum lycopersicum",
        "disease_name": "Healthy Foliage",
        "pathogen": "None (Optimal Vigor)",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Uniform vibrant green foliage with robust venation",
            "No necrotic spots, haloes, or leaf curling observed",
            "Normal turgidity and balanced vegetative-reproductive growth"
        ],
        "spread_favorable_conditions": "Optimal agronomic conditions (20-28°C, balanced moisture, fertile soil).",
        "organic_remedy": [
            "Maintain soil organic carbon with well-decomposed Farm Yard Manure (FYM) or Vermicompost @ 5 tons/acre.",
            "Apply Panchagavya or Jeevamrutha foliar spray (3%) once every 15 days."
        ],
        "chemical_remedy": [
            "No chemical intervention needed.",
            "Balanced N:P:K (19:19:19 @ 5 g/liter) foliar nutrition during active flowering."
        ],
        "preventive_practices": [
            "Consistent regular drip irrigation scheduling.",
            "Routine weekly scout checks on underside of leaves."
        ]
    },

    # ------------------ POTATO ------------------
    "potato_early_blight": {
        "id": "potato_early_blight",
        "crop": "Potato",
        "category": "Vegetables",
        "crop_scientific": "Solanum tuberosum",
        "disease_name": "Early Blight",
        "pathogen": "Alternaria solani (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Moderate",
        "early_stage_indicators": [
            "Target-like dark brown circular to angular spots on lower mature leaflets",
            "Yellow halo around lesions, leaflets turn chlorotic and wither"
        ],
        "spread_favorable_conditions": "Alternating wet and dry periods with temperatures around 20-25°C.",
        "organic_remedy": [
            "Spray Trichoderma viride @ 5 g/liter at tuber bulking stage.",
            "Apply 5% NSKE (Neem seed kernel extract) to fortify plant defense."
        ],
        "chemical_remedy": [
            "Mancozeb 75% WP @ 2.5 g/liter or Propineb 70% WP @ 2.0 g/liter.",
            "For active spread: Difenoconazole 25% EC @ 0.5 ml/liter or Tebuconazole 25.9% EC @ 1.0 ml/liter."
        ],
        "preventive_practices": [
            "Ensure certified disease-free seed tubers.",
            "Proper earthing up to prevent spore wash into daughter tubers.",
            "Practice minimum 2 to 3 years crop rotation."
        ]
    },
    "potato_late_blight": {
        "id": "potato_late_blight",
        "crop": "Potato",
        "category": "Vegetables",
        "crop_scientific": "Solanum tuberosum",
        "disease_name": "Late Blight",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "pathogen_type": "Oomycete / Water Mold",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Water-soaked dark lesions rapidly engulfing tips and margins of leaves",
            "White mildew/cottony growth on underside of leaves under humid mornings",
            "Foul smell from decaying foliage in severely affected fields"
        ],
        "spread_favorable_conditions": "High relative humidity (>85%), temperatures 10-20°C, persistent dew or rain.",
        "organic_remedy": [
            "Preventive spray with Copper oxychloride @ 3 g/liter.",
            "Bio-agent Pseudomonas fluorescens @ 10 g/liter foliar spray.",
            "De-haulming (cutting off top foliage) 10-15 days before harvest if late blight strikes to protect tubers."
        ],
        "chemical_remedy": [
            "Preventive spray: Mancozeb 75% WP @ 2.5 g/liter or Chlorothalonil 75% WP @ 2.0 g/liter.",
            "Curative spray: Cymoxanil 8% + Mancozeb 64% WP @ 2.5 g/liter OR Metalaxyl-M + Mancozeb @ 2.5 g/liter.",
            "Systemic: Fluopicolide + Propamocarb hydrochloride (Infinito) @ 2.5 ml/liter."
        ],
        "preventive_practices": [
            "Store seed tubers in cold storage at 3-4°C.",
            "Monitor local agro-meteorological blight forecast alerts.",
            "Burn or bury infected potato residues deep into the soil."
        ]
    },
    "potato_healthy": {
        "id": "potato_healthy",
        "crop": "Potato",
        "category": "Vegetables",
        "crop_scientific": "Solanum tuberosum",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Lush green, crisp, and robust leaves without discoloration",
            "Smooth leaf surface without lesions or necrotic margins",
            "Healthy stem turgidity and vigorous tuber development"
        ],
        "spread_favorable_conditions": "Cool temperate climate (15-24°C) with well-drained loamy soil.",
        "organic_remedy": [
            "Apply microbial consortium (VAM, Azotobacter, PSB) during earthing up.",
            "Regular compost top dressing."
        ],
        "chemical_remedy": [
            "No chemical fungicides required.",
            "Apply balanced micronutrient foliar spray (Zinc + Boron @ 1.5 g/L) during tuber initiation."
        ],
        "preventive_practices": [
            "Timely earthing-up to insulate developing tubers from sunlight.",
            "Optimal ridge and furrow irrigation without waterlogging."
        ]
    },

    # ------------------ BRINJAL / EGGPLANT ------------------
    "eggplant_phomopsis_blight": {
        "id": "eggplant_phomopsis_blight",
        "crop": "Brinjal / Eggplant",
        "category": "Vegetables",
        "crop_scientific": "Solanum melongena",
        "disease_name": "Phomopsis Blight & Fruit Rot",
        "pathogen": "Phomopsis vexans (Diaporthe vexans) (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Clearly defined circular to irregular brownish spots on lower leaves",
            "Centers of leaf spots turn pale grey with numerous tiny black specks (pycnidia)",
            "Sunken, pale brown, water-soaked rotting spots on fruits"
        ],
        "spread_favorable_conditions": "Warm (28-32°C) and humid weather with frequent showers.",
        "organic_remedy": [
            "Seed treatment with Trichoderma viride @ 4 g/kg seed.",
            "Spray 5% Neem oil emulsion or fermented cow urine decoction every 10 days.",
            "Promptly pick and bury diseased fruits."
        ],
        "chemical_remedy": [
            "Mancozeb 75% WP @ 2.5 g/liter or Copper Oxychloride 50% WP @ 3.0 g/liter.",
            "Carbendazim 50% WP @ 1.0 g/liter or Thiophanate-methyl 70% WP @ 1.0 g/liter.",
            "Spray during early flowering and repeat after 12-14 days."
        ],
        "preventive_practices": [
            "Hot water seed treatment at 50°C for 30 minutes.",
            "Adopt 3-year crop rotation avoiding Solanaceous hosts.",
            "Stake plants to keep branches and fruits off wet soil."
        ]
    },
    "eggplant_little_leaf": {
        "id": "eggplant_little_leaf",
        "crop": "Brinjal / Eggplant",
        "category": "Vegetables",
        "crop_scientific": "Solanum melongena",
        "disease_name": "Little Leaf Disease",
        "pathogen": "Phytoplasma (transmitted by Leafhopper Hishimonus phycitis)",
        "pathogen_type": "Phytoplasma (Vector-borne)",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Severe reduction in leaf size; newly formed leaves are miniature, glabrous and pale green",
            "Internodes become extremely short, giving a dense, bushy 'witch's broom' appearance",
            "Floral parts turn green and leafy (phyllody); plants bear no marketable fruit"
        ],
        "spread_favorable_conditions": "Warm dry conditions favoring high leafhopper vector flight activity.",
        "organic_remedy": [
            "Install yellow sticky traps @ 15/acre to catch vector leafhoppers.",
            "Neem cake application @ 100 kg/acre to soil at planting.",
            "Uproot and burn diseased plants immediately upon visual identification."
        ],
        "chemical_remedy": [
            "Control Leafhopper vector: Dimethoate 30% EC @ 1.7 ml/liter or Imidacloprid 17.8% SL @ 0.5 ml/liter.",
            "Oxytetracycline hydrochloride @ 500 PPM root drenching at early stage."
        ],
        "preventive_practices": [
            "Dip roots of seedlings in Tetracycline hydrochloride (100 PPM) for 15 minutes before transplanting.",
            "Destroy weed hosts (Datura, Solanum nigrum) around field borders."
        ]
    },
    "eggplant_healthy": {
        "id": "eggplant_healthy",
        "crop": "Brinjal / Eggplant",
        "category": "Vegetables",
        "crop_scientific": "Solanum melongena",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Large, broad, pubescent green leaves with vigorous petioles",
            "Uniform violet-purple blossoms and firm developing glossy eggplants"
        ],
        "spread_favorable_conditions": "Warm tropical sunshine (22-30°C) with fertile, well-drained loam.",
        "organic_remedy": [
            "Apply enriched vermicompost with bio-fertilizers (Azospirillum, PSB).",
            "Foliar spray with Panchagavya 3%."
        ],
        "chemical_remedy": [
            "No chemical intervention needed.",
            "Foliar micronutrient mix (Zinc + Boron) to promote flower retention."
        ],
        "preventive_practices": [
            "Regular scout for Shoot & Fruit Borer (Leucinodes orbonalis) using pheromone traps."
        ]
    },

    # ------------------ ONION & GARLIC ------------------
    "onion_purple_blotch": {
        "id": "onion_purple_blotch",
        "crop": "Onion & Garlic",
        "category": "Vegetables",
        "crop_scientific": "Allium cepa",
        "disease_name": "Purple Blotch",
        "pathogen": "Alternaria porri (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Small, sunken, whitish water-soaked flecks on leaves expanding into elliptical lesions",
            "Lesions develop a characteristic purple-brown center surrounded by yellow chlorotic halo",
            "Infected leaves collapse, snap over at the lesion point, and dry up prematurely"
        ],
        "spread_favorable_conditions": "Warm humid conditions (25-30°C) with 80-90% relative humidity and prolonged leaf wetness.",
        "organic_remedy": [
            "Seed treatment with Trichoderma viride @ 5 g/kg seed.",
            "Foliar spray with 5% Neem seed kernel extract + soap spreader.",
            "Sour buttermilk (10%) spray to suppress fungal spore germination."
        ],
        "chemical_remedy": [
            "Mancozeb 75% WP @ 2.5 g/liter + sticker/spreader (Sandovit/Triton @ 0.5 ml/L).",
            "Propiconazole 25% EC @ 1.0 ml/liter or Difenoconazole 25% EC @ 1.0 ml/liter.",
            "Tebuconazole 25.9% EC @ 1.0 ml/liter for systemic suppression."
        ],
        "preventive_practices": [
            "Dip onion seedlings in carbendazim solution (1 g/L) before transplanting.",
            "Maintain raised nursery beds to avoid water stagnation.",
            "Practice 3-year crop rotation avoiding Allium species."
        ]
    },
    "onion_healthy": {
        "id": "onion_healthy",
        "crop": "Onion & Garlic",
        "category": "Vegetables",
        "crop_scientific": "Allium cepa",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Erect, tubular, waxy bluish-green leaves free of spots or thrips silvering",
            "Firm neck development and uniform bulb expansion"
        ],
        "spread_favorable_conditions": "Mild sunny winter weather (13-24°C) with low humidity during bulb maturation.",
        "organic_remedy": [
            "Apply composted poultry manure and wood ash (potash source).",
            "Spray vermiwash (5%) every 2 weeks."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed.",
            "Sulphur (80% WDG) @ 2.5 g/liter basal/foliar nutrition for pungency and storage quality."
        ],
        "preventive_practices": [
            "Stop irrigation 10-15 days prior to bulb harvest to prevent post-harvest neck rot.",
            "Maintain proper bulb curing under shaded ventilation."
        ]
    },

    # ------------------ OKRA / LADY'S FINGER (BHINDI) ------------------
    "okra_yellow_vein_mosaic": {
        "id": "okra_yellow_vein_mosaic",
        "crop": "Okra / Bhindi",
        "category": "Vegetables",
        "crop_scientific": "Abelmoschus esculentus",
        "disease_name": "Yellow Vein Mosaic Virus (YVMV)",
        "pathogen": "Bhendi yellow vein mosaic virus (BYVMV, Whitefly vector)",
        "pathogen_type": "Viral (Vector-borne)",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Network of bright yellow veins on a background of green leaf tissue",
            "Complete vein clearing where leaf blade turns entirely golden-yellow or creamy-white",
            "Fruits become small, hard, yellowish-white, and unmarketable"
        ],
        "spread_favorable_conditions": "Hot, humid monsoon weather supporting heavy whitefly (Bemisia tabaci) populations.",
        "organic_remedy": [
            "Install yellow sticky traps @ 15-20 per acre.",
            "Spray 5% Neem seed kernel extract (NSKE) or Neem oil 10,000 PPM @ 2 ml/liter every 7-10 days.",
            "Uproot and bury virus-infected plants as soon as symptoms emerge."
        ],
        "chemical_remedy": [
            "Control Whitefly vector: Acetamiprid 20% SP @ 0.3 g/liter or Thiamethoxam 25% WG @ 0.35 g/liter.",
            "Alternative vector control: Imidacloprid 17.8% SL @ 0.5 ml/liter."
        ],
        "preventive_practices": [
            "Sow YVMV-resistant varieties (e.g., Arka Anamika, Parbhani Kranti, Varsha Uphar).",
            "Avoid planting during peak whitefly migration seasons.",
            "Erect border rows of tall crops like maize or pearl millet."
        ]
    },
    "okra_healthy": {
        "id": "okra_healthy",
        "crop": "Okra / Bhindi",
        "category": "Vegetables",
        "crop_scientific": "Abelmoschus esculentus",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Deep green lobed palmate leaves without vein discoloration",
            "Prolific yellow blossoms and tender, straight, ribbed pods"
        ],
        "spread_favorable_conditions": "Warm sunny climate (25-35°C) with moist well-drained loam.",
        "organic_remedy": [
            "Top-dress with vermicompost and neem cake (50 kg/acre).",
            "Foliar spray with Panchagavya 3%."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed.",
            "Balanced 19:19:19 foliar spray @ 5 g/liter at 30 and 45 DAS."
        ],
        "preventive_practices": [
            "Frequent harvest every 2-3 days to maintain productive plant vigor."
        ]
    },

    # ------------------ CABBAGE & CAULIFLOWER ------------------
    "cabbage_black_rot": {
        "id": "cabbage_black_rot",
        "crop": "Cabbage & Cauliflower",
        "category": "Vegetables",
        "crop_scientific": "Brassica oleracea",
        "disease_name": "Black Rot",
        "pathogen": "Xanthomonas campestris pv. campestris (Bacteria)",
        "pathogen_type": "Bacterial",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Characteristic V-shaped yellow chlorotic lesions starting at leaf margins with point of 'V' directed toward vein",
            "Veins inside the chlorotic lesions turn dark brown to black",
            "Cross-section of petiole or stem reveals a ring of blackened vascular bundles"
        ],
        "spread_favorable_conditions": "Warm (25-30°C) rainy or windy weather with heavy morning dew.",
        "organic_remedy": [
            "Seed treatment with hot water at 50°C for 25-30 minutes.",
            "Foliar spray with Copper soap or Bordeaux mixture 0.5%."
        ],
        "chemical_remedy": [
            "Spray Copper Oxychloride 50% WP @ 2.5 g/liter tank-mixed with Streptocycline @ 0.1 g/liter.",
            "Kasugamycin 3% SL @ 2.0 ml/liter applied at early V-lesion onset."
        ],
        "preventive_practices": [
            "Practice 3-year crop rotation avoiding Cruciferous crops (radish, mustard, broccoli).",
            "Avoid overhead sprinkler irrigation.",
            "Control flea beetles and root maggots that create bacterial wounds."
        ]
    },
    "cabbage_healthy": {
        "id": "cabbage_healthy",
        "crop": "Cabbage & Cauliflower",
        "category": "Vegetables",
        "crop_scientific": "Brassica oleracea",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Firm, waxy, glaucous green or purple outer wrapper leaves",
            "Tight compact head/curd formation without browning"
        ],
        "spread_favorable_conditions": "Cool temperate conditions (12-20°C) with regular moisture.",
        "organic_remedy": [
            "Incorporate well-rotted farmyard manure.",
            "Spray neem bio-pesticides for diamondback moth (DBM)."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed.",
            "Boron (Solubor @ 1 g/liter) foliar spray to prevent hollow stem and curd browning."
        ],
        "preventive_practices": [
            "Plant mustard as a trap crop for diamondback moth around cabbage plots."
        ]
    },

    # ------------------ CUCUMBER & GOURDS ------------------
    "cucumber_downy_mildew": {
        "id": "cucumber_downy_mildew",
        "crop": "Cucumber & Gourds",
        "category": "Vegetables",
        "crop_scientific": "Cucumis sativus",
        "disease_name": "Downy Mildew",
        "pathogen": "Pseudoperonospora cubensis (Oomycete)",
        "pathogen_type": "Oomycete / Water Mold",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Angular, sharp-edged yellow chlorotic spots strictly bounded by leaf veins on upper leaf surface ('mosaic pattern')",
            "Purplish-grey to brown downy felt growth on the corresponding underside of spots under humid mornings",
            "Leaves curl upward, scorch, and perish rapidly, giving a 'wildfire' appearance"
        ],
        "spread_favorable_conditions": "Cool to moderate temperatures (16-22°C) with persistent high humidity (>85%) or heavy dews.",
        "organic_remedy": [
            "Spray Copper Hydroxide @ 2.0 g/liter or Bordeaux mixture (1%).",
            "Foliar application of Potassium phosphite or bio-agent Bacillus subtilis @ 5 ml/L.",
            "Remove and destroy severely affected lower leaves."
        ],
        "chemical_remedy": [
            "Cymoxanil 8% + Mancozeb 64% WP @ 2.5 g/liter at first symptom.",
            "Metalaxyl-M + Mancozeb @ 2.5 g/liter or Dimethomorph 50% WP @ 1.0 g/liter.",
            "Famoxadone + Cymoxanil @ 1.0 g/liter with thorough under-leaf coverage."
        ],
        "preventive_practices": [
            "Trellis cucurbit vines to improve aeration and prevent ground contact.",
            "Use drip irrigation under mulch.",
            "Plant downy-mildew tolerant hybrid varieties."
        ]
    },
    "cucumber_healthy": {
        "id": "cucumber_healthy",
        "crop": "Cucumber & Gourds",
        "category": "Vegetables",
        "crop_scientific": "Cucumis sativus",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Large, crisp, heart-shaped or palmate green leaves without chlorotic mosaics",
            "Abundant yellow male/female blooms and straight, crisp green cucumbers"
        ],
        "spread_favorable_conditions": "Warm sunny weather (20-30°C) with consistent drip moisture.",
        "organic_remedy": [
            "Side dress with vermicompost and rock phosphate.",
            "Foliar spray with fermented seaweed extract."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed."
        ],
        "preventive_practices": [
            "Hand pollination or encourage bee activity for optimal fruit set."
        ]
    },

    # ------------------ GINGER & TURMERIC ------------------
    "ginger_rhizome_rot": {
        "id": "ginger_rhizome_rot",
        "crop": "Ginger & Turmeric",
        "category": "Vegetables",
        "crop_scientific": "Zingiber officinale",
        "disease_name": "Rhizome Rot / Soft Rot",
        "pathogen": "Pythium aphanidermatum / myriotylum (Oomycete)",
        "pathogen_type": "Oomycete / Water Mold",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Water-soaked yellowing of leaf margins advancing to central blade, starting from lower leaves",
            "Base of the pseudostem becomes soft, water-soaked, and easily pulls away with a gentle tug",
            "Infected rhizomes become mushy, foul-smelling, and rot entirely in the soil"
        ],
        "spread_favorable_conditions": "Heavy monsoon rains, waterlogged soils, and temperatures around 28-32°C.",
        "organic_remedy": [
            "Seed rhizome treatment with Trichoderma harzianum @ 10 g/kg rhizome.",
            "Soil drenching with Pseudomonas fluorescens @ 20 g/liter.",
            "Soil solarization of beds with transparent polythene film for 30 days during summer."
        ],
        "chemical_remedy": [
            "Seed rhizome dip in Metalaxyl 8% + Mancozeb 64% WP @ 3.0 g/liter for 30 minutes before planting.",
            "Soil drenching with Copper Oxychloride 50% WP @ 3.0 g/liter or Metalaxyl @ 2.5 g/liter at first sign of yellowing."
        ],
        "preventive_practices": [
            "Provide raised beds (15 cm high) with deep drainage channels to prevent water stagnation.",
            "Select healthy, plump, certified disease-free seed rhizomes.",
            "Rotate with non-host crops like maize or finger millet."
        ]
    },
    "ginger_healthy": {
        "id": "ginger_healthy",
        "crop": "Ginger & Turmeric",
        "category": "Vegetables",
        "crop_scientific": "Zingiber officinale",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Erect, lush, deep-green reed-like foliage with upright pseudostems",
            "Clean stem bases with solid firm aromatic underground rhizomes"
        ],
        "spread_favorable_conditions": "Warm, humid tropical climate with partial shade and rich organic loam.",
        "organic_remedy": [
            "Heavy mulching with green leaves (10-12 tons/acre) in 3 splits.",
            "Farmyard manure enriched with VAM."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed."
        ],
        "preventive_practices": [
            "Timely application of green leaf mulch to conserve moisture and suppress weeds."
        ]
    },

    # ------------------ BELL PEPPER / CHILLI ------------------
    "pepper_bacterial_spot": {
        "id": "pepper_bacterial_spot",
        "crop": "Bell Pepper / Chilli",
        "category": "Vegetables",
        "crop_scientific": "Capsicum annuum",
        "disease_name": "Bacterial Leaf Spot",
        "pathogen": "Xanthomonas euvesicatoria (Bacteria)",
        "pathogen_type": "Bacterial",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Small, yellow-green spots on young leaves that turn brownish-black with water-soaked margins",
            "Spots on leaf underside look slightly raised or blister-like",
            "Extensive leaf drop leading to sun-scalded developing peppers"
        ],
        "spread_favorable_conditions": "High temperatures (24-32°C) combined with frequent rainfall or heavy dew.",
        "organic_remedy": [
            "Apply Copper Octanoate (Copper soap) or Copper Hydroxide @ 2.5 g/liter every 7-10 days.",
            "Spray bio-control agent Bacillus subtilis @ 5 g/liter.",
            "Mulch bed with silver-on-black reflective plastic mulch."
        ],
        "chemical_remedy": [
            "Copper Oxychloride 50% WP @ 2.5 g/liter + Streptocycline @ 0.1 g/liter (1 g in 10 L water).",
            "Kasugamycin 3% SL @ 2.0 ml/liter for systemic prevention."
        ],
        "preventive_practices": [
            "Hot water soak seed at 50°C for 25 minutes prior to sowing.",
            "Rotate fields with non-solanaceous crops for 2 years."
        ]
    },
    "pepper_healthy": {
        "id": "pepper_healthy",
        "crop": "Bell Pepper / Chilli",
        "category": "Vegetables",
        "crop_scientific": "Capsicum annuum",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Glossy dark-green lanceolate leaves without spotting or leaf curl",
            "Stout upright stem with vigorous white blossom production",
            "Crisp, firm, well-proportioned bell peppers or chilli pods"
        ],
        "spread_favorable_conditions": "Warm climate (20-30°C) with balanced moisture and well-aerated sandy-loam soil.",
        "organic_remedy": [
            "Top-dress with vermicompost and Neem cake powder (50 kg/acre).",
            "Spray Panchagavya (3%) every 2 weeks."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed.",
            "Calcium Nitrate @ 5 g/liter spray to prevent Blossom End Rot."
        ],
        "preventive_practices": [
            "Maintain consistent soil moisture through drip irrigation."
        ]
    },

    # =========================================================================
    # 2. FRUITS
    # =========================================================================

    # ------------------ MANGO ------------------
    "mango_anthracnose": {
        "id": "mango_anthracnose",
        "crop": "Mango",
        "category": "Fruits",
        "crop_scientific": "Mangifera indica",
        "disease_name": "Anthracnose & Blossom Blight",
        "pathogen": "Colletotrichum gloeosporioides (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Small, circular to angular, dark brown necrotic spots on tender young leaves",
            "Spots coalesce into irregular holes ('shot hole' effect) as dead tissue drops out",
            "Panicle blight: Black necrotic lesions on blossom clusters causing total blossom drop",
            "Tear-staining and black sunken rot lesions on ripening mango fruit"
        ],
        "spread_favorable_conditions": "Warm humid conditions (24-30°C) with >90% humidity or frequent showers during flowering.",
        "organic_remedy": [
            "Prune dead twigs and sanitize canopy 2-3 months before flowering.",
            "Spray bio-fungicide Bacillus subtilis @ 5 g/liter.",
            "Hot water fruit dip at 52°C for 10 minutes post-harvest to control latent infections."
        ],
        "chemical_remedy": [
            "Pre-bloom & Blossom stage: Carbendazim 50% WP @ 1.0 g/liter or Mancozeb 75% WP @ 2.5 g/liter.",
            "Active infection: Azoxystrobin 23% SC @ 1.0 ml/liter or Difenoconazole 25% EC @ 0.75 ml/liter.",
            "Copper Oxychloride 50% WP @ 3.0 g/liter during rainy season flush."
        ],
        "preventive_practices": [
            "Post-harvest canopy pruning to open center for sunlight and rapid drying.",
            "Avoid orchard intercropping with susceptible solanaceous or cucurbit hosts."
        ]
    },
    "mango_powdery_mildew": {
        "id": "mango_powdery_mildew",
        "crop": "Mango",
        "category": "Fruits",
        "crop_scientific": "Mangifera indica",
        "disease_name": "Powdery Mildew",
        "pathogen": "Oidium mangiferae (Acrosporium mangiferae) (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "White powdery talcum-like superficial patches on panicles, flowers, and tender young leaves",
            "Infected flowers turn dark brown, fail to open, and shed prematurely (up to 70-80% crop loss)",
            "Young fruitlets drop or develop russeted corky cracked skin"
        ],
        "spread_favorable_conditions": "Cool cloudy nights with warm days (15-26°C) and moderate relative humidity (65-80%) during flowering (Dec-March).",
        "organic_remedy": [
            "Wettable Sulfur (80% WDG) @ 2.5 g/liter at bud swell.",
            "Potassium bicarbonate (3 g/L) + Neem oil (3 ml/L) foliar spray."
        ],
        "chemical_remedy": [
            "Hexaconazole 5% EC @ 1.5 ml/liter or Penconazole 10% EC @ 0.5 ml/liter.",
            "Dinocap 48% EC @ 1.0 ml/liter or Tebuconazole 25.9% EC @ 1.0 ml/liter.",
            "First spray at panicle emergence, second at 50% bloom, third at pea-size fruit set."
        ],
        "preventive_practices": [
            "Scout flower panicles weekly starting at bud burst.",
            "Prune overcrowded center branches for maximum wind and sun penetration."
        ]
    },
    "mango_healthy": {
        "id": "mango_healthy",
        "crop": "Mango",
        "category": "Fruits",
        "crop_scientific": "Mangifera indica",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Deep glossy dark-green lanceolate leaves free of powder, soot, or holes",
            "Healthy copper-bronze new vegetative flushes maturing smoothly into emerald green",
            "Clean flower panicles and heavy retention of developing fruits"
        ],
        "spread_favorable_conditions": "Tropical and subtropical dry seasons during flowering and fruit ripening.",
        "organic_remedy": [
            "Annual application of 50 kg well-decomposed FYM + 2 kg bone meal per mature tree.",
            "Foliar spray with Panchagavya 3%."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed.",
            "Foliar Potassium Nitrate (13:00:45) @ 10 g/liter to induce uniform flowering."
        ],
        "preventive_practices": [
            "Prune criss-cross branches after annual harvest.",
            "Wrap tree trunk with polythene band (40 cm wide) in Dec to prevent mealybug ascent."
        ]
    },

    # ------------------ BANANA ------------------
    "banana_sigatoka": {
        "id": "banana_sigatoka",
        "crop": "Banana",
        "category": "Fruits",
        "crop_scientific": "Musa acuminata",
        "disease_name": "Black / Yellow Sigatoka",
        "pathogen": "Pseudocercospora fijiensis / musae (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Tiny, yellowish-brown or reddish-brown narrow streaks parallel to leaf veins",
            "Streaks enlarge into elliptical spots with sunken greyish-white centers and dark brown borders",
            "Large areas of leaf blade become prematurely necrotic and dry up, reducing bunch filling by 50%"
        ],
        "spread_favorable_conditions": "High temperatures (25-30°C), heavy rainfall, high relative humidity (>85%), and thick morning dew.",
        "organic_remedy": [
            "De-trashing: Systematically cut off severely diseased leaf sections and place face down on soil to speed decay.",
            "Mineral oil / Agricultural spray oil (1%) emulsion with Neem oil (0.5%).",
            "Spray bio-agent Pseudomonas fluorescens @ 10 g/liter."
        ],
        "chemical_remedy": [
            "Propiconazole 25% EC @ 1.0 ml/liter + 1% petroleum spray oil emulsified with detergent.",
            "Azoxystrobin 18.2% + Difenoconazole 11.4% SC @ 1.0 ml/liter.",
            "Mancozeb 75% WP @ 2.5 g/liter alternated to manage fungal resistance."
        ],
        "preventive_practices": [
            "Maintain optimal plant spacing (1.8m x 1.8m) to facilitate fast drying.",
            "Ensure effective drainage canals between rows to prevent water stagnation.",
            "Keep plantation weed-free."
        ]
    },
    "banana_panama_wilt": {
        "id": "banana_panama_wilt",
        "crop": "Banana",
        "category": "Fruits",
        "crop_scientific": "Musa acuminata",
        "disease_name": "Panama Wilt (Fusarium Wilt)",
        "pathogen": "Fusarium oxysporum f. sp. cubense (Fungus)",
        "pathogen_type": "Fungal (Soil-borne)",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Yellowing of lower leaf margins progressing inward toward the midrib",
            "Buckling or breaking of petiole at the junction with pseudostem; dead leaves hang skirt-like around stem",
            "Longitudinal splitting of pseudostem base and reddish-brown to black vascular discoloration inside corm"
        ],
        "spread_favorable_conditions": "Warm sandy acidic soils (pH 5.5-6.5), soil nematodes, and poor drainage.",
        "organic_remedy": [
            "Apply Trichoderma viride enriched FYM (5 kg/plant) at planting and 3rd month.",
            "Neem cake @ 250 g/plant in planting pit.",
            "Apply lime @ 1-2 kg/pit in acidic soils to raise pH above 7.0."
        ],
        "chemical_remedy": [
            "Capsule application of 2,4-D or Carbendazim (50 mg) into the pseudostem.",
            "Corm injection with Carbendazim 2% (20 ml) or soil drenching with Carbendazim @ 2 g/liter."
        ],
        "preventive_practices": [
            "Plant tissue-culture disease-free plantlets.",
            "Grow tolerant varieties like Grand Naine instead of highly susceptible Gros Michel/Malbhog.",
            "Strictly avoid moving suckers from wilt-infected plantations."
        ]
    },
    "banana_healthy": {
        "id": "banana_healthy",
        "crop": "Banana",
        "category": "Fruits",
        "crop_scientific": "Musa acuminata",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Expansive, broad, undamaged green paddle leaves emerging in quick succession",
            "Stout, upright pseudostem and large, heavy, symmetrical fruit bunch development"
        ],
        "spread_favorable_conditions": "Warm humid tropics with abundant rainfall and deep fertile organic soil.",
        "organic_remedy": [
            "Heavy mulching with banana pseudo-stems and dry leaves.",
            "Apply 20 kg FYM + 250 g bio-NPK consortium per plant."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed.",
            "Apply Potassium (MOP) in split doses to maximize bunch weight and finger length."
        ],
        "preventive_practices": [
            "De-suckering: Retain only 1 mother plant and 1 follower sucker for optimal bunch nutrition.",
            "Propping bunches with bamboo poles to prevent lodging under wind."
        ]
    },

    # ------------------ CITRUS (LEMON / ORANGE / LIME) ------------------
    "citrus_canker": {
        "id": "citrus_canker",
        "crop": "Citrus (Lemon / Orange)",
        "category": "Fruits",
        "crop_scientific": "Citrus spp.",
        "disease_name": "Citrus Canker",
        "pathogen": "Xanthomonas axonopodis pv. citri (Bacteria)",
        "pathogen_type": "Bacterial",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Small, raised, blister-like corky lesions with oily margins on leaves and twigs",
            "Prominent bright yellow chlorotic halo surrounding brown crater-like eruptions",
            "Fruit exhibits rough, raised, corky scabs that crack open, reducing fresh market value"
        ],
        "spread_favorable_conditions": "Warm rainy weather (25-35°C), high winds, and Citrus Leaf Miner insect tunneling wounds.",
        "organic_remedy": [
            "Prune infected twigs during dry season before flush and burn them.",
            "Spray 1% Bordeaux mixture at new leaf flush.",
            "Neem oil (0.5%) spray to suppress leaf miner pests that create bacterial entry portals."
        ],
        "chemical_remedy": [
            "Copper Oxychloride 50% WP @ 3.0 g/liter + Streptocycline @ 0.1 g/liter (1 g in 10 L water).",
            "Spray first at new vegetative flush, second after petal fall, and third at fruit pea size.",
            "Control leaf miner: Imidacloprid 17.8% SL @ 0.5 ml/liter."
        ],
        "preventive_practices": [
            "Plant windbreak trees (Casuarina, Sesbania) around citrus orchards to diminish wind-driven splash.",
            "Disinfect harvesting shears and pruning tools with 10% sodium hypochlorite."
        ]
    },
    "citrus_greening_hlb": {
        "id": "citrus_greening_hlb",
        "crop": "Citrus (Lemon / Orange)",
        "category": "Fruits",
        "crop_scientific": "Citrus spp.",
        "disease_name": "Citrus Greening (Huanglongbing - HLB)",
        "pathogen": "Candidatus Liberibacter asiaticus (transmitted by Asian Citrus Psyllid)",
        "pathogen_type": "Bacterial (Phloem-limited, Vector-borne)",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Asymmetrical blotchy mottle on leaves (one side of leaf vein is green while other side is chlorotic)",
            "Yellow shoots ('yellow dragon') standing out against otherwise green canopy",
            "Fruits remain small, lopsided, poorly colored (green at bottom) with bitter, salty taste and aborted dark seeds"
        ],
        "spread_favorable_conditions": "Mild to warm climate supporting Asian Citrus Psyllid (Diaphorina citri) vectors.",
        "organic_remedy": [
            "Install yellow sticky traps @ 20/acre to monitor psyllid flights.",
            "Spray Neem oil 1% or horticultural oil to coat psyllid nymphs.",
            "Uproot and destroy confirmed HLB-positive trees to halt orchard-wide spread."
        ],
        "chemical_remedy": [
            "Aggressive psyllid vector control: Thiamethoxam 25% WG @ 0.4 g/liter or Dimethoate 30% EC @ 1.5 ml/liter.",
            "Foliar micro-nutrient complex (Zinc, Iron, Manganese, Boron) to alleviate phloem block stress."
        ],
        "preventive_practices": [
            "Use only certified disease-free budwood and rootstock from screenhouses.",
            "Eradicate wild alternative host plants (Murraya paniculata / Mock orange) near orchards."
        ]
    },
    "citrus_healthy": {
        "id": "citrus_healthy",
        "crop": "Citrus (Lemon / Orange)",
        "category": "Fruits",
        "crop_scientific": "Citrus spp.",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Glossy, dark green, aromatic unblemished leaves with distinct winged petioles",
            "Smooth green shoots without cankers, gummosis, or dieback",
            "Uniform blossom set and vibrant developing citrus fruits"
        ],
        "spread_favorable_conditions": "Subtropical warm days with cool nights and well-aerated sandy-loam soil.",
        "organic_remedy": [
            "Annual compost application around tree drip line.",
            "Bio-fertilizer consortium (VAM, Azotobacter, PSB)."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed.",
            "Foliar spray of Zinc Sulphate (0.5%) + Magnesium Sulphate (0.5%) to prevent interveinal chlorosis."
        ],
        "preventive_practices": [
            "Paint tree trunks with Bordeaux paste up to 60 cm height to prevent Phytophthora gummosis."
        ]
    },

    # ------------------ PAPAYA ------------------
    "papaya_ring_spot": {
        "id": "papaya_ring_spot",
        "crop": "Papaya",
        "category": "Fruits",
        "crop_scientific": "Carica papaya",
        "disease_name": "Papaya Ring Spot Virus (PRSV)",
        "pathogen": "Papaya ringspot potyvirus (PRSV, Aphid vector)",
        "pathogen_type": "Viral (Vector-borne)",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Yellow vein clearing and severe mosaic mottling on young leaf canopy",
            "Leaves become severely blistered, strap-like, or shoe-stringed with reduced blade area",
            "Water-soaked dark green greasy streaks on petioles and upper trunk",
            "Prominent concentric dark green rings ('doughnut spots') on fruit skin"
        ],
        "spread_favorable_conditions": "Warm dry periods promoting rapid Aphid (Aphis gossypii, Myzus persicae) migration.",
        "organic_remedy": [
            "Intercrop with barrier crops: 2-3 border rows of maize, sorghum, or castor around papaya field.",
            "Spray cold-pressed Neem oil (5 ml/L) weekly to deter transient aphid vectors.",
            "Immediately roguing and burning virus-affected plants."
        ],
        "chemical_remedy": [
            "Chemical sprays do not cure PRSV; control aphid vectors: Dimethoate 30% EC @ 1.5 ml/liter or Imidacloprid 17.8% SL @ 0.5 ml/liter.",
            "Zinc Sulphate (0.5%) + Borax (0.1%) foliar spray to bolster plant vitality."
        ],
        "preventive_practices": [
            "Raise papaya seedlings inside insect-proof net screenhouses.",
            "Cultivate PRSV-tolerant varieties.",
            "Avoid planting cucurbits (pumpkin, cucumber) near papaya as they host aphids and PRSV."
        ]
    },
    "papaya_healthy": {
        "id": "papaya_healthy",
        "crop": "Papaya",
        "category": "Fruits",
        "crop_scientific": "Carica papaya",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Expansive, deeply palmately-lobed bright green leaves with long hollow petioles",
            "Strong single upright trunk without streaks or cankers",
            "Dense spiral fruit set at leaf axils without rings or deformities"
        ],
        "spread_favorable_conditions": "Tropical sunshine (25-35°C), frost-free, with deep well-drained fertile loam.",
        "organic_remedy": [
            "Apply 20 kg FYM + 2 kg neem cake per tree annually.",
            "Bio-fertilizer root drench with Trichoderma."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed.",
            "Boron (0.1%) spray to prevent bumpy fruit syndrome."
        ],
        "preventive_practices": [
            "Ensure elevated planting mounds to protect root collar from waterlogging and collar rot."
        ]
    },

    # ------------------ POMEGRANATE ------------------
    "pomegranate_bacterial_blight": {
        "id": "pomegranate_bacterial_blight",
        "crop": "Pomegranate",
        "category": "Fruits",
        "crop_scientific": "Punica granatum",
        "disease_name": "Bacterial Blight (Oily Spot / Telya)",
        "pathogen": "Xanthomonas axonopodis pv. punicae (Bacteria)",
        "pathogen_type": "Bacterial",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Small, water-soaked, translucent dark spots on leaves turning brown to black with oily appearance",
            "Spots on fruit surface turn into characteristic dark brown-black 'L' or 'Y' shaped cracked lesions",
            "Stem cankers causing girdle and sudden branch dieback ('nodal blight')"
        ],
        "spread_favorable_conditions": "Warm humid cloudy weather (25-35°C) with persistent monsoon drizzle and high humidity (>80%).",
        "organic_remedy": [
            "Rigorous pruning of diseased twigs followed by immediate Bordeaux paste (10%) application on cut ends.",
            "Foliar spray with Copper Hydroxide (2.5 g/L).",
            "Collect and burn all fallen leaves, flowers, and infected fruits."
        ],
        "chemical_remedy": [
            "Bordeaux mixture (1%) or Copper Oxychloride 50% WP @ 2.5 g/liter + Streptocycline @ 0.5 g/liter.",
            "Kasugamycin 3% SL @ 2.0 ml/liter or Bronopol (2-bromo-2-nitropropane-1,3-diol) @ 0.5 g/liter.",
            "Spray at 10-12 day intervals throughout monsoon and active flushing."
        ],
        "preventive_practices": [
            "Select tissue-culture disease-free saplings.",
            "Sterilize secateurs with 10% sodium hypochlorite between plants.",
            "Adopt 'Hasta Bahar' flowering season (Sept-Oct) to escape peak monsoon bacterial blight."
        ]
    },
    "pomegranate_healthy": {
        "id": "pomegranate_healthy",
        "crop": "Pomegranate",
        "category": "Fruits",
        "crop_scientific": "Punica granatum",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Glossy, narrow, oblong, vibrant green leaves with reddish young twigs",
            "Showy orange-red trumpet flowers and smooth, round, crack-free developing fruits"
        ],
        "spread_favorable_conditions": "Semi-arid warm dry conditions (25-38°C) with well-drained loamy soil.",
        "organic_remedy": [
            "Apply well-decomposed FYM (20 kg/plant) and vermicompost.",
            "Soil drench with VAM."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed.",
            "Foliar spray of Calcium Nitrate (0.5%) + Boron (0.1%) during fruit development to prevent fruit cracking."
        ],
        "preventive_practices": [
            "Regulate bahar treatment by controlled water withholding followed by balanced fertilization."
        ]
    },

    # ------------------ GUAVA ------------------
    "guava_wilt": {
        "id": "guava_wilt",
        "crop": "Guava",
        "category": "Fruits",
        "crop_scientific": "Psidium guajava",
        "disease_name": "Guava Wilt",
        "pathogen": "Fusarium oxysporum f. sp. psidii (Fungus)",
        "pathogen_type": "Fungal (Soil-borne)",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Light yellowing of foliage with dull green appearance on one branch or whole tree",
            "Leaves droop, turn yellow-red, curl, and senesce prematurely",
            "Bark of stem base splits longitudinally and xylem vessels show dark vascular discoloration"
        ],
        "spread_favorable_conditions": "High soil moisture, poorly drained heavy clay or alkaline soils (pH > 7.5), and root knot nematode injury.",
        "organic_remedy": [
            "Apply Trichoderma viride or T. harzianum enriched FYM (5-10 kg/tree) in tree basin.",
            "Neem cake @ 2 kg/tree to manage root knot nematodes.",
            "Apply gypsum or sulfur to lower alkalinity in alkaline soils."
        ],
        "chemical_remedy": [
            "Soil drenching with Carbendazim 50% WP @ 2.0 g/liter or Propiconazole 25% EC @ 1.5 ml/liter in the root zone.",
            "Trunk injection with 0.1% Carbendazim at early onset of leaf yellowing."
        ],
        "preventive_practices": [
            "Plant resistant rootstocks (Psidium cattleianum / Chinese guava).",
            "Provide deep drainage trenches between tree rows.",
            "Solarize planting pits before introducing new guava saplings."
        ]
    },
    "guava_healthy": {
        "id": "guava_healthy",
        "crop": "Guava",
        "category": "Fruits",
        "crop_scientific": "Psidium guajava",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Elliptic, aromatic, leathery dark-green leaves with prominent veins",
            "Smooth copper-colored peeling bark and vigorous flowering and fruit set"
        ],
        "spread_favorable_conditions": "Tropical to subtropical climate (20-32°C) with moderate water requirement.",
        "organic_remedy": [
            "Farmyard manure @ 25 kg/tree annually.",
            "Foliar spray with Panchagavya 3%."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed.",
            "Foliar Zinc Sulphate (0.5%) to avoid small leaf 'bronzing' disorder."
        ],
        "preventive_practices": [
            "Annual pruning of terminal 10-15 cm shoots after harvesting to induce productive lateral flushes."
        ]
    },

    # ------------------ STRAWBERRY ------------------
    "strawberry_leaf_scorch": {
        "id": "strawberry_leaf_scorch",
        "crop": "Strawberry",
        "category": "Fruits",
        "crop_scientific": "Fragaria × ananassa",
        "disease_name": "Leaf Scorch",
        "pathogen": "Diplocarpon earlianum (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Moderate",
        "early_stage_indicators": [
            "Small, irregular purple to dark brown blotches scattered over the upper leaf surface",
            "Blotches enlarge without distinct white centers (differentiating it from leaf spot), causing margins to curl up and look scorched or burned",
            "Calyx (green fruit caps) turn brown and dry, ruining berry appeal"
        ],
        "spread_favorable_conditions": "Prolonged leaf wetness, overhead irrigation, and temperatures between 18-25°C.",
        "organic_remedy": [
            "Remove and compost or burn scorched older leaves after harvest.",
            "Apply Copper Octanoate (Copper soap) @ 2.5 ml/L.",
            "Bio-fungicide spray with Bacillus subtilis."
        ],
        "chemical_remedy": [
            "Captan 50% WP @ 2.0 g/liter or Thiophanate-methyl 70% WP @ 1.0 g/liter.",
            "Azoxystrobin 23% SC @ 0.8 ml/liter or Pyraclostrobin @ 1.0 g/liter.",
            "Spray early in spring at first flush of new leaves."
        ],
        "preventive_practices": [
            "Use black plastic mulch to insulate leaves and fruit from wet soil.",
            "Use drip irrigation under mulch exclusively.",
            "Ensure wide spacing (30 cm) on raised beds for rapid canopy drying."
        ]
    },
    "strawberry_healthy": {
        "id": "strawberry_healthy",
        "crop": "Strawberry",
        "category": "Fruits",
        "crop_scientific": "Fragaria × ananassa",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Lush trifoliate serrated emerald-green leaves free of spots or mildew",
            "Healthy runners, clean white blossoms, and bright red conical strawberries"
        ],
        "spread_favorable_conditions": "Cool temperate sunshine (15-22°C) with rich organic soil and consistent moisture.",
        "organic_remedy": [
            "Top-dress with composted worm castings and bone meal.",
            "Straw mulching around crowns."
        ],
        "chemical_remedy": [
            "No chemical intervention needed."
        ],
        "preventive_practices": [
            "Never bury strawberry crowns beneath soil during planting."
        ]
    },

    # ------------------ APPLE ------------------
    "apple_scab": {
        "id": "apple_scab",
        "crop": "Apple",
        "category": "Fruits",
        "crop_scientific": "Malus domestica",
        "disease_name": "Apple Scab",
        "pathogen": "Venturia inaequalis (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Olive-green, velvety, circular spots with indistinct margins on young leaves",
            "Lesions turn metallic dark brown/black and leaves become crinkled and distorted",
            "Fruit develops scabbed corky lesions that crack and ruin marketability"
        ],
        "spread_favorable_conditions": "Cool (13-24°C), wet, rainy spring days with sustained leaf wetness for 9+ hours.",
        "organic_remedy": [
            "Spray Lime Sulfur (3%) during dormancy / green tip stage.",
            "Apply Copper soap or Potassium bicarbonate @ 3 g/liter at bud break.",
            "Compost fallen autumn leaves with 5% urea spray."
        ],
        "chemical_remedy": [
            "Preventive: Mancozeb 75% WP @ 2.5 g/liter or Captan 50% WP @ 2.5 g/liter.",
            "Curative: Difenoconazole 25% EC @ 0.3 ml/liter or Kresoxim-methyl 44.3% SC @ 0.5 ml/liter.",
            "Systemic: Trifloxystrobin 25% + Tebuconazole 50% WG @ 0.4 g/liter."
        ],
        "preventive_practices": [
            "Prune canopy annually to optimize sunlight penetration and fast leaf drying.",
            "Plant scab-resistant cultivars."
        ]
    },
    "apple_black_rot": {
        "id": "apple_black_rot",
        "crop": "Apple",
        "category": "Fruits",
        "crop_scientific": "Malus domestica",
        "disease_name": "Black Rot (Frogeye Leaf Spot)",
        "pathogen": "Botryosphaeria obtusa (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Moderate",
        "early_stage_indicators": [
            "Small purple spots on leaves expanding into circular lesions with light brown center ('frogeye')",
            "Black rotting cankers on branches and limbs",
            "Fruit exhibits concentric brown/black rotting rings"
        ],
        "spread_favorable_conditions": "Warm humid conditions (20-27°C) following rainy periods in spring.",
        "organic_remedy": [
            "Prune and burn dead wood, cankered limbs, and mummified fruits.",
            "Apply Copper Octanoate or Bordeaux mixture during dormant season."
        ],
        "chemical_remedy": [
            "Captan 50% WP @ 2.5 g/liter or Thiophanate-methyl 70% WP @ 1.0 g/liter.",
            "Pyraclostrobin + Boscalid @ 0.8 g/liter at petal fall."
        ],
        "preventive_practices": [
            "Sterilize pruning tools with 70% rubbing alcohol between trees."
        ]
    },
    "apple_healthy": {
        "id": "apple_healthy",
        "crop": "Apple",
        "category": "Fruits",
        "crop_scientific": "Malus domestica",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Broad, glossy green leaves with serrated margins free of spots or powdery film",
            "Vigorous spur growth and balanced annual shoot extension",
            "Clean smooth bark without cankers or gummosis"
        ],
        "spread_favorable_conditions": "Temperate climate with adequate winter chilling hours and sunny summers.",
        "organic_remedy": [
            "Apply rich organic compost around tree drip line in early winter.",
            "Bio-fungicide root drench with Trichoderma harzianum."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed.",
            "Foliar calcium nitrate spray (0.5%) during fruit development."
        ],
        "preventive_practices": [
            "Annual canopy training (Central leader system)."
        ]
    },

    # ------------------ GRAPE ------------------
    "grape_black_rot": {
        "id": "grape_black_rot",
        "crop": "Grape",
        "category": "Fruits",
        "crop_scientific": "Vitis vinifera",
        "disease_name": "Black Rot",
        "pathogen": "Guignardia bidwellii (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Small circular reddish-brown leaf spots with dark margins and tiny black pycnidia specks in a ring",
            "Infected berries shrivel into hard, black, wrinkled mummies in clusters ('raisin effect')"
        ],
        "spread_favorable_conditions": "Warm (20-27°C) weather with frequent rain and high relative humidity.",
        "organic_remedy": [
            "Dormant Bordeaux mixture (1%) spray on vines and trellis posts.",
            "Remove all mummified berries from vines and ground.",
            "Apply Copper Hydroxide @ 2.5 g/liter early in spring."
        ],
        "chemical_remedy": [
            "Mancozeb 75% WP @ 2.5 g/liter from bud break to bloom.",
            "Myclobutanil 10% WP @ 1.0 g/liter or Tebuconazole 25.9% EC @ 0.75 ml/liter.",
            "Kresoxim-methyl 44.3% SC @ 0.7 ml/liter."
        ],
        "preventive_practices": [
            "Canopy management: Leaf pulling around fruit zone for fast drying.",
            "Cultivate soil under vines to bury mummies before spring bud break."
        ]
    },
    "grape_healthy": {
        "id": "grape_healthy",
        "crop": "Grape",
        "category": "Fruits",
        "crop_scientific": "Vitis vinifera",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Expansive fan-shaped emerald-green foliage with distinct lobing",
            "Clean leaf blades without chlorosis, necrotic patches, or powdery residue",
            "Strong tendril growth and uniform grape berry enlargement"
        ],
        "spread_favorable_conditions": "Warm sunny days with dry canopy during berry maturation.",
        "organic_remedy": [
            "Apply composted cow manure and sea kelp foliar extract."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed.",
            "Foliar Potassium schoenite (0.5%) for sugar accumulation."
        ],
        "preventive_practices": [
            "Proper shoot positioning and cluster thinning."
        ]
    },

    # =========================================================================
    # 3. CEREALS, GRAINS & MILLETS
    # =========================================================================

    # ------------------ RICE / PADDY ------------------
    "rice_blast": {
        "id": "rice_blast",
        "crop": "Rice / Paddy",
        "category": "Cereals & Grains",
        "crop_scientific": "Oryza sativa",
        "disease_name": "Rice Leaf Blast",
        "pathogen": "Magnaporthe oryzae (Pyricularia oryzae) (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Spindle/diamond-shaped elliptical lesions with greyish/whitish centers and reddish-brown borders",
            "Spots coalesce, leading to complete desiccation ('burnt' appearance) of leaf blades",
            "Neck blast: Black necrosis at panicle base resulting in chaffy, empty grains"
        ],
        "spread_favorable_conditions": "Excessive nitrogen fertilizer, cool nights (20°C), high relative humidity (>90%), and prolonged dew.",
        "organic_remedy": [
            "Seed treatment with Pseudomonas fluorescens @ 10 g/kg seed followed by seedling root dip @ 2.5 kg/acre.",
            "Foliar spray with 10% cow urine + 10% neem leaf extract decoction.",
            "Apply Silicon-rich fertilizer (Diatomite / Rice husk ash) to strengthen silica cuticle barrier."
        ],
        "chemical_remedy": [
            "Tricyclazole 75% WP @ 0.6 g/liter (Highly effective standard for blast).",
            "Isoprothiolane 40% EC @ 1.5 ml/liter or Kasugamycin 3% SL @ 2.5 ml/liter.",
            "Combination: Azoxystrobin 18.2% + Difenoconazole 11.4% SC @ 1.0 ml/liter.",
            "Spray at early tillering and before boot leaf emergence."
        ],
        "preventive_practices": [
            "Avoid split-dosing excessive nitrogenous fertilizers (urea). Apply in 3-4 balanced splits.",
            "Treat seed with Carbendazim 50% WP @ 2 g/kg seed before nursery sowing.",
            "Maintain intermittent field aeration rather than continuous deep flooding."
        ]
    },
    "rice_brown_spot": {
        "id": "rice_brown_spot",
        "crop": "Rice / Paddy",
        "category": "Cereals & Grains",
        "crop_scientific": "Oryza sativa",
        "disease_name": "Brown Spot",
        "pathogen": "Bipolaris oryzae / Helminthosporium oryzae (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Moderate",
        "early_stage_indicators": [
            "Small oval to circular dark brown to purple-brown spots on leaf surface",
            "Larger spots develop a greyish-white necrotic center surrounded by yellow halo",
            "Grain discolouration with poor grain filling"
        ],
        "spread_favorable_conditions": "Poor or nutrient-deficient soils (low potash/silicon/nitrogen), water stress, and 25-30°C temperature.",
        "organic_remedy": [
            "Soil application of FYM @ 5 tons/ha enriched with Trichoderma viride.",
            "Foliar application of Panchagavya 3% or fermented seaweed extract."
        ],
        "chemical_remedy": [
            "Mancozeb 75% WP @ 2.0 g/liter or Propiconazole 25% EC @ 1.0 ml/liter.",
            "Edifenphos 50% EC @ 1.0 ml/liter or Hexaconazole 5% EC @ 2.0 ml/liter."
        ],
        "preventive_practices": [
            "Correct soil potash (MOP) deficiency in split doses.",
            "Ensure proper soil drainage and avoid drought stress.",
            "Hot water seed treatment at 53-54°C for 10-12 minutes."
        ]
    },
    "rice_healthy": {
        "id": "rice_healthy",
        "crop": "Rice / Paddy",
        "category": "Cereals & Grains",
        "crop_scientific": "Oryza sativa",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Vibrant green, erect, upright leaf canopy",
            "Clean leaf sheaths with absence of discoloration or water soaking",
            "Strong tillering and healthy fibrous root system"
        ],
        "spread_favorable_conditions": "Balanced soil fertility, appropriate water level (2-5 cm), and warm sunny weather.",
        "organic_remedy": [
            "Green manuring (Dhaincha / Sunhemp) incorporated prior to puddling.",
            "Apply Azospirillum and Phosphate Solubilizing Bacteria (PSB)."
        ],
        "chemical_remedy": [
            "No chemical fungicides or bactericides required.",
            "Zinc Sulphate (21%) @ 10 kg/acre basal application to prevent Khaira disease."
        ],
        "preventive_practices": [
            "Adopt Alternate Wetting and Drying (AWD) water management.",
            "Optimal plant spacing (20 cm x 15 cm)."
        ]
    },

    # ------------------ CORN / MAIZE ------------------
    "corn_common_rust": {
        "id": "corn_common_rust",
        "crop": "Corn / Maize",
        "category": "Cereals & Grains",
        "crop_scientific": "Zea mays",
        "disease_name": "Common Rust",
        "pathogen": "Puccinia sorghi (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Moderate",
        "early_stage_indicators": [
            "Small, oval to elongated golden-brown to cinnamon-brown pustules scattered across both leaf surfaces",
            "Pustules rupture epidermal tissue, releasing powdery rusty-red fungal spores",
            "Older leaves become chlorotic and senesce prematurely"
        ],
        "spread_favorable_conditions": "Cool to moderate temperatures (16-25°C) with high relative humidity (>95%) and 6 hours of leaf wetness.",
        "organic_remedy": [
            "Spray wettable sulfur bio-formulation (80% WDG) @ 2.5 g/liter.",
            "Neem oil spray (0.5%) to inhibit urediniospore germination."
        ],
        "chemical_remedy": [
            "Azoxystrobin 18.2% + Difenoconazole 11.4% SC @ 1.0 ml/liter.",
            "Propiconazole 25% EC @ 1.0 ml/liter or Mancozeb 75% WP @ 2.0 g/liter."
        ],
        "preventive_practices": [
            "Select rust-tolerant maize hybrid varieties.",
            "Early planting to avoid mid-season cool, humid rust migration windows."
        ]
    },
    "corn_healthy": {
        "id": "corn_healthy",
        "crop": "Corn / Maize",
        "category": "Cereals & Grains",
        "crop_scientific": "Zea mays",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Deep emerald-green broad leaves with smooth parallel veins",
            "Absence of pustules, striping, or blighted leaf edges",
            "Thick sturdy stalk and vigorous ear/tassel development"
        ],
        "spread_favorable_conditions": "Abundant sunshine, daytime temperatures 25-32°C, and fertile well-drained loam.",
        "organic_remedy": [
            "Side dress with vermicompost and Bio-NPK liquid inoculants.",
            "Maintain soil mulch to preserve moisture."
        ],
        "chemical_remedy": [
            "No chemical intervention needed.",
            "Urea top-dressing in 2 splits: knee-high stage and tasseling stage."
        ],
        "preventive_practices": [
            "Maintain 60 cm row-to-row and 20 cm plant-to-plant spacing."
        ]
    },

    # ------------------ WHEAT ------------------
    "wheat_leaf_rust": {
        "id": "wheat_leaf_rust",
        "crop": "Wheat",
        "category": "Cereals & Grains",
        "crop_scientific": "Triticum aestivum",
        "disease_name": "Brown / Leaf Rust",
        "pathogen": "Puccinia triticina (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Small circular to oval bright orange-brown pustules randomly distributed on upper leaf surface",
            "Pustules erupt powdery spores that stain fingers orange when touched",
            "Severe infection leads to rapid leaf drying and shrivelled grain"
        ],
        "spread_favorable_conditions": "Mild temperatures (15-22°C) with overnight dew and moderate humidity.",
        "organic_remedy": [
            "Seed treatment with Trichoderma harzianum @ 5 g/kg.",
            "Foliar spray of 5% cow urine + botanical extracts at boot stage."
        ],
        "chemical_remedy": [
            "Propiconazole 25% EC (Tilt) @ 1.0 ml/liter water at first appearance of rust pustules.",
            "Alternative: Tebuconazole 25.9% EC @ 1.0 ml/liter or Mancozeb 75% WP @ 2.5 g/liter."
        ],
        "preventive_practices": [
            "Sow rust-resistant varieties recommended for your agro-climatic zone.",
            "Adhere to recommended sowing time (early-to-mid November in northern plains)."
        ]
    },
    "wheat_healthy": {
        "id": "wheat_healthy",
        "crop": "Wheat",
        "category": "Cereals & Grains",
        "crop_scientific": "Triticum aestivum",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Uniform green leaf blades without rust flecks, powder, or spots",
            "Broad, erect flag leaves providing maximum photosynthesis to the earhead",
            "Stout tillers and clean leaf sheaths"
        ],
        "spread_favorable_conditions": "Cool winters with ample sunlight and scheduled irrigation at crown root initiation (CRI).",
        "organic_remedy": [
            "Apply Jeevamrutha through irrigation water."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed.",
            "Foliar spray of 00:52:34 @ 10 g/liter + Boron @ 1 g/liter during heading."
        ],
        "preventive_practices": [
            "Timely 5-6 critical stage irrigations (CRI, tillering, jointing, flowering, milk, dough)."
        ]
    },

    # ------------------ PEARL MILLET / BAJRA ------------------
    "millet_downy_mildew": {
        "id": "millet_downy_mildew",
        "crop": "Pearl Millet / Bajra",
        "category": "Cereals & Grains",
        "crop_scientific": "Pennisetum glaucum",
        "disease_name": "Downy Mildew (Green Ear Disease)",
        "pathogen": "Sclerospora graminicola (Oomycete)",
        "pathogen_type": "Oomycete / Water Mold",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Chlorosis on young leaves starting at blade base and progressing upward in longitudinal yellow stripes",
            "Downy white fungal growth on leaf undersides under humid morning air",
            "Green Ear stage: Floral parts of the earhead are transformed into leafy structures, producing zero grain"
        ],
        "spread_favorable_conditions": "High relative humidity (>90%) with moderate temperatures (20-25°C) and heavy morning dews.",
        "organic_remedy": [
            "Seed treatment with bio-agent Pseudomonas fluorescens @ 10 g/kg seed.",
            "Foliar spray with fermented cow urine decoction (10%).",
            "Rogue out and bury infected green-ear plants before spore release."
        ],
        "chemical_remedy": [
            "Seed treatment: Metalaxyl-M (Apron XL) @ 2.0 g/kg seed before sowing.",
            "Foliar spray: Metalaxyl + Mancozeb (Ridomil MZ 72 WP) @ 2.5 g/liter at 20 and 35 DAS."
        ],
        "preventive_practices": [
            "Plant downy-mildew resistant bajra hybrids.",
            "Practice deep summer plowing to bury oospores.",
            "Crop rotation with pulses (pigeonpea, moong, cowpea)."
        ]
    },
    "millet_healthy": {
        "id": "millet_healthy",
        "crop": "Pearl Millet / Bajra",
        "category": "Cereals & Grains",
        "crop_scientific": "Pennisetum glaucum",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Robust, erect, coarse lanceolate green leaves with strong tillering",
            "Compact, dense, cylindrical earheads packed with plump pearl-like grains"
        ],
        "spread_favorable_conditions": "Semi-arid dry climate with warm sunny days (28-36°C) and well-drained sandy loam.",
        "organic_remedy": [
            "Incorporate farmyard manure and bio-fertilizers (Azospirillum).",
            "Intercrop with green gram or cowpea."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed."
        ],
        "preventive_practices": [
            "Timely thinning at 15-20 days after emergence to maintain 10-12 cm plant spacing."
        ]
    },

    # =========================================================================
    # 4. CASH CROPS, PULSES & OILSEEDS
    # =========================================================================

    # ------------------ SUGARCANE ------------------
    "sugarcane_red_rot": {
        "id": "sugarcane_red_rot",
        "crop": "Sugarcane",
        "category": "Cash Crops & Pulses",
        "crop_scientific": "Saccharum officinarum",
        "disease_name": "Red Rot",
        "pathogen": "Colletotrichum falcatum (Glomerella tucumanensis) (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Third or fourth leaf from crown shows yellowing and drying along margins",
            "Midrib of upper leaves exhibits blood-red lesions with dark margins and white centers",
            "Splitting the cane stalk longitudinally reveals dull red internal discoloration interrupted by distinctive white horizontal cross-bands",
            "Sour alcoholic odor emitted from split infected stalks"
        ],
        "spread_favorable_conditions": "High rainfall, waterlogged soils, temperatures between 25-30°C, and cultivation of susceptible cultivars.",
        "organic_remedy": [
            "Sett treatment with Trichoderma viride @ 10 g/liter for 30 minutes before planting.",
            "Soil application of Trichoderma enriched press mud / FYM (5 tons/acre).",
            "Rogue out and burn infected clumps immediately."
        ],
        "chemical_remedy": [
            "Sett treatment: Dip setts in Carbendazim 50% WP @ 1.0 g/liter or Thiophanate-methyl @ 1.0 g/liter for 15 minutes.",
            "Moist Hot Air Treatment (MHAT) of seed setts at 54°C for 2.5 hours."
        ],
        "preventive_practices": [
            "Cultivate red-rot resistant varieties (e.g., Co 0238, Co 86032).",
            "Never use setts from affected ratoon crops.",
            "Ensure proper field drainage and avoid flood irrigation between affected and healthy plots."
        ]
    },
    "sugarcane_healthy": {
        "id": "sugarcane_healthy",
        "crop": "Sugarcane",
        "category": "Cash Crops & Pulses",
        "crop_scientific": "Saccharum officinarum",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Dense canopy of broad, emerald-green arching leaves with intact midribs",
            "Thick, solid, juicy internodes free of borers, red pith, or cavities"
        ],
        "spread_favorable_conditions": "Warm tropical sun (28-35°C), long daylight hours, and fertile deep alluvial/loamy soil.",
        "organic_remedy": [
            "Trash mulching between rows to conserve moisture and suppress weeds.",
            "Apply Gluconacetobacter diazotrophicus nitrogen-fixing bio-fertilizer."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed."
        ],
        "preventive_practices": [
            "Earthing-up at 90 and 120 days to anchor canes against lodging."
        ]
    },

    # ------------------ COTTON ------------------
    "cotton_bacterial_blight": {
        "id": "cotton_bacterial_blight",
        "crop": "Cotton",
        "category": "Cash Crops & Pulses",
        "crop_scientific": "Gossypium hirsutum",
        "disease_name": "Bacterial Blight / Angular Leaf Spot",
        "pathogen": "Xanthomonas citri pv. malvacearum (Bacteria)",
        "pathogen_type": "Bacterial",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Small, angular, water-soaked spots constrained by leaf veins",
            "Spots turn dark reddish-brown to black, lesions advance along primary veins (Vein Blight)",
            "Black arm stage: Long black lesions on branches and stems causing breakage",
            "Boll rot: Round sunken dark brown lesions on developing cotton bolls"
        ],
        "spread_favorable_conditions": "Warm (25-30°C) with persistent rains, wind-driven showers, and high humidity (>85%).",
        "organic_remedy": [
            "Delinting seed with concentrated sulfuric acid (100 ml/kg seed) followed by cold water wash.",
            "Seed treatment with Pseudomonas fluorescens @ 10 g/kg seed.",
            "Foliar spray with fresh cow urine (5%) + neem extract (5%)."
        ],
        "chemical_remedy": [
            "Copper Oxychloride 50% WP @ 2.5 g/liter + Streptocycline @ 0.1 g/liter (1 g per 10 L water).",
            "Repeat spray at 15-day intervals if wet monsoon weather continues.",
            "Spray kasugamycin 3% SL @ 2.0 ml/liter for systemic infection."
        ],
        "preventive_practices": [
            "Use acid-delinted certified seeds.",
            "Burn or bury cotton stubble after harvest to eliminate bacterial inoculum.",
            "Ensure proper field drainage to prevent stagnant water."
        ]
    },
    "cotton_healthy": {
        "id": "cotton_healthy",
        "crop": "Cotton",
        "category": "Cash Crops & Pulses",
        "crop_scientific": "Gossypium hirsutum",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Broad, dark green palmate leaves with clean lobes and venation",
            "No angular water-soaked markings, curling, or leaf reddening",
            "Healthy squares (flower buds) and developing boll retention"
        ],
        "spread_favorable_conditions": "Warm tropical sunshine (25-35°C) with deep, well-aerated black cotton soil (Vertisols).",
        "organic_remedy": [
            "Soil incorporation of enriched Farm Yard Manure with Trichoderma and Mycorrhiza.",
            "Castor or marigold border crops."
        ],
        "chemical_remedy": [
            "No fungicides required.",
            "Magnesium Sulphate (1%) + 19:19:19 (1%) foliar spray at 60 and 90 DAS."
        ],
        "preventive_practices": [
            "Timely detopping at 100-120 days to channel energy into boll development."
        ]
    },

    # ------------------ SOYBEAN ------------------
    "soybean_rust": {
        "id": "soybean_rust",
        "crop": "Soybean",
        "category": "Cash Crops & Pulses",
        "crop_scientific": "Glycine max",
        "disease_name": "Asian Soybean Rust",
        "pathogen": "Phakopsora pachyrhizi (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Tiny, pinhead-sized, polygonal chlorotic or grey-brown flecks on lower leaves",
            "Volcano-shaped raised pustules (uredinia) on the underside of leaves releasing powdery tan spores",
            "Rapid premature defoliation starting from bottom canopy upward, resulting in empty or shrivelled pods"
        ],
        "spread_favorable_conditions": "Temperatures 18-28°C with prolonged leaf wetness (>6-8 hours) and relative humidity >80%.",
        "organic_remedy": [
            "Seed treatment with Trichoderma viride @ 5 g/kg seed.",
            "Foliar spray with Wettable Sulfur 80% WDG @ 2.5 g/liter at flowering.",
            "Neem oil (0.5%) foliar spray to hinder urediniospore germination."
        ],
        "chemical_remedy": [
            "First Line: Hexaconazole 5% EC @ 1.0 ml/liter or Propiconazole 25% EC @ 1.0 ml/liter.",
            "Combination: Azoxystrobin 18.2% + Difenoconazole 11.4% SC @ 1.0 ml/liter or Tebuconazole 25.9% EC @ 1.25 ml/liter.",
            "Spray at early flowering (R1-R3 stage) upon first symptom detection on lower leaves."
        ],
        "preventive_practices": [
            "Plant early-maturing rust-tolerant soybean cultivars.",
            "Avoid overly dense plant stands to facilitate canopy ventilation.",
            "Practice crop rotation with non-legume crops (maize, sorghum)."
        ]
    },
    "soybean_healthy": {
        "id": "soybean_healthy",
        "crop": "Soybean",
        "category": "Cash Crops & Pulses",
        "crop_scientific": "Glycine max",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Vibrant green trifoliate leaves with clean lamina and veins",
            "Abundant pink-white blossoms and heavy cluster setting of 3-seeded pods",
            "Active root nodules showing pink interior (nitrogen fixation)"
        ],
        "spread_favorable_conditions": "Warm sunny monsoon days (22-30°C) with well-drained loamy soil.",
        "organic_remedy": [
            "Seed inoculation with Rhizobium japonicum and PSB cultures @ 5 g/kg seed.",
            "Foliar spray with vermiwash 5%."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed."
        ],
        "preventive_practices": [
            "Maintain 45 cm row spacing and 10 cm plant-to-plant spacing."
        ]
    },

    # ------------------ GROUNDNUT / PEANUT ------------------
    "groundnut_tikka_leaf_spot": {
        "id": "groundnut_tikka_leaf_spot",
        "crop": "Groundnut / Peanut",
        "category": "Cash Crops & Pulses",
        "crop_scientific": "Arachis hypogaea",
        "disease_name": "Tikka Disease (Early & Late Leaf Spot)",
        "pathogen": "Cercospora arachidicola & Phaeoisariopsis personata (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Early spot: Sub-circular dark brown spots surrounded by a prominent yellow halo on upper leaf surface",
            "Late spot: Small, circular, carbon-black spots without yellow halo on lower leaf surface",
            "Severe infection leads to widespread premature leaf fall, leaving bare stems and small immature pods"
        ],
        "spread_favorable_conditions": "Warm humid conditions (25-30°C) with persistent rain or dew and prolonged cloudiness.",
        "organic_remedy": [
            "Seed treatment with Trichoderma viride @ 4 g/kg kernel.",
            "Foliar spray with 5% Neem Seed Kernel Extract (NSKE) at 40 and 55 DAS.",
            "Sour buttermilk (5%) spray to suppress spore colonization."
        ],
        "chemical_remedy": [
            "Mancozeb 75% WP @ 2.5 g/liter + Carbendazim 50% WP @ 1.0 g/liter (Saaf @ 2.0 g/L).",
            "Tebuconazole 25.9% EC @ 1.0 ml/liter or Hexaconazole 5% EC @ 1.5 ml/liter.",
            "First spray at 35-40 DAS and second spray 15 days later."
        ],
        "preventive_practices": [
            "Destroy crop residues and volunteer groundnut plants.",
            "Rotate with pearl millet, sorghum, or maize for 2 seasons.",
            "Sow disease-tolerant cultivars."
        ]
    },
    "groundnut_healthy": {
        "id": "groundnut_healthy",
        "crop": "Groundnut / Peanut",
        "category": "Cash Crops & Pulses",
        "crop_scientific": "Arachis hypogaea",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Bright emerald-green pinnate leaflets with upright posture",
            "Abundant yellow pea-flowers and prolific subterranean peg penetration into soil"
        ],
        "spread_favorable_conditions": "Warm climate (25-30°C) with well-drained sandy loam allowing easy pegging.",
        "organic_remedy": [
            "Apply Gypsum @ 200 kg/acre at 40-45 DAS during flowering/pegging for shell and kernel development.",
            "Bio-fertilizer seed treatment with Bradyrhizobium."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed."
        ],
        "preventive_practices": [
            "Never disturb or hoe soil after pegging begins to protect developing subterranean pods."
        ]
    },

    # ------------------ CHICKPEA / BENGAL GRAM ------------------
    "chickpea_ascochyta_blight": {
        "id": "chickpea_ascochyta_blight",
        "crop": "Chickpea / Gram",
        "category": "Cash Crops & Pulses",
        "crop_scientific": "Cicer arietinum",
        "disease_name": "Ascochyta Blight",
        "pathogen": "Ascochyta rabiei (Didymella rabiei) (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Small circular water-soaked spots on leaflets and pods with concentric rings of tiny black specks (pycnidia)",
            "Elongated dark brown sunken cankers on stems causing them to break over ('stem girdling')",
            "Patches of diseased plants in the field rapidly turn brown and dry up, simulating frost damage"
        ],
        "spread_favorable_conditions": "Cool (15-20°C) and wet weather with overcast skies and high humidity (>85%).",
        "organic_remedy": [
            "Seed treatment with Trichoderma harzianum @ 5 g/kg seed.",
            "Foliar spray with Copper soap or Bordeaux mixture 1%."
        ],
        "chemical_remedy": [
            "Seed treatment: Carbendazim 50% WP @ 2 g/kg seed + Thiram 75% WP @ 2 g/kg seed.",
            "Foliar spray: Chlorothalonil 75% WP @ 2.0 g/liter or Mancozeb 75% WP @ 2.5 g/liter at first symptom.",
            "Systemic: Azoxystrobin @ 1.0 ml/liter or Difenoconazole @ 1.0 ml/liter."
        ],
        "preventive_practices": [
            "Use certified disease-free seed.",
            "Practice deep summer plowing to bury infected stubble.",
            "Rotate crops for at least 3 years with non-host cereals (wheat, barley)."
        ]
    },
    "chickpea_healthy": {
        "id": "chickpea_healthy",
        "crop": "Chickpea / Gram",
        "category": "Cash Crops & Pulses",
        "crop_scientific": "Cicer arietinum",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Feathery, serrated, gland-dotted bluish-green pinnate leaflets with acidic exudate",
            "Clean upright branching and vigorous pod setting with 1-2 plump seeds per pod"
        ],
        "spread_favorable_conditions": "Cool dry winter weather (10-25°C) with well-drained loamy soil.",
        "organic_remedy": [
            "Seed inoculation with Mesorhizobium ciceri and PSB.",
            "Spray vermiwash 5%."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed."
        ],
        "preventive_practices": [
            "Install pheromone traps for Helicoverpa pod borer."
        ]
    },

    # ------------------ TEA ------------------
    "tea_blister_blight": {
        "id": "tea_blister_blight",
        "crop": "Tea",
        "category": "Cash Crops & Pulses",
        "crop_scientific": "Camellia sinensis",
        "disease_name": "Blister Blight",
        "pathogen": "Exobasidium vexans (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Small, pale yellowish, translucent, circular spots on tender young leaves and buds",
            "Spots enlarge into blister-like depressions on upper leaf surface, with corresponding white velvety convex blisters on the underside",
            "Severe blister coalescence shrivels tender shoots, stopping harvest flushes"
        ],
        "spread_favorable_conditions": "High elevation, persistent fog, relative humidity >85%, temperatures 15-22°C, and daily sunshine <3 hours.",
        "organic_remedy": [
            "Regulate shade trees: Thin heavy shade canopy to allow sunshine penetration onto bushes.",
            "Spray Copper Hydroxide @ 2.0 g/liter at 5-7 day intervals.",
            "Strict regular 7-day plucking rounds to remove susceptible young flush."
        ],
        "chemical_remedy": [
            "Copper Oxychloride 50% WP (210 g) + Nickel Chloride (210 g) per hectare in 175 L water.",
            "Systemic: Hexaconazole 5% EC @ 200 ml/ha or Propiconazole 25% EC @ 125 ml/ha tank-mixed with Copper Oxychloride.",
            "Spray following every plucking round during monsoon."
        ],
        "preventive_practices": [
            "Annual shade tree lopping before monsoon rains begin.",
            "Maintain proper bush frame hygiene and eliminate moss/lichen."
        ]
    },
    "tea_healthy": {
        "id": "tea_healthy",
        "crop": "Tea",
        "category": "Cash Crops & Pulses",
        "crop_scientific": "Camellia sinensis",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Vibrant, glossy, serrated dark-green mature leaves with tender golden-green 'two leaves and a bud'",
            "Dense healthy table canopy without blisters or dieback"
        ],
        "spread_favorable_conditions": "Humid subtropical highlands with acidic soils (pH 4.5-5.5) and well-distributed rainfall.",
        "organic_remedy": [
            "Apply compost and bio-fertilizers in tea trenches.",
            "Foliar spray with zinc sulphate and magnesium sulphate."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed."
        ],
        "preventive_practices": [
            "Maintain level plucking table to maximize light interception."
        ]
    },

    # ------------------ COFFEE ------------------
    "coffee_leaf_rust": {
        "id": "coffee_leaf_rust",
        "crop": "Coffee",
        "category": "Cash Crops & Pulses",
        "crop_scientific": "Coffea arabica",
        "disease_name": "Coffee Leaf Rust (Roya)",
        "pathogen": "Hemileia vastatrix (Fungus)",
        "pathogen_type": "Fungal",
        "severity_level": "Severe (High Threat)",
        "early_stage_indicators": [
            "Small, pale-yellow chlorotic spots on the upper surface of leaves",
            "Underside of spots develops a powdery, bright orange-yellow fungal spore mass",
            "Infected leaves drop prematurely, causing branch dieback and severely reducing subsequent seasons' bean yield"
        ],
        "spread_favorable_conditions": "Temperatures 20-25°C, high relative humidity, rain splash, and dense unpruned shade.",
        "organic_remedy": [
            "Pre-monsoon and post-monsoon Bordeaux mixture (0.5% - 1%) spray.",
            "Prune shade trees to achieve 50% filtered sunlight.",
            "Bio-control spray with Bacillus thuringiensis or Verticillium lecanii."
        ],
        "chemical_remedy": [
            "Triadimefon 25% WP (Bayleton) @ 1.0 g/liter or Hexaconazole 5% EC @ 1.5 ml/liter.",
            "Epoxiconazole or Pyraclostrobin + Epoxiconazole (Opera) @ 1.0 ml/liter.",
            "Pre-monsoon spray in May-June followed by mid-monsoon and post-monsoon sprays."
        ],
        "preventive_practices": [
            "Plant rust-resistant cultivars (e.g., Chandragiri, Selection 9, Catimor).",
            "Maintain balanced shade to avoid excessive leaf wetness.",
            "Annual handling and desuckering of coffee bushes."
        ]
    },
    "coffee_healthy": {
        "id": "coffee_healthy",
        "crop": "Coffee",
        "category": "Cash Crops & Pulses",
        "crop_scientific": "Coffea arabica",
        "disease_name": "Healthy Foliage",
        "pathogen": "None",
        "pathogen_type": "Healthy",
        "severity_level": "None",
        "early_stage_indicators": [
            "Deep, glossy, dark emerald-green elliptical leaves with wavy margins",
            "Robust lateral branches loaded with tight clusters of glossy green ripening coffee berries"
        ],
        "spread_favorable_conditions": "Tropical highland climate (15-28°C) under well-managed two-tier shade trees.",
        "organic_remedy": [
            "Apply coffee pulp compost and neem cake.",
            "Bio-fertilizer consortium application in drip zones."
        ],
        "chemical_remedy": [
            "No chemical fungicides needed.",
            "Foliar spray of 19:19:19 + Zinc + Boron at berry development."
        ],
        "preventive_practices": [
            "Annual desuckering and center pruning to maintain bush frame."
        ]
    }
}

# Categorized Quick Index
CROPS_CATALOG = [
    {
        "category": "Vegetables",
        "crops": [
            {"name": "Tomato", "icon": "🍅", "key": "tomato"},
            {"name": "Potato", "icon": "🥔", "key": "potato"},
            {"name": "Brinjal / Eggplant", "icon": "🍆", "key": "eggplant"},
            {"name": "Onion & Garlic", "icon": "🧅", "key": "onion"},
            {"name": "Okra / Bhindi", "icon": "🌱", "key": "okra"},
            {"name": "Cabbage & Cauliflower", "icon": "🥬", "key": "cabbage"},
            {"name": "Cucumber & Gourds", "icon": "🥒", "key": "cucumber"},
            {"name": "Ginger & Turmeric", "icon": "🫚", "key": "ginger"}
        ]
    },
    {
        "category": "Fruits",
        "crops": [
            {"name": "Mango", "icon": "🥭", "key": "mango"},
            {"name": "Banana", "icon": "🍌", "key": "banana"},
            {"name": "Citrus (Lemon / Orange)", "icon": "🍋", "key": "citrus"},
            {"name": "Papaya", "icon": "🍈", "key": "papaya"},
            {"name": "Pomegranate", "icon": "🫐", "key": "pomegranate"},
            {"name": "Guava", "icon": "🍏", "key": "guava"},
            {"name": "Strawberry", "icon": "🍓", "key": "strawberry"},
            {"name": "Apple", "icon": "🍎", "key": "apple"},
            {"name": "Grape", "icon": "🍇", "key": "grape"}
        ]
    },
    {
        "category": "Cereals & Grains",
        "crops": [
            {"name": "Rice / Paddy", "icon": "🌾", "key": "rice"},
            {"name": "Corn / Maize", "icon": "🌽", "key": "corn"},
            {"name": "Wheat", "icon": "🌾", "key": "wheat"},
            {"name": "Pearl Millet / Bajra", "icon": "🌾", "key": "millet"}
        ]
    },
    {
        "category": "Cash Crops & Pulses",
        "crops": [
            {"name": "Sugarcane", "icon": "🎋", "key": "sugarcane"},
            {"name": "Cotton", "icon": "🌱", "key": "cotton"},
            {"name": "Soybean", "icon": "🫘", "key": "soybean"},
            {"name": "Groundnut / Peanut", "icon": "🥜", "key": "groundnut"},
            {"name": "Chickpea / Gram", "icon": "🫘", "key": "chickpea"},
            {"name": "Tea", "icon": "🍵", "key": "tea"},
            {"name": "Coffee", "icon": "☕", "key": "coffee"}
        ]
    }
]

# Flattened list for backwards compatibility
CROPS_LIST = [crop for cat in CROPS_CATALOG for crop in cat["crops"]]

def get_disease_info(disease_id: str) -> Dict[str, Any]:
    """Retrieve full disease profile by disease_id or closest match."""
    if disease_id in CROP_DISEASES:
        return CROP_DISEASES[disease_id]
    # Fallback to general healthy
    return CROP_DISEASES.get("tomato_healthy", {})
