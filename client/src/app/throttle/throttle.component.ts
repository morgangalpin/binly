import { Component, OnInit, Input } from '@angular/core';

import { ThrottleService } from './throttle.service';

@Component({
    selector: 'app-throttle',
    templateUrl: './throttle.component.html',
    styleUrls: ['./throttle.component.css']
})
export class ThrottleComponent implements OnInit {

    throttle: number = 0;

    constructor(
        private throttleService: ThrottleService
    ) {}

    setThrottle(value: number) {
        if (value != this.throttle) {
            console.log("Changing throttle value from: " + this.throttle + " to " + value)
            this.throttle = value;
            this.throttleService.setThrottle(value);
        }
    }

    ngOnInit() {
    }

}
