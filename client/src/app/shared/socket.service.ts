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

    constructor() {}

    // Get items observable
    get(name: string): void {
        this.name = name;
        let socketUrl = this.host + "/" + this.name;
        this.socket = io.connect(socketUrl);
        this.socket.on("connect", () => this.connect());
        this.socket.on("disconnect", () => this.disconnect());
        this.socket.on("error", (error: string) => {
            console.log(`ERROR: "${error}" (${socketUrl})`);
        });

    }

    // Handle connection opening
    private connect() {
        // console.log(`Connected to "${this.name}"`);

        // Request initial list when connected
        // this.socket.emit("list");
    }

    // Handle connection closing
    private disconnect() {
        // console.log(`Disconnected from "${this.name}"`);
    }
}