import { Injectable } from "@angular/core";

import { SocketService } from "../shared";

@Injectable()
export class GpsService {

    namespace:string = 'gps';
    gpsEvent:string = 'feed';

    constructor(
        private socketService: SocketService
    ) {
        console.log('GpsService.constructor()');
        this.socketService.connect(this.namespace, 'GpsService.socketService');
    }

    onProcessGpsEvent(callback) : void {
        console.log('GpsService.onProcessGpsEvent("%s")', this.gpsEvent);
        this.socketService.on(this.gpsEvent, callback);
    }

    processEvent(currentGps:number): void {
    }
}