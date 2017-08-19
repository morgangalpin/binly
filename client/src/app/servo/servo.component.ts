import { Component, OnInit } from '@angular/core';

import { ServoFormatterSet } from './ServoFormatterSet';
import { SocketService, SimpleSocketService, FormatterSet } from '../shared';

@Component({
    selector: 'app-servo',
    templateUrl: './servo.component.html',
    styleUrls: ['./servo.component.css']
})
export class ServoComponent implements OnInit {

    public value: number;
    public label: string;
    private socketService: SimpleSocketService;

    constructor(
        readonly name: string,
        readonly valueMin: number,
        readonly valueMax: number,
        readonly valueStep: number,
        socketService: SocketService,
        private readonly labelUpdater: FormatterSet = null
    ) {
      this.socketService = new SimpleSocketService(socketService, this.name, 'update');
      if (!this.labelUpdater) {
          this.labelUpdater = new ServoFormatterSet();
      }
    }

    setValue(value: number) {
        if (value != this.value) {
            console.log("Changing servo value from: " + this.value + " to " + value)
            this.value = value;
            this.labelUpdater.update({'value': value});
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

    ngOnInit() {
        this.setValue(0);
    }
}
