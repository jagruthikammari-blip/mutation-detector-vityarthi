def validate_dna(sequence):
    """Check whether a DNA sequence contains only A, T, C, and G."""
    return all(base in "ATCG" for base in sequence)


def find_mutations(original, mutated):
    mutations = []

    # Compare positions that exist in both sequences
    common_length = min(len(original), len(mutated))

    for i in range(common_length):
        if original[i] != mutated[i]:
            mutations.append({
                "position": i + 1,
                "original": original[i],
                "mutated": mutated[i]
            })

    # Detect insertions
    if len(mutated) > len(original):
        for i in range(common_length, len(mutated)):
            mutations.append({
                "position": i + 1,
                "original": "-",
                "mutated": mutated[i]
            })

    # Detect deletions
    elif len(original) > len(mutated):
        for i in range(common_length, len(original)):
            mutations.append({
                "position": i + 1,
                "original": original[i],
                "mutated": "-"
            })

    return mutations


print("================================")
print("      DNA MUTATION DETECTOR")
print("================================")

original = input("Enter original DNA sequence: ").upper().strip()
mutated = input("Enter mutated DNA sequence: ").upper().strip()

# Validate sequences
if not validate_dna(original):
    print("Error: Original sequence contains invalid DNA bases.")
elif not validate_dna(mutated):
    print("Error: Mutated sequence contains invalid DNA bases.")
else:
    mutations = find_mutations(original, mutated)

    print("\n========== RESULT ==========")

    if not mutations:
        print("No differences detected.")
    else:
        print(f"Number of differences: {len(mutations)}\n")

        for mutation in mutations:
            position = mutation["position"]
            old = mutation["original"]
            new = mutation["mutated"]

            if old == "-":
                print(f"Position {position}: INSERTION ({new})")

            elif new == "-":
                print(f"Position {position}: DELETION ({old})")

            else:
                print(
                    f"Position {position}: "
                    f"{old} → {new}"
                )

    print("============================")N




                                                           FLOWCHART






             DNA Mutation Detector
                      │
                      ↓
             Enter original DNA
                      │
                      ↓
              Enter mutated DNA
                      │
                      ↓
                Validate DNA
                      │
                      ↓
             Compare positions
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
     Same base   Different    Length differs
          │          base          │
          │           │            │
          │           ↓       Insertion/
          │       Mutation       Deletion
          │           │            │
          └───────────┴────────────┘
                      ↓
               Display results