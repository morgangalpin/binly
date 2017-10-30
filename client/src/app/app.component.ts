import { Component } from '@angular/core';

import { SocketService } from './shared';

@Component({
  selector: 'app-binly',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title:string = 'Binly';

  isConnected:boolean = false;

  constructor() {}
}
