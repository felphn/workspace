function mergeSort(arr) {
    if (arr.length > 1) {
        let leftArr = arr.slice(0, Math.round(arr.length/2));
        let rightArr = arr.slice(Math.round(arr.length/2), arr.length);
        mergeSort(leftArr);
        mergeSort(rightArr);
        let a = b = c = 0;
        while (a < leftArr.length && b < rightArr.length) {
            if (leftArr[a] < rightArr[b]) {
                arr[c] = leftArr[a];
                a++;
            } else {
                arr[c] = rightArr[b];
                b++;
            };
            c++;
        };
        while (a < leftArr.length) {
            arr[c] = leftArr[a];
            a++;
            c++;
        };
        while (b < rightArr.length) {
            arr[c] = rightArr[b];
            b++;
            c++;
        };
    };
};

const valuesLst = [15, 2, 7, 26, 35, 9, 4, 8, 52, 68];
console.log(`List: [${valuesLst.join(', ')}]`)
mergeSort(valuesLst);
console.log(`Sorted List: [${valuesLst.join(', ')}]`);