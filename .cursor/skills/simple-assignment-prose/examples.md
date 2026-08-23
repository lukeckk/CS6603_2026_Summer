# Voice samples

Copy this register. These are from Luke's CS6603 reports.

## Gold samples (write like this)

### Explaining a formula

> To create this score, we start everyone at a base of 100 points and then subtract points based on how late their payments have been by looking at each of the six payment history fields such as PAY_0, and PAY_2 through PAY_6, and for each one, we only count it as delay if the value is positive, meaning 0 or negative values do not count against the score. For every month of delay found in each field, I deduct 10 points from the total. Finally, I make sure the score never drops below 0 by clipping any negative result to 0, so the formula is "score = max(0, 100 - (10 * sum of all positive PAY values))".

### Reading a fairness metric

> Based on the two fairness metrics, there is not much age bias between the privileged group (younger than age 40) and the unprivileged group (age 40 and older) on the training dataset. The Disparate Impact is 0.9969, which is very close to the ideal value of 1.0 and well within the fair range of 0.8 to 1.2, meaning the loan approval rates for young and old applicants were almost the same. Equal Opportunity is 0.0022, which is also near the ideal of 0, so amongst applicants who did not default, both age groups were approved at nearly the same rate. This result makes sense with our threshold of 25, because most people are approved under that cutoff, so there is little room for one age group to be treated much better or worse than the other. Overall, the metrics do not show bias for or against either the privileged or unprivileged age group at this stage.

### Tradeoff wrap-up

> By using different thresholds of 35 for young and 40 for old group, Disparate Impact improved from 0.9969 to 1.0002, and the approval rates became even closer with both groups being around 90.8%. Because there was only a little bias to begin with, neither group gained a large advantage. Both groups were approved a bit less often than under the single threshold of 25, and total profit dropped from 86335 to 85600. So the mitigation made the groups more equal, but it also made approval stricter for both, with a small tradeoff in profit.

### Summarizing an article

> This report shows how automated hiring tools used by major companies are biased against job seekers with certain ethnicity. When filtering through applicants, these tools tend to filter out Black and Asian candidates while favoring White candidates. Instead of filtering based on their qualifications, the algorithm relies on older, biased data and clues like test games or educational background. As a result, qualified minority applicants are frequently rejected before a human recruiter ever sees their application.

> To make it worse, over 150 top companies use the same hiring software, thus a single flaw in the system gets repeated everywhere. For example, if a candidate is mistakenly rejected by this algorithm once, they will end up getting rejected as well from jobs across other companies as they are using the same tools.

### Ethics critique

> The 2016 claim regarding Mercedes-Benz aligns with the Protectionist Ethics algorithm which prioritizes the vehicle's occupants first. If two autonomous cars operating under this identical algorithm, and neither car is programmed to give way or take the hit, they will end up crashing into each other.

> But if these self-driving cars could communicate to one another, the outcome will change positively. For example, in the bicycle scenario both blue cars can work together and come up with a solution that works for both party rather than blindly executing the action that favors the occupants, such as minimizing the impact to sideswipe rather than a head on impact, thereby occupants in both cars get to survive.

> This Tesla approach is closest to the Protectionist Ethics algorithm. The reason is it only focuses on the driver and ignores people outside the car. By refusing to take over the wheel even when the driver is doing something bad, it behaves with total loyalty to the driver and it is ok with anything as long as the driver is safe.

## Rewrite down, not up

Same content. Left column is the goal. Right column is what this skill must not produce.

**Simple (goal):**
This result makes sense with our threshold of 25, because most people are approved under that cutoff, so there is little room for one age group to be treated much better or worse than the other.

**Too polished (reject):**
This outcome is consistent with the selected decision threshold, as the high overall approval rate leaves limited opportunity for systematic disparities between age groups.

---

**Simple (goal):**
The graph is showing one big overall average and hiding bias against black and asian applicants. For example, if the tool hires a lot of Black candidates for entry-level warehouse jobs, but rejects them for high-paying manager jobs, the overall average makes it look like everything is fair.

**Too polished (reject):**
Aggregate visualizations can obscure subgroup disparities. A high overall hiring rate may conceal inequitable outcomes concentrated in higher-status roles.

---

**Simple (goal):**
Candidates never get a fresh start.

**Too polished (reject):**
Applicants are consequently denied independent reconsideration across employers.

---

**Simple (goal):**
So in this case, the car need to have a completely different setting where it may move at slower speed and do more screening and predictions of the surrounding.

**Too polished (reject):**
Accordingly, the vehicle's policy should be geographically conditioned, reducing speed and increasing predictive coverage in dense mixed-traffic environments.
