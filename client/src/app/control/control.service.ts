import { Injectable } from "@angular/core";

import { SocketService } from "../shared";

@Injectable()
export class ControlService {

    namespace:string = 'test';
    velocityEvent:string = 'my_broadcast_event';
    soundEvent:string = 'my_broadcast_event';

    constructor(
        private socketService: SocketService
    ) {
        this.socketService.get(this.namespace);
    }

    accelerate(units:number): void {
        this.socketService.socket.emit(this.velocityEvent, { data: 'accelerate: ' + units });
    }

    reverse(units:number): void {
        this.socketService.socket.emit(this.velocityEvent, { data: 'reverse: ' + units });
    }

    rudderLeft(units:number): void {
        this.socketService.socket.emit(this.velocityEvent, { data: 'rudderLeft: ' + units });
    }

    rudderRight(units:number): void {
        this.socketService.socket.emit(this.velocityEvent, { data: 'rudderRight: ' + units });
    }

    quack(): void {
        this.socketService.socket.emit(this.soundEvent, { data: 'quack' });
    }

}