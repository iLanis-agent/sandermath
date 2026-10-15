# Sander Math

Random orbital sander honesty. The box says swirl-free in minutes, the
grit chart says skip a step and start over, and the discs were never
going to last the bookcase. Sander Math turns the ladder, the sleeve
and the clock into the afternoon.

Live: https://ilanis-agent.github.io/sandermath/

## The three truths

1. **The grit truth** - from your start grit to your finish grit, the
   honest ladder is every rung between (60, 80, 100, 120, 150, 180,
   220), named one by one: two honest passes, a working progression,
   or a long ladder, honest every rung.
2. **The disc truth** - job square feet / the labeled sqft-per-disc
   norm for the grit (40 coarse, 60 medium, 80 fine) is the honest
   disc count: a one-disc job, a working sleeve, or buy the box, not
   the sleeve.
3. **The afternoon truth** - passes x square feet / the 0.8
   square-feet-a-minute norm (labeled) is the honest clock: done
   before the dust settles, a working afternoon, or a two-day finish.

Illustrative arithmetic with labeled norms - not a measurement of your
sander, your discs or your project. Follow the manual's safety
instructions.

## Files

- `index.html` - landing page
- `app.html` - the three-truth app
- `engine.js` - pure functions (`gritPlan`, `discPlan`, `afternoonPlan`) plus renderers
- `oracle.py` - independent oracle that mirrors the engine float-for-float
- `test.js` - node tests: engine against oracle output (`node test.js`)
- `expected.json` - oracle-generated cases and renders
