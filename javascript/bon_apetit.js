/*
 * Complete the 'bonAppetit' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY bill
 *  2. INTEGER k
 *  3. INTEGER b
 */

function bonAppetit(bill, k, b) {
    let total = 0;
    bill.forEach((e) => {
        total += e;
    });

    let annasBill = (total - bill[k]) / 2;
    if (annasBill === b) {
        console.log("Bon Appetit");
    }else {
        console.log(annasBill - b);
    }
}

bill = [3, 10, 2, 9];
k = 1;
b = 7;

bonAppetit(bill, k, b);