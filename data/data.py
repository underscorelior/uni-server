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
        "DVADM07",  # Yield - full time
        "DVADM08",  # Yield - full time men
        "DVADM09",  # Yield - full time women
        "DVADM10",  # Yield - part time
        "DVADM11",  # Yield - part time men
        "DVADM12",  # Yield - part time women
    ],
    # "C2023_A": [  # Completions by CIP code
    #     "UNITID",
    #     "CIPCODE",
    #     "AWLEVEL",  # Award Level
    #     "CTOTALT",  # Grand total
    #     "CTOTALM",  # Grand total men
    #     "CTOTALW",  # Grand total women
    # ],  # IDEAS: Add a filter to see how many people graduated by specific major, dont show if doesnt exist. Maybe other forms of search too.
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
        "DSTNCED3",  # Does not offer distance edu opportunities
        "DISTNCED",  # All programs offered completely via distance education
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
        "ADDR": "ADDRESS",
        "CITY": "CITY",
        "STABBR": "STATE",
        "GENTELE": "PHONE",
        "WEBADDR": "WEBSITE",
        "ADMINURL": "ADMISSIONS_URL",
        "FAIDURL": "AID_URL",
        "APPLURL": "APPLY_URL",
        "NPRICURL": "NET_PRICE_URL",
    },
    "admissions": {
        "UNITID": "ID",
        "ADMCON1": "HS_GPA",
        "ADMCON2": "CLASS_RANK",
        "ADMCON3": "HS_RECORD",
        "ADMCON4": "PREP_PROGRAM",
        "ADMCON5": "RECOMMENDATIONS",
        "ADMCON6": "COMPETENCIES",
        "ADMCON7": "TEST_SCORES",
        "ADMCON8": "ENGLISH_TEST",
        "ADMCON9": "OTHER_TESTS",
        "ADMCON10": "WORK_EXPERIENCE",
        "ADMCON11": "ESSAY",
        "ADMCON12": "LEGACY",
        "APPLCNM": "APPLICANTS_MEN",
        "APPLCNW": "APPLICANTS_WOMEN",
        "APPLCNAN": "APPLICANTS_OTHER",
        "APPLCNUN": "APPLICANTS_UNKNOWN",
        "ADMSSNM": "ADMITS_MEN",
        "ADMSSNW": "ADMITS_WOMEN",
        "ADMSSNAN": "ADMITS_OTHER",
        "ADMSSNUN": "ADMITS_UNKNOWN",
        "ENRLM": "ENROLLED_MEN",
        "ENRLW": "ENROLLED_WOMEN",
        "ENRLAN": "ENROLLED_OTHER",
        "ENRLUN": "ENROLLED_UNKNOWN",
        "ENRLT": "ENROLLED_TOTAL",
        "APPLCN": "APPLICANTS_TOTAL",
        "ADMSSN": "ADMITS_TOTAL",
        "ENRLPT": "PART_TIME",
        "ENRLFT": "FULL_TIME",
        "SATPCT": "SAT_SUBMIT_PCT",
        "ACTPCT": "ACT_SUBMIT_PCT",
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
        "DVADM01": "PCT_ADMITTED_TOTAL",
        "DVADM04": "YIELD_TOTAL",
    },
    "enrollment": {
        "UNITID": "ID",
        "FTE12MN": "FTE_ENROLLMENT",
        "UNDUP": "UNDUPLICATED_TOTAL",
        "UNDUPUG": "UNDUP_UNDERGRAD",
        "E12GRAD": "UNDUP_GRAD",
        "E12FT": "FULL_TIME_HEADCOUNT",
        "E12PT": "PART_TIME_HEADCOUNT",
        "PCTE12AN": "PCT_NATIVE_AMERICAN",
        "PCTE12AS": "PCT_ASIAN",
        "PCTE12BK": "PCT_BLACK",
        "PCTE12HS": "PCT_HISPANIC",
        "PCTE12NH": "PCT_HAWAIIAN",
        "PCTE12WH": "PCT_WHITE",
        "PCTE122M": "PCT_TWO_OR_MORE",
        "PCTE12UN": "PCT_UNKNOWN_RACE",
        "PCTE12NR": "PCT_NONRESIDENT",
        "PCTE12W": "PCT_WOMEN",
        "PCTE12DEEXC": "ALL_DISTANCE",
        "PCTE12DESOM": "SOME_DISTANCE",
        "PCTE12DENON": "NO_DISTANCE",
        "EFYDEEXC": "EFFY_ALL_ONLINE",
        "EFYDESOM": "EFFY_SOME_ONLINE",
        "EFYDENON": "EFFY_NO_ONLINE",
    },
    "costs": {
        "UNITID": "ID",
        "CHG2AY3": "TUITION_FEES_IN_STATE",
        "CHG3AY3": "TUITION_FEES_OUT_STATE",
        "CHG4AY3": "BOOKS_SUPPLIES",
        "CHG5AY3": "ON_CAMPUS_LIVING",
        "CHG6AY3": "ON_CAMPUS_OTHER",
        "CHG7AY3": "OFF_CAMPUS_LIVING",
        "CHG8AY3": "OFF_CAMPUS_OTHER",
        "CHG9AY3": "WITH_FAMILY_OTHER",
        "SCFA12P": "PCT_IN_STATE_RATE",
        "SCFA13P": "PCT_OUT_STATE_RATE",
        "SCFA14P": "PCT_UNKNOWN_RATE",
        "UAGRNTP": "PCT_UNDERGRAD_AID",
        "UAGRNTA": "AVG_UNDERGRAD_AID",
    },
    "outcomes": {
        "UNITID": "ID",
        "RET_PCF": "RETENTION_FULL_TIME",
        "RET_PCP": "RETENTION_PART_TIME",
        "STUFACR": "STUDENT_FACULTY_RATIO",
        "TRRTTOT": "TRANSFER_RATE",
        "GBA4RTT": "GRAD_RATE_4YR",
        "GBA5RTT": "GRAD_RATE_5YR",
        "GBA6RTT": "GRAD_RATE_6YR",
    },
    "services": {
        "UNITID": "ID",
        "ALLONCAM": "REQUIRES_ON_CAMPUS",
        "ROOM": "HAS_HOUSING",
        "ROOMCAP": "HOUSING_CAPACITY",
        "ROOMAMT": "HOUSING_COST",
        "BOARD": "HAS_MEALS",
        "MEALSWK": "MEALS_PER_WEEK",
        "BOARDAMT": "MEAL_COST",
        "RMBRDAMT": "TOTAL_LIVING_COST",
        "STUSRV2": "COUNSELING",
        "STUSRV3": "EMPLOYMENT_SERVICES",
        "STUSRV4": "PLACEMENT_SERVICES",
    },
    "sports": {
        "UNITID": "ID",
        "ASSOC1": "NCAA_AFFILIATION",
        "SPORT1": "FOOTBALL",
        "CONFNO1": "FOOTBALL_CONF",
        "SPORT2": "BASKETBALL",
        "CONFNO2": "BASKETBALL_CONF",
        "SPORT3": "BASEBALL",
        "CONFNO3": "BASEBALL_CONF",
        "SPORT4": "TRACK",
        "CONFNO4": "TRACK_CONF",
    },
}


schema_2 = {
    "core": {
        "UNITID": "UNITID",
        "INSTNM": "NAME",
        "IALIAS": "ALIAS",
        "ADDR": "ADDRESS",
        "CITY": "CITY",
        "STABBR": "STATE",
        "LONGITUD": "LONGITUDE",
        "LATITUDE": "LATITUDE",
        "GENTELE": "PHONE",
        "WEBADDR": "WEBSITE",
        "HDEGOFR1": "HIGHEST_DEGREE",
        "HOSPITAL": "HAS_HOSPITAL",
        "MEDICAL": "IS_MEDICAL_SCHOOL",
        "C21BASIC": "CARNEGIE_BASIC",
        "C21UGPRF": "CARNEGIE_UG_PROFILE",
        "C21ENPRF": "CARNEGIE_ENROLL_PROFILE",
        "C21SZSET": "CARNEGIE_SIZE_SETTING",
        "LOCALE": "LOCALE_TYPE",
        "F1SYSTYP": "SYSTEM_TYPE",
        "F1SYSNAM": "SYSTEM_NAME",
        "F1SYSCOD": "SYSTEM_ID",
        "CNTLAFFI": "INSTITUTION_CONTROL",
        "RELAFFIL": "RELIGIOUS_AFFILIATION",
        "CALSYS": "CALENDAR_SYSTEM",
        "DSTNCED3": "NO_DISTANCE_ED",
        "DISTNCED": "FULLY_ONLINE",
        "ALLONCAM": "FRESHMEN_ON_CAMPUS_REQUIRED",
    },
    "admissions": {
        "UNITID": "UNITID",
        "ADMCON1": "CONSIDERATION_GPA",
        "ADMCON2": "CONSIDERATION_RANK",
        "ADMCON3": "CONSIDERATION_RECORD",
        "ADMCON4": "CONSIDERATION_COLLEGE_PREP",
        "ADMCON5": "CONSIDERATION_RECOMMENDATIONS",
        "ADMCON6": "CONSIDERATION_COMPETENCIES",
        "ADMCON7": "CONSIDERATION_TEST_SCORES",
        "ADMCON8": "CONSIDERATION_ENGLISH_TEST",
        "ADMCON9": "CONSIDERATION_OTHER_TEST",
        "ADMCON10": "CONSIDERATION_WORK_EXP",
        "ADMCON11": "CONSIDERATION_ESSAY",
        "ADMCON12": "CONSIDERATION_LEGACY",
        "APPLCNM": "APPLICANTS_MEN",
        "APPLCNW": "APPLICANTS_WOMEN",
        "APPLCNAN": "APPLICANTS_ANOTHER_GENDER",
        "APPLCNUN": "APPLICANTS_GENDER_UNKNOWN",
        "ADMSSNM": "ADMITTED_MEN",
        "ADMSSNW": "ADMITTED_WOMEN",
        "ADMSSNAN": "ADMITTED_ANOTHER_GENDER",
        "ADMSSNUN": "ADMITTED_GENDER_UNKNOWN",
        "APPLCN": "APPLICANTS_TOTAL",
        "ADMSSN": "ADMITTED_TOTAL",
        "SATPCT": "SAT_SUBMIT_PERCENT",
        "ACTPCT": "ACT_SUBMIT_PERCENT",
        "SATVR25": "SAT_EBRW_25_PCT",
        "SATVR50": "SAT_EBRW_50_PCT",
        "SATVR75": "SAT_EBRW_75_PCT",
        "SATMT25": "SAT_MATH_25_PCT",
        "SATMT50": "SAT_MATH_50_PCT",
        "SATMT75": "SAT_MATH_75_PCT",
        "ACTCM25": "ACT_COMPOSITE_25_PCT",
        "ACTCM50": "ACT_COMPOSITE_50_PCT",
        "ACTCM75": "ACT_COMPOSITE_75_PCT",
        "ACTEN25": "ACT_ENGLISH_25_PCT",
        "ACTEN50": "ACT_ENGLISH_50_PCT",
        "ACTEN75": "ACT_ENGLISH_75_PCT",
        "ACTMT25": "ACT_MATH_25_PCT",
        "ACTMT50": "ACT_MATH_50_PCT",
        "ACTMT75": "ACT_MATH_75_PCT",
        "DVADM01": "ADMIT_RATE_TOTAL",
        "DVADM02": "ADMIT_RATE_MEN",
        "DVADM03": "ADMIT_RATE_WOMEN",
        "CREDITS3": "ACCEPTS_AP_CREDIT",
    },
    "enrollment": {
        "UNITID": "UNITID",
        "UGOFFER": "HAS_UNDERGRAD_OFFERING",
        "GROFFER": "HAS_GRAD_OFFERING",
        "INSTSIZE": "INSTITUTION_SIZE",
        "ENRLM": "ENROLLED_MEN",
        "ENRLW": "ENROLLED_WOMEN",
        "ENRLAN": "ENROLLED_ANOTHER_GENDER",
        "ENRLUN": "ENROLLED_GENDER_UNKNOWN",
        "ENRLT": "ENROLLED_TOTAL",
        "ENRLPT": "ENROLLED_PART_TIME",
        "ENRLFT": "ENROLLED_FULL_TIME",
        "FTE12MN": "FTE_ENROLLMENT_12_MONTH",
        "UNDUP": "HEADCOUNT_12_MONTH",
        "UNDUPUG": "UG_HEADCOUNT_12_MONTH",
        "E12GRAD": "GRAD_HEADCOUNT_12_MONTH",
        "E12FT": "FT_HEADCOUNT_12_MONTH",
        "E12PT": "PT_HEADCOUNT_12_MONTH",
        "PCTE12AN": "PCT_AMERICAN_INDIAN_ALASKA_NATIVE",
        "PCTE12AS": "PCT_ASIAN",
        "PCTE12BK": "PCT_BLACK",
        "PCTE12HS": "PCT_HISPANIC",
        "PCTE12NH": "PCT_HAWAIIAN_PACIFIC_ISLANDER",
        "PCTE12WH": "PCT_WHITE",
        "PCTE122M": "PCT_TWO_OR_MORE_RACES",
        "PCTE12UN": "PCT_RACE_UNKNOWN",
        "PCTE12NR": "PCT_NONRESIDENT",
        "PCTE12W": "PCT_WOMEN",
        "PCTE12DEEXC": "PCT_ONLINE_ONLY",
        "PCTE12DESOM": "PCT_SOME_ONLINE",
        "PCTE12DENON": "PCT_NO_ONLINE",
    },
    "costs": {
        "UNITID": "UNITID",
        "APPLFEEU": "UG_APP_FEE",
        "NPRICURL": "NET_PRICE_CALC_URL",
        "TUITVARY": "TUITION_VARIES_BY_RESIDENCY",
        "ROOM": "OFFERS_HOUSING",
        "ROOMCAP": "HOUSING_CAPACITY",
        "BOARD": "OFFERS_MEAL_PLAN",
        "MEALSWK": "MEALS_PER_WEEK",
        "ROOMAMT": "HOUSING_COST_AY",
        "BOARDAMT": "MEAL_PLAN_COST_AY",
        "RMBRDAMT": "ROOM_AND_BOARD_COST_AY",
        "CHG2AT3": "TUITION_IN_STATE",
        "CHG2AF3": "FEES_IN_STATE",
        "CHG2AY3": "TUITION_FEES_IN_STATE",
        "CHG3AT3": "TUITION_OUT_OF_STATE",
        "CHG3AF3": "FEES_OUT_OF_STATE",
        "CHG3AY3": "TUITION_FEES_OUT_OF_STATE",
        "CHG4AY3": "BOOKS_SUPPLIES_COST",
        "CHG5AY3": "ON_CAMPUS_ROOM_BOARD_COST",
        "CHG6AY3": "ON_CAMPUS_OTHER_EXPENSES",
        "CHG7AY3": "OFF_CAMPUS_ROOM_BOARD_COST",
        "CHG8AY3": "OFF_CAMPUS_OTHER_EXPENSES",
        "CHG9AY3": "OFF_CAMPUS_WITH_FAMILY_OTHER_EXPENSES",
        "SCFA12P": "PCT_PAYING_IN_STATE",
        "SCFA13P": "PCT_PAYING_OUT_OF_STATE",
        "SCFA14P": "PCT_PAYING_UNKNOWN_RATE",
        "UAGRNTP": "PCT_RECEIVING_GRANT_AID",
        "UAGRNTA": "AVG_GRANT_AID_AMOUNT",
        "TUITPL": "HAS_TUITION_PLAN",
        "TUITPL1": "HAS_GUARANTEED_TUITION_PLAN",
        "TUITPL2": "HAS_PREPAID_TUITION_PLAN",
        "TUITPL3": "HAS_TUITION_PAYMENT_PLAN",
        "TUITPL4": "HAS_OTHER_TUITION_PLAN",
    },
    "outcomes": {
        "UNITID": "UNITID",
        "RET_PCF": "RETENTION_RATE_FULL_TIME",
        "RET_PCP": "RETENTION_RATE_PART_TIME",
        "STUFACR": "STUDENT_FACULTY_RATIO",
        "TRRTTOT": "TRANSFER_OUT_RATE_TOTAL",
        "GBA4RTT": "GRAD_RATE_4_YEAR",
        "GBA5RTT": "GRAD_RATE_5_YEAR",
        "GBA6RTT": "GRAD_RATE_6_YEAR",
        "DVADM04": "YIELD_RATE_TOTAL",
        "DVADM05": "YIELD_RATE_MEN",
        "DVADM06": "YIELD_RATE_WOMEN",
        "DVADM07": "YIELD_RATE_FULL_TIME",
        "DVADM08": "YIELD_RATE_FT_MEN",
        "DVADM09": "YIELD_RATE_FT_WOMEN",
        "DVADM10": "YIELD_RATE_PART_TIME",
        "DVADM11": "YIELD_RATE_PT_MEN",
        "DVADM12": "YIELD_RATE_PT_WOMEN",
    },
    "services": {
        "UNITID": "UNITID",
        "ADMINURL": "ADMISSIONS_URL",
        "FAIDURL": "FINANCIAL_AID_URL",
        "APPLURL": "APPLICATION_URL",
        "SLO5": "OFFERS_ROTC",
        "SLO6": "OFFERS_STUDY_ABROAD",
        "SLO8": "OFFERS_TEACHER_CERT",
        "SLOA": "OFFERS_UG_RESEARCH",
        "SLO9": "NO_SPECIAL_LEARNING_OPPS",
        "STUSRV2": "HAS_ACADEMIC_CAREER_COUNSELING",
        "STUSRV3": "HAS_EMPLOYMENT_SERVICES",
        "STUSRV4": "HAS_PLACEMENT_SERVICES",
        "STUSRV9": "NO_STUDENT_SERVICES",
    },
    "sports": {
        "UNITID": "UNITID",
        "ASSOC1": "ATHLETIC_ASSOCIATION",
        "SPORT1": "HAS_FOOTBALL",
        "CONFNO1": "FOOTBALL_CONFERENCE",
        "SPORT2": "HAS_BASKETBALL",
        "CONFNO2": "BASKETBALL_CONFERENCE",
        "SPORT3": "HAS_BASEBALL",
        "CONFNO3": "BASEBALL_CONFERENCE",
        "SPORT4": "HAS_TRACK",
        "CONFNO4": "TRACK_CONFERENCE",
    },
}
