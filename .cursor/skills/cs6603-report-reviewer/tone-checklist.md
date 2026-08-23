# Tone checklist for report review

Luke wants simple spoken English on purpose. It matches how he learns, and it
should read like a student wrote it — not like a model polished it.

Compare paragraphs to the **gold samples** below. Flag text that matches the
**reject** patterns.

---

## Pass signals (sounds like Luke)

- Everyday words: `not much`, `almost the same`, `this makes sense because`,
  `to make it worse`, `a little`, `pretty close`, `end up`, `ok with`
- Mixed `I` / `we` like lab notes
- Numbers in the sentence, then plain meaning (`meaning ...`, `so ...`)
- Chains with `and`, `so`, `because` instead of formal transitions
- Wrap-ups: `Overall, ...` / `So ...` / `This makes sense because ...`
- Course terms kept, then explained in normal words
- Walkthrough explanations (how a score or method is built step by step)
- 3–6 sentence paragraphs, one idea each — not padded

## Fail signals (AI-polish / academic filler)

Flag these when they show up in **paragraph** prose:

| Signal | Examples |
|--------|----------|
| Formal transitions | `furthermore`, `moreover`, `additionally`, `nonetheless`, `consequently` |
| Paper voice | `this paper demonstrates`, `this analysis reveals`, `it is worth noting`, `the aforementioned` |
| Essay hedges | `it can be argued that`, `one might consider`, `it may be the case that`, `potentially` stacks |
| Perfect arc | Topic sentence → evidence → implication, every paragraph the same shape |
| Synonym inflation | `utilize` / `leverage` / `facilitate` where `use` / `help` would do |
| Detached third person only | Whole section as "the study" / "the model" with no I/we when Luke usually mixes |
| Blog cadence | Balanced three-clause sentences that sound like LinkedIn or a textbook summary |

**Borderline:** one `Furthermore` at the start of a paragraph Luke already
wrote is not automatic fail — weigh against the rest of the paragraph. Many
fail signals together = high risk.

---

## Gold samples (pass)

### Explaining a formula

> To create this score, we start everyone at a base of 100 points and then subtract points based on how late their payments have been by looking at each of the six payment history fields such as PAY_0, and PAY_2 through PAY_6, and for each one, we only count it as delay if the value is positive, meaning 0 or negative values do not count against the score. For every month of delay found in each field, I deduct 10 points from the total. Finally, I make sure the score never drops below 0 by clipping any negative result to 0, so the formula is "score = max(0, 100 - (10 * sum of all positive PAY values))".

### Reading a fairness metric

> Based on the two fairness metrics, there is not much age bias between the privileged group (younger than age 40) and the unprivileged group (age 40 and older) on the training dataset. The Disparate Impact is 0.9969, which is very close to the ideal value of 1.0 and well within the fair range of 0.8 to 1.2, meaning the loan approval rates for young and old applicants were almost the same. Equal Opportunity is 0.0022, which is also near the ideal of 0, so amongst applicants who did not default, both age groups were approved at nearly the same rate. This result makes sense with our threshold of 25, because most people are approved under that cutoff, so there is little room for one age group to be treated much better or worse than the other. Overall, the metrics do not show bias for or against either the privileged or unprivileged age group at this stage.

### Tradeoff wrap-up

> By using different thresholds of 35 for young and 40 for old group, Disparate Impact improved from 0.9969 to 1.0002, and the approval rates became even closer with both groups being around 90.8%. Because there was only a little bias to begin with, neither group gained a large advantage. Both groups were approved a bit less often than under the single threshold of 25, and total profit dropped from 86335 to 85600. So the mitigation made the groups more equal, but it also made approval stricter for both, with a small tradeoff in profit.

### Summarizing an artifact

> This report shows how automated hiring tools used by major companies are biased against job seekers with certain ethnicity. When filtering through applicants, these tools tend to filter out Black and Asian candidates while favoring White candidates. Instead of filtering based on their qualifications, the algorithm relies on older, biased data and clues like test games or educational background. As a result, qualified minority applicants are frequently rejected before a human recruiter ever sees their application.

> To make it worse, over 150 top companies use the same hiring software, thus a single flaw in the system gets repeated everywhere. For example, if a candidate is mistakenly rejected by this algorithm once, they will end up getting rejected as well from jobs across other companies as they are using the same tools.

### Ethics critique

> This Tesla approach is closest to the Protectionist Ethics algorithm. The reason is it only focuses on the driver and ignores people outside the car. By refusing to take over the wheel even when the driver is doing something bad, it behaves with total loyalty to the driver and it is ok with anything as long as the driver is safe.

---

## Side-by-side (reject the right column)

**Pass:**
This result makes sense with our threshold of 25, because most people are approved under that cutoff, so there is little room for one age group to be treated much better or worse than the other.

**Fail:**
This outcome is consistent with the selected decision threshold, as the high overall approval rate leaves limited opportunity for systematic disparities between age groups.

---

**Pass:**
The graph is showing one big overall average and hiding bias against black and asian applicants. For example, if the tool hires a lot of Black candidates for entry-level warehouse jobs, but rejects them for high-paying manager jobs, the overall average makes it look like everything is fair.

**Fail:**
Aggregate visualizations can obscure subgroup disparities. A high overall hiring rate may conceal inequitable outcomes concentrated in higher-status roles.

---

**Pass:**
Candidates never get a fresh start.

**Fail:**
Applicants are consequently denied independent reconsideration across employers.

---

## How to score voice risk

| Risk | When |
|------|------|
| **Low** | Most paragraphs match gold samples; at most 1–2 soft flags |
| **Medium** | Several formal transitions or one whole section sounds upgraded |
| **High** | Long stretches of paper voice, synonym inflation, or perfect essay arcs |

When rewriting after review: rewrite **down**, not up. Keep course terms.
Do not add fake typos.
