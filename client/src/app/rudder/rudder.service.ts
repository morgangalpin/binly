import { Injectable } from "@angular/core";

import { SocketService } from "../shared";

@Injectable()
export class RudderService {

    namespace:string = 'rudder';
    rudderEvent:string = 'my_response';

    constructor(
        private socketService: SocketService
    ) {
        this.socketService.get(this.namespace);
    }
    
    setRudder(value:number): void {
        this.socketService.socket.emit(this.rudderEvent, { data: 'rudder: ' + value });
    }
}