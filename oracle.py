#!/usr/bin/env python3
# Sander Math oracle - mirrors engine.js float-for-float.
import json, math
LADDER = [60, 80, 100, 120, 150, 180, 220]
RATE = 0.8
def r1(x): return math.floor(x*10+0.5)/10
def f1(x): return "%.1f" % r1(x)
def jsnum(x):
    i = int(x)
    return i if x == i else x
def disc_norm(grit): return 40 if grit < 80 else (60 if grit < 150 else 80)

def grit_plan(start, end):
    if not (start > 0): return {"error": "the start grit must be above zero"}
    if not (end > 0): return {"error": "the finish grit must be above zero"}
    rungs = [g for g in LADDER if start < g <= end]
    if not rungs: return {"error": "the finish grit must sit above the start grit on the ladder"}
    verdict = "two honest passes" if len(rungs) <= 2 else ("a working progression" if len(rungs) <= 4 else "a long ladder, honest every rung")
    return {"steps": len(rungs), "rungs": ", ".join(str(g) for g in rungs), "verdict": verdict}
def render_grit(r, start, end):
    pass_word = "1 pass" if r["steps"] == 1 else "%s passes" % r["steps"]
    return ("From %s to %s the honest ladder is %s - %s - %s."
            % (start, end, pass_word, r["rungs"], r["verdict"]))

def disc_plan(sqft, grit):
    if not (sqft > 0): return {"error": "the square feet must be above zero"}
    if not (grit > 0): return {"error": "the grit must be above zero"}
    norm = disc_norm(grit)
    discs = math.ceil(sqft / norm)
    verdict = "a one-disc job" if discs <= 1 else ("a working sleeve" if discs <= 8 else "buy the box, not the sleeve")
    return {"norm": norm, "discs": discs, "verdict": verdict}
def render_disc(r, sqft, grit):
    disc_word = "1 disc" if r["discs"] == 1 else "%s discs" % r["discs"]
    return ("The %s square feet at %s grit eats a disc every %s square feet (labeled norm) - %s, %s."
            % (sqft, grit, r["norm"], disc_word, r["verdict"]))

def afternoon_plan(sqft, passes):
    if not (sqft > 0): return {"error": "the square feet must be above zero"}
    if not (passes > 0): return {"error": "the passes must be above zero"}
    min_raw = sqft * passes / RATE
    verdict = "done before the dust settles" if min_raw <= 45 else ("a working afternoon" if min_raw <= 120 else "a two-day finish")
    return {"minutes": jsnum(r1(min_raw)), "verdict": verdict}
def render_afternoon(r, sqft, passes):
    pass_word = "1 pass" if passes == 1 else "%s passes" % passes
    min_word = "1 minute" if r["minutes"] == 1 else f1(r["minutes"]) + " minutes"
    return ("%s over %s square feet at the 0.8 square-feet-a-minute norm is %s - %s."
            % (pass_word, sqft, min_word, r["verdict"]))

CASES = [
    ("grit", (60,220)), ("grit", (80,120)), ("grit", (100,180)),
    ("grit", (60,120)), ("grit", (150,220)), ("grit", (80,220)),
    ("disc", (120,60)), ("disc", (80,120)), ("disc", (300,220)),
    ("disc", (50,80)), ("disc", (700,60)), ("disc", (200,100)),
    ("afternoon", (30,2)), ("afternoon", (25,1)), ("afternoon", (60,3)),
    ("afternoon", (40,2)), ("afternoon", (15,1)), ("afternoon", (100,6)),
    ("grit", (0,120)), ("grit", (80,0)), ("grit", (220,60)),
    ("disc", (0,60)), ("disc", (120,0)),
    ("afternoon", (0,2)), ("afternoon", (30,0)),
]
PLANS = {"grit": (grit_plan, render_grit), "disc": (disc_plan, render_disc), "afternoon": (afternoon_plan, render_afternoon)}
out = []
for tool, args in CASES:
    plan, render = PLANS[tool]
    r = plan(*args)
    case = {"tool": tool, "args": list(args), "result": r}
    if "error" not in r:
        case["render"] = render(r, *args)
    out.append(case)
print(json.dumps(out, separators=(",", ":")), end="")
