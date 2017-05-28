import { Component, OnInit, Input } from '@angular/core';

import { ThrottleService } from './throttle.service';

@Component({
    selector: 'app-throttle',
    templateUrl: './throttle.component.html',
    styleUrls: ['./throttle.component.css']
})
export class ThrottleComponent implements OnInit {

    throttle: number;
    label: string;

    constructor(
        private throttleService: ThrottleService
    ) {}

    setThrottle(value: number) {
        if (value != this.throttle) {
            console.log("Changing throttle value from: " + this.throttle + " to " + value)
            this.throttle = value;
            this.updateLabel(this.throttle);
            this.throttleService.setThrottle(value);
        }
    }

    // Update the label value based on the given value.
    updateLabel(value) {
        if (value > 0) {
            this.label = 'Forward ' + value;
        } else if (value < 0) {
            this.label = 'Backward ' + -value;
        } else {
            this.label = 'Stop'
        }
    }

    ngOnInit() {
        this.setThrottle(0);
    }

}
