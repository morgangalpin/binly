import { Component, OnInit } from '@angular/core';

import { RudderService } from './rudder.service';

@Component({
    selector: 'app-rudder',
    templateUrl: './rudder.component.html',
    styleUrls: ['./rudder.component.css']
})
export class RudderComponent implements OnInit {

    rudder: number;
    direction: string;

    constructor(
        private rudderService: RudderService
    ) {}

    setRudder(value: number) {
        if (value != this.rudder) {
            console.log("Changing rudder value from: " + this.rudder + " to " + value)
            this.rudder = value;
            this.updateDirection();
            this.rudderService.setRudder(value);
        }
    }

    // Update the direction value based on the current rudder value.
    updateDirection() {
        if (this.rudder > 0) {
            this.direction = 'Right ' + this.rudder;
        } else if (this.rudder < 0) {
            this.direction = 'Left ' + -this.rudder;
        } else {
            this.direction = 'Center'
        }
    }

    ngOnInit() {
        this.setRudder(0);
    }
}
