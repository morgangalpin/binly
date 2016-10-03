import { Injectable } from "@angular/core";

import { SocketService } from "../shared";

@Injectable()
export class SpeedService {

    namespace:string = 'test';
    speedEvent:string = 'my_response';

    constructor(
        private socketService: SocketService
    ) {
      this.socketService.get(this.namespace);
    }

    onProcessSpeedEvent(callback) : void {
      console.log('SpeedService.onProcessSpeedEvent("%s")', this.speedEvent);
      this.socketService.socket.on(this.speedEvent, callback);
    }

    processEvent(currentSpeed:number): void {
    }
}