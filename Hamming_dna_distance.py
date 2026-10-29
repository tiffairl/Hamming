"""Made to calculate the Hamming distance between two DNA strands."""

def distance(strand_a, strand_b):
    """To include the rule: """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    differences = 0

    for nucleotide_a, nucleotide_b in zip(strand_a, strand_b):
        if nucleotide_a != nucleotide_b:
            differences += 1

    return differences