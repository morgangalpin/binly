import { Component, OnInit, Input, Optional } from '@angular/core';

import { ServoFormatterSet } from './ServoFormatterSet';
import { SocketService, SimpleSocketService, FormatterSet } from '../shared';

@Component({
    selector: 'app-servo',
    templateUrl: './servo.component.html',
    styleUrls: ['./servo.component.css']
})
export class ServoComponent implements OnInit {
    @Input() name: string;
    @Input() valueMin: number;
    @Input() valueMax: number;
    @Input() valueStep: number;
    public value: number;
    public label: string;
    private socketService: SimpleSocketService;

    constructor(
        private readonly baseSocketService: SocketService,
        @Optional() private labelUpdater: FormatterSet
    ) {
        if (!this.labelUpdater) {
            this.labelUpdater = new ServoFormatterSet();
        }
    }

    ngOnInit() {
        console.log("Initializing servo: " + this.name);
        this.socketService = new SimpleSocketService(this.baseSocketService, this.name, 'update');
        this.setValue(Math.round((this.valueMin + this.valueMax) / 2));
    }

    setValue(value: number) {
        if (value != this.value) {
            console.log("Changing " + this.name + " servo value from: " + this.value + " to " + value)
            this.value = value;
            this.label = this.labelUpdater.update({'value': value});
            this.socketService.setValue(value);
        }
    }

    // Update the label value based on the given value.
    // updateLabel(value) {
    //     if (value > 0) {
    //         this.label = this.positiveLabel ? this.positiveLabel.apply(value) : '';
    //     } else if (value < 0) {
    //         this.label = this.negativeLabel ? this.negativeLabel.apply(-value) : '';
    //     } else {
    //         this.label = this.zeroLabel.apply(value);
    //     }
    // }
}
