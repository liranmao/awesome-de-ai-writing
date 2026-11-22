# Contributing

1. **Check inclusion.** Tools need ≥1,000 GitHub stars. Detection or watermarking code tied to a peer-reviewed paper may be added regardless (set `research: true`). Tools marketed for evading detectors get `warn: true`.
2. **Classify the layer** by what the tool changes, not what it promises:
   - `L1` watermark: embeds, detects or removes a generation-time signal.
   - `L2` wording: edits words, punctuation, sentence patterns from a list of tells.
   - `L2-3` data-calibrated: picks what to edit from measured corpus statistics.
   - `L3` structure: edits paragraph or argument structure, narrative architecture, or claim–evidence fit.
   - `L4` distribution: targets detector scores directly (round-trip translation, programmatic substitution, detector-in-the-loop rewriting), or detects at this level.
3. **Set `timing`** (`post-hoc`, `generation`, `model`), `langs`, `use`, and write one-line `en` and `zh` descriptions that say how the tool works, not how good it is.
4. Run `pip install pyyaml && python scripts/build_readme.py`, commit the regenerated READMEs, and open a pull request.

Star counts are refreshed by a weekly GitHub Action (`scripts/update_stars.py`); you do not need to update them by hand.
