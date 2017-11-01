import { Component, OnInit, Input, Optional } from '@angular/core';

import { FormatterSet, OpenCloseFormatterSet, PositiveNegativeFormatterSet } from '../formatter';
import { SocketService, SimpleSocketService } from '../shared';

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
    @Input() valueInitial: number;
    @Input() labelStyle: string;
    public value: number;
    public label: string;
    private socketService: SimpleSocketService;

    constructor(
        private readonly baseSocketService: SocketService,
        @Optional() private labelUpdater: FormatterSet
    ) {
    }

    ngOnInit() {
        console.log("Initializing servo: " + this.name);
        this.initLabelUpdater();
        this.socketService = new SimpleSocketService(this.baseSocketService, this.name, 'update');
        this.setValue(this.valueInitial);
    }

    private initLabelUpdater() {
        if (!this.labelUpdater) {
            switch (this.labelStyle) {
                case "open-close":
                    this.labelUpdater = new OpenCloseFormatterSet(this.valueMin, this.valueMax);
                    break;
                case "up-down":
                    this.labelUpdater = new PositiveNegativeFormatterSet('Up', 'Down', 'Center');
                    break;
                case "down-up":
                    this.labelUpdater = new PositiveNegativeFormatterSet('Down', 'Up', 'Center');
                    break;
                case "forward-backward":
                    this.labelUpdater = new PositiveNegativeFormatterSet('Forward', 'Backward', 'Stop');
                    break;
                case "left-right":
                    this.labelUpdater = new PositiveNegativeFormatterSet('Left', 'Right', 'Center');
                    break;
                case "right-left":
                default:
                    this.labelUpdater = new PositiveNegativeFormatterSet('Right', 'Left', 'Center');
            }
        }
    }

    setValue(value: number) {
        if (value != this.value) {
            console.log("Changing " + this.name + " servo value from: " + this.value + " to " + value)
            this.value = value;
            this.label = this.labelUpdater.update({'value': value});
            this.socketService.setValue(value);
        }
    }
}
