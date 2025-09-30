import { getData } from './data_out';

export async function generateDescription(
	id: number
): Promise<string | DBError> {
	const AI_URL = process.env.AI_URL || '';

	if (!AI_URL) {
		return { status: 500, message: 'AI URL not set up.' } as DBError;
	}

	const info = await getData(
		id,
		'core,admissions,enrollment,costs,outcomes,services'
	);
	if ('status' in info) {
		return info as DBError;
	}

	// TODO: PREVENT HAVING ISSUES WITH "Data not provided" or something. - http://localhost:3000/info/215062
	// TODO: http://localhost:3000/info/240620 wtf??

	const prompt = `Your Role: You are an expert copywriter for a leading college information platform.

Your Task: Generate a short, concise, and factual description for the university specified. The description should be approximately 80-120 words.

CRITICAL INSTRUCTIONS
Strict Data Adherence: You MUST use ONLY the data provided for all statistics, figures, and specific details.

NO STATISTICAL HALLUCINATION: Do not, under any circumstances, invent, estimate, or infer any numerical data. If a statistic is not present in the provided JSON, you must not mention it.

Handling Missing Data: If a data point is null or missing, simply omit that information. Do not write "data not available."

Tone and Style: The tone should be objective and factual. Be direct and avoid verbose or flowery language. Do not use emojis or em-dashes (—). When presenting a strong statistic (e.g., a high graduation rate), you may use a single, objective positive descriptor (e.g., "an impressive 86%"). Avoid subjective analysis.

Number Formatting: Ensure all numbers are formatted for readability. Use commas for thousands separators (e.g., 38,000). Do not put a space between a number and a percentage sign (e.g., 26%).

CONTENT AND STRUCTURE GUIDELINES
Your generated description should be a dense, informative paragraph. Weave in the following points logically, if the data exists:

Introduction: Combine the university's name (${info.core.name}), location (${
		info.core.city
	}, ${info.core.state}), and type (${
		info.core.inst_control
	}) in the opening sentence with its founding date (${
		info.core.year
	}). Based on the text in ${
		info.core.crn_ugrd
	}, describe its selectivity (e.g., if the text contains "more selective," describe it as "highly selective"; if it contains "selective," describe it as "selective"). If ${
		info.core.relig_control
	} is not null, mention its religious affiliation. Use ${
		info.core.crn_basic
	} to state its research activity level as "R1," "R2," or "R3" without the full description.

Student Body: State the total student population (${
		info.enrollment.total_pop
	}). Based on ${
		info.core.crn_enrl
	}, if it signifies a higher undergraduate presence, also state the undergraduate population (${
		info.enrollment.ugrd_pop
	}); if it signifies a higher graduate presence, state the graduate population (${
		info.enrollment.grad_pop
	}).

Admissions Profile:

State the acceptance rate (${info.admissions.acc_rate}).

For standardized tests, check ${
		info.admissions.considerations.con_test_scores.value
	}. If the policy is to not consider scores even if submitted, state the university is "test-blind." If scores are considered if submitted, state it is "test-optional."

If test scores are considered and available, mention the 50th percentile SAT (${
		(info.admissions.sat.rw_50 || 0) + (info.admissions.sat.math_50 || 0) ||
		null
	}) and/or the 50th percentile ACT Composite score (${
		info.admissions.act.comp_50
	}).

Academic Outcomes: Include the six-year graduation rate (${
		info.outcomes.grad_rate_6_yr
	}) and the student-to-faculty ratio (${info.outcomes.stu_fac}).

Athletics: If ${
		info.core.ncaa_affl
	} is true, mention that the university is an NCAA member and state its division (${
		info.core.ncaa_div
	}).`;
	console.log(prompt);
	const response = await fetch(AI_URL, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({
			model: 'openai/gpt-oss-20b',
			messages: [
				{ role: 'system', content: prompt },
				{ role: 'user', content: 'Please write me a description:' },
			],
		}),
	});

	if (!response.ok) {
		return { status: 500, message: 'AI service error' } as DBError;
	}

	const r = (await response.json()) as {
		choices: { message: { content: string } }[];
	};
	return r.choices[0].message.content;
}
