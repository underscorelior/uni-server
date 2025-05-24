// export const shorthands: { [name: string]: string[] } = {
// 	mit: ['massachusetts', 'institute', 'technology'],
// 	utd: ['university', 'texas', 'dallas'],
// 	ucsc: ['university', 'california', 'santa', 'cruz'],
// 	ucr: ['university', 'california', 'riverside'],
// 	ucm: ['university', 'california', 'merced'],
// 	ucd: ['university', 'california', 'davis'],
// 	gatech: ['georgia', 'institute', 'technology'],
// 	'georgia tech': ['georgia', 'institute', 'technology'],
// };
export const shorthands: { [name: string]: number } = {
	mit: 166683,
	utd: 228787,
	ucsc: 110714,
	ucr: 110671,
	ucm: 445188,
	ucd: 110644,
	gatech: 139755,
	'georgia tech': 139755,
};

export function getIDs(uni: SearchResult[]): number[] {
	return uni.map((u) => parseInt(u.id) || 0);
}
