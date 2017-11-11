import { Component, OnInit } from '@angular/core';

import { ServoComponent } from '../servo/servo.component';

@Component({
    selector: 'app-arm',
    templateUrl: './arm.component.html',
    styleUrls: ['./arm.component.css']
})
export class ArmComponent implements OnInit {
    public servos: { [index: string]: ServoComponent } = {};

    constructor() {}

    ngOnInit() {
    }
}
