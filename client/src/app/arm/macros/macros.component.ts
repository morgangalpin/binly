import { Component, OnInit, Input } from '@angular/core';

import { ServoComponent } from '../../servo/servo.component';

@Component({
    selector: 'app-arm-macros',
    templateUrl: './macros.component.html',
    styleUrls: ['./macros.component.css']
})
export class MacrosComponent implements OnInit {
    @Input() controls: { [index: string]: ServoComponent } = {};

    constructor() {}

    ngOnInit() {
        console.log("Initializing arm macros. Have access to following controls: " + Object.keys(this.controls));
    }

    onClickRestPosition() {
        console.log("Setting servos to rest position.");
        this.setToPosition(this.controls['Gripper'].valueInitial, this.controls['WristRotate'].valueInitial,
            this.controls['WristBend'].valueInitial, this.controls['ElbowBend'].valueInitial,
            this.controls['ShoulderBend'].valueInitial, this.controls['ShoulderRotate'].valueInitial);
    }

    onClickReadyToPickupPosition() {
        console.log("Setting servos to Ready to Pickup position.");
        this.setToPosition(0, 0, 0, 0, 90, 0);
    }

    private setToPosition(gripperValue: number, wristRotateValue: number, wristBendValue: number,
            elbowBendValue: number, shoulderBendValue: number, shoulderRotateValue: number) {
        console.log("Setting servos to positions: " + gripperValue + "," + wristRotateValue + "," + wristBendValue + "," +
            elbowBendValue + "," + shoulderBendValue + "," + shoulderRotateValue +  ".");
        this.controls['Gripper'].setValue(gripperValue);
        this.controls['WristRotate'].setValue(wristRotateValue);
        this.controls['WristBend'].setValue(wristBendValue);
        this.controls['ElbowBend'].setValue(elbowBendValue);
        this.controls['ShoulderBend'].setValue(shoulderBendValue);
        this.controls['ShoulderRotate'].setValue(shoulderRotateValue);
    }
}
