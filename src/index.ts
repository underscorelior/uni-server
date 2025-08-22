import express, { Request, Response } from 'express';
import { getData, search } from './data_out';

const app = express();

app.get('/api/search', async (req: Request, res: Response): Promise<void> => {
	const result = await search(req.query.search as string);
	if ('status' in result) {
		res.status(result.status).json({ message: result.message });
		return;
	}
	res.json(result);
});

app.get('/api/get', async (req: Request, res: Response): Promise<void> => {
	const id = req.query.id;
	let type = req.query.type;

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
