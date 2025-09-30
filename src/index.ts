import express, { Request, Response } from 'express';
import {
	deleteAllDescriptions,
	deleteDescription,
	description,
	getData,
	getValues,
	list,
	search,
} from './data_out';

const app = express();

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
		(req.query.offset as unknown as number) || 0,
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
	console.log(`Server running on port ${PORT}`);
});
