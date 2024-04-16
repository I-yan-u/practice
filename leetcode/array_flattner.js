// Solution doesn't perofrm well on Time and Memory benchmarks, but it works for all the test cases
// Scores average time for Time usage and above average for Memory usage

/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
let subArrays = [];
let subArray = 0;
var flat = function (arr, n) {
    let len = subArrays.length;
    if (len > 1 &&
     subArrays[len - 1] === subArrays[len - 2]){
        subArrays = [];
        subArray = 0;
        return arr
    }
    
    if (n <= 0) {
        return arr;
    };
    
    n--;
    const newarr = [];
    arr.forEach((val) => {
        if (Array.isArray(val)){
            newarr.push(...val);
            subArray ++;
        } else {
            newarr.push(val);
        }
    })
    subArrays.push(subArray);
    return flat(newarr, n);
};