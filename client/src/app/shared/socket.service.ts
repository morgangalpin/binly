import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import * as io from "socket.io-client";

import { environment } from '../../environments/environment';

// import { IMessage, ISocketItem } from "../../models";

@Injectable()
export class SocketService {
    // private host: string = "http://192.168.1.64:8080";
    private host: string = environment.host;

    constructor() {}

    // Get a connected socket.
    get(name: string, id: string) {
        let socketUrl = this.host + "/" + name;
        console.log(`SocketService: Connecting to "${socketUrl}" on "${id}"`);
        let socket = io.connect(socketUrl);
        socket.id = id;
        socket.on("connect", () => {
            console.log(`Connected to "${socketUrl}"`);
        });
        socket.on("disconnect", () => {
            console.log(`Disconnected from "${socketUrl}"`);
        });
        socket.on("error", (error: string) => {
            console.log(`ERROR: on "${socketUrl}": "${error}"`);
        });
        return socket;
    }
}