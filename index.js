class Observable {
    constructor() {
        this.observers = [];
    }

    addObserver(observer) {
        this.observers.push(observer);
    }

    notifyObservers(data) {
        this.observers.forEach(observer => observer.update(data));
    }

    setData(data) {
        // 只有当数据变化时才通知观察者
        if (this.data !== data) {
            this.data = data;
            this.notifyObservers(data);
        }
    }
}

class Computation {
    constructor(observable) {
        this.observable = observable;
        this.observable.addObserver(this);
    }

    update(data) {
        console.log("基于新数据进行计算: ", data * 2);
    }
}

const observable = new Observable();
const computation = new Computation(observable);
observable.setData(10); // 触发计算