
import math

def rental_yield(monthly_rent, price):
    if not price or not monthly_rent:
        return None
    return round((monthly_rent * 12 / price) * 100, 2)

def net_yield(monthly_rent, price, annual_costs):
    if not price or not monthly_rent:
        return None
    net = (monthly_rent * 12) - annual_costs
    return round((net / price) * 100, 2)

def mortgage_payment(principal, annual_rate, years):
    r = annual_rate / 12
    n = years * 12
    if r == 0:
        return principal / n
    return round((principal * r) / (1 - (1 + r)**(-n)), 2)

def cashflow(monthly_rent, mortgage_payment, annual_costs):
    return round((monthly_rent*12) - (mortgage_payment*12) - annual_costs, 2)

def dcf_valuation(cashflows, discount_rate):
    return round(sum(cf / ((1+discount_rate)**i) for i,cf in enumerate(cashflows,1)), 2)

def appreciation_model(price, growth_rate, years):
    return round(price * ((1 + growth_rate)**years), 2)

def renovation_adjustment(price, renovation_cost):
    return price + renovation_cost

def investment_score(yield_pct, net_yield_pct, undervalued_flag):
    score = 0
    if yield_pct: score += min(yield_pct, 15) * 3
    if net_yield_pct: score += min(net_yield_pct, 12) * 4
    if undervalued_flag: score += 20
    return min(score, 100)
