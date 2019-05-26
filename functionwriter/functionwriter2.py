tobedone = [
    "EffectiveInterestRate",
    "ReferenceFloorRate",
    "ReferenceCapRate",
    "AdvancedRepayment",
    "RetainedInterestCollected",
    "RetainedInterestUtilized",
    "CashCollateralCollected",
    "CashCollateralUtilized",
    "AccruedInterest",
    "AccruedUpto"
]

for element in tobedone:

    print("public String get" + element + "(){return wait.visibilityOf(" + element + ").getText();String[] value = expected.split(\":\");return value[1];}")