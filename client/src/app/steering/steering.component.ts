import { Component, OnInit } from '@angular/core';

import { ServoComponent } from '../servo/servo.component';

@Component({
    selector: 'app-steering',
    templateUrl: './steering.component.html'
})
export class SteeringComponent extends ServoComponent { }
