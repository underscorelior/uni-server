interface UniversityInfo {
	id: number;
	core: CoreInfo;
	description?: string;
	admissions: Admissions;
	enrollment: EnrollmentInfo;
	costs: Costs;
	outcomes: Outcomes;
	services: Services;
	// sports: Sports;
	rankings: Ranking;
}

type CoreInfo = {
	name: string;
	alias: string;
	address: string;
	city: string;
	state: string;
	longitude: number;
	latitude: number;
	phone?: number;
	url: string;
	year: number | null;
	hgh_deg: string | boolean | null;
	hospital: boolean | null;
	med_deg: boolean | null;
	crn_basic: string;
	crn_ugrd: string;
	crn_enrl: string;
	crn_size: string;
	urban: string | null;
	mc_sys: boolean | null;
	mc_sys_nm?: string;
	mc_sys_id?: number;
	inst_control: string | null;
	relig_control: string | null;
	cal_sys: string | null;
	ncaa_affl: boolean | null;
	ncaa_div: number | null;
	rnd_spend: number | null;
	endow_fte: number | null;
};

type Admissions = {
	considerations: {
		con_hs_gpa: { name: string | null; value: string | null };
		con_class_rank: { name: string | null; value: string | null };
		con_hs_record: { name: string | null; value: string | null };
		con_prep_program: { name: string | null; value: string | null };
		con_recommendations: { name: string | null; value: string | null };
		con_competencies: { name: string | null; value: string | null };
		con_test_scores: { name: string | null; value: string | null };
		con_english_test: { name: string | null; value: string | null };
		con_other_tests: { name: string | null; value: string | null };
		con_work_experience: { name: string | null; value: string | null };
		con_essay: { name: string | null; value: string | null };
		con_legacy: { name: string | null; value: string | null };
	};
	appl: {
		male: number | null;
		female: number | null;
		other: number | null;
		unknown: number | null;
		total: number | null;
	};
	adm: {
		male: number | null;
		female: number | null;
		other: number | null;
		unknown: number | null;
		total: number | null;
	};
	enrl: {
		male: number | null;
		female: number | null;
		other: number | null;
		unknown: number | null;
		total: number | null;
	};
	acc_rate: number | null;
	acc_rate_male: number | null;
	acc_rate_female: number | null;
	yield_rate: number | null;
	yield_rate_male: number | null;
	yield_rate_female: number | null;
	sat: {
		pct: number | null;
		rw_25: number | null;
		rw_50: number | null;
		rw_75: number | null;
		math_25: number | null;
		math_50: number | null;
		math_75: number | null;
	};
	act: {
		pct: number | null;
		comp_25: number | null;
		comp_50: number | null;
		comp_75: number | null;
		eng_25: number | null;
		eng_50: number | null;
		eng_75: number | null;
		math_25: number | null;
		math_50: number | null;
		math_75: number | null;
	};
	ap_credit: boolean | null;
	ug_app_fee: number;
	gr_app_fee: number;
	adm_url: string | null;
	appl_url: string | null;
};

type EnrollmentInfo = {
	offers_ugrd: boolean | null;
	offers_grad: boolean | null;
	instsize: string;
	total_pop: number;
	fte_pop: number;
	ugrd_pop: number;
	grad_pop: number;
	ft_pop: number;
	pt_pop: number;
	pct: {
		native: number;
		asian: number;
		black: number;
		hispanic: number;
		pacific: number;
		white: number;
		two: number;
		unknown: number;
		nonresident: number;
		female: number;
		online_only: number;
		some_online: number;
		no_online: number;
	};
	frsh_camp_req: boolean | null;
	online: boolean | null;
};

type Costs = {
	net_calc_url: string;
	tuit_vary: boolean | null;
	offers_housing: boolean | null;
	housing_capacity: number | null;
	offers_meal_plan: boolean | string | null;
	meals_wk: number | null;
	dorm_cost: number | null;
	meal_cost: number | null;
	rm_mls_cost: number | null;
	supp_cost: number | null;
	in: {
		tuition: number;
		fees: number;
		pct: number;
		total_cost: number;
		// net_cost: number;
	};
	out: {
		tuition: number;
		fees: number;
		pct: number;
		total_cost: number;
		// net_cost: number;
	};
	on_dorm_mls_cost: number | null;
	on_other_cost: number | null;
	off_dorm_mls_cost: number | null;
	off_other_cost: number | null;
	off_family_other_cost: number | null;
	pct_unkwn_tuit: number | null;
	pct_grant_aid: number | null;
	avg_grant_aid_amt: number | null;
};

type Outcomes = {
	grad_rate_4_yr: number;
	grad_rate_5_yr: number;
	grad_rate_6_yr: number;
	ret_rate_ft: number;
	ret_rate_pt: number;
	stu_fac: number;
	transfer_out_rate: number;
};

type Services = {
	faid_url: string | null;
	rotc: boolean | null;
	study_abroad: boolean | null;
	teacher_cert: boolean | null;
	ug_research: boolean | null;
	no_special_learning: boolean | null;
	career_counseling: boolean | null;
	employment_services: boolean | null;
	placement_services: boolean | null;
	no_student_services: boolean | null;
};

// type Sports = {
// 	// ncaa_affl: boolean | null;
// 	// ncaa_div: number | null;
// 	football: boolean | null;
// 	football_conf: string | null;
// 	football_conf_id: number | null;
// 	basketball: boolean | null;
// 	basketball_conf: string | null;
// 	basketball_conf_id: number | null;
// 	baseball: boolean | null;
// 	baseball_conf: string | null;
// 	baseball_conf_id: number | null;
// 	track: boolean | null;
// 	track_conf: string | null;
// 	track_conf_id: number | null;
// };

type Ranking = {
	overall: number | null;
	state: number | null;
	control: number | null;
	state_control: number | null;
	score: number | null;
};

type DBError = {
	message: string;
	status: number;
};

interface Search {
	id: number;
	name: string;
	alias: string;
	gen_alias: string;
	full_time: number;
	part_time: number;
	city: string;
	state: string;
	online: boolean | null;
}

interface SearchResult {
	id: number;
	name: string;
	city: string;
	state: string;
	online: boolean | null;
}

interface CollegeList {
	count: number;
	offset: number; // MAYBE NOT NEEDED
	list: ListItem[];
}

interface ListItem {
	id: number;
	name: string;
	url: string;
	city: string;
	state: string;
	year: number | null;
	inst_control: number;
	fte_pop: number;
	acc_rate: number;
	score: number;
}
