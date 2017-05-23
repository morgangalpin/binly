import { Component, OnInit } from '@angular/core';

import { SteeringService } from './steering.service';

@Component({
    selector: 'app-steering',
    templateUrl: './steering.component.html',
    styleUrls: ['./steering.component.css']
})
export class SteeringComponent implements OnInit {

    steering: number;
    label: string;

    constructor(
        private steeringService: SteeringService
    ) {}

    setSteering(value: number) {
        if (value != this.steering) {
            console.log("Changing steering value from: " + this.steering + " to " + value)
            this.steering = value;
            this.updateLabel(this.steering);
            this.steeringService.setSteering(value);
        }
    }

    // Update the label value based on the given value.
    updateLabel(value) {
        if (value > 0) {
            this.label = 'Right ' + value;
        } else if (value < 0) {
            this.label = 'Left ' + -value;
        } else {
            this.label = 'Center'
        }
    }

    ngOnInit() {
        this.setSteering(0);
    }
}
