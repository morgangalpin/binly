import { Injectable } from "@angular/core";

import { SocketService } from "../shared";

@Injectable()
export class ThrottleService {

    socket: SocketIOClient.Socket;
    namespace:string = 'throttle';
    throttleEvent:string = 'update';

    constructor(
        private socketService: SocketService
    ) {
        this.socket = this.socketService.get(this.namespace, 'ThrottleService.socketService');
    }

    setThrottle(value:number): void {
        console.log('Sending throttle update on ' + this.socket.id)
        this.socket.emit(this.throttleEvent, { throttle: value });
    }
}