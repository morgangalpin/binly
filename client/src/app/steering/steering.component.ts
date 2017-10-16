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
            this.labelStyle = 'left-right';
        }
        super.ngOnInit();
    }
}
