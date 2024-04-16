/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const newarr = {};

    arr1.forEach((value, index) => {
        newarr[value.id] = value;
    })
    arr2.forEach((value, index) => {
        newarr[value.id] = {...newarr[value.id], ...value};
    })
    return Object.values(newarr);
};