import express, { Request, Response } from 'express';
import sqlite3 from 'sqlite3';
import { open, Database } from 'sqlite';
import { createObject } from './create-object';
import { getIDs, shorthands } from './utils';

const app = express();

const initDb = async (): Promise<Database> => {
	return open({
		filename: 'colleges.db',
		driver: sqlite3.Database,
	});
};

// @ts-ignore
app.get('/api/search', async (req: Request, res: Response) => {
	const search = (req.query.search as string).toLowerCase();
	if (!search) {
		return res.status(400).json({ message: "Missing 'search' parameter" });
	}
	let words = search
		.replace(/[^0-9a-z]/gi, ' ')
		.split(' ')
		.filter(Boolean);

	if (words.length === 0) {
		return res.status(400).json({ message: 'Invalid search parameter' });
	}

	const clauses = words
		.map(() => `(inst_name LIKE ? OR short LIKE ? )`)
		.join(' AND ');
	const query = `SELECT DISTINCT id, inst_name, state, city FROM college_view WHERE ${clauses} ORDER BY total_students + 0 DESC LIMIT 50`;
	// order by population, if only online offered it goes below

	try {
		const db = await initDb();
		const params = words.flatMap((w) => [`%${w}%`, `%${w}%`]);
		const rows = await db.all(query, params);

		if (Object.keys(shorthands).includes(search)) {
			if (getIDs(rows).includes(shorthands[search])) {
				rows.splice(getIDs(rows).indexOf(shorthands[search]), 1);
			}
			const sh = await db.all(
				`SELECT DISTINCT id, inst_name, state, city FROM college_view WHERE id IS ${shorthands[search]} LIMIT 1`
			);
			rows.unshift(sh[0]);
		}

		if (search == 'mit') {
			// make it such that if MIT is in the results, append
			rows.push(
				[
					...(await db.all(
						`SELECT DISTINCT id, inst_name, state, city FROM college_view WHERE inst_name IS 'The University of Texas at Dallas' LIMIT 1`
					)),
				][0]
			);
		}
		res.json(rows);
	} catch (error) {
		console.error(error);
		res.status(500).json({ message: 'Database query error' });
	}
});

// @ts-ignore
app.get('/api/get-inst-data', async (req: Request, res: Response) => {
	const id = req.query.id as string;

	if (
		!id ||
		isNaN(Number(id)) ||
		!Number.isInteger(Number(id)) ||
		Number(id) < 0
	) {
		return res.status(400).json({ message: 'Invalid id parameter' });
	}

	const query = `SELECT * FROM college_view WHERE id = ?`;

	try {
		const db = await initDb();
		const row = await db.get(query, Number(id));

		if (!row) {
			return res.status(404).json({ message: 'Institution not found' });
		}

		const out = createObject(row);

		res.json(out);
	} catch (error) {
		console.error(error);
		res.status(500).json({ message: 'Database query error' });
	}
});

const PORT = process.env.PORT || 1234;
app.listen(PORT, () => {
	console.log(`Server running on port ${PORT}`);
});
