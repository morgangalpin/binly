import { Injectable } from "@angular/core";

import { SocketService } from "../shared";

@Injectable()
export class SteeringService {

    socket: SocketIOClient.Socket;
    namespace:string = 'steering';
    steeringEvent:string = 'update';

    constructor(
        private socketService: SocketService
    ) {
        this.socket = this.socketService.get(this.namespace, 'SteeringService.socketService');
    }

    setSteering(value:number): void {
        console.log('Sending steering update on ' + this.socket.id)
        this.socket.emit(this.steeringEvent, { steering: value });
    }
}