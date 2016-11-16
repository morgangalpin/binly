import { Injectable } from "@angular/core";

import { SocketService } from "../shared";

@Injectable()
export class GpsService {

    socket: SocketIOClient.Socket;
    namespace:string = 'gps';
    gpsEvent:string = 'feed';

    constructor(
        private socketService: SocketService
    ) {
        console.log('GpsService.constructor()');
        this.socket = this.socketService.get(this.namespace, 'GpsService.socketService');
    }

    onProcessGpsEvent(callback) : void {
        console.log('GpsService.onProcessGpsEvent("%s")', this.gpsEvent);
        this.socket.on(this.gpsEvent, callback);
    }

    processEvent(currentGps:number): void {
    }
}