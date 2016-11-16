import { Injectable } from "@angular/core";

import { SocketService } from "../shared";

@Injectable()
export class RudderService {

    socket: SocketIOClient.Socket;
    namespace:string = 'rudder';
    rudderEvent:string = 'update';

    constructor(
        private socketService: SocketService
    ) {
        this.socket = this.socketService.get(this.namespace, 'RudderService.socketService');
    }

    setRudder(value:number): void {
        console.log('Sending rudder update on ' + this.socket.id)
        this.socket.emit(this.rudderEvent, { rudder: value });
    }
}