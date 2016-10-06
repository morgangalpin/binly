import { Component, OnInit } from '@angular/core';

import { RudderService } from './rudder.service';

@Component({
    selector: 'app-rudder',
    templateUrl: './rudder.component.html',
    styleUrls: ['./rudder.component.css']
})
export class RudderComponent implements OnInit {

    currentRudder: number = 0;

    constructor(
        private rudderService: RudderService
    ) {
        // this.rudderService.onProcessRudderEvent((data) => { console.log('RudderComponent.onProcessRudderEvent("%o")', data); this.currentRudder = data.num; });
    }

    ngOnInit() {
    }
}
