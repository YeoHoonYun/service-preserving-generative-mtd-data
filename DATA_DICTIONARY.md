# Data dictionary: v2.1.0 without three-arm cohorts

The v1 evidence base contains 60 accepted MiniShop/Flaskr generation slots and their selected validation records. The added Juice Shop archive covers four bounded edge-adapter candidates, not the whole application. Public URLs, authentication, database, and vulnerable upstream remain fixed. `accepted_first_attempt` counts generation slots; tokens count provider input plus output. `observed_pin_exposure_lower_bound_seconds` is an observed minimum, not a cookie lifetime. Flaskr timing comes from fixed targets and cannot estimate rotation benefit. `NON_THREE_ARM_RESULTS.json` contains no S0/S1/S2 arm comparison.

The 3-arm source folders named in that file are intentionally absent. Existing v1 baselines B0–B3/P1 are validation-policy comparisons, not the excluded S0/S1/S2 attack arms.
