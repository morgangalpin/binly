import { Component, OnInit } from '@angular/core';
import { Observable } from "rxjs";

import { GpsService } from './gps.service';

@Component({
  selector: 'app-gps',
  templateUrl: './gps.component.html',
  styleUrls: ['./gps.component.css']
})
export class GpsComponent implements OnInit {

  latitude: number = 49.289324;
  longitude: number = -123.129219;

  constructor(
    private gpsService: GpsService
  ) {
    this.gpsService.onProcessGpsEvent((data) => {
      console.log('GpsComponent.onProcessGpsEvent("%o")', data);
      this.latitude = data.latitude;
      this.longitude = data.longitude;
    });
  }

  ngOnInit() {
  }

}
