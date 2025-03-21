interface UniversityInfo {
	id: number;
	general: {
		name: string;
		location: {
			city: string;
			state: string;
			// coords: { longitude: number; latitude: number };
			campusLocale: number;
		};
		// description?: string; // TODO: CANNOT BE FOUND IN IPEDS
		// foundedYear?: number; // TODO: cannot be found in IPEDS
		// imageUrl?: string; // TODO: Not found in IPEDS
		controlOfInst: number;
		URLs: {
			general: string;
			admissions: string;
			financialAid: string;
			application: string;
			netPriceCalc: string;
		};
		// missionStatement: string; // TODO: Needed??
	};
	academics: {
		highestDegreeOffered: number;
		// calendarSystem: string[]; // TODO: Needed?
		studentFacultyRatio: string;
		graduationRate: {
			'4yr': number;
			'5yr': number;
			'6yr': number;
		};
		retentionRate: number;
	};
	enrollment: {
		total: number;
		graduate: number;
		undergraduate: number;
		demographics: {
			gender: { [key: string]: { percent: number; total: number } };
			race: { [key: string]: { percent: number } };
		};
	};
	admissions: {
		applicationFee: number;
		// averageGPA?: number; // TODO: NOT INCLUDED IN IPEDS
		testScores: {
			sat: {
				pctSubmit: number;
				math: {
					'25th': number;
					'50th': number;
					'75th': number;
				};
				reading: {
					'25th': number;
					'50th': number;
					'75th': number;
				};
			};
			act: {
				pctSubmit: number;
				'25th': number;
				'50th': number;
				'75th': number;
			};
		};
		acceptanceRate: {
			overall: number;
			// male: number;
			// female: number;
		};
		// yieldRate: number;
		applicants: {
			total: number;
			male: number;
			female: number;
			other: number;
		};
		admitted: {
			total: number;
			// male: number;
			// female: number;
			// other: number;
		};
		enrolled: {
			total: number;
			// male: number;
			// female: number;
			// other: number;
		};
		// considerations: {
		// 	gpa: number;
		// 	rank: number;
		// 	record: number;
		// 	collegePrep: number;
		// 	recommendations: number;
		// 	demonstration: number;
		// 	tests: number;
		// 	workExp: number;
		// 	essay: number;
		// 	legacy: number;
		// };
	};
	financial: {
		tuitionvaries: boolean;
		costs: {
			inState: {
				tuition: number;
				fees: number;
				percentage: number;
				totalcost: number;
				net: number;
			};
			outOfState: {
				tuition: number;
				fees: number;
				percentage: number;
				totalcost: number;
				net: number;
			};
			// room: {
			// 	offered: boolean;
			// 	capacity: number;
			// 	cost: number;
			// };
			// board: {
			// 	offered: boolean;
			// 	mealsWk: number;
			// 	cost: number;
			// };
		};
		aid: {
			general: {
				percentage: number;
				average: number;
			};
			// federal: {
			// 	percentage: number;
			// 	average: number;
			// };
			// state: {
			// 	percentage: number;
			// 	average: number;
			// };
			// institutional: {
			// 	percentage: number;
			// 	average: number;
			// };
		};
	};
}
