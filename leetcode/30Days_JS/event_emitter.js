class EventEmitter {

    constructor() {
        this.events = {};
    }
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        if (this.events[eventName]) {
         this.events[eventName].fn.push(callback)   
        } else {
            this.events[eventName] = {};
            this.events[eventName].fn = [];
            this.events[eventName].fn.push(callback);
        }
        return {
            unsubscribe: () => {
                const index = this.events[eventName].fn.indexOf(callback);
                if (index !== -1) {
                    this.events[eventName].fn.splice(index, 1);
                }
                return undefined;
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        if (!this.events[eventName]) return [];
        const event = this.events[eventName];
        if (event.fn.length === 0) return [];
        if (event.fn.length > 1) {
            const res = []
            event.fn.forEach(v => {
                res.push(v(...args));
            })
            return res;
        }
        return [event.fn[0](...args)];
    }
}

// Run the test cases
function test() {
    const emitter = new EventEmitter();
    const sub1 = emitter.subscribe("firstEvent", x => x + 1);
    const sub2 = emitter.subscribe("firstEvent", x => x + 2);
    const sub3 = emitter.subscribe("firstEvent", x => x + 3);

    sub2.unsubscribe();
    sub3.unsubscribe();
    console.log(emitter.emit("firstEvent", [5])); // [6]
}
