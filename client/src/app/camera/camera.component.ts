import { Component, OnInit, Input } from '@angular/core';
import { Observable } from "rxjs";

import { CameraService } from './camera.service';

@Component({
  selector: 'app-camera',
  templateUrl: './camera.component.html',
  styleUrls: ['./camera.component.css']
})
export class CameraComponent implements OnInit {

  currentImageUrl: string = 'the default';

  constructor(
    private cameraService: CameraService
  ) {
    this.cameraService.onProcessCameraEvent((data) => {
      console.log('CameraComponent.onProcessCameraEvent("%o")', data);
      this.currentImageUrl = data.url + '/' + data.count;
    });
  }

  ngOnInit() {
  }

}
