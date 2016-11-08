import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import * as io from "socket.io-client";

import { environment } from '../../environments/environment';

// import { IMessage, ISocketItem } from "../../models";

@Injectable()
export class SocketService {
    private name: string;
    // private host: string = window.location.protocol + "//" + window.location.hostname + ":" + window.location.port;
    // private host: string = "http://192.168.1.64:8080";
    private host: string = environment.host;
    socket: SocketIOClient.Socket;
    id: string;

    constructor() {}

    // Get the connected socket.
    connect(name: string, id: string): void {
        this.name = name;
        this.id = id;
        let socketUrl = this.host + "/" + this.name;
        console.log(`SocketService: Connecting to "${socketUrl}" on "${this.id}"`);
        this.socket = io.connect(socketUrl);
        this.socket.on("connect", () => this.on_connect());
        this.socket.on("disconnect", () => this.on_disconnect());
        this.socket.on("error", (error: string) => {
            console.log(`ERROR: "${error}" (${socketUrl})`);
        });
    }

    // Bind an event handler to an event name.
    on(eventName: string, callback) {
        this.socket.on(eventName, callback);
    }

    // Handle connection opening
    private on_connect() {
        console.log(`Connected to "${this.name}"`);

        // Request initial list when connected
        // this.socket.emit("list");
    }

    // Handle connection closing
    private on_disconnect() {
        console.log(`Disconnected from "${this.name}"`);
    }
}