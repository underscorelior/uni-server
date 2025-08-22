function tokenize(s: string) {
	return s
		.toLowerCase()
		.replace(/[^a-z0-9\s]/g, ' ')
		.split(/\s+/)
		.filter(Boolean);
}

export async function searchRanking(
	query: string,
	rows: Search[]
): Promise<SearchResult[]> {
	const q = query.trim().toLowerCase();
	if (!q) return [];
	const maxPop =
		rows.reduce((m, r) => {
			let pt = r.part_time / 10;
			if (r.full_time && pt && r.full_time + pt > m)
				return r.full_time + pt;
			return m;
		}, 0) || 1;

	const scored = rows.map((r) => {
		if (!r)
			return {
				r: {} as Search,
				score: -Infinity,
			};

		r.part_time = r.part_time / 10;

		const aliases = new Set([
			...tokenize(r.name || ''),
			// ...tokenize(r.alias || ''),
			...tokenize(r.gen_alias || ''),
		]);
		const name = (r.name || '').toLowerCase();
		let score = 0;

		if (name === q) score += 1200;
		if (aliases.has(q)) score += 1000;

		if (name.startsWith(q)) score += 320;
		if (Array.from(aliases).some((a) => a.startsWith(q))) score += 260;

		const h = tokenize(q).filter((t) => aliases.has(t)).length;
		if (h) score += h * 160;

		if (r.full_time && r.part_time)
			score += ((r.full_time + r.part_time) / maxPop) * 900;

		if ((r.city || '').toLowerCase() === q) score += 140;

		if (r.online) score -= 600;
		return { r, score };
	});

	const byId = new Map<number, { r: Search; score: number }>();

	for (const it of scored) {
		if (it.r.id < 0) continue;
		const ex = byId.get(it.r.id);
		if (!ex || it.score > ex.score) byId.set(it.r.id, it);
	}

	const out = Array.from(byId.values()).sort(
		(a, b) =>
			b.score - a.score ||
			(b.r.full_time + b.r.part_time || 0) -
				(a.r.full_time + a.r.part_time || 0) ||
			a.r.name.localeCompare(b.r.name)
	);

	return out.slice(0, 50).map(({ r }) => ({
		id: r.id,
		name: r.name,
		city: r.city,
		// alias: r.alias,
		// gen_alias: r.gen_alias,
		state: r.state,
		online: r.online,
	}));
}
