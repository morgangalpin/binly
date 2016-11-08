import { Injectable } from "@angular/core";

import { SocketService } from "../shared";

@Injectable()
export class ThrottleService {

    namespace:string = 'throttle';
    throttleEvent:string = 'update';

    constructor(
        private socketService: SocketService
    ) {
        this.socketService.connect(this.namespace, 'ThrottleService.socketService');
    }

    setThrottle(value:number): void {
        this.socketService.socket.emit(this.throttleEvent, { throttle: value });
    }
}