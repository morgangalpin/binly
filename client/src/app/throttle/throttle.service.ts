import { Injectable } from "@angular/core";

import { SocketService } from "../shared";

@Injectable()
export class ThrottleService {

    namespace:string = 'throttle';
    throttleEvent:string = 'my_response';

    constructor(
        private socketService: SocketService
    ) {
        this.socketService.get(this.namespace);
    }

    onProcessThrottleEvent(callback) : void {
        console.log('ThrottleService.onProcessThrottleEvent("%s")', this.throttleEvent);
        this.socketService.socket.on(this.throttleEvent, callback);
    }

    processEvent(currentThrottle:number): void {
    }
}