import numpy as np
from scipy import stats


def combined_retention(row):
    ft, pt = row["FT_POP"], row["PT_POP"]
    ret_ft, ret_pt = row["RET_RATE_FT"], row["RET_RATE_PT"]

    if (ft + pt) == 0:
        return ret_ft or 0

    if ret_ft is None or ret_ft == 0:
        return ret_pt
    if ret_pt is None or ret_pt == 0:
        return ret_ft

    return (ft * ret_ft + pt * ret_pt) / (ft + pt)


def pop_log_minmax_score(series, value, clip=100000):
    if value is None or value <= 0 or np.isnan(value):
        return 0
    clean = series[series > 0].dropna().clip(upper=clip)
    value = min(value, clip)
    l = np.log1p(clean)
    v = np.log1p(value)
    return (v - l.min()) / (l.max() - l.min()) * 100


def log_percentile(series, value):
    if value is None or value <= 0 or np.isnan(value):
        return 0

    clean_series = series[series > 0].dropna()
    if clean_series.empty:
        return 0

    return stats.percentileofscore(np.log1p(clean_series), np.log1p(value))


def scoring_components(row, df):
    comps = {}

    p_endow_fte = log_percentile(df["ENDOW_FTE"], row["ENDOW_FTE"])
    p_endow = log_percentile(
        df["ENDOW_FTE"] * df["FTE_POP"], row["ENDOW_FTE"] * row["FTE_POP"]
    )
    p_pop = pop_log_minmax_score(df["FTE_POP"], row["FTE_POP"])
    p_apps = log_percentile(df["APPL_TOTAL"], row.get("APPL_TOTAL", 0))

    if row["ACC_RATE"] > 0 and row["YIELD_RATE"] > 0:
        desirability = row["YIELD_RATE"] / row["ACC_RATE"]
        ratio_series = (df["YIELD_RATE"] / df["ACC_RATE"]).replace([np.inf, -np.inf], 0)
        p_des = log_percentile(ratio_series, desirability)
    else:
        p_des = 0

    p_grad = row["GRAD_RATE_6_YR"] or 0
    p_ret = combined_retention(row)

    # Endowment and size - 15pts total
    comps["endow_fte"] = 4 * p_endow_fte / 100
    comps["endow"] = 4 * p_endow / 100
    comps["fte_pop"] = 7 * p_pop / 100

    # Outcomes - 20pts total
    comps["grad"] = 12 * p_grad
    comps["ret"] = 8 * p_ret

    # Demand - 30pts total
    comps["desir"] = 25 * p_des / 100
    comps["apps"] = 5 * p_apps / 100

    # Research spend/impact/classification - 35pts total
    if row["RND_SPEND"] and row["RND_SPEND"] > 0:
        p_rnd_fte = log_percentile(
            df["RND_SPEND"] / df["FTE_POP"], row["RND_SPEND"] / row["FTE_POP"]
        )
        p_rnd = log_percentile(df["RND_SPEND"], row["RND_SPEND"])

        comps["rnd_spend"] = 11 * p_rnd / 100
        comps["rnd_spend_fte"] = 4 * p_rnd_fte / 100
    else:
        comps["rnd_spend"] = 0
    comps["cpf"] = row.get("QS_CPF", 0) / 100 * 4

    if row["CRN_BASIC"] == 15:  # R1
        comps["research"] = 16
    elif row["CRN_BASIC"] == 16:  # R2
        comps["research"] = 9
    elif row["CRN_BASIC"] in [17, 18]:
        comps["research"] = 4
    else:
        comps["research"] = 0

    # online penalty - -5pts total
    comps["online"] = -5 if row["ONLINE"] == 1 else 0

    return comps
