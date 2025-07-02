type location = {
	city: string; // HD2023 - CITY
	state: string; // HD2023 - STABBR
	coord_lat: number; // HD2023 - LATITUDE
	coord_long: number; // HD2023 - LONGITUD
	region: number; // conv state to region
	locale: number; // HD2023 - LOCALE
	/*
			11	City: Large
			12	City: Midsize
			13	City: Small
			21	Suburb: Large
			22	Suburb: Midsize
			23	Suburb: Small
			31	Town: Fringe
			32	Town: Distant
			33	Town: Remote
			41	Rural: Fringe
			42	Rural: Distant
			43	Rural: Remote
			-3	{Not available}
		*/
};

type inst = {
	name: string; // HD2023 - INSTNM
	alias: string; // HD2023 - IALIAS
	affiliation: 'public' | 'private' | 'private religious'; // IC2023 - CNTLAFFI
	/*
			1 Public
	        2 Private for-profit
		    3 Private nonprofit (no religious affiliation)
		    4 Private nonprofit (religious affiliation)
		    -1 Not reported
		*/
	population: number; // HD2023 - INSTSIZE
	/*
			1	Under 1,000
			2	1,000 - 4,999
			3	5,000 - 9,999
			4	10,000 - 19,999
			5	20,000 and above
			-1	Not reported
			-2	Not applicable
		*/
	acceptance_rate: number; // DRVADM2023 - DVADM01
	yield_rate: number; // DRVADM2023 - DVADM04
	stu_fac: number; // EF2023D - STUFACR
	highest_degree: number; // HD2023 - HDEGOFR1
	/*
			11 - Doctor's degree - research/scholarship and professional practice
			12 - Doctor's degree - research/scholarship
			13 - Doctor's degree - professional practice
			14 - Doctor's degree - other
			20 - Master's degree
			30 - Bachelor's degree
			40 - Associate's degree
			0 - Non-degree granting
			-3 - {Not available}
		*/
};

interface University {
	institution: inst;
	location: location;
}
