# Data dictionary, v2.2.0

`V2_2_RESULTS.json` distinguishes the three newly added cohorts from the v2.1.0 base. `provider_usage` counts provider-reported input and output tokens for earlier router/adapter generation only. The frontend/backend implementation extension used trusted templates selected by those model outputs; its new model calls and tokens are zero. `fixed_known_bypass_success` and `rotated_adapted_known_bypass_success` count issued authentication tokens from a previously documented local regression input. The rotating client read the current route from public JavaScript after a stale-route 404. HTTP request counts exclude page assets and setup. The three pairs share adjacent generations and are descriptive, not independent population samples.

The retained v2.1.0 evidence includes 60 MiniShop/Flaskr generation slots. The RealWorld cohort has no browser frontend test. The Juice Shop variant does not replace upstream authentication, authorization or database code. The three failed implementation development runs are retained as partial JSON records, but excluded from accepted-generation denominators.

## v2.3.0 additions

`input_plus_output_tokens` sums provider-reported input and output tokens; cached input is already part of input. Rejected Helpdesk calls count toward cost. The separate aborted onboarding call has unknown usage, so its known token subtotal is only a lower bound. `provider/usage-public.json` omits local evidence paths and authentication mode, retaining call IDs, usage and source-ledger hashes. Service scopes are heterogeneous; totals are descriptive.
