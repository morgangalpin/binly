import { Component, OnInit } from '@angular/core';

import { SteeringService } from './steering.service';

@Component({
    selector: 'app-steering',
    templateUrl: './steering.component.html',
    styleUrls: ['./steering.component.css']
})
export class SteeringComponent implements OnInit {

    steering: number;
    direction: string;

    constructor(
        private steeringService: SteeringService
    ) {}

    setSteering(value: number) {
        if (value != this.steering) {
            console.log("Changing steering value from: " + this.steering + " to " + value)
            this.steering = value;
            this.updateDirection();
            this.steeringService.setSteering(value);
        }
    }

    // Update the direction value based on the current steering value.
    updateDirection() {
        if (this.steering > 0) {
            this.direction = 'Right ' + this.steering;
        } else if (this.steering < 0) {
            this.direction = 'Left ' + -this.steering;
        } else {
            this.direction = 'Center'
        }
    }

    ngOnInit() {
        this.setSteering(0);
    }
}
