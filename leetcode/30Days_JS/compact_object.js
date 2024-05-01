/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    const final = Array.isArray(obj) ? [] : {};

    if (Array.isArray(obj)) {
        obj.forEach(value => {
            if (typeof value === 'object' && Boolean(value)){
                final.push(compactObject(value))
            } else {
                if (Boolean(value))
                final.push(value)
            }
        })
    } else {
        for (let prop of Object.entries(obj)){
            if (typeof prop[1] === 'object' && Boolean(prop[1])){
                final[prop[0]] = compactObject(prop[1])
            } else {
                if (Boolean(prop[1]))
                final[prop[0]] = prop[1]
            }
        }
    }
    return final
};