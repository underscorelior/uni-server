import sqlite3 from 'sqlite3';
import { open } from 'sqlite';
import {
	ADMISSIONS_CONV,
	COMMON_CONV,
	CONSIDERATIONS_CONV,
	COSTS_CONV,
	ENROLLMENT_CONV,
	INFO_CONV,
	SERVICES_CONV,
} from './conversions';
import { searchRanking } from './utils';
import { generateDescription } from './ai_utils';

export async function query<T>(
	table: string,
	id: number
): Promise<T | DBError> {
	try {
		const db = await open({
			filename: 'data/universities.sqlite',
			driver: sqlite3.Database,
		});

		let out: any = await db.get(`SELECT * FROM ${table} WHERE id = ?`, id);

		if (!out) {
			await db.close();
			return { status: 404, message: 'Institution not found' } as DBError;
		}

		const lowercased: any = {};
		for (const key in out) {
			lowercased[key.toLowerCase()] = out[key];
		}

		await db.close();
		return lowercased as T;
	} catch (error) {
		console.error(error);
		return { status: 500, message: 'Database query error' } as DBError;
	}
}

export async function core(id: number): Promise<CoreInfo | DBError> {
	const result = await query<CoreInfo>('core', id);
	if ('status' in result) {
		return result;
	}

	const output = Object.fromEntries(
		Object.entries(result).map(([col, val]) => {
			const key = col.toLowerCase();
			const conv = INFO_CONV[key as keyof typeof INFO_CONV];

			const value = conv
				? (conv as any)[String(val)]
				: typeof val === 'string'
				? val.trim()
				: val;

			return [key, value];
		})
	);

	return output as CoreInfo;
}

// TODO: Improve the splitting
export async function admissions(id: number): Promise<Admissions | DBError> {
	const result = await query<Admissions>('admissions', id);
	if ('status' in result) {
		return result;
	}
	const output = {} as Admissions;

	Object.entries(result).forEach(([col, val]) => {
		const key = col.toLowerCase();
		const conv = ADMISSIONS_CONV[key as keyof typeof ADMISSIONS_CONV];

		const value = conv
			? (conv as any)[String(val)]
			: typeof val === 'string'
			? (val as string).trim()
			: val;
		if (key.startsWith('con_')) {
			if (!(output as any).considerations) {
				(output as any).considerations =
					{} as Admissions['considerations'];
			}
			(output as any).considerations[key] = {
				name: CONSIDERATIONS_CONV.names[
					key as keyof typeof CONSIDERATIONS_CONV.names
				],
				value: CONSIDERATIONS_CONV[
					String(val) as keyof typeof CONSIDERATIONS_CONV
				],
			};
		} else if (
			(key.startsWith('sat_') ||
				key.startsWith('act_') ||
				key.startsWith('adm_')) &&
			!key.endsWith('url')
		) {
			if (!(output as any)[key.slice(0, 3)]) {
				(output as any)[key.slice(0, 3)] = {} as Admissions[
					| 'sat'
					| 'act'
					| 'adm'];
			}
			(output as any)[key.slice(0, 3)][key.slice(4)] = value;
		} else if (
			(key.startsWith('appl_') || key.startsWith('enrl_')) &&
			!key.endsWith('url')
		) {
			if (!(output as any)[key.slice(0, 4)]) {
				(output as any)[key.slice(0, 4)] = {} as Admissions[
					| 'appl'
					| 'enrl'];
			}
			(output as any)[key.slice(0, 4)][key.slice(5)] = value;
		} else {
			(output as any)[key] = value;
		}
	});

	return output;
}

export async function enrollment(
	id: number
): Promise<EnrollmentInfo | DBError> {
	const result = await query<EnrollmentInfo>('enrollment', id);
	if ('status' in result) {
		return result;
	}

	const output = {} as EnrollmentInfo;

	Object.entries(result).forEach(([col, val]) => {
		const key = col.toLowerCase();
		const conv = ENROLLMENT_CONV[key as keyof typeof ENROLLMENT_CONV];

		const value = conv
			? (conv as any)[String(val)]
			: typeof val === 'string'
			? (val as string).trim()
			: val;
		if (key.startsWith('pct_')) {
			if (!(output as any)['pct']) {
				(output as any)['pct'] = {} as EnrollmentInfo['pct'];
			}
			(output as any)['pct'][key.slice(4)] = value;
		} else {
			(output as any)[key] = value;
		}
	});

	return output as EnrollmentInfo;
}

export async function costs(id: number): Promise<Costs | DBError> {
	const result = await query<Costs>('costs', id);
	if ('status' in result) {
		return result;
	}

	const output = {} as Costs;

	Object.entries(result).forEach(([col, val]) => {
		const key = col.toLowerCase();
		const conv = COSTS_CONV[key as keyof typeof COSTS_CONV];

		const value = conv
			? (conv as any)[String(val)]
			: typeof val === 'string'
			? (val as string).trim()
			: val;

		if (key.startsWith('out_')) {
			if (!(output as any)['out']) {
				(output as any)['out'] = {} as Costs['out'];
			}
			(output as any)['out'][key.slice(4)] = value;
		} else if (key.startsWith('in_')) {
			if (!(output as any)['in']) {
				(output as any)['in'] = {} as Costs['in'];
			}
			(output as any)['in'][key.slice(3)] = value;
		} else {
			(output as any)[key] = value;
		}
	});

	return output as Costs;
}

export async function outcomes(id: number): Promise<Outcomes | DBError> {
	const result = await query<Outcomes>('outcomes', id);
	if ('status' in result) {
		return result;
	}

	const output = Object.fromEntries(
		Object.entries(result).map(([col, val]) => {
			const key = col.toLowerCase();
			return [key, val];
		})
	);

	return output as Outcomes;
}

export async function services(id: number): Promise<Services | DBError> {
	const result = await query<Services>('services', id);
	if ('status' in result) {
		return result;
	}

	const output = Object.fromEntries(
		Object.entries(result).map(([col, val]) => {
			const key = col.toLowerCase();
			const conv = SERVICES_CONV[key as keyof typeof SERVICES_CONV];

			const value = conv
				? (conv as any)[String(val)]
				: typeof val === 'string'
				? val.trim()
				: val;

			return [key, value];
		})
	);

	return output as Services;
}

export const validTypes = [
	'core',
	'description',
	'admissions',
	'enrollment',
	'costs',
	'outcomes',
	'services',
	// 'sports'
];

export async function getData(
	id: number,
	type?: string
): Promise<UniversityInfo | DBError> {
	const output: UniversityInfo = {} as UniversityInfo;

	output.id = id;

	let types = type;

	if (!types) {
		types = validTypes.join(',');
	}

	for (const t of types.split(',')) {
		if (!validTypes.includes(t)) {
			return { status: 400, message: `Invalid type: ${t}` };
		}
		switch (t) {
			case 'core': {
				const coreResult = await core(id);
				if ('status' in coreResult) return coreResult as DBError;
				output.core = coreResult;
				break;
			}
			case 'description': {
				const descriptionResult = await description(id);
				if (
					typeof descriptionResult !== 'string' &&
					'status' in descriptionResult
				)
					return descriptionResult as DBError;
				output.description = descriptionResult;
				break;
			}
			case 'admissions': {
				const admissionsResult = await admissions(id);
				if ('status' in admissionsResult)
					return admissionsResult as DBError;
				output.admissions = admissionsResult;
				break;
			}
			case 'enrollment': {
				const enrollmentResult = await enrollment(id);
				if ('status' in enrollmentResult)
					return enrollmentResult as DBError;
				output.enrollment = enrollmentResult;
				break;
			}
			case 'costs': {
				const costsResult = await costs(id);
				if ('status' in costsResult) return costsResult as DBError;
				output.costs = costsResult;
				break;
			}
			case 'outcomes': {
				const outcomesResult = await outcomes(id);
				if ('status' in outcomesResult)
					return outcomesResult as DBError;
				output.outcomes = outcomesResult;
				break;
			}
			case 'services': {
				const servicesResult = await services(id);
				if ('status' in servicesResult)
					return servicesResult as DBError;
				output.services = servicesResult;
				break;
			}
			// case 'sports': {
			// 	const sportsResult = await sports(id);
			// 	if ('status' in sportsResult) return sportsResult as DBError;
			// 	output.sports = sportsResult;
			// 	break;
			// }
			default:
				return {
					status: 400,
					message: `Invalid type: ${t}`,
				} as DBError;
		}
	}

	return output;
}

export async function search(input: string): Promise<SearchResult[] | DBError> {
	if (!input || !input.trim()) return [];
	const safe = input.replace(/'/g, "''");
	const clauses = [
		`name LIKE '%${safe}%'`,
		`city LIKE '%${safe}%'`,
		`state LIKE '%${safe}%'`,
		`alias LIKE '%${safe}%'`,
		`gen_alias LIKE '%${safe}%'`,
	].join(' OR ');

	let rows: Search[] = [];
	try {
		const db = await open({
			filename: 'data/universities.sqlite',
			driver: sqlite3.Database,
		});
		rows = await db.all<Search[]>(`SELECT * FROM search WHERE ${clauses}`);
		await db.close();
	} catch (error) {
		console.error(error);
		return { status: 500, message: 'Database query error' } as DBError;
	}

	if (!rows.length) return [];

	const normalized: Search[] = rows.map((r: Search) => {
		const lower = Object.fromEntries(
			Object.entries(r as unknown as Record<string, unknown>).map(
				([k, v]) => [k.toLowerCase().trim(), v]
			)
		) as Record<string, unknown> & { online?: unknown };

		lower.online =
			COMMON_CONV[String(lower.online) as keyof typeof COMMON_CONV];

		return lower as unknown as Search;
	});

	return searchRanking(input, normalized);
}

export async function saveDescription(
	id: number,
	description: string
): Promise<void | DBError> {
	try {
		const db = await open({
			filename: 'data/universities.sqlite',
			driver: sqlite3.Database,
		});

		const existing = await db.get(
			`SELECT id FROM descriptions WHERE id = ?`,
			id
		);
		if (!existing) {
			await db.run(
				`INSERT INTO descriptions (id, description) VALUES (?, ?)`,
				id,
				description
			);
		}

		await db.close();
	} catch (error) {
		console.error(error);
		return { status: 500, message: 'Database query error' } as DBError;
	}
}

export async function deleteDescription(id: number): Promise<void | DBError> {
	try {
		const db = await open({
			filename: 'data/universities.sqlite',
			driver: sqlite3.Database,
		});

		await db.run(`DELETE FROM descriptions WHERE id = ?`, id);
		await db.close();
	} catch (error) {
		console.error(error);
		return { status: 500, message: 'Database query error' } as DBError;
	}
}

export async function deleteAllDescriptions(): Promise<void | DBError> {
	try {
		const db = await open({
			filename: 'data/universities.sqlite',
			driver: sqlite3.Database,
		});

		await db.run(`DELETE FROM descriptions`);
		await db.close();
	} catch (error) {
		console.error(error);
		return { status: 500, message: 'Database query error' } as DBError;
	}
}

export async function description(id: number): Promise<string | DBError> {
	try {
		const db = await open({
			filename: 'data/universities.sqlite',
			driver: sqlite3.Database,
		});

		const result = await db.get<{ description: string }>(
			`SELECT description FROM descriptions WHERE id = ? LIMIT 1`,
			id
		);

		console.log(`Fetched description for ID ${id}:`, result);

		await db.close();
		if (!result) {
			try {
				const desc = await generateDescription(id);

				if (typeof desc !== 'string') {
					return desc as DBError;
				}

				await saveDescription(id, desc);
				return desc;
			} catch (error: any) {
				console.error('Error generating description:', error);
				return {
					status: 500,
					message: 'Error generating description: ' + error.message,
				} as DBError;
			}
		}

		return result.description;
	} catch (error) {
		console.error('Error fetching description:', error);
		return { status: 500, message: 'Database query error' } as DBError;
	}
}

export async function list(
	filter: string,
	offset: number,
	limit: number
): Promise<CollegeList[] | DBError> {
	// query format: "x=y" ex. "state=CA:size>5000"
	try {
		let rows: CollegeList[] = [];
		const db = await open({
			filename: 'data/universities.sqlite',
			driver: sqlite3.Database,
		});

		const where = [] as string[];

		filter.split(':').forEach((f) => {
			let out = '';
			if (!(f.length >= 2)) return;

			if (f.includes('=')) {
				out = ` ${f.split('=')[0].trim()}${
					f.split('=')[1].includes(',') ? ' IN (' : "= '"
				}${f.split('=')[1].trim()}${
					f.split('=')[1].includes(',') ? ')' : "'"
				}`;
			}
			where.push(out);
		}); // TODO: Improve this to not be so messy

		const result = await db.all<CollegeList[]>(
			`SELECT * FROM list ${
				filter ? `WHERE ${where.join(' AND ')}` : ''
			} ORDER BY score DESC LIMIT ? OFFSET ?`,
			limit,
			offset
		);

		rows = result ?? [];

		await db.close();

		return rows;
	} catch (error) {
		console.error('Error fetching list:', error);
		return { status: 500, message: 'Database query error' } as DBError;
	}
}

export async function getValues(
	table: string,
	col: string
): Promise<string[] | DBError> {
	try {
		let rows: string[] = [];
		const db = await open({
			filename: 'data/universities.sqlite',
			driver: sqlite3.Database,
		});

		const result = await db.all<{ [key: string]: string }[]>(
			`SELECT DISTINCT ${col} FROM ${table}`
		);

		rows =
			result
				.map((row) => {
					return row[col];
				})
				.sort() ?? [];

		await db.close();

		return rows;
	} catch (error) {
		console.error('Error fetching values:', error);
		return { status: 500, message: 'Database query error' } as DBError;
	}
}

export async function getTotalPages(limit: number) {
	try {
		const db = await open({
			filename: 'data/universities.sqlite',
			driver: sqlite3.Database,
		});

		const result = await db.get<{ 'COUNT(*)': number }>(
			`SELECT COUNT(*) from core`
		);

		await db.close();

		if (!result) {
			return { status: 500, message: 'Database query error' } as DBError;
		}

		return Math.ceil((result['COUNT(*)'] ?? 0) / limit);
	} catch (error) {
		console.error('Error fetching description:', error);
		return { status: 500, message: 'Database query error' } as DBError;
	}
}
