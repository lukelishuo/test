tobedone = [
    "TD_TransactionRef",
    "TD_TransactionrevRef",
    "remarks",
    "reversedremark",
    "TransactionAmount1",
    "TransactionAmount2",
    "TransactionEntrydate1",
    "TransactionEntrydate2",
    "TransactionEnteredby1",
    "TransactionEnteredby2",
    "TransactionView1",
    "TransactionView2",
    "TransactionReverseDetail",
    "TransactionreverseArrow",


]

for element in tobedone:

        print("public String get" + element + "(){return wait.visibilityOf(" + element + ").getText();}")\

        #print("public void click" + element + "() {OnActions.click(" + element + ");}")

        #print("public String get" + element + "status(){ return " + element + ".getAttribute(\"class\");}")
