import { Component, OnInit } from '@angular/core';

import { ControlService } from './control.service';

@Component({
  selector: 'app-control',
  templateUrl: './control.component.html',
  styleUrls: ['./control.component.css']
})
export class ControlComponent implements OnInit {

  constructor( private controlService:ControlService) {
  }

  ngOnInit() {
  }

  accelerate():void {
    this.controlService.accelerate(Math.floor(Math.random() * 4) + 1);
  }

  reverse():void {
    this.controlService.reverse(Math.floor(Math.random() * 4) + 1);
  }

  rudderLeft():void {
    this.controlService.rudderLeft(Math.floor(Math.random() * 4) + 1);
  }

  rudderRight():void {
    this.controlService.rudderRight(Math.floor(Math.random() * 4) + 1);
  }
}
