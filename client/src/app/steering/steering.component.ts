import { Component } from '@angular/core';

import { ServoComponent } from '../servo/servo.component';

@Component({
    selector: 'app-steering',
    templateUrl: './steering.component.html'
})
export class SteeringComponent extends ServoComponent {
    ngOnInit() {
        if (!this.name) {
            this.name = 'Steering';
        }
        if (!this.labelStyle) {
            this.labelStyle = 'right-left';
        }
        super.ngOnInit();
    }

    onKeyPress(key: string) {
        switch (key) {
            case 'a':
                if (this.value > this.valueMin) {
                    this.setValue(this.value - 1);
                }
                break;

            case 'd':
                if (this.value < this.valueMax) {
                    this.setValue(this.value + 1);
                }
                break;

            default:
        }
    }
}
