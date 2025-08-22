data = {
    "HD2023": [  # Directory information
        "UNITID",
        "INSTNM",  # Institution (entity) name
        "IALIAS",  # Institution name alias
        "ADDR",  # Street address or post office box
        "CITY",  # City location of institution
        "STABBR",  # State abbreviation
        "LONGITUD",  # Longitude location of institution
        "LATITUDE",  # Latitude location of institution
        "GENTELE",  # General information telephone number
        "WEBADDR",  # Institution's internet website address
        "ADMINURL",  # Admissions office web address
        "FAIDURL",  # Financial aid office web address
        "APPLURL",  # Online application web address
        "NPRICURL",  # Net price calculator web address
        "UGOFFER",  # Undergraduate offering
        "GROFFER",  # Graduate offering
        "HDEGOFR1",  # Highest degree offered
        "HOSPITAL",  # Institution has hospital
        "MEDICAL",  # Institution grants a medical degree
        "C21BASIC",  # Carnegie Classification 2021: Basic
        "C21UGPRF",  # Carnegie Classification 2021: Undergraduate Profile
        "C21ENPRF",  # Carnegie Classification 2021: Enrollment Profile
        "C21SZSET",  # Carnegie Classification 2021: Size and Setting
        "LOCALE",  # Degree of urbanization (Urban-centric locale)
        "INSTSIZE",  # Institution size category
        "F1SYSTYP",  # Multi-institution or multi-campus organization
        "F1SYSNAM",  # Name of multi-institution or multi-campus organization
        "F1SYSCOD",  # Identification number of multi-institution or multi-campus organization
    ],
    "ADM2023": [  # Admission considerations, applicants, admissions, and test scores
        "UNITID",
        # For all ADMCON#:
        #    1	Required to be considered for admission
        #    5	Not required for admission, but considered if submitted
        #    3	Not considered for admission, even if submitted
        #    -1	Not reported
        #    -2	Not applicable
        "ADMCON1",  # HS GPA
        "ADMCON2",  # Secondary school rank
        "ADMCON3",  # Secondary school record (AKA Rigor)
        "ADMCON4",  # Completion of college-preparatory program
        "ADMCON5",  # Recommendations
        "ADMCON6",  # Formal demonstration of competencies
        "ADMCON7",  # Admission test scores
        "ADMCON8",  # English Proficiency Test
        "ADMCON9",  # Other Test (Wonderlic, WISC-III, etc.)
        "ADMCON10",  # Work experience
        "ADMCON11",  # Personal statement or essay
        "ADMCON12",  # Legacy status
        "APPLCNM",  # Applicants men
        "APPLCNW",  # Applicants women
        "APPLCNAN",  # Applicants another gender
        "APPLCNUN",  # Applicants gender unknown
        "ADMSSNM",  # Admitted men
        "ADMSSNW",  # Admitted women
        "ADMSSNAN",  # Admitted another gender
        "ADMSSNUN",  # Admitted gender unknown
        "ENRLM",  # Enrolled  men
        "ENRLW",  # Enrolled  women
        "ENRLAN",  # Enrolled another gender
        "ENRLUN",  # Enrolled gender unknown
        "ENRLT",  # Enrolled total
        "APPLCN",  # Applicants total
        "ADMSSN",  # Admissions total
        "ENRLPT",  # Enrolled part time total
        "ENRLFT",  # Enrolled full time total
        "SATPCT",  # Percent of first-time students submitting SAT scores
        "ACTPCT",  # Percent of first-time students submitting ACT scores
        "SATVR25",  # SAT Evidence-Based Reading and Writing 25th percentile score
        "SATVR50",  # SAT Evidence-Based Reading and Writing 50th percentile score
        "SATVR75",  # SAT Evidence-Based Reading and Writing 75th percentile score
        "SATMT25",  # SAT Math 25th percentile score
        "SATMT50",  # SAT Math 50th percentile score
        "SATMT75",  # SAT Math 75th percentile score
        "ACTCM25",  # ACT Composite 25th percentile score
        "ACTCM50",  # ACT Composite 50th percentile score
        "ACTCM75",  # ACT Composite 75th percentile score
        "ACTEN25",  # ACT English 25th percentile score
        "ACTEN50",  # ACT English 50th percentile score
        "ACTEN75",  # ACT English 75th percentile score
        "ACTMT25",  # ACT Math 25th percentile score
        "ACTMT50",  # ACT Math 50th percentile score
        "ACTMT75",  # ACT Math 75th percentile score
    ],
    "DRVADM2023": [  # NOTE: Not sure if this is needed since I can just calculate this.
        "UNITID",
        "DVADM01",  # Percent admitted - total
        "DVADM02",  # Percent admitted - men
        "DVADM03",  # Percent admitted - women
        "DVADM04",  # Yield - total
        "DVADM05",  # Yield - men
        "DVADM06",  # Yield - women
    ],
    # "C2023_A": [  # Completions by CIP code # TODO: Pack this into its own table for a col for each state instead of having multiple rows for each college
    #     "UNITID",
    #     "CIPCODE",
    #     "AWLEVEL",  # Award Level
    #     "CTOTALT",  # Grand total
    #     "CTOTALM",  # Grand total men
    #     "CTOTALW",  # Grand total women
    # ],  # TODO: Add a filter to see how many people graduated by specific major, dont show if doesnt exist. Maybe other forms of search too.
    "DRVEF122023": [  # Derived variables for 12-month enrollment, 2022-23
        "UNITID",
        "FTE12MN",  # 12-month full-time equivalent enrollment
        "UNDUP",  # Total 12-month unduplicated headcount
        "UNDUPUG",  # Undergraduate 12-month unduplicated headcount
        "E12GRAD",  # Graduate 12-month unduplicated headcount
        "E12FT",  # Full-time 12-month unduplicated headcount
        "E12PT",  # Part-time 12-month unduplicated headcount
        "PCTE12AN",  # Percent of 12-month unduplicated headcount that are American Indian or Alaska Native
        "PCTE12AS",  # Percent of 12-month unduplicated headcount that are Asian
        "PCTE12BK",  # Percent of 12-month unduplicated headcount that are Black or African American
        "PCTE12HS",  # Percent of 12-month unduplicated headcount that are Hispanic/Latino
        "PCTE12NH",  # Percent of 12-month unduplicated headcount that are Native Hawaiian or Other Pacific Islander
        "PCTE12WH",  # Percent of 12-month unduplicated headcount that are White
        "PCTE122M",  # Percent of 12-month unduplicated headcount that are two or more races
        "PCTE12UN",  # Percent of 12-month unduplicated headcount that are race/ethnicity unknown
        "PCTE12NR",  # Percent of 12-month unduplicated headcount that are U.S. Nonresident
        "PCTE12W",  # Percent of 12-month unduplicated headcount that are women
        "PCTE12DEEXC",  # Percent of 12-month unduplicated headcount enrolled exclusively in distance education courses
        "PCTE12DESOM",  # Percent of 12-month unduplicated headcount enrolled in some but not all distance education courses
        "PCTE12DENON",  # Percent of 12-month unduplicated headcount not enrolled in any distance education courses
    ],
    # "EF2023C": [  # Residence and migration of first-time freshman
    #     "UNITID",
    #     "EFCSTATE",  # State of residence when student was first admitted
    #     "EFRES01",  # First-time degree/certificate-seeking undergraduate students
    #     "EFRES02",  # First-time degree/certificate-seeking undergraduate students who graduated from high school in the past 12 months
    #     "LINE",  # State of residence  (original line number on survey form)
    # ],  # TODO: Pack this into its own table for a col for each state instead of having multiple rows for each college
    "EF2023D": [  # Total entering class, retention rates, and student-to-faculty ratio
        "UNITID",
        "RET_PCF",  # Full-time retention rate
        "RET_PCP",  # Part-time retention rate
        "STUFACR",  # Student-to-faculty ratio
    ],
    "DRVGR2023": [  # Derived variables of 150% (6yr) grad rates
        "UNITID",
        "TRRTTOT",  # Transfer-out rate, total cohort
        "GBA4RTT",  # Graduation rate - Bachelor degree within 4 years, total
        "GBA5RTT",  # Graduation rate - Bachelor degree within 5 years, total
        "GBA6RTT",  # Graduation rate - Bachelor degree within 6 years, total
    ],
    "IC2023": [  # Institutional Characteristics
        "UNITID",
        "CNTLAFFI",  # Control of Institution
        "RELAFFIL",  # Religious Affiliation
        "CALSYS",  # Calendar System
        "CREDITS3",  # AP Credits
        "APPLFEEU",  # Undergraduate Application Fee
        "APPLFEEG",  # Graduate Application Fee
        "SLO5",  # ROTC
        "SLO6",  # Study Abroad
        "SLO8",  # Teacher Cert
        "SLOA",  # Undergraduate Research
        "SLO9",  # None of above special learning opportunities are offered
        "STUSRV2",  # Academic/career Counseling
        "STUSRV3",  # Employment Services
        "STUSRV4",  # Placement Services
        "STUSRV9",  # None of above selected services are offered
        "TUITPL",  # Any alternative tuition plans are offered
        "TUITPL1",  # Tuition guaranteed plan (4-6yr tuition freeze while student)
        "TUITPL2",  # Prepaid tuition plan (pay for future credits at current prices)
        "TUITPL3",  # Tuition payment plan (Klarna)
        "TUITPL4",  # Other alternative tuition plan
        "ALLONCAM",  # First time students required to live on campus
        "TUITVARY",  # Does tuition vary for in-state vs out-of-state
        "ROOM",  # Provides institutionally-controlled housing? (on/off campus)
        "ROOMCAP",  # Housing capacity
        "BOARD",  # Offers food or meal plans
        "MEALSWK",  # Number of meals per week (only not None if above is 1)
        "ROOMAMT",  # Typical housing charges for an AY
        "BOARDAMT",  # Typical food charges for an AY
        "RMBRDAMT",  # Combined charges
        "ASSOC1",  # NCAA Stuff
        "SPORT1",  # Football
        "CONFNO1",  # Conf
        "SPORT2",  # Basketball
        "CONFNO2",  # Conf
        "SPORT3",  # Baseball
        "CONFNO3",  # Conf
        "SPORT4",  # Track
        "CONFNO4",  # Conf
    ],
    "IC2023_AY": [  # Student charges for academic year programs
        "UNITID",
        "CHG2AT3",  # Published in-state tuition 2023-24
        "CHG2AF3",  # Published in-state fees 2023-24
        "CHG2AY3",  # Published in-state tuition and fees 2023-24
        "CHG3AT3",  # Published out-of-state tuition 2023-24
        "CHG3AF3",  # Published out-of-state fees 2023-24
        "CHG3AY3",  # Published out-of-state tuition and fees 2023-24
        "CHG4AY3",  # Books and supplies 2023-24
        "CHG5AY3",  # On campus, food and housing 2023-24
        "CHG6AY3",  # On campus, other expenses 2023-24
        "CHG7AY3",  # Off campus (not with family), food and housing 2023-24
        "CHG8AY3",  # Off campus (not with family), other expenses 2023-24
        "CHG9AY3",  # Off campus (with family), other expenses 2023-24
    ],
    "SFA2223_P1": [  # Student financial aid
        "UNITID",
        "SCFA12P",  # Percentage of students in fall cohort who paying in-state tuition rates
        "SCFA13P",  # Percentage of students in fall cohort who are paying out-of-state tuition rates
        "SCFA14P",  # Percentage of students in fall cohort whose residence/ tuition rate is unknown
        "UAGRNTP",  # Percent of undergraduate students awarded federal, state, local, institutional or other sources of grant aid
        "UAGRNTA",  # Average amount of federal, state, local, institutional or other sources of grant aid awarded to undergraduate students
    ],
}

""" TABLES IGNORED:
AL2023, DRVAL2023 - Academic Libraries (Not sure if this is useful)
C2023_B, C2023_C, C2023DEP - Useless, C2023_A covers it fine enough
CUSTOMCGIDS2023 - IDK what this is used for
DRVC2023 - Derived variables for completions (Not sure if this is useful)
EAP2023 - Number of staff by occupational category, faculty and tenure status (Not really needed)
DRVEF2023 - Derived variables for Fall enrollment 2023 (Using 12mo)
EF2023 - Gender, attendance status, and level of student (Already in DRVEF122023)
EF2023A - Race/ethnicity, gender, attendance status, and level of student (Already in DRVEF122023)
EF2023A_DIST - Distance learning status of students FALL2023 (Using 12mo)
EF2023B - Age category, gender, attendance status, and level of student (Not really needed)
EFFY2023 - 12-month unduplicated headcount (Already in DRVEF122023)
EFFY2023_HS - 12MO Headcount for Dual Enrollment Students (Not really needed)
EFIA2023 - Instructional Activity
DRVF2023, F2223_F1A, F2223_F2, F2223_F3 - Financial data (Not really needed)
GR200_23 - 200% (8yr) grad rate for 2yr and 4yr (Not really needed)
GR2023 - 150% (6yr) grad rate for 2yr and 4yr (Derived variables give it better)
GR2023_L2 - 150% grad rate for less than 2yr institutions (Ignoring sub 2yr)
GR2023_GENDER - 150% grad rate for 2,4yr institutions for those of an unknown gender (Not really needed)
GR2023_PELL_SSL - 150% grad rate for 2,4yr institutions for those geting pell/stafford grants (Not really needed)
DRVHR2023 - HR Data (Not really needed)
OM2023, DRVOM2023 - Outcome Measures (Can find from other tables)
IC2023_PCCAMPUSES - Branch campus locations (Few schools are branch campuses)
IC2023Mission - Mission Statements (Not really needed)
IC2023_PY - Vocational Programs (Ignored)
DRVIC2023 - Derived variables for student charges (Can be easily calculated using the few variables in IC2023_AY)
SAL2023_IS, SAL2023_NIS - Salary Information (Not needed)
S2023_IS, S2023_NH, S2023_OC, S2023_SIS -  Staff data (Maybe implement later)
SFAV2223 - Veterans FA (Too niche)
SFA2223_P2 - Student financial aid (use data from SFA2223_P1)
"""


schema = {
    "core": {
        "UNITID": "ID",
        "INSTNM": "NAME",
        "IALIAS": "ALIAS",
        "GALIAS": "GEN_ALIAS",
        "ADDR": "ADDRESS",
        "CITY": "CITY",
        "STABBR": "STATE",
        "LONGITUD": "LONGITUDE",
        "LATITUDE": "LATITUDE",
        "GENTELE": "PHONE",
        "WEBADDR": "URL",
        "HDEGOFR1": "HGH_DEG",
        "HOSPITAL": "HOSPITAL",
        "MEDICAL": "MED_DEG",
        "C21BASIC": "CRN_BASIC",
        "C21UGPRF": "CRN_UGRD",
        "C21ENPRF": "CRN_ENRL",
        "C21SZSET": "CRN_SIZE",
        "LOCALE": "URBAN",
        "F1SYSTYP": "MC_SYS",
        "F1SYSNAM": "MC_SYS_NM",
        "F1SYSCOD": "MC_SYS_ID",
        "CNTLAFFI": "INST_CONTROL",
        "RELAFFIL": "RELIG_CONTROL",
        "CALSYS": "CAL_SYS",
        "ASSOC1": "NCAA_AFFL",
        "DIV_DIV": "NCAA_DIV",
    },
    "admissions": {
        "UNITID": "ID",
        "ADMCON1": "CON_HS_GPA",
        "ADMCON2": "CON_CLASS_RANK",
        "ADMCON3": "CON_HS_RECORD",
        "ADMCON4": "CON_PREP_PROGRAM",
        "ADMCON5": "CON_RECOMMENDATIONS",
        "ADMCON6": "CON_COMPETENCIES",
        "ADMCON7": "CON_TEST_SCORES",
        "ADMCON8": "CON_ENGLISH_TEST",
        "ADMCON9": "CON_OTHER_TESTS",
        "ADMCON10": "CON_WORK_EXPERIENCE",
        "ADMCON11": "CON_ESSAY",
        "ADMCON12": "CON_LEGACY",
        "APPLCNM": "APPL_MEN",
        "APPLCNW": "APPL_WOMEN",
        "APPLCNAN": "APPL_OTHER",
        "APPLCNUN": "APPL_UNKNOWN",
        "APPLCN": "APPL_TOTAL",
        "ADMSSNM": "ADM_MEN",
        "ADMSSNW": "ADM_WOMEN",
        "ADMSSNAN": "ADM_OTHER",
        "ADMSSNUN": "ADM_UNKNOWN",
        "ADMSSN": "ADM_TOTAL",
        "ENRLM": "ENRL_MEN",
        "ENRLW": "ENRL_WOMEN",
        "ENRLAN": "ENRL_OTHER",
        "ENRLUN": "ENRL_UNKNOWN",
        "ENRLT": "ENRL_TOTAL",
        "SATPCT": "SAT_PCT",
        "ACTPCT": "ACT_PCT",
        "SATVR25": "SAT_RW_25",
        "SATVR50": "SAT_RW_50",
        "SATVR75": "SAT_RW_75",
        "SATMT25": "SAT_MATH_25",
        "SATMT50": "SAT_MATH_50",
        "SATMT75": "SAT_MATH_75",
        "ACTCM25": "ACT_COMP_25",
        "ACTCM50": "ACT_COMP_50",
        "ACTCM75": "ACT_COMP_75",
        "ACTEN25": "ACT_ENG_25",
        "ACTEN50": "ACT_ENG_50",
        "ACTEN75": "ACT_ENG_75",
        "ACTMT25": "ACT_MATH_25",
        "ACTMT50": "ACT_MATH_50",
        "ACTMT75": "ACT_MATH_75",
        "DVADM01": "ACC_RATE",
        "DVADM02": "ACC_RATE_MEN",
        "DVADM03": "ACC_RATE_WOMEN",
        "DVADM04": "YIELD_RATE",
        "DVADM05": "YIELD_RATE_MEN",
        "DVADM06": "YIELD_RATE_WOMEN",
        "CREDITS3": "AP_CREDIT",
    },
    "enrollment": {
        "UNITID": "ID",
        "UGOFFER": "OFFERS_UGRD",
        "GROFFER": "OFFERS_GRAD",
        "INSTSIZE": "INSTSIZE",
        "UNDUP": "TOTAL_POP",
        "UNDUPUG": "UGRD_POP",
        "E12GRAD": "GRAD_POP",
        "E12FT": "FT_POP",
        "E12PT": "PT_POP",
        "PCTE12AN": "PCT_NATIVE",
        "PCTE12AS": "PCT_ASIAN",
        "PCTE12BK": "PCT_BLACK",
        "PCTE12HS": "PCT_HISPANIC",
        "PCTE12NH": "PCT_PACIFIC",
        "PCTE12WH": "PCT_WHITE",
        "PCTE122M": "PCT_TWO",
        "PCTE12UN": "PCT_UNKNOWN",
        "PCTE12NR": "PCT_NONRESIDENT",
        "PCTE12W": "PCT_WOMEN",
        "PCTE12DEEXC": "PCT_ONLINE_ONLY",
        "PCTE12DESOM": "PCT_SOME_ONLINE",
        "PCTE12DENON": "PCT_NO_ONLINE",
        "ALLONCAM": "FRSH_CAMP_REQ",
    },
    "costs": {
        "UNITID": "ID",
        "APPLFEEU": "UG_APP_FEE",
        "APPLFEEG": "GR_APP_FEE",
        "NPRICURL": "NET_CALC_URL",
        "TUITVARY": "TUIT_VARY",
        "ROOM": "OFFERS_HOUSING",
        "ROOMCAP": "HOUSING_CAPACITY",
        "BOARD": "OFFERS_MEAL_PLAN",
        "MEALSWK": "MEALS_WK",
        "ROOMAMT": "DORM_COST",
        "BOARDAMT": "MEALS_COST",
        "RMBRDAMT": "RM_MLS_COST",
        "SCFA12P": "IN_PCT",
        "CHG2AT3": "IN_TUITION",
        "CHG2AF3": "IN_FEES",
        "CHG2AY3": "IN_TOTAL_COST",
        "SCFA13P": "OUT_PCT",
        "CHG3AT3": "OUT_TUIT",
        "CHG3AF3": "OUT_FEES",
        "CHG3AY3": "OUT_TOTAL_COST",
        "CHG4AY3": "SUPP_COST",
        "CHG5AY3": "ON_DORM_MLS_COST",
        "CHG6AY3": "ON_OTHER_COST",
        "CHG7AY3": "OFF_DORM_MLS_COST",
        "CHG8AY3": "OFF_OTHER_COST",
        "CHG9AY3": "OFF_FAMILY_OTHER_COST",
        "SCFA14P": "PCT_UNKWN_TUIT",
        "UAGRNTP": "PCT_GRANT_AID",
        "UAGRNTA": "AVG_GRANT_AID_AMT",
        # "TUITPL": "HAS_TUITION_PLAN",
        # "TUITPL1": "HAS_GUARANTEED_TUITION_PLAN",
        # "TUITPL2": "HAS_PREPAID_TUITION_PLAN",
        # "TUITPL3": "HAS_TUITION_PAYMENT_PLAN",
        # "TUITPL4": "HAS_OTHER_TUITION_PLAN",
    },
    "outcomes": {
        "UNITID": "ID",
        "RET_PCF": "RET_RATE_FT",
        "RET_PCP": "RET_RATE_PT",
        "STUFACR": "STU_FAC",
        "TRRTTOT": "TRANSFER_OUT_RATE",
        "GBA4RTT": "GRAD_RATE_4_YR",
        "GBA5RTT": "GRAD_RATE_5_YR",
        "GBA6RTT": "GRAD_RATE_6_YR",
    },
    "services": {
        "UNITID": "ID",
        "ADMINURL": "ADM_URL",
        "FAIDURL": "FAID_URL",
        "APPLURL": "APPL_URL",
        "SLO5": "ROTC",
        "SLO6": "STUDY_ABROAD",
        "SLO8": "TEACHER_CERT",
        "SLOA": "UG_RESEARCH",
        "SLO9": "NO_SPECIAL_LEARNING",
        "STUSRV2": "CAREER_COUNSELING",
        "STUSRV3": "EMPLOYMENT_SERVICES",
        "STUSRV4": "PLACEMENT_SERVICES",
        "STUSRV9": "NO_STUDENT_SERVICES",
    },
    # "sports": {
    #     "UNITID": "ID",
    # "ASSOC1": "NCAA_AFFL",
    # "DIV_DIV": "NCAA_DIV",
    #     "SPORT1": "FOOTBALL",
    #     "CONFNO1_DUP": "FOOTBALL_CONF",
    #     "CONFNO1": "FOOTBALL_CONF_ID",
    #     "SPORT2": "BASKETBALL",
    #     "CONFNO2_DUP": "BASKETBALL_CONF",
    #     "CONFNO2": "BASKETBALL_CONF_ID",
    #     "SPORT3": "BASEBALL",
    #     "CONFNO3_DUP": "BASEBALL_CONF",
    #     "CONFNO3": "BASEBALL_CONF_ID",
    #     "SPORT4": "TRACK",
    #     "CONFNO4_DUP": "TRACK_CONF",
    #     "CONFNO4": "TRACK_CONF_ID",
    # },
}
# TODO: GET EARNINGS DATA FROM SCORECARD OR SOMETHING SIMILAR
