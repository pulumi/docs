// Service to persist state into local storage. We can expound on this more
// in the future, but for now gives us what we need and something to work
// with when persisting state.
export class LocalStorageService {
    state: {};
    serviceName: string;

    // name is the name of the key this service will use to store state.
    constructor(name: string) {
        this.serviceName = name;
        // load state from local storage.
        this.state = JSON.parse(window.localStorage.getItem(name) || "{}");
    }
    
    getState() {
        return this.state;
    }

    getKey(key: string): any {
        return this.state[key];
    }

    updateKey(key: string, val:any) {
        this.state = Object.assign(this.state, { [key]: val});
        // persist state to local storage.
        window.localStorage.setItem(this.serviceName, JSON.stringify(this.state));
    }
};
