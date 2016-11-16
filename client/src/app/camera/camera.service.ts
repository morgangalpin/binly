import { Injectable } from "@angular/core";

import { SocketService } from "../shared";

@Injectable()
export class CameraService {

    socket: SocketIOClient.Socket;
    namespace:string = 'camera';
    cameraEvent:string = 'feed';

    constructor(
        private socketService: SocketService
    ) {
        console.log('CameraService.constructor()');
        this.socket = this.socketService.get(this.namespace, 'CameraService.socketService');
    }

    onProcessCameraEvent(callback) : void {
        console.log('CameraService.onProcessCameraEvent("%s")', this.cameraEvent);
        this.socket.on(this.cameraEvent, callback);
    }

    processEvent(currentCamera:number): void {
    }
}