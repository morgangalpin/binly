import { Component, OnInit, Input } from '@angular/core';
import { Observable } from "rxjs";

import { SpeedService } from './speed.service';

@Component({
  selector: 'app-speed',
  templateUrl: './speed.component.html',
  styleUrls: ['./speed.component.css']
})
export class SpeedComponent implements OnInit {

  currentSpeed: number = 0;

  constructor(
    private speedService: SpeedService
  ) {
    this.speedService.onProcessSpeedEvent((data) => { console.log('SpeedComponent.onProcessSpeedEvent("%o")', data); this.currentSpeed = data.num; });
  }

  ngOnInit() {
  }

}
