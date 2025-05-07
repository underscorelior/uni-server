# Database Information

This is a filtered list of the data inside the access database provided by [IPEDS](https://nces.ed.gov/ipeds/). The selected data is what I need for the project.

## General Information

### HD2023 - Directory Information

-   UNITID - ID
-   INSTNM - Name of the institution
-   IALIAS - Alias
-   CITY - City where the institution is located
-   STABBR - State abbreviation
-   WEBADDR - Web address
-   ADMINURL - Admissions URL
-   FAIDURL - Financial aid URL
-   APPLURL - Application URL
-   NPRICURL - Net price calculator URL - Maybe include link next to all the fin data saying "CALCULATE HERE"
-   LONGITUD - Longitude
-   LATITUDE - Latitude
-   HDEGOFR1 - Highest degree offered
    -   11 - Doctor's degree - research/scholarship and professional practice
    -   12 - Doctor's degree - research/scholarship
    -   13 - Doctor's degree - professional practice
    -   14 - Doctor's degree - other
    -   20 - Master's degree
    -   30 - Bachelor's degree
    -   40 - Associate's degree
    -   0 - Non-degree granting
    -   -3 - {Not available}

### IC2023 - Institutional Characteristics

-   CNTLAFFI - Control of institution

    -   1 Public
    -   2 Private for-profit
    -   3 Private nonprofit (no religious affiliation)
    -   4 Private nonprofit (religious affiliation)
    -   -1 Not reported

-   CALSYS - Calendar system
    -   1 Semester
    -   2 Quarter
    -   3 Trimester
    -   4 Four-one-four plan
    -   5 Other academic year
    -   6 Differs by program
    -   7 Continuous
    -   -2 Not applicable
-   APPLFEEU - Undergraduate application fee
-   ROOMAMT - Room charges
-   ROOMCAP - Room capacity
-   BOARDAMT - Board charges (food)
-   MEALSWK - Meals per week
-   TUITVARY - Does tuition vary for in-state vs out-of-state students
    -   1 Yes
    -   2 No
    -   -1 Not reported
    -   -2 Not applicable
-   ROOM - Does the institution provide on-campus housing
    -   1 Yes
    -   2 No
    -   -1 Not reported
    -   -2 Not applicable
-   BOARD - Does the institution provide a meal plan
    -   1 Yes
    -   2 No
    -   -1 Not reported
    -   -2 Not applicable

### IC2023Mission - Mission Statement

-   MISSIONURL - URL to mission statement (if admission statement missing)
-   MISSION - Mission statement

### IC2023_PCCAMPUSES

-   PCLOCALE - Sector of institution
    -   11 - City: Large
    -   12 - City: Midsize
    -   13 - City: Small
    -   21 - Suburb: Large
    -   22 - Suburb: Midsize
    -   23 - Suburb: Small
    -   31 - Town: Fringe
    -   32 - Town: Distant
    -   33 - Town: Remote
    -   41 - Rural: Fringe
    -   42 - Rural: Distant
    -   43 - Rural: Remote
    -   -3 - Not available

## Academic Data

### EF2023D - Total entering class, retention rates, and student-to-faculty

-   STUFACR - Student-to-faculty ratio
-   RET_PCF - Full-time retention rate
-   RET_PCP - Part-time retention rate

### DRVGR2023 - Derived variables for graduation rates

-   GRRTTOT - Total graduation rate
-   TRRTTOT - Total transfer-out rate
-   GBA4RTT - Graduation rate - Bachelor degree within 4 years, total
-   GBA5RTT - Graduation rate - Bachelor degree within 5 years, total
-   GBA6RTT - Graduation rate - Bachelor degree within 6 years, total

## Admission Data

### ADM2023 - Admission considerations, applicants, admissions, and test scores

-   ADMCON1 - Secondary School GPA

    -   1 Required to be considered for admission
    -   5 Not required for admission, but considered if submitted
    -   3 Not considered for admission, even if submitted
    -   -1 Not reported
    -   -2 Not applicable

-   ADMCON2 - Secondary School Rank

    -   1 Required to be considered for admission
    -   5 Not required for admission, but considered if submitted
    -   3 Not considered for admission, even if submitted
    -   -1 Not reported
    -   -2 Not applicable

-   ADMCON3 - Secondary School Record (aka Rigor of secondary school record on CDS)

    -   1 Required to be considered for admission
    -   5 Not required for admission, but considered if submitted
    -   3 Not considered for admission, even if submitted
    -   -1 Not reported
    -   -2 Not applicable

-   ADMCON4 - Completion of College Preparatory Program

    -   1 Required to be considered for admission
    -   5 Not required for admission, but considered if submitted
    -   3 Not considered for admission, even if submitted
    -   -1 Not reported
    -   -2 Not applicable

-   ADMCON5 - Recommendations

    -   1 Required to be considered for admission
    -   5 Not required for admission, but considered if submitted
    -   3 Not considered for admission, even if submitted
    -   -1 Not reported
    -   -2 Not applicable

-   ADMCON6 - Formal Demonstration of Competencies (portfolio, etc.)

    -   1 Required to be considered for admission
    -   5 Not required for admission, but considered if submitted
    -   3 Not considered for admission, even if submitted
    -   -1 Not reported
    -   -2 Not applicable

-   ADMCON7 - Admission Test Scores

    -   1 Required to be considered for admission
    -   5 Not required for admission, but considered if submitted
    -   3 Not considered for admission, even if submitted
    -   -1 Not reported
    -   -2 Not applicable

-   ADMCON10 - Work Experience

    -   1 Required to be considered for admission
    -   5 Not required for admission, but considered if submitted
    -   3 Not considered for admission, even if submitted
    -   -1 Not reported
    -   -2 Not applicable

-   ADMCON11 - Personal Statement or essay

    -   1 Required to be considered for admission
    -   5 Not required for admission, but considered if submitted
    -   3 Not considered for admission, even if submitted
    -   -1 Not reported
    -   -2 Not applicable

-   ADMCON12 - Legacy

    -   1 Required to be considered for admission
    -   5 Not required for admission, but considered if submitted
    -   3 Not considered for admission, even if submitted
    -   -1 Not reported
    -   -2 Not applicable

-   APPLCN - Total number of applicants
-   ADMSSN - Total number of admitted students
-   ENRLT - Total number of enrolled students
-   APPLCNM - Number of male applicants
-   APPLCNW - Number of female applicants
-   APPLCNAN - Number of applicants of another gender
-   APPLCNUN - Number of applicants of unknown gender
-   ADMSSNM - Number of admitted males
-   ADMSSNW - Number of admitted females
-   ADMSSNAN - Number of admitted another gender
-   ADMSSNUN - Number of admitted unknown gender
-   ENRLM - Number of enrolled males
-   ENRLW - Number of enrolled females
-   ENRLAN - Number of enrolled another gender
-   ENRLUN - Number of enrolled unknown gender

-   SATNUM - Number of students submitting SAT scores
-   SATPCT - Percentage of students submitting SAT scores
-   ACTNUM - Number of students submitting ACT scores
-   ACTPCT - Percentage of students submitting ACT scores
-   SATVR25 - 25th percentile SAT ERW score
-   SATVR50 - 50th percentile SAT ERW score
-   SATVR75 - 75th percentile SAT ERW score
-   SATMT25 - 25th percentile SAT Math score
-   SATMT50 - 50th percentile SAT Math score
-   SATMT75 - 75th percentile SAT Math score
-   ACTCM25 - 25th percentile ACT Composite score
-   ACTCM50 - 50th percentile ACT Composite score
-   ACTCM75 - 75th percentile ACT Composite score

## Enrollment Data

### EFFY2023 - 12-month unduplicated headcount

> I will only be using rows where the EFFYLEV = 1 (All students total) and EFFYALEV = 1 (All students total)

-   EFFYLEV - Undergraduate or graduate level of student
    -   1 - All students total
    -   2 - Undergraduate
    -   4 - Graduate
    -   -2 - Not applicable, undergraduate detail
-   EFFYALEV - Level and degree/certificate-seeking status of student
    > _I will not be including every single value set, there are 27_
    -   1 - All students total
    -   2 - All students, undergraduate total
    -   12 - All students, graduate total
-   EFYTOTLM - Grand total men
-   EFYTOTLW - Grand total women
-   EFYTOTLT - Grand total
-   EFYAIANT - American Indian or Alaska Native total\*
-   EFYASIAT - Asian total\*
-   EFYBKAAT - Black or African American total\*
-   EFYHISPT - Hispanic or Latino total\*
-   EFYNHPIT - Native Hawaiian or Other Pacific Islander total\*
-   EFYWHITT - White total\*
-   EFY2MORT - Two or more races total\*
-   EFYNRALT - U.S. Nonresident total\*
-   EFYUNKNT - Race/ethnicity unknown total\*
-   EFYGUUN - Gender unknown
-   EFYGUAN - Another gender
-   EFYGUKN - Total gender reported as one of the mutually exclusive binary categories (Men/Women)
-   EFYGUTOT - Total of gender unknown and another gender

\*you can replace the T with an M or a W to get the male and female values

### DRVEF122023 - Derived variables for 12-month unduplicated headcount

-   UNDUP - Total headcount
-   UNDUPUG - Undergraduate headcount
-   E12GRAD - Graduate headcount
-   PCTE12AN - Percent of headcount that are American Indian or Alaska Native
-   PCTE12AS - Percent of headcount that are Asian
-   PCTE12BK - Percent of headcount that are Black or African American
-   PCTE12HS - Percent of headcount that are Hispanic/Latino
-   PCTE12NH - Percent of headcount that are Native Hawaiian or Other Pacific Islander
-   PCTE12WH - Percent of headcount that are White
-   PCTE122M - Percent of headcount that are two or more races
-   PCTE12UN - Percent of headcount that are race/ethnicity unknown
-   PCTE12NR - Percent of headcount that are U.S. Nonresident
-   PCTE12W - Percent of headcount that are women

## Financial Data

> NOTE: I will ignore "in-district" tuition and fees because they are a bit too niche.

### IC2023_AY - Student charges for academic year programs

-   TUITION2 - In-state avg tuition for full-time undergrads
-   FEE2 - In-state avg required fees for full-time undergrads
-   TUITION3 - Out-of-state avg tuition for full-time undergrads
-   FEE3 - Out-of-state avg required fees for full-time undergrads
-   chg4ay3 - Books and supplies
-   chg5ay3- On-campus food and housing
-   chg6ay3 - On-campus, Other expenses
-   chg7ay3 - Off-campus w/o family food and housing
-   chg8ay3 - Off-campus w/o family other expenses
-   chg9ay3 - Off-campus w/ family food and housing
-   chg10ay3 - Off-campus w/ family other expenses
-   chg2at3 - Published in-state tuition
-   chg2af3- Published in-state fees
-   chg3at3 - Published out-of-state tuition
-   chg3af3 - Published out-of-state fees

### SFA2223_P1 - Student financial aid

-   SCFA12P - Percentage of students who are paying in-state tuititon
-   SCFA13P - Percentage of students who are paying out-of-state tuition
-   SCFA14P - Percentage of students who are paying unknown tuition
-   ANYAIDP - Percent of undergraduates awarded any financial aid
-   FGRNT_P - Percent of undergraduates awarded federal grant aid
-   FGRNT_A - Average amount of federal grant aid awarded to undergraduates
-   SGRNT_P - Percent of undergraduates awarded state/local grant aid
-   SGRNT_A - Average amount of state/local grant aid awarded to undergraduates
-   IGRNT_P - Percent of undergraduates awarded institutional grant aid
-   IGRNT_A - Average amount of institutional grant aid awarded to undergraduates
-   LOAN_P - Percent of undergraduates awarded student loan aid
-   LOAN_A - Average amount of student loan aid awarded to undergraduates
-   AGRNT_A - Average amount of federal, state, local or institutional grant aid awarded to undergraduates

### DRVIC2023 - Derived variables for student financial aid

> [!NOTE] To find net price, you can subtract the average amount of financial aid from the total price. (AGRNT_A)

-   CINSON - Total price for in-state students living on campus 2023-24
-   COTSON - Total price for out-of-state students living on campus 2023-24
-   CINSOFF - Total price for in-state students living off campus (not with family) 2023-24
-   COTSOFF - Total price for out-of-state students living off campus (not with family) 2023-24
-   CINSFAM - Total price for in-state students living off campus (with family) 2023-24
-   COTSFAM - Total price for out-of-state students living off campus (with family) 2023-24
