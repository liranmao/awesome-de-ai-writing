# Contributing

Contributions are welcome. Every entry is held to the same standard as a citation in a review article: it should be verifiable, described by what it does rather than by what it promises, and classified consistently with the taxonomy in Table 1 of the README.

1. **Check eligibility.** Tools require at least 1,000 GitHub stars. Detection or watermarking code accompanying a peer-reviewed publication may be added regardless of star count (set `research: true`). Tools marketed primarily for evading detectors must carry `warn: true`.
2. **Assign a layer** according to what the tool changes, not what it claims:
   - `L1` watermark: embeds, detects or removes a generation-time signal.
   - `L2` wording: edits vocabulary, punctuation or sentence patterns against a list of markers.
   - `L2-3` corpus-calibrated: selects what to edit from measured corpus statistics.
   - `L3` structure: edits paragraph or argument structure, narrative architecture, or the fit between claims and evidence.
   - `L4` distribution: targets detector scores directly (round-trip translation, programmatic substitution, detector-in-the-loop rewriting), or detects at this level.
3. **Complete the metadata**: `timing` (`post-hoc`, `generation` or `model`), `langs` and `use`. Write one-sentence `en` and `zh` descriptions in neutral, declarative language that state the mechanism, report claims as claims ("claims…", "advertised as…"), and avoid evaluative adjectives.
4. Run `pip install pyyaml && python scripts/build_readme.py`, commit the regenerated READMEs and figures, and open a pull request.

Star counts are refreshed weekly by a GitHub Action (`scripts/update_stars.py`) and need not be updated by hand.
