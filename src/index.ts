import express, { Request, Response } from 'express';
import { getData, getValues, list, search } from './data_out';

import sqlite3 from 'sqlite3';

import * as fs from 'fs';
import * as path from 'path';
import { logVisit } from './utils';

const LOGGING_DIR = './logs';
const LOGGING_FILENAME = 'logging.sqlite';

const app = express();

app.use((req, _res, next) => {
	try {
		logVisit({
			db_path: path.join(LOGGING_DIR, LOGGING_FILENAME),
			route: req.path.replace('/api/', ''),
			id: Number(req.query.id) || -1,
		});
	} catch (e) {
		console.error('Logging error:', e);
	}
	next();
});

// TODO: Find a way to reliably obtain images of campuses, etc.
app.get('/api/search', async (req: Request, res: Response): Promise<void> => {
	const result = await search(req.query.search as string);
	if ('status' in result) {
		res.status(result.status).json({ message: result.message });
		return;
	}
	res.json(result);
});

app.get('/api/list', async (req: Request, res: Response): Promise<void> => {
	const result = await list(
		(req.query.filter as string) || '',
		(req.query.page as unknown as number) || 0,
		(req.query.limit as unknown as number) || 50
	);

	if ('status' in result) {
		res.status(result.status).json({ message: result.message });
		return;
	}

	res.json(result);
});

app.get(
	'/api/get-values',
	async (req: Request, res: Response): Promise<void> => {
		const table = req.query.table;
		const col = req.query.col;

		if (!table || Number.isInteger(Number(table))) {
			res.status(400).json({ message: 'Invalid table parameter' });
			return;
		}

		if (!table || Number.isInteger(Number(table))) {
			res.status(400).json({ message: 'Invalid col parameter' });
			return;
		}

		const output = await getValues(String(table), String(col));

		if ('status' in output) {
			res.status(output.status).json({ message: output.message });
			return;
		}

		res.json(output);
	}
);
// app.get('/test/ai', async (req: Request, res: Response): Promise<void> => {
// 	const id = req.query.id;
// 	const del = req.query.del;

// 	if (
// 		!id ||
// 		isNaN(Number(id)) ||
// 		!Number.isInteger(Number(id)) ||
// 		Number(id) < 0
// 	) {
// 		res.status(400).json({ message: 'Invalid id parameter' });
// 		return;
// 	}

// 	if (del) {
// 		deleteDescription(Number(id));
// 	}

// 	const result = await description(Number(id));
// 	if (typeof result !== 'string') {
// 		res.status(result.status).json({ message: result.message });
// 		return;
// 	}
// 	res.json({ result });
// });

// app.get(
// 	'/test/desc-delete-all',
// 	async (req: Request, res: Response): Promise<void> => {
// 		const result = await deleteAllDescriptions();
// 		if (result) {
// 			res.status(result.status).json({ message: result.message });
// 			return;
// 		}
// 		res.json({ message: 'All descriptions deleted successfully' });
// 	}
// );

app.get('/api/get', async (req: Request, res: Response): Promise<void> => {
	const id = req.query.id;
	const type = req.query.type;

	if (
		!id ||
		isNaN(Number(id)) ||
		!Number.isInteger(Number(id)) ||
		Number(id) < 0
	) {
		res.status(400).json({ message: 'Invalid id parameter' });
		return;
	}

	const output = await getData(
		Number(id),
		typeof type === 'string' ? type : undefined
	);

	if ('status' in output) {
		res.status(output.status).json({ message: output.message });
		return;
	}

	res.json(output);
});

// TODO: implement statistics for # of searches for specific colleges or queries, etc.

const PORT = process.env.PORT || 1234;
app.listen(PORT, () => {
	console.log(`Creating ${LOGGING_FILENAME} if it doesn't exist.`);

	fs.mkdir(LOGGING_DIR, () => {});

	const db = new sqlite3.Database(
		path.join(LOGGING_DIR, LOGGING_FILENAME),
		(err) => {
			if (err) {
				console.error('Error connecting to database:', err.message);
			} else {
				console.log('Connected to the logging database.');
			}
		}
	);

	db.serialize(() => {
		db.run(
			`CREATE TABLE IF NOT EXISTS visits (
			unit_id INTEGER,
			route TEXT,
			timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
		)`,

			(err) => {
				if (err) {
					console.error('Error creating visits table:', err.message);
				}
			}
		);
	});
	setTimeout(() => {
		db.close((err) => {
			if (err) {
				console.error(
					'Error closing the database connection:',
					err.message
				);
			}
		});
	}, 1000);
	console.log(`Server running on port ${PORT}`);
});

// TODO: Add ability to compare with national stats
