// Sander Math engine - random orbital sander honesty, labeled norms, honest arithmetic.
(function(root){
"use strict";
var LADDER = [60, 80, 100, 120, 150, 180, 220]; // the honest grit ladder
var RATE = 0.8; // labeled norm: honest square feet a minute with overlap passes
function r1(x){ return Math.round(x*10)/10; }
function f1(x){ return r1(x).toFixed(1); }
function discNorm(grit){ return grit < 80 ? 40 : (grit < 150 ? 60 : 80); } // labeled sqft-per-disc norms

function gritPlan(startGrit, endGrit){
  if (!(startGrit > 0)) return { error: "the start grit must be above zero" };
  if (!(endGrit > 0)) return { error: "the finish grit must be above zero" };
  var rungs = LADDER.filter(function(g){ return g > startGrit && g <= endGrit; });
  if (rungs.length === 0) return { error: "the finish grit must sit above the start grit on the ladder" };
  var verdict = rungs.length <= 2 ? "two honest passes" : (rungs.length <= 4 ? "a working progression" : "a long ladder, honest every rung");
  return { steps: rungs.length, rungs: rungs.join(", "), verdict: verdict };
}
function renderGrit(r, startGrit, endGrit){
  var passWord = r.steps === 1 ? "1 pass" : r.steps + " passes";
  return "From " + startGrit + " to " + endGrit + " the honest ladder is " + passWord + " - " + r.rungs + " - " + r.verdict + ".";
}

function discPlan(sqft, grit){
  if (!(sqft > 0)) return { error: "the square feet must be above zero" };
  if (!(grit > 0)) return { error: "the grit must be above zero" };
  var norm = discNorm(grit);
  var discs = Math.ceil(sqft / norm);
  var verdict = discs <= 1 ? "a one-disc job" : (discs <= 8 ? "a working sleeve" : "buy the box, not the sleeve");
  return { norm: norm, discs: discs, verdict: verdict };
}
function renderDisc(r, sqft, grit){
  var discWord = r.discs === 1 ? "1 disc" : r.discs + " discs";
  return "The " + sqft + " square feet at " + grit + " grit eats a disc every " + r.norm + " square feet (labeled norm) - " + discWord + ", " + r.verdict + ".";
}

function afternoonPlan(sqft, passes){
  if (!(sqft > 0)) return { error: "the square feet must be above zero" };
  if (!(passes > 0)) return { error: "the passes must be above zero" };
  var minRaw = sqft * passes / RATE;
  var verdict = minRaw <= 45 ? "done before the dust settles" : (minRaw <= 120 ? "a working afternoon" : "a two-day finish");
  return { minutes: r1(minRaw), verdict: verdict };
}
function renderAfternoon(r, sqft, passes){
  var passWord = passes === 1 ? "1 pass" : passes + " passes";
  var minWord = r.minutes === 1 ? "1 minute" : f1(r.minutes) + " minutes";
  return passWord + " over " + sqft + " square feet at the 0.8 square-feet-a-minute norm is " + minWord + " - " + r.verdict + ".";
}

root.SanderMath = { gritPlan: gritPlan, renderGrit: renderGrit, discPlan: discPlan, renderDisc: renderDisc, afternoonPlan: afternoonPlan, renderAfternoon: renderAfternoon };
})(typeof window !== "undefined" ? window : globalThis);
