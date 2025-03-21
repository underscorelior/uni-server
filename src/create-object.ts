export function createObject(row): UniversityInfo {
	const output: UniversityInfo = {
		id: row['id'],
		general: {
			name: row['inst_name'],
			location: {
				city: row['city'],
				state: row['state'],
				campusLocale: row['campus_locale'],
			},
			controlOfInst: row['control_of_inst'],
			URLs: {
				general: row['url_general'],
				admissions: row['url_admissions'],
				financialAid: row['url_finaid'],
				application: row['url_application'],
				netPriceCalc: row['url_netprice'],
			},
		},
		academics: {
			highestDegreeOffered: row['highest_degree_offered'],
			studentFacultyRatio: row['student_faculty_ratio'],
			graduationRate: {
				'4yr': row['grad_rate_4yr'],
				'5yr': row['grad_rate_5yr'],
				'6yr': row['grad_rate_6yr'],
			},
			retentionRate: row['retention_rate'],
		},
		enrollment: {
			total: row['total_students'],
			graduate: row['graduate_students'],
			undergraduate: row['undergraduate_students'],
			demographics: {
				gender: {
					male: {
						percent: 100 - row['pct_women'],
						total: row['men_total'],
					},
					female: {
						percent: row['pct_women'],
						total: row['women_total'],
					},
					other: {
						percent:
							((row['total_students'] -
								row['women_total'] -
								row['men_total']) /
								row['total_students']) *
							100,
						total:
							row['total_students'] -
							row['women_total'] -
							row['men_total'],
					},
				},
				race: {
					White: {
						percent: row['pct_white'],
					},
					Black: {
						percent: row['pct_black'],
					},
					Hispanic: {
						percent: row['pct_hispanic'],
					},
					Asian: {
						percent: row['pct_asian'],
					},
					'American Indian': {
						percent: row['pct_native_am'],
					},
					International: {
						percent: row['pct_non_resident'],
					},
					Other: {
						percent: row['pct_other'],
					},
				},
			},
		},
		admissions: {
			applicationFee: row['app_fee'],
			testScores: {
				sat: {
					pctSubmit: row['sat_pct_submit'],
					math: {
						'25th': row['sat_math_25'],
						'50th': row['sat_math_50'],
						'75th': row['sat_math_75'],
					},
					reading: {
						'25th': row['sat_read_25'],
						'50th': row['sat_read_50'],
						'75th': row['sat_read_75'],
					},
				},
				act: {
					pctSubmit: row['act_pct_submit'],
					'25th': row['act_25'],
					'50th': row['act_50'],
					'75th': row['act_75'],
				},
			},
			acceptanceRate: {
				overall: row['acceptance_rate'],
			},
			applicants: {
				total: row['applicants_total'],
				male: row['applicants_male'],
				female: row['applicants_female'],
				other:
					row['applicants_total'] -
					row['applicants_male'] -
					row['applicants_female'],
			},
			admitted: {
				total: row['admitted_total'],
			},
			enrolled: {
				total: row['enrolled_total'],
			},
		},

		financial: {
			tuitionvaries: row['tuition_varies'],
			costs: {
				inState: {
					tuition: row['tuition_in_state'],
					fees: row['fees_in_state'],
					percentage: row['costs_instate_percentage'],
					totalcost: row['cost_in_state'],
					net: row['net_price_in_state'],
				},
				outOfState: {
					tuition: row['tuition_out_state'],
					fees: row['fees_out_state'],
					percentage: row['cost_outofstate_percentage'],
					totalcost: row['cost_out_state'],
					net: row['net_price_out_state'],
				},
			},
			aid: {
				general: {
					percentage: row['pct_any_aid'],
					average: row['avg_aid_amount'],
				},
			},
		},
	};
	return output;
}
