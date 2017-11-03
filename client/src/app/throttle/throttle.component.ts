import { Component } from '@angular/core';

import { ServoComponent } from '../servo/servo.component';

@Component({
    selector: 'app-throttle',
    templateUrl: './throttle.component.html'
})
export class ThrottleComponent extends ServoComponent {
    ngOnInit() {
        if (!this.name) {
            this.name = 'Throttle';
        }
        if (!this.labelStyle) {
            this.labelStyle = 'forward-backward';
        }
        super.ngOnInit();
    }

    onKeyPress(key: string) {
        switch (key) {
            case 's':
                if (this.value > this.valueMin) {
                    this.setValue(this.value - 1);
                }
                break;

            case 'w':
                if (this.value < this.valueMax) {
                    this.setValue(this.value + 1);
                }
                break;

            default:
        }
    }
}
