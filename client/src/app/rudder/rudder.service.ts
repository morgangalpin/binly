import { Injectable } from "@angular/core";

import { SocketService } from "../shared";

@Injectable()
export class RudderService {

    namespace:string = 'rudder';
    rudderEvent:string = 'update';

    constructor(
        private socketService: SocketService
    ) {
        this.socketService.connect(this.namespace, 'RudderService.socketService');
    }

    setRudder(value:number): void {
        this.socketService.socket.emit(this.rudderEvent, { rudder: value });
    }
}