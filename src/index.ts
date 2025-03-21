import express, { Request, Response } from 'express';
import sqlite3 from 'sqlite3';
import { open, Database } from 'sqlite';
import { createObject } from './create-object';

const app = express();

const initDb = async (): Promise<Database> => {
	return open({
		filename: 'colleges.db',
		driver: sqlite3.Database,
	});
};

// @ts-ignore
app.get('/api/search', async (req: Request, res: Response) => {
	const search = req.query.search as string;
	if (!search) {
		return res.status(400).json({ message: "Missing 'search' parameter" });
	}
	const words = search
		.toLowerCase()
		.replace(/[^0-9a-z]/gi, ' ')
		.split(' ')
		.filter(Boolean);

	if (words.length === 0) {
		return res.status(400).json({ message: 'Invalid search parameter' });
	}

	if (search.toLowerCase() == 'mit') {
		words.push('massachusetts', 'institute', 'technology');
	}

	const clauses = words
		.map(() => `(inst_name LIKE ? OR short LIKE ? )`)
		.join(' AND ');
	const query = `SELECT DISTINCT id, inst_name, state, city FROM college_view WHERE ${clauses} LIMIT 50`;

	try {
		const db = await initDb();
		const params = words.flatMap((w) => [`%${w}%`, `%${w}%`]);
		const rows = await db.all(query, params);
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
