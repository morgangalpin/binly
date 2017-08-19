import { Injectable } from "@angular/core";

import { SocketService } from "./socket.service";

@Injectable()
export class SimpleSocketService {

    protected socket: SocketIOClient.Socket;

    constructor(
        private socketService: SocketService,
        protected namespace: string,
        protected eventName: string
    ) {
        this.socket = this.socketService.get(this.namespace, this.namespace + 'Service.socketService');
    }

    setValue(value:number): void {
        console.log('Sending ' + this.eventName + ' event to ' + this.namespace + ' namespace on socket: ' + this.socket.id)
        this.socket.emit(this.eventName, value);
    }
}
