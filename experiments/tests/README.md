# Test discovery

The transferred exact tests retain their original filenames at experiments/
for stable provenance and standard-library discovery. Run from the repository
root: `python3 -m unittest discover -s experiments`. New test modules may be
added here when they have an independent mathematical verification purpose;
keep discovery explicit rather than adding infrastructure without need.
