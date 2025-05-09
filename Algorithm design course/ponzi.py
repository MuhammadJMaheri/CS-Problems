"""Ponzi problem"""
from decimal import Decimal
def remove_exponent(d):
    return (
        d.quantize(Decimal(1))
        if d == d.to_integral()
        else d.normalize()
    )
W , n = map(int, input().split())
Asset_Price = list(map(int, input().split()))
Asset_Weight = list(map(int, input().split()))

asset = ([(Asset_Price[i], Asset_Weight[i], Asset_Price[i]/Asset_Weight[i])
                    for i in range(0, n)])
asset_prioritised = sorted(asset, key=lambda tup: tup[2], reverse=True)
CASE_PRICE = 0
CASE_WEIGHT = 0
i = 0
for asset in asset_prioritised:
    if asset[1] + CASE_WEIGHT <= W:
        CASE_WEIGHT += asset[1]
        CASE_PRICE += asset[0]
        continue
    CASE_PRICE += ((W - CASE_WEIGHT)/asset[1])*asset[0]
    break

output = Decimal(round(CASE_PRICE, 2))
print(round(remove_exponent(output), 2))
