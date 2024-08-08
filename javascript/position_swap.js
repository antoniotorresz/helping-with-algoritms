function swapPositions(arr) {
    let max_idx = arr.length - 1;
    for (let i = 0; i <= max_idx / 2; i++) {
        let temp = arr[i];
        arr[i] = arr[max_idx - i];
        arr[max_idx - i] = temp;
    }
    return arr;
}
console.log(swapPositions([1, 2, 3, 4, 5]));
console.log(swapPositions([3, 2, 5, 2, 6, 2, 1, 9, 0, 11]));