import { Component } from '@angular/core';

import { SocketService } from './shared';

@Component({
  selector: 'app-duckomatic',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title:string = 'Duckomatic';

  isConnected:boolean = false;

  progress: number = 0;

  constructor(
    private socketService: SocketService
  ) {
    // this.socketService.
    // Update the value for the progress-bar on an interval.
    setInterval(() => {
      this.progress = (this.progress + Math.floor(Math.random() * 4) + 1) % 100;
    }, 200);
  }

  // connect():void {
  //   this.socketService.get('test', 'AppComponent.connect()');
  //   this.isConnected = true;
  // }
}
