def vowel_indices(word):
	return [i+1 for i, c in enumerate(word) if c in 'aAeEiIoOuUyY']
