import { Component, OnInit, Input } from '@angular/core';
import { Observable } from "rxjs";

import { ThrottleService } from './throttle.service';

@Component({
  selector: 'app-throttle',
  templateUrl: './throttle.component.html',
  styleUrls: ['./throttle.component.css']
})
export class ThrottleComponent implements OnInit {

  currentThrottle: number = 0;

  constructor(
    private throttleService: ThrottleService
  ) {
    this.throttleService.onProcessThrottleEvent((data) => { console.log('ThrottleComponent.onProcessThrottleEvent("%o")', data); this.currentThrottle = data.num; });
  }

  ngOnInit() {
  }

}
