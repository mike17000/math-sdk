# Olympus Rising - Math SDK Configuration

**Game ID:** olympus_rising  
**Theme:** Greek Mythology (Zeus and the Olympians)  
**Type:** Lines-pay (5×3, 20 paylines)  
**RTP Target:** 96.0% ±0.5%  
**Volatility:** High (71.4% zero wins)  
**Max Win:** 5000x bet  

## Symbols

| Symbol | Name | Type | 5oak | 4oak | 3oak |
|--------|------|------|------|------|------|
| W | Wild | wild | 50x | 20x | 10x |
| S | Scatter | scatter | - | - | - |
| H1 | Zeus | high | 25x | 10x | 5x |
| H2 | Hera | high | 15x | 5x | 3x |
| H3 | Poseidon | high | 10x | 3x | 2x |
| H4 | Athena | high | 8x | 2x | 1x |
| L1 | Golden Coin | low | 5x | 1x | 0.5x |
| L2 | Amphora | low | 3x | 0.7x | 0.3x |
| L3 | Laurel Wreath | low | 3x | 0.7x | 0.3x |

## Free Spins

**Trigger:** 3+ Scatters anywhere  
**Awards:**
- 3 scatters → 10 free spins
- 4 scatters → 15 free spins
- 5 scatters → 20 free spins

**Retrigger:** Same scatter counts → 5/10/15 additional spins

**Reel set:** FR0 (more wilds, fewer low symbols)

## Reel Strips

### BR0 (Base Game) - 30 positions

| Symbol | Count | % |
|--------|-------|---|
| L1, L2 | 27 each | 18% |
| L3 | 20 | 13.3% |
| H3 | 18 | 12% |
| H4 | 17 | 11.3% |
| H2 | 14 | 9.3% |
| W, S | 10 each | 6.7% |
| H1 | 7 | 4.7% |

**Total:** 150 symbols (30 × 5 reels)

### FR0 (Free Spins) - 30 positions

| Symbol | Count | % | vs BR0 |
|--------|-------|---|--------|
| W | 20 | 13.3% | +6.7% ↑ |
| H4, H3 | 20 each | 13.3% | +2% ↑ |
| H2 | 18 | 12% | +2.7% ↑ |
| H1 | 17 | 11.3% | +6.7% ↑ |
| L2, L3 | 17 each | 11.3% | -6.7% ↓ |
| L1 | 16 | 10.7% | -7.3% ↓ |
| S | 5 | 3.3% | -3.3% ↓ |

**Key change:** Double wilds (6.7% → 13.3%), reduce lows (49% → 33%)

## Distribution Quotas

| Criteria | Quota | Description |
|----------|-------|-------------|
| wincap | 0.001 | Max win (5000x) |
| freegame | 0.08 | Free spins trigger |
| zerowin | 0.714 | No win (high volatility) |
| basegame | 0.185 | Regular wins |

**Total:** 1.000 (100%)

## Run Simulation

```bash
cd /tmp/math-sdk/games/olympus_rising
python run.py
```

**Output:**
- `library/books/*.jsonl.zst` — Game books
- `library/stats/analysis.csv` — RTP analysis
- `library/tests/validation_report.json` — Format validation

## Files

```
olympus_rising/
├── game_config.py       # Main configuration (edited)
├── gamestate.py         # Game logic (from 0_0_lines)
├── game_override.py     # Custom overrides
├── game_executables.py  # Win evaluation
├── run.py               # Simulation script
└── reels/
    ├── BR0.csv          # Base game reel strips
    └── FR0.csv          # Free spins reel strips
```

## Status

✅ Configuration complete  
✅ Reel strips created (30 positions)  
✅ Validation passed (no import errors)  
⏳ Ready for simulation

## Next Steps

1. Run simulation (`python run.py`)
2. Check RTP (target 95.5%-96.5%)
3. Optimize reel strips if needed
4. Expand to 150-220 positions (production)
5. Generate books for Web SDK

---

**Created:** 2026-02-17  
**Converted from:** `games/game1/game_config.json`  
**Based on:** 0_0_lines template
