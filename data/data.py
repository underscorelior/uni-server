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
    "DRVF2023": [  # Derived variables of financial data
        "UNITID",
        "F1ENDMFT",  # Form 1 - Endowment assets - Market value at the end of the fiscal year (Public)
        "F2ENDMFT",  # Form 2 - Endowment assets - Market value at the end of the fiscal year (Private non-profit)
        "F3CORREV",  # Form 3 - Core revenues (Private for-profit - used to calculate endowment per FTE)
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
F2223_F1A, F2223_F2, F2223_F3 - Financial data (Not really needed)
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
        "UNITID": "id",
        "INSTNM": "name",
        "IALIAS": "alias",
        "GALIAS": "gen_alias",
        "ADDR": "address",
        "CITY": "city",
        "STABBR": "state",
        "LONGITUD": "longitude",
        "LATITUDE": "latitude",
        "GENTELE": "phone",
        "WEBADDR": "url",
        "YEAR": "year",
        "HDEGOFR1": "hgh_deg",
        "HOSPITAL": "hospital",
        "MEDICAL": "med_deg",
        "C21BASIC": "crn_basic",
        "C21UGPRF": "crn_ugrd",
        "C21ENPRF": "crn_enrl",
        "C21SZSET": "crn_size",
        "LOCALE": "urban",
        "F1SYSTYP": "mc_sys",
        "F1SYSNAM": "mc_sys_nm",
        "F1SYSCOD": "mc_sys_id",
        "CNTLAFFI": "inst_control",
        "RELAFFIL": "relig_control",
        "CALSYS": "cal_sys",
        "ASSOC1": "ncaa_affl",
        "DIV_DIV": "ncaa_div",
        "RND_SPEND": "rnd_spend",
        "ENDOW_FTE": "endow_fte",
        "QS_CPF": "qs_cpf",
    },
    "admissions": {
        "UNITID": "id",
        "ADMCON1": "con_hs_gpa",
        "ADMCON2": "con_class_rank",
        "ADMCON3": "con_hs_record",
        "ADMCON4": "con_prep_program",
        "ADMCON5": "con_recommendations",
        "ADMCON6": "con_competencies",
        "ADMCON7": "con_test_scores",
        "ADMCON8": "con_english_test",
        "ADMCON9": "con_other_tests",
        "ADMCON10": "con_work_experience",
        "ADMCON11": "con_essay",
        "ADMCON12": "con_legacy",
        "APPLCNM": "appl_male",
        "APPLCNW": "appl_female",
        "APPLCNAN": "appl_other",
        "APPLCNUN": "appl_unknown",
        "APPLCN": "appl_total",
        "ADMSSNM": "adm_male",
        "ADMSSNW": "adm_female",
        "ADMSSNAN": "adm_other",
        "ADMSSNUN": "adm_unknown",
        "ADMSSN": "adm_total",
        "ENRLM": "enrl_male",
        "ENRLW": "enrl_female",
        "ENRLAN": "enrl_other",
        "ENRLUN": "enrl_unknown",
        "ENRLT": "enrl_total",
        "SATPCT": "sat_pct",
        "ACTPCT": "act_pct",
        "SATVR25": "sat_rw_25",
        "SATVR50": "sat_rw_50",
        "SATVR75": "sat_rw_75",
        "SATMT25": "sat_math_25",
        "SATMT50": "sat_math_50",
        "SATMT75": "sat_math_75",
        "ACTCM25": "act_comp_25",
        "ACTCM50": "act_comp_50",
        "ACTCM75": "act_comp_75",
        "ACTEN25": "act_eng_25",
        "ACTEN50": "act_eng_50",
        "ACTEN75": "act_eng_75",
        "ACTMT25": "act_math_25",
        "ACTMT50": "act_math_50",
        "ACTMT75": "act_math_75",
        "DVADM01": "acc_rate",
        "DVADM02": "acc_rate_male",
        "DVADM03": "acc_rate_female",
        "DVADM04": "yield_rate",
        "DVADM05": "yield_rate_male",
        "DVADM06": "yield_rate_female",
        "CREDITS3": "ap_credit",
        "ADMINURL": "adm_url",
        "APPLURL": "appl_url",
        "APPLFEEU": "ug_app_fee",
        "APPLFEEG": "gr_app_fee",
    },
    "enrollment": {
        "UNITID": "id",
        "UGOFFER": "offers_ugrd",
        "GROFFER": "offers_grad",
        "INSTSIZE": "instsize",
        "UNDUP": "total_pop",
        "FTE12MN": "fte_pop",
        "UNDUPUG": "ugrd_pop",
        "E12GRAD": "grad_pop",
        "E12FT": "ft_pop",
        "E12PT": "pt_pop",
        "PCTE12AN": "pct_native",
        "PCTE12AS": "pct_asian",
        "PCTE12BK": "pct_black",
        "PCTE12HS": "pct_hispanic",
        "PCTE12NH": "pct_pacific",
        "PCTE12WH": "pct_white",
        "PCTE122M": "pct_two",
        "PCTE12UN": "pct_unknown",
        "PCTE12NR": "pct_nonresident",
        "PCTE12W": "pct_female",
        "PCTE12DEEXC": "pct_online_only",
        "PCTE12DESOM": "pct_some_online",
        "PCTE12DENON": "pct_no_online",
        "ALLONCAM": "frsh_camp_req",
    },
    "costs": {
        "UNITID": "id",
        "NPRICURL": "net_calc_url",
        "TUITVARY": "tuit_vary",
        "ROOM": "offers_housing",
        "ROOMCAP": "housing_capacity",
        "BOARD": "offers_meal_plan",
        "MEALSWK": "meals_wk",
        "ROOMAMT": "dorm_cost",
        "BOARDAMT": "meals_cost",
        "RMBRDAMT": "rm_mls_cost",
        "SCFA12P": "in_pct",
        "CHG2AT3": "in_tuition",
        "CHG2AF3": "in_fees",
        "CHG2AY3": "in_total_cost",
        "SCFA13P": "out_pct",
        "CHG3AT3": "out_tuition",
        "CHG3AF3": "out_fees",
        "CHG3AY3": "out_total_cost",
        "CHG4AY3": "supp_cost",
        "CHG5AY3": "on_dorm_mls_cost",
        "CHG6AY3": "on_other_cost",
        "CHG7AY3": "off_dorm_mls_cost",
        "CHG8AY3": "off_other_cost",
        "CHG9AY3": "off_family_other_cost",
        "SCFA14P": "pct_unkwn_tuit",
        "UAGRNTP": "pct_grant_aid",
        "UAGRNTA": "avg_grant_aid_amt",
        # "TUITPL": "HAS_TUITION_PLAN",
        # "TUITPL1": "HAS_GUARANTEED_TUITION_PLAN",
        # "TUITPL2": "HAS_PREPAID_TUITION_PLAN",
        # "TUITPL3": "HAS_TUITION_PAYMENT_PLAN",
        # "TUITPL4": "HAS_OTHER_TUITION_PLAN",
    },
    "outcomes": {
        "UNITID": "id",
        "RET_PCF": "ret_rate_ft",
        "RET_PCP": "ret_rate_pt",
        "STUFACR": "stu_fac",
        "TRRTTOT": "transfer_out_rate",
        "GBA4RTT": "grad_rate_4_yr",
        "GBA5RTT": "grad_rate_5_yr",
        "GBA6RTT": "grad_rate_6_yr",
    },
    "services": {
        "UNITID": "id",
        "FAIDURL": "faid_url",
        "SLO5": "rotc",
        "SLO6": "study_abroad",
        "SLO8": "teacher_cert",
        "SLOA": "ug_research",
        "SLO9": "no_special_learning",
        "STUSRV2": "career_counseling",
        "STUSRV3": "employment_services",
        "STUSRV4": "placement_services",
        "STUSRV9": "no_student_services",
    },
    "rankings": {
        "UNITID": "id",
        "SCORE": "score",
        "OVERALL": "overall",
        "ST_RNK": "state",
        "INST_RNK": "control",
        "ST_INST_RNK": "state_control",
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
